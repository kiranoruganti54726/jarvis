import boto3

client = boto3.client(
    's3',
    aws_access_key_id="AKIA4XCPHACSQIWNES75",
    aws_secret_access_key="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",

)
#bucket creation from python boto3
'''response = client.create_bucket(

    Bucket='s4frompythonboto3',
    CreateBucketConfiguration={
        'LocationConstraint': 'ap-south-1' }

)'''

#upload this file(object) to aws s3
'''response = client.put_object(

    Body=open("awsboto3.py","r").read(),
    Bucket='s3frompythonboto3',

    Key='file1frompythonboto3'#key ante manam upload chesna file name
)
print(response)'''

#download a file from s3 using boto3
'''response = client.get_object(
    Bucket='s3frompythonboto3',
     Key='file1frompythonboto3'
)
data=response.get("Body").read().decode()
file1=open("file1frompythonboto3","w")#file1frompythonboto3 ane notepad file ni create chesnam andulo ee code antha untundi left dashboard lo chusthe kanipistadi
file1.writelines(data)#decode aina data variable ni file1 variable lo pettam
file1.close()# left side chusthe kanipisthadi download aina file'''

#listing buckets from s3 using s3
'''response = client.list_buckets()
print(response)#motham data print chesthadi including buckets,owner and user name etc
buckets=response.get("Buckets")#gets only buckets list from aws s3
print(f"total buckets={len(buckets)}")#prints no of buckets
print(buckets)'''

#listing objects from s3 bucket

'''response = client.list_objects(
    Bucket='s3frompythonboto3')
print(response)
buckets1=response.get("Contents")#response lo  contents lopala object names untay anduke contents
print(buckets1)'''

#delete object from boto3
'''response = client.delete_object(
    Bucket='s3frompythonboto3',
    Key='file2'# deletes file2 object from s3
)

print(response)'''

#delete bucket from s3
'''response = client.delete_bucket(
    Bucket='s4frompyt'''honboto3')#to delete a bucket it must be empty otherwise you get an error
print(response)'''