from __init__ import api

from api.class_stock import ClassStockResource
from api.stock import StockResource

api.add_resource(ClassStockResource, '/ohya/class_stock')
api.add_resource(StockResource, '/ohya/stock')
