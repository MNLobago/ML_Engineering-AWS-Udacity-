"""
 serializeImageData:  Lambda function to serialize the image data
"""

import json
import boto3
import base64

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """A function to serialize target data from S3"""
    
    # Get the s3 address from the Step Function event input
    key = event["s3_key"] ## TODO: fill in
    bucket = event["s3_bucket"] ## TODO: fill in
    
    # Download the data from s3 to /tmp/image.png
    ## TODO: fill in
    s3.download_file(bucket, key, '/tmp/image.png')
    
    # We read the data from a file
    with open("/tmp/image.png", "rb") as f:
        image_data = base64.b64encode(f.read())

    # Pass the data back to the Step Function
    print("Event:", event.keys())
    return {
        'statusCode': 200,
        'body': {
            "image_data": image_data,
            "s3_bucket": bucket,
            "s3_key": key,
            "inferences": []
        }
    }


"""
ImageClassifier : Lambda function to predict image classification
"""

import json
import boto3
import base64

# Replace this with the name of your deployed SageMaker model endpoint
ENDPOINT = "image-classification-2024-08-06-09-24-33-942"

# Create a SageMaker runtime client
runtime = boto3.Session().client('sagemaker-runtime')

def lambda_handler(event, context):
    try:
        # Decode the base64 encoded image data from the event
        image = base64.b64decode(event['body']['image_data'])
        
        # Invoke the SageMaker endpoint with the image data
        response = runtime.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType='image/png',  # Ensure this matches the expected content type
            Body=image
        )
        
        # Read and decode the response from SageMaker
        predictions = json.loads(response['Body'].read().decode())
        
        # Create a new key at the top level of the response
        result = {
            'image_data': event['body']['image_data'],
            's3_bucket': event['body']['s3_bucket'],
            's3_key': event['body']['s3_key'],
            'inferences': predictions
        }
        
        return {
            'statusCode': 200,
            'body': json.dumps(result)  # Convert the result to a JSON string
        }
    
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

"""
InferenceConfidenceFilter : Lambda function tofiter inference results based on confidence
"""

import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    try:
        # Ensure the event and body are properly formatted
        if 'body' not in event:
            raise Exception("Missing 'body' in event")
        
        # Parse the JSON body
        body = json.loads(event['body'])
        
        if 'inferences' not in body:
            raise Exception("Missing 'inferences' in body")
        
        inferences = body['inferences']
        
        # Check if any values in our inferences are above THRESHOLD
        if not isinstance(inferences, list):
            raise Exception("Inferences should be a list")
        
        if not inferences:
            raise Exception("No inferences provided")
        
        meets_threshold = max(inferences) > THRESHOLD
        
        # If our threshold is met, pass our data back out of the Step Function
        if meets_threshold:
            return {
                'statusCode': 200,
                'body': json.dumps(event)
            }
        else:
            raise Exception("THRESHOLD_CONFIDENCE_NOT_MET")
    
    except Exception as e:
        # Handle any exceptions and return a 500 error with the exception message
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }

