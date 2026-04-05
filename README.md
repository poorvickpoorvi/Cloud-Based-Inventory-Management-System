# Cloud Inventory Management System

Serverless backend for an inventory management system using AWS services.

## Tech Stack

- AWS Lambda
- API Gateway
- DynamoDB
- SNS
- Python

## Features

- Add products
- View inventory
- Update stock
- Low stock alerts

## API Endpoints

POST /add-product  
GET /products  
PUT /update-stock

## Database

DynamoDB Table: InventoryTable

Attributes:
product_id  
product_name  
category  
price  
stock  
threshold

## Deployment

Each folder represents an AWS Lambda function.
Deploy using AWS Lambda console or AWS CLI.
