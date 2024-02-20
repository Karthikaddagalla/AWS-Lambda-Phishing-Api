You can install and start using the above api by following the below steps.

## Step 1: Install Serverless
```
npm install -g serverless

serverless config credentials --provider aws --key XXXX --secret XXXXX -o
# 1st XXXX -> access key, 2nd XXXX -> secret key

```


## Step 2: Create Project 
```
serverless create --template aws-python3 --name phishing-api --path phishing-api

cd  lambda-learn

```


## Step 3: Install plugins
```
serverless plugin install -n serverless-python-requirements

```

## Step 4:  

* Delete handler.py and serverless.yml files in the project.
* Clone the above Repo
* Copy the cloned files into the project

## Step 5:  
```
serverless deploy
```
