# aws-with-boto3
This repository is dedicated for AWS cloud automation with Python Boto3 Package

# Prerequisite 
# Download and Install Python

URL : https://www.python.org/downloads/

## Check the Python version : 
python --version

# Install and setup AWS CLI 

curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
aws --version

# We have 2 ways to configure AWS Credentials In Command Line Interface

# First Way 

Create IAM USER in AWS Console

aws configure | Here provide Access Key and Secret Key Details and the Default Region. Example : ap-south-1 (Mumbai Region)

# Second Way

Otherwise alternative way is to create a folder .aws and inside that create two files named credentials and config

# For Example

C:\Users\ACER\: Under this Folder create a folder named .aws 
Then inside the folder .aws create 2 Files, One: credentials and Second: config


Then write these details inside the credentials file


[default]
aws_access_key_id = ACCESS_KEY
aws_secret_access_key = SECRET_KEY



In the config file write these details :


[default]
region = ap-south-1
output = json

# Finally 

Install boto3 package with this below command 

pip install boto3 







