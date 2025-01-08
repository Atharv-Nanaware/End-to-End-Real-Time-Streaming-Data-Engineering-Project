from datetime import datetime,timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
import random
import requests
import logging
import json
from kafka import KafkaProducer
import time


default_args = {
    'owner': 'data_engineer',
    'start_date': datetime(2024, 11, 11, 11, 0),
    'retries': 3,  #
    'retry_delay': timedelta(minutes=5),
}
def get_data():

    try:
        response = requests.get("https://randomuser.me/api/")
        response.raise_for_status()
        user_data = response.json()['results'][0]
        logging.info("Data fetched successfully from API.")
        return user_data
    except requests.RequestException as e:
        logging.error(f"Error fetching data from API: {e}")
        raise

def format_data(res):

    try:
        location = res['location']
        formatted_data = {
            'first_name': res['name']['first'],
            'last_name': res['name']['last'],
            'gender': res['gender'],
            'address': f"{location['street']['number']} {location['street']['name']}, "
                       f"{location['city']}, {location['state']}, {location['country']}",
            'post_code': location['postcode'],
            'email': res['email'],
            'username': res['login']['username'],
            'dob': res['dob']['date'],
            'registered_date': res['registered']['date'],
            'phone': res['phone'],
            'picture': res['picture']['medium'],
        }
        logging.info("Data formatted successfully.")
        return formatted_data
    except KeyError as e:
        logging.error(f"Error formatting data: Missing key {e}")
        raise

def stream_data():


    producer = KafkaProducer(bootstrap_servers='broker:9092', max_block_ms=5000)
    curr_time = time.time()

    while True:
        if time.time() > curr_time + 120: #2 minutes
            break
        try:
            res = get_data()
            res = format_data(res)

            producer.send('user_profile_stream', json.dumps(res).encode('utf-8'))
            sleep_duration = random.uniform(0.5, 2.0)
            time.sleep(sleep_duration)
        except Exception as e:
            logging.error(f'An error occurred: {e}')
            continue

with DAG('realtime_user_streaming_pipeline',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False) as dag:

    streaming_task = PythonOperator(
        task_id='stream_data_from_api',
        python_callable=stream_data
    )