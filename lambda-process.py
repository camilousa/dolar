import json
import boto3
from datetime import datetime 

def lambda_handler(event, context):
    nuevo = event['Records'][0]['s3']['object']['key']
    #nuevo = "dolar-2024-07-31.json"
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('data-scrapping-255423')
    obj = bucket.Object(nuevo)
    body = obj.get()['Body'].read()
    datos = json.loads(body)
    s3_client = boto3.client('s3')

    s = "fecha,valor\n" 
    for d in datos:
        fecha = datetime.fromtimestamp(int(d[0])/1000)
        s+=fecha.strftime("%Y-%m-%d %H:%M:%S")+","+d[1]+"\n"

    s3_client.put_object(Body=s, Bucket='dolar-final-255423', Key=nuevo.replace(".json", ".csv"), ContentType='text/csv')
    return {
        'statusCode': 200,
        'body': json.dump(s)
    }
