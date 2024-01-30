from flask import Flask, request, redirect, url_for
from flask_cors import CORS
import json
from kvzawpeyvm.rulpawirintukuwe.KimamWirintukun import chuchiWirintukun, zulliafiel_rulpawirintukuwe 
from kvzawpeyvm.wvzalkawe.koyam import Koyam
from kvzawpeyvm.rulpawirintukuwe.Reglas import reglas12, reglas13, reglas21, reglas23, reglas31, reglas32
from kvzawpeyvm.wvzalkawe.xoy import Xoy
from kvzawpeyvm.wvzalkawe.kellual import pepikaam_hemvl
import time
import datetime
import os
import re
#import random 
#import os
import joblib
application = Flask(__name__)   
cors = CORS(application,resources={r'/*': {'origins': '*'}})
application.config['CORS_HEADERS'] = 'Content-Type'

encoder = json.JSONEncoder()
decoder = json.JSONDecoder()


##json.load()
grafs = json.load(open('config/ab_graf.json','r'))
zugun = json.load(open('config/zugun.json','r'))
rulpawe2rakin= json.load(open('config/rulpawe2rakin.json','r'))

@application.route('/', methods=['GET'])
def konwe():    
    return encoder.encode('Mari mari! tami mvlerki tati api tami kelluaetu kim mapuzugual!!')

##<>VARIABLE

@application.route('/api/narvmal/metadata/', methods=['GET'])
def narvmal_metadata():
    return encoder.encode(zugun)



@application.route('/api/rulpazugual/', methods=['POST'])
def rulpazugual():
    response = {}
    if request.method == 'POST':
        data = request.get_json()
        xoyzugun = data['xoyzugun']
        response['xoyzugun'] = xoyzugun
        response['grafemario_konlu'] = data['grafemario_konlu']
        response['grafemario_xipalu'] = data['grafemario_txipalu']
        g1 = rulpawe2rakin[data['grafemario_konlu']]
        g2 = rulpawe2rakin[data['grafemario_txipalu']]
        response['rulgepalu'] = zulliafiel_rulpawirintukuwe(g1,g2)(xoyzugun)
        
    return encoder.encode(response)   


@application.route('/api/wvzalkafe/', methods=['POST'])
def pegelwe():
    params=request.get_json()
    response={}
    if 'hemvl' in params.keys():
        hemvl = params['hemvl']
        if len(hemvl) > 0:
            pegelam_hemvl = pepikaam_hemvl(hemvl)
            response['code'] = 1
            response['msg'] = pegelam_hemvl['eypial']
            if pegelam_hemvl['xipai']:
                response['data'] = pegelam_hemvl['puhemvl']
            else:
                response['data'] = 'Gelai data'
            
            
        else:
            response['code'] = -1
            response['msg'] = 'amulelgelan zugun '
    return encoder.encode(response)   


@application.route('/api/chuchiWirintukun/', methods=['POST'])
def kimChuchiWirintukun():
    response = {}
    if request.method == 'POST':    
        data = request.get_json()
        try:
            if len(data)==0:
                response = 'Tukul-laimi tami xoy zugun'
            else:
                tvfa =  chuchiWirintukun(data['xoyzugunw'])
                if len(tvfa)==0:
                    response = {'code':-1,'msg':"Perkelafiiñ tati wirintukun tami xoy zugun mu,Ka kiñe tukul-afuimi,"}
                else:
                    res = []
                    for i in tvfa:
                        res.append(i)
                    response['wirintukunArray']=res
                    response['code']=1
                    
        except Exception as e:
            
            print(f'->ERROR{e}->ERROR')
        
    return encoder.encode(response)   

        
@application.errorhandler(404)
def page_not_found(error):
    response={}
    response['msg'] = 'Chew amuleimi cha?' 
    return encoder.encode(response)


if __name__ == '__main__':
    application.run('127.0.0.1', 5001, debug=True)
   # application.run(host='0.0.0.0', port=5000, debug=True,ssl_context='adhoc')
