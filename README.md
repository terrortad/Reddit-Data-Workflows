## Data Engineering on Reddit Posts: A Complete Pipeline

This project sets up a high-performance ETL pipeline for Reddit data. The pipeline uses a modern technology stack, with Apache Airflow directing the flow and Celery handling distributed jobs. Data is extracted from the API, converted using AWS Glue, and actively queried with Athena before being placed into the Amazon Redshift data warehouse for in-depth analysis.

### Table of Contents
Overview
Architecture
Prerequisites
System Setup

### Overview
The pipeline is designed to:

Extract data from Reddit using its API.
- Store the raw data into an S3 bucket from Airflow.
- Transform the data using AWS Glue and Amazon Athena.
- Load the transformed data into Amazon Redshift for analytics and querying.

### Architecture

**Components:**

- **Reddit API**: Source of the data.
- **Apache Airflow & Celery**: Orchestrates the ETL process and manages task distribution.
- **PostgreSQL**: Temporary storage and metadata management.
- **Amazon S3**: Raw data storage.
- **AWS Glue**: Data cataloging and ETL jobs.
- **Amazon Athena**: SQL-based data transformation.
- **Amazon Redshift**: Data warehousing and analytics.

### Prerequisites
AWS Account with appropriate permissions for S3, Glue, Athena, and Redshift.
Reddit API credentials.
Docker Installation
Python 3.9 or higher


### System Setup

**Clone the Repository**

```git clone https://github.com/terrortad/Reddit-Data-Workflows.git```
```cd RedditDataEngineering```

**Create a Virtual Environment**
```python3 -m venv venv```
```source venv/bin/activate```

**Install the Dependencies**
```pip install -r requirements.txt```

**Configure the Project**
Rename the configuration file and add your credentials:

```mv config/config.conf.example config/config.conf```

**Start the Containers**
```docker-compose up -d```

**Launch Airflow Web UI**
Open the Airflow web UI:
```open http://localhost:8080```
