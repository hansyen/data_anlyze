from builtins import staticmethod, dict, int

from __init__ import db
from models import User

from flask_restful import Resource
from urllib import parse
from flask import request, jsonify
import datetime, json
import pandas as pd
import pandas_datareader.data as web
from pandas import DataFrame

class StockResource(Resource):
    @staticmethod
    def get():
        payload = dict(parse.parse_qsl(parse.urlsplit(request.url).query))
        
        try:
            name = payload['account_name']
            api_code = payload['api_code']
            
            user_info = User.query.filter_by(name=name).first()
            start_year = payload['start_year']
            start_month = payload['start_month']
            start_date = payload['start_date']
            end_year = payload['end_year']
            end_month = payload['end_month']
            end_date = payload['end_date']
            search_stock = payload['search_stock']
            if user_info == None:
                return jsonify({'Warning': 'User isn\'t exist! You need register in my web first'})
            elif user_info.api_code != api_code:
                return jsonify({'Warning': 'Api code isn\'t match!'})
            elif user_info.api_code == api_code:
                start = datetime.datetime(int(start_year), int(start_month), int(start_date))
                end = datetime.datetime(int(end_year), int(end_month), int(end_date))
                stock = search_stock
                result = web.DataReader(stock,'yahoo',start,end)

                result_use = result.reset_index().to_json(None, orient="records", date_format='iso')
                
                return jsonify({'Data': result_use })
            else:
                return jsonify({'Warning': 'Please check the input information!'})
        except:
            return jsonify({'Warning': 'Please check the input information!'})




