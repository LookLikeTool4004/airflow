# Overview
This project implements a machine learning pipeline for predicting car prices. It uses Apache Airflow for workflow orchestration, ensuring that data processing, model training, and prediction are executed in a systematic and automated manner.

# Files Description
hw_dag.py: This script defines an Airflow DAG (Directed Acyclic Graph) named car_price_prediction. It orchestrates two main tasks:

pipeline: For processing data and training the machine learning model.
predict: For making predictions using the trained model.
pipeline.py: Implements the data processing and machine learning pipeline. Key features:

# Data preprocessing functions.
A machine learning pipeline setup using sklearn, with various classifiers and preprocessing techniques.
predict.py: Used for making predictions on new data with the trained model. Features include:

Loading the serialized model.
Reading and processing test data.
Making and storing predictions.
Installation
To set up the project, follow these steps:

Ensure Python 3.x is installed.
Install required packages: pandas, sklearn, dill, apache-airflow.
Clone this repository to your local machine.
Usage
Start the Airflow server.
Place your data in the respective directories as expected by the scripts.
Trigger the car_price_prediction DAG from the Airflow UI or CLI.

