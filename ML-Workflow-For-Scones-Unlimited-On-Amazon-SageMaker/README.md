<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ML Workflow for Scones Unlimited on Amazon SageMaker</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        h1, h2, h3 {
            color: #333;
        }
        ul {
            list-style-type: disc;
            margin-left: 20px;
        }
    </style>
</head>
<body>
    <h1>ML Workflow for Scones Unlimited on Amazon SageMaker</h1>

    <h2>Overview</h2>
    <p>In this project, we focus on optimizing delivery operations for Scones Unlimited by leveraging machine learning. Specifically, we develop an image classification model to distinguish between bicycles and motorcycles. This differentiation allows us to better route delivery drivers, assigning nearby orders to those on bicycles and distant orders to those on motorcycles. This targeted routing aims to enhance operational efficiency and streamline delivery logistics.</p>
    <p>Our approach uses Amazon SageMaker for model development and deployment, AWS Lambda for supporting services, and AWS Step Functions to orchestrate our workflows. By the end of this project, we will have a robust, scalable ML solution integrated into a serverless architecture.</p>

    <h2>Project Goals</h2>
    <ul>
        <li><strong>Develop a Classification Model:</strong> Create a machine learning model to classify images of delivery vehicles.</li>
        <li><strong>Deploy and Scale:</strong> Use AWS SageMaker for scalable model deployment.</li>
        <li><strong>Integrate Supporting Services:</strong> Utilize AWS Lambda and AWS Step Functions to build a comprehensive, event-driven application.</li>
        <li><strong>Demonstrate Capabilities:</strong> Provide a portfolio-ready demo showcasing the ability to create and integrate scalable ML solutions on AWS.</li>
    </ul>

    <h2>Project Steps</h2>
    <ol>
        <li><strong>Data Staging:</strong> Prepare and stage the image data required for training the classification model.</li>
        <li><strong>Model Training and Deployment:</strong>
            <ul>
                <li><strong>Model Training:</strong> Train the image classification model using AWS SageMaker.</li>
                <li><strong>Deployment:</strong> Deploy the trained model on SageMaker for scalable inference.</li>
            </ul>
        </li>
        <li><strong>Lambda Functions and Step Function Workflow:</strong>
            <ul>
                <li><strong>AWS Lambda:</strong> Develop Lambda functions to handle various tasks related to data processing and model inference.</li>
                <li><strong>AWS Step Functions:</strong> Create workflows to orchestrate Lambda functions and manage the end-to-end ML pipeline.</li>
            </ul>
        </li>
        <li><strong>Testing and Evaluation:</strong> Test the integrated system to ensure it performs as expected. Evaluate the model's accuracy and the efficiency of the Lambda functions and Step Functions.</li>
        <li><strong>Optional Challenge:</strong> Explore additional features or optimizations that could further enhance the system. This could involve tuning the model, optimizing performance, or integrating additional services.</li>
        <li><strong>Cleanup:</strong> Ensure that all AWS resources are properly cleaned up to avoid unnecessary charges.</li>
    </ol>

    <h2>Code and Resources</h2>
    <p>The project repository includes:</p>
    <ul>
        <li><strong>Lambda Functions Code:</strong> Scripts for creating and managing AWS Lambda functions.</li>
        <li><strong>Step Functions Definitions:</strong> JSON/YAML definitions for AWS Step Functions workflows.</li>
        <li><strong>Model Training Scripts:</strong> Code for training the image classification model on AWS SageMaker.</li>
        <li><strong>Deployment Scripts:</strong> Instructions for deploying the trained model and integrating with AWS services.</li>
    </ul>
</body>
</html>
