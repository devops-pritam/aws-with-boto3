import boto3
import csv

ec2 = boto3.client('ec2')

# Mentioning the instance ids or the servers which needs to be start or stop
instance_id1 = 'i-0ccbf38404313361c'
instance_id2 = 'i-0aca7b5bd086731b4'

def startServer(id):
     # Describe the instance to get its status
     response = ec2.describe_instances(InstanceIds=[id])
     # Check the instance state
     if response['Reservations']:
        instance = response['Reservations'][0]['Instances'][0]
        state = instance['State']['Name']
        if state == 'stopped':
            # Start the EC2 instance
            ec2.start_instances(InstanceIds=[id])
            # Wait for the instance to start (optional)
            ec2.get_waiter('instance_running').wait(InstanceIds=[id])
            print('Server {} started successfully'.format(id))
        elif state == 'running':
            print('Server {} is already running'.format(id))
    
    
def stopServer(id):
     # Describe the instance to get its status
     response = ec2.describe_instances(InstanceIds=[id])
     # Check the instance state
     if response['Reservations']:
        instance = response['Reservations'][0]['Instances'][0]
        state = instance['State']['Name']
        if state == 'running':
            # Stop the EC2 instance
            ec2.stop_instances(InstanceIds=[id])
            # Wait for the instance to stop (optional)
            ec2.get_waiter('instance_stopped').wait(InstanceIds=[id])
            print('Server {} stopped successfully'.format(id))
        elif state == 'stopped':
            print('Server {} is already stopped'.format(id))
     
       
    
    


if __name__ == "__main__":
    
    startServer(instance_id1)
    stopServer(instance_id2)
    
