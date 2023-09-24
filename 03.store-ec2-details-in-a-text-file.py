import boto3

ec2 = boto3.client('ec2')

def getEc2Response():
     response = ec2.describe_instances()

     return response

def getServerDetails(response):

     op = []
     

     for i in response['Reservations']: 
         
         get_details = {}     
     
         for j in i['Instances']:              

               
               get_keys = j.keys()
               
               if 'InstanceId' in get_keys:
                    id = j['InstanceId']
               else: id = 'null'

               get_details['InstanceId']=id

               if 'ImageId' in get_keys:
                    ami_id = j['ImageId']
                    
               else: ami_id = 'null'
               get_details['ImageId']=ami_id

               if 'InstanceType' in get_keys:
                    instance_type = j['InstanceType']
                    
               else:  instance_type = 'null'
               get_details['InstanceType']=instance_type


               if 'PublicIpAddress' in get_keys:
                    public_ip = j['PublicIpAddress']
                    
               else: public_ip = 'null'
               get_details['PublicIpAddress']=public_ip

               if 'PrivateIpAddress' in get_keys:
                    private_ip = j['PrivateIpAddress']
                    
               else: private_ip = 'null'
               get_details['PrivateIpAddress']=private_ip

               if 'State' in get_keys:
                    state = j['State']['Name']
                    
               else: state = 'null'
               get_details['state']=state


               if 'KeyName' in get_keys:
                    key_name = j['KeyName']
                    
               else: key_name = 'null'

               get_details['KeyName']=key_name

               op.append(get_details)

     return(op)

def saveToTextFile(name,data):
     # Writing to file
     with open(name, "w") as file:
         
         # Writing data to a file         
         file.writelines([f"{line}\n" for line in data])       
         
    
    


if __name__ == "__main__":
    
    res = getEc2Response()
    op = getServerDetails(res)
    saveToTextFile('serverDetails.txt',op)
  
