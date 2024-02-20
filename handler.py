

try:
    import unzip_requirements
except ImportError:
    pass
import json
from predictor import predictor





def hello(event, context):
    url = event['queryStringParameters']['url']

    if url=="up":    # Waking the system up when page is reloaded to avoid delays
        res_body={"message": "Thanks for waking me up"}

    else:
        result = predictor(url)

        res_body = {
            "message": "Given link is Good link, if below output is 0",
            "output": result
        }


    http_res = {}
    http_res['statusCode'] = 200
    http_res['headers'] = {'Content-Type':'application/json',
                    'Access-Control-Allow-Origin':'*',
                    'Access-Control-Allow-Methods':'POST,PATCH,OPTIONS'}
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




_res
