# Airflow Patents Crawler

This is a sample project to illustrate a real-world usage of [Apache Airflow](https://airflow.apache.org/).

## Requirements

We will need the following requirements for the project:

- Python 3.6 or higher
- Docker
- Docker-compose
- [AWS S3 account](https://supsystic.com/documentation/id-secret-access-key-amazon-s3/) 

## Project structure

- `/airflow-dags` , where we will include the airflow scripts.
- `requirements.txt` where we will include the dependencies of the project

## Starting the project

You have to set the following environment variables:
``` bash
AWS_ACCESS_KEY=AKIAJBS31275GTIWD...
AWS_SECRET_KEY=dBZDFEIsuZmt49Y9Sk..
AWS_BUCKET_NAME=patents-bucket'
AWS_BUCKET_REGION=us-east-1
```


Run `doker-compose.yml` in the root folder and go to [http://localhost:8090/admin/](http://localhost:8090/admin)

## Patents API

We are going to consume public patent API from [api.patentsview.org](https://api.patentsview.org/doc.html)

## Further help

If you want to know more about apache airflow, contact [Juan Roldan](https://juanbroldan.com/contact/).