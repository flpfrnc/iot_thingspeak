from django.shortcuts import render
import requests
import json
import datetime
from dateutil import tz

def dashboard(request):
    json_data = requests.get('https://thingspeak.com/channels/1052510/feed.json').text
    json_loaded = json.loads(json_data)
    local_zone = tz.gettz("America/Fortaleza")
    context = {}

    dados = json_loaded["feeds"][-10:]
    leitura = list()
    chuva_valor = list()
    umidade_valor = list()
    temperatura_valor = list()
    pressaoatm_valor = list()

    for x in range(len(dados)):
        date = dados[x]["created_at"]
        value_rain = dados[x]["field1"]
        value_umidity = dados[x]["field3"]
        value_temperature = dados[x]["field4"]
        value_pressure = dados[x]["field6"]

        formatted_date = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%SZ").astimezone(local_zone).strftime('%d-%m %H:%M')
        leitura.append(formatted_date)
        temperatura_valor.append(value_temperature)
        chuva_valor.append(value_rain)
        umidade_valor.append(value_umidity)
        pressaoatm_valor.append(value_pressure)
    
    context = { "data" :  leitura, "temperatura" : str(temperatura_valor), "milimetros" : str(chuva_valor), "umidade": str(umidade_valor), "pressaoatmosferica": str(pressaoatm_valor) }          
    return render(request, 'index.html', {'contextos' : context})
