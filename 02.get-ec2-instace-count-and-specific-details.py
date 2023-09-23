import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()


print('Number of instaces : {}'.format(len(response['Reservations'])))
for i in response['Reservations']:
    
    for j in i['Instances']:
         print("Instance ID : {}".format(j['InstanceId']))
         print("AMI ID : {}".format(j['ImageId']))
         print("Instace Type : {}".format(j['InstanceType']))
         print("Public Ip Address: {}".format(j['PublicIpAddress']))
         print("Private IP Address : {}".format(j['PrivateIpAddress']))
         print("Instance State: {}".format(j['State']['Name']))
         print("Token : {}".format(j['KeyName']))
