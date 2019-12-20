from builtins import int

from flask import Blueprint, request, flash, redirect, url_for, render_template, make_response, session
from flask_login import current_user, login_user, login_required
from models import User

from __init__ import db

import pandas as pd
import pandas_datareader.data as web
import datetime, sys, io
from io import StringIO

import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from tkinter import *
from tkinter.messagebox import showinfo
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

from pandas.plotting import register_matplotlib_converters


from stock.forms import StockForm, StockSelectForm

stock = Blueprint('stock', __name__)

pd.set_option('display.max_rows', 9999)
pd.set_option('display.max_columns',  9999)

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
                result = web.DataReader(stock, 'yahoo', start, end)
                # df = pd.DataFrame(column.values, columns=['選擇', '股票代號', '時間', '成交', '買進', '賣出', '漲跌', '張數', '昨收', '開盤', '最高', '最低'])
                session['result'] = result.to_json()

            except Exception as e:
                print('error====', e)
                flash('Type error!', 'warning')
                return redirect(url_for('stock.collect'))

            return render_template('stock_result.html', data=result.to_html())
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('stock.html', form=form)

def make_figure(result, type):
    try:
        data = result[type]
        register_matplotlib_converters()

        photo = Figure()
        axis = photo.add_subplot(1, 1, 1)
        xs = data.index
        ys = data.values
        axis.plot(xs, ys)
        canvas = FigureCanvas(photo)
        output = io.BytesIO()
        canvas.print_png(output)
        if type == 'Adj Close':
            photo.savefig('static/Adj_Close.png')
        photo.savefig('static/' + type + '.png')
    except Exception as e:
        print('error====', e)

@stock.route("/stock/high")
def highplot():
    try:
        type = 'High'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/High.png'
        session.pop('result', None)
        return render_template('stock_result_high.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))

@stock.route("/stock/low")
def lowplot():
    try:
        type = 'Low'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/Low.png'
        session.pop('result', None)
        return render_template('stock_result_fig.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))

@stock.route("/stock/open")
def openplot():
    try:
        type = 'Open'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/Open.png'
        session.pop('result', None)
        return render_template('stock_result_fig.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))

@stock.route("/stock/close")
def closeplot():
    try:
        type = 'Close'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/Close.png'
        session.pop('result', None)
        return render_template('stock_result_fig.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))

@stock.route("/stock/volumn")
def volumnplot():
    try:
        type = 'Volumn'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/Volumn.png'
        session.pop('result', None)
        return render_template('stock_result_fig.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))

@stock.route("/stock/adj_close")
def adjcloseplot():
    try:
        type = 'Adj Close'
        result = pd.read_json(session['result'])
        make_figure(result, type)
        image = '/static/Adj_Close.png'
        session.pop('result', None)
        return render_template('stock_result_fig.html', data=result.to_html(), image=image)

    except Exception as e:
        print('error====', e)
        flash('debugging!', 'warning')
        return redirect(url_for('stock.collect'))
