from builtins import int

from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import current_user, login_user, login_required
from models import User

from __init__ import db

import pandas as pd
import pandas_datareader.data as web
import datetime, sys

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter.messagebox import showinfo
import numpy as np
import matplotlib.pyplot as plt

from stock.forms import StockForm, StockSelectForm

stock = Blueprint('stock', __name__)

pd.set_option('display.max_rows', 9999)
pd.set_option('display.max_columns',  9999)

result_info = {}
stocl_info = []
start_year = []
start_month = []
start_date = []
end_year = []
end_month = []
end_date = []

@login_required
@stock.route("/stock", methods=['GET', 'POST'])
def collect():
    if current_user.is_authenticated:
    
        form = StockForm()
        
        if form.validate_on_submit():
            try:
                start = datetime.datetime(int(form.start_year.data), int(form.start_month.data), int(form.start_date.data))
                end = datetime.datetime(int(form.end_year.data), int(form.end_month.data), int(form.end_date.data))
                stock = form.search_stock.data
                print('stock======', stock, type(stock))
                result = web.DataReader(stock, 'yahoo', start, end)
                # df = pd.DataFrame(column.values, columns=['選擇', '股票代號', '時間', '成交', '買進', '賣出', '漲跌', '張數', '昨收', '開盤', '最高', '最低'])
                result_info.update(result)
                stocl_info.append(form.search_stock.data)
                start_year.append(form.start_year.data)
                start_month.append(form.start_month.data)
                start_date.append(form.start_date.data)
                end_year.append(form.end_year.data)
                end_month.append(form.end_month.data)
                end_date.append(form.end_date.data)
                print('result========', result, type(result))
            except:
                flash('Type error!', 'warning')
                return redirect(url_for('stock.collect'))


            return render_template('stock_result.html', data=result.to_html())
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('stock.html', form=form)

@stock.route("/stock/high")
def highplot():
    
    stock_use = ''.join(stocl_info)
    start_year_use = ''.join(start_year)
    start_month_use = ''.join(start_month)
    start_date_use = ''.join(start_date)
    end_year_use = ''.join(end_year)
    end_month_use = ''.join(end_month)
    end_date_use = ''.join(end_date)
    start = datetime.datetime(int(start_year_use),int(start_month_use),int(start_date_use))
    end = datetime.datetime(int(end_year_use),int(end_month_use),int(end_date_use))
    stock = stock_use
    result = web.DataReader(stock,'yahoo',start,end)
    result['High'].plot()
    plt.show()
    
    # return redirect(url_for('stock.collect'))
    # plt.mainloop()  
    


   
