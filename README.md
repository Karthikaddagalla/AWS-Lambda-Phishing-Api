## What does above API do ?

If someone sends a url as query parameter to the above api then the api will return whether the given link is phishing or not.For example

Api_url = https://ebm56282jg.execute-api.us-west-1.amazonaws.com/phishingStage/phishingResource?url=https://github.com/Karthikaddagalla/

Response:
```json
{
    "message": "Given link is Good link, if below output is 0",
    "output": 0
}
```

## How you can use it ?

You can install and start using the above api by following the below steps.

### Step 1: Install Serverless
```
npm install -g serverless

serverless config credentials --provider aws --key XXXX --secret XXXXX -o
# 1st XXXX -> access key, 2nd XXXX -> secret key

```


### Step 2: Create Project 
```
serverless create --template aws-python3 --name phishing-api --path phishing-api

cd  phishing-api

```


### Step 3: Install plugins
```
serverless plugin install -n serverless-python-requirements

```

### Step 4:  

* Delete handler.py and serverless.yml files in the project.
* Clone the above Repo
* Copy the cloned files into the project

### Step 5:  
```
serverless deploy
```

## Want access to the api ?

If you want to integrate this api into your application just mail me at karthiksatyasai7@gmail.com to get access to the already deployed api. You can check how it is working [here](https://phishing-domain-detection-gz559ebq4-karthikaddagallas-projects.vercel.app/)



