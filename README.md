
# **End-to-End DataFlow: Python & Real-Time Streaming**

This project demonstrates a robust, end-to-end real-time data pipeline designed to efficiently process, transform, 
and store streaming data. Leveraging cutting-edge technologies like Python, Docker, Airflow, Apache Kafka, 
Apache Spark, and Cassandra, the pipeline is fully scalable, containerized, and tailored to handle 
high-velocity data streams with ease and reliability.


### Key Features:

Real-Time Data Processing: Uses Apache Kafka for distributed streaming and Apache Spark for high-speed processing.
Pipeline Orchestration: Managed with Apache Airflow, ensuring modular and fault-tolerant workflows.
Data Storage: Stores processed data in Cassandra, a highly scalable NoSQL database for fast reads and writes.
Containerization: The entire pipeline is containerized using Docker, ensuring portability and consistency across environments.
Python-Powered: Python scripts for API data extraction, streaming, and integration with Kafka and Spark.
UI for Monitoring: Includes Kafka's monitoring UI for stream visualization.

### System Architecture :




### Architecture Overview:

* Data is ingested from a Random Name API via Python.
* Streaming data is sent to Apache Kafka for distributed processing.
* Apache Spark processes data in real-time using a master-worker node setup.
* Processed data is stored in Cassandra for persistence.
* Airflow orchestrates the pipeline and stores metadata in PostgreSQL.
* The entire system is deployed using Docker, ensuring scalability and easy deployment.


## My Learnings :

* Gained hands-on experience in building scalable real-time data pipelines using cutting-edge technologies.
* Developed a deep understanding of Apache Kafka and its role in enabling distributed streaming and pub-sub patterns.
* Enhanced skills in Apache Spark for real-time data transformation and processing.
* Learned to effectively orchestrate workflows and schedule tasks using Apache Airflow, ensuring a seamless pipeline execution.
* Mastered the use of Cassandra as a high-performance database for storing streaming data in a distributed architecture.
* Improved knowledge of containerization with Docker, enabling efficient development and deployment of microservices.
* Strengthened expertise in designing and implementing end-to-end data pipelines, ensuring reliability and scalability in handling high-velocity data.


## Setup Instructions

1. #### Clone the Repository:

   Clone the project repository to your local machine:


    git clone https://github.com/Atharv-Nanaware/End-to-End-Real-Time-Streaming-Data-Engineering-Project.git


2. #### Navigate to the Project Directory

   Move into the project directory:


    cd End-to-End-Real-Time-Streaming-Data-Engineering-Project


3. #### Initialize Airflow :

   Run Docker Compose to perform database migrations and create the initial Airflow user account:


    docker-compose up airflow-init


4. #### Run Docker Compose again to spin up the services:


    docker compose up -d



## Usage :

#### Verify Containers :
  
  Make sure all containers are up and running:


    docker ps

#### Access Airflow:

* Open your browser at http://localhost:8080 (or the port specified in your docker-compose.yml).
* Log in using the credentials you set in the initialization step.
* Enable the DAG (data pipeline) in the Airflow UI to start scheduling.

#### Check Kafka Topics & UI :

Visit the Kafka UI (if configured in docker-compose.yml) at http://localhost:8085 for monitoring the Kafka topics and messages.

#### Monitor Spark Jobs

By default, Spark’s master WebUI may be accessible at http://localhost:9090 .
Check the status of your running jobs, executors, and worker nodes.

#### Inspect Cassandra

Connect to Cassandra container or use a client (like cqlsh) to verify that the data is being stored properly.



    docker exec -it cassandra cqlsh -u cassandra -p cassandra localhost 9042

    cqlsh> DESCRIBE KEYSPACES;

    cqlsh> SELECT * FROM spark_streaming.created_users;


    

#### Thank you for checking out the End-to-End Real-Time Data Pipeline Project.
    