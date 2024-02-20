

try:
    import unzip_requirements
except ImportError:
    pass
import json
from predictor import predictor





def hello(event, context):
    url = event['queryStringParameters']['url']

    result = predictor(url)

    res_body = {
        "message": "Given link is Good link, if below output is 0",
        "output": result
    }


    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {}
    http_res['headers']['Content-Type'] = 'application/json'
    http_res['body'] = json.dumps(res_body)
    
    return http_res
    

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """






















# try:
#     import unzip_requirements
# except ImportError:
#     pass

# import json
# import os

# def hello(event, context):
#     # Print current directory
   

#     # Access the contents of gradient_classifier_98
#     file_path = 'Models/gradient_classifier_98'
#     try:
#         with open(file_path, 'r') as file:
#             classifier_contents = file.read()
#     except FileNotFoundError:
#         classifier_contents = "File not found."

#     # Construct response body
#     res_body = {
#         "message": "Given link is Good link, if below output is 0",
#         "output_total": os.listdir('.'),
#         "output_models": os.listdir('Models'),
#         "gradient_classifier_98_contents": classifier_contents
#     }

#     # Construct HTTP response
#     http_res = {
#         "statusCode": 200,
#         "headers": {
#             "Content-Type": "application/json"
#         },
#         "body": json.dumps(res_body)
#     }
    
#     return http_res
