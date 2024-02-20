You can install and start using it by following the below steps.

## Step 1: Install Serverless
```
npm install -g serverless

serverless config credentials --provider aws --key XXXX  --secret XXXXX -o

```


## Step 2: Create Project 
```
serverless create --template aws-python3 --name lambda-learn  --path lambda-learn

cd  lambda-learn
```


## Step 3: Install plugins
```
sls plugin install -n serverless-python-requirements

```
* Clone the Repo
* * Replace the existing handler.py and serverless.yaml with above files.

## Step 4:  
```
sls deploy
```
