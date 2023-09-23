import boto3

ec2 = boto3.client('ec2')
response = ec2.describe_instances()

print('Number of instaces : {}'.format(len(response['Reservations'])))

for i in response['Reservations']:    
    
    for j in i['Instances']:
         
         get_keys = j.keys()
         
         if 'InstanceId' in get_keys:
              print("Instance ID : {}".format(j['InstanceId']))
         else: print('No Instance ID available')

         if 'ImageId' in get_keys:
              print("AMI ID: {}".format(j['ImageId']))
         else: print('No AMI ID available')

         if 'InstanceType' in get_keys:
              print("Instance Type : {}".format(j['InstanceType']))
         else: print('No Instance Type available')

         if 'PublicIpAddress' in get_keys:
              print("Public Ip Address : {}".format(j['PublicIpAddress']))
         else: print('No Public Ip Address available')

         if 'PrivateIpAddress' in get_keys:
              print("Private Ip Address : {}".format(j['PrivateIpAddress']))
         else: print('No Private Ip Address available')

         if 'State' in get_keys:
              print("Instance ID : {}".format(j['State']['Name']))
         else: print('No Status available for state')

         if 'KeyName' in get_keys:
              print("KeyName : {}".format(j['KeyName']))
         else: print('No KeyName available')
