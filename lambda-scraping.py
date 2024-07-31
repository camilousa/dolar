import json
import urllib.request
from datetime import datetime 
import boto3

url_banco = ("https://totoro.banrep.gov.co/estadisticas-economicas/rest/consultaDatosService/consultaMercadoCambiario")

def lambda_handler(event, context):
    # TODO implement
    
    s3_client = boto3.client('s3')
    with urllib.request.urlopen(url_banco) as response:
      datos = response.read()
      
    fecha = datetime.today().strftime('%Y-%m-%d')  
    s3_client.put_object(Body=datos, Bucket='data-scrapping-255423', Key=f'dolar-{fecha}.json', ContentType='text/json')  
    return { "body": url_banco}
