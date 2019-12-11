#-*- coding: cp950 -*-
from builtins import staticmethod, dict

from __init__ import db
from models import User
# import sys

import flask
from flask_restful import Resource
from urllib import parse
from flask import request, jsonify

from utils import GetWebInfo

# reload(sys)
# sys.setdefaultencoding('utf-8')

class ClassStockResource(Resource):
    @staticmethod
    def get():
        payload = dict(parse.parse_qsl(parse.urlsplit(request.url).query))
        
        
        try:
            name = payload['account_name']
            api_code = payload['api_code']
            choose_stock = payload['stock_number']
            user_info = User.query.filter_by(name=name).first()
            if user_info == None:
                return jsonify({'Warning': 'User isn\'t exist! You need register in my web first'})
            elif user_info.api_code != api_code:
                return jsonify({'Warning': 'Api code isn\'t match!'})
            elif user_info.api_code == api_code:
                if choose_stock == '1':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '2':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AD%B9%AB%7E&rr=0.35528600%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '3':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.35528700%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '4':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AF%BC%C2%B4&rr=0.35528900%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '5':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '6':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%B9%B9q%C6l&rr=0.35529200%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '7':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A4%C6%BE%C7&rr=0.35529300%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '8':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A5%CD%A7%DE%C2%E5%C0%F8&rr=0.35529400%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '9':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AC%C1%BC%FE&rr=0.35529600%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '10':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B3y%AF%C8&rr=0.35529700%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '11':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%BF%FB%C5K&rr=0.35529800%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '12':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%BE%F3%BD%A6&rr=0.35530000%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '13':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A8T%A8%AE&rr=0.35530100%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '14':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9&rr=0.35530200%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '15':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%B8%A3%B6g%C3%E4&rr=0.35530300%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '16':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A5%FA%B9q&rr=0.35530500%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '17':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B3q%ABH%BA%F4%B8%F4&rr=0.35530600%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '18':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B9s%B2%D5%A5%F3&rr=0.35530700%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '19':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B3q%B8%F4&rr=0.35530900%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '20':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B8%EA%B0T%AAA%B0%C8&rr=0.35531000%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '21':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5%A6%B9q%A4l&rr=0.35531100%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '22':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%C0%E7%AB%D8&rr=0.35531200%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '23':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AF%E8%B9B&rr=0.35531400%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '24':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%C6%5B%A5%FA&rr=0.35531500%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '25':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AA%F7%BF%C4&rr=0.35531600%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '26':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%B6T%A9%F6%A6%CA%B3f&rr=0.35531700%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '27':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AAo%B9q%BFU%AE%F0&rr=0.35531800%201535770407h"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '28':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5L&rr=0.35532000%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '29':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A6s%B0U%BE%CC%C3%D2&rr=0.35532100%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '30':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%AB%FC%BC%C6%C3%FE&rr=0.35532500%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '31':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=ETF&rr=0.35532600%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                elif choose_stock == '32':
                    url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%FC%AFq%C3%D2%A8%E9&rr=0.35532700%201535770407"
                    result = GetWebInfo.class_stock(url)
                    return jsonify({'Stock': result })
                else:
                    return jsonify({'Warning': 'Stock number out of range!'})
            else:
                return jsonify({'Warning': 'Please check the api information!'})
        except:
            return jsonify({'Warning': 'Please check the input information!'})


