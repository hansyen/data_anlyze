#-*- coding: cp950 -*-
from builtins import staticmethod, type

import flask
import requests
from bs4 import BeautifulSoup

class GetWebInfo:
    @staticmethod
    def class_stock(url):
        html = requests.get(url)
        # html.encoding = "big5"
        

        sp = BeautifulSoup(html.text, "html.parser")

        data = sp.find_all("table")

        result = data[4].text
        result = result.replace("\n \n\n", "@")
        result = result.replace("\n\n\n\n", "@")
        result = result.replace("\n\n", "\n")
        result = result.replace("\n", ",")
        result = result.replace("@", "\n")
        list_result = result.split("\n")

        return list_result

