# ML Workflow for Scones Unlimited on Amazon SageMaker

## Overview

In this project, we focus on optimizing delivery operations for Scones Unlimited by leveraging machine learning. Specifically, we develop an image classification model to distinguish between bicycles and motorcycles used for deliveries. This differentiation allows us to better route delivery drivers, assigning nearby orders to those on bicycles and distant orders to those on motorcycles. This targeted routing aims to enhance operational efficiency and streamline delivery logistics.

Our approach uses Amazon SageMaker for model development and deployment, AWS Lambda for supporting services, and AWS Step Functions to orchestrate our workflows. By the end of this project, we will have a robust, scalable ML solution integrated into a serverless architecture.

## Project Goals

- **Develop a Classification Model:** Create a machine learning model to classify images of delivery vehicles, specifically bicycles and motorcycles.
- **Deploy and Scale:** Use AWS SageMaker for scalable model deployment.
- **Integrate Supporting Services:** Utilize AWS Lambda and AWS Step Functions to build a comprehensive, event-driven application.
- **Demonstrate Capabilities:** Provide a portfolio-ready demo showcasing the ability to create and integrate scalable ML solutions on AWS.

## Project Steps

1. **Data Staging**  
   Prepare and stage the image data required for training the classification model.

2. **Model Training and Deployment**  
   - **Model Training:** Train the image classification model using AWS SageMaker.
   - **Deployment:** Deploy the trained model on SageMaker for scalable inference.

3. **Lambda Functions and Step Function Workflow**  
   - **AWS Lambda:** Develop Lambda functions to handle various tasks related to data processing and model inference.
   - **AWS Step Functions:** Create workflows to orchestrate Lambda functions and manage the end-to-end ML pipeline.

4. **Testing and Evaluation**  
   Test the integrated system to ensure it performs as expected. Evaluate the model's accuracy and the efficiency of the Lambda functions and Step Functions.

5. **Optional Challenge**  
   Explore additional features or optimizations that could further enhance the system. This could involve tuning the model, optimizing performance, or integrating additional services.

6. **Cleanup**  
   - **Resource Cleanup:** Ensure that all AWS resources are properly cleaned up to avoid unnecessary charges.

## Code and Resources

The project repository includes:

- **Lambda Functions Code:** Scripts for creating and managing AWS Lambda functions.
- **Step Functions Definitions:** JSON/YAML definitions for AWS Step Functions workflows.
- **Model Training Scripts:** Code for training the image classification model on AWS SageMaker.
- **Deployment Scripts:** Instructions for deploying the trained model and integrating with AWS services.
