<<<<<<< HEAD:descarga_periodicos.py
import boto3
import urllib.request
import datetime


def descarga_contenido(url, bucket, nombre):
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    today = datetime.date.today().strftime('%Y-%m-%d')
    s3 = boto3.resource('s3')
    s3.Object(bucket,
              'headlines/raw/{}{}.html'.format(nombre,
                                               today)).put(Body=content)


descarga_contenido('https://www.eltiempo.com',
                   'parcial2-periodicos',
                   'ElTiempo-')
descarga_contenido('https://www.elespectador.com', 'parcial2-periodicos',
                   'ElEspectador-')
=======
import boto3
import urllib.request
import datetime


def descarga_contenido(url, bucket, nombre):
    response = urllib.request.urlopen(url)
    content = response.read().decode('utf-8')
    today = datetime.date.today().strftime('%Y-%m-%d')
    s3 = boto3.resource('s3')
    s3.Object(bucket,
              'headlines/raw/{}{}.html'.format(nombre,
                                               today)).put(Body=content)


descarga_contenido('https://www.eltiempo.com', 'parcial2-periodicos', 'ElTiempo-')
descarga_contenido('https://www.elespectador.com', 'parcial2-periodicos',
              'ElEspectador-')
>>>>>>> 0e60599ce8b47b8ef7ee1ca91b637fe447e23f10:descarga/descarga_periodicos.py
