import boto3

s3_client = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')
print(table.table_status)


def handler(event, context):
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    s3_file_name = event['Records'][0]['s3']['object']['key']
    print(bucket_name)
    print(s3_file_name)
    resp =s3_client.get_object(Bucket=bucket_name, Key=s3_file_name)
    data = resp['Body'].read().decode('utf-8')
    print('data' + data)
    employees = data.split('\n')
    print('table status is:' + table.table_status)
    for emp in employees:
        print('emp is:' + emp[0])
        emp_data = emp.split(',')
        table.put_item(
            Item = {
                "id" : emp_data[0],
                "name" : emp_data[1],
                "location" : emp_data[2]
            }
        )

         
    
