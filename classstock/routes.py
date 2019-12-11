from builtins import type, len, range, int, list
from io import open
from flask import Blueprint, request, flash, redirect, url_for, render_template
from flask_login import login_user, logout_user, current_user, login_required
from bs4 import BeautifulSoup

import requests
import numpy as np
import pandas as pd


classstock = Blueprint('classstock', __name__)

def get_big_data():
    file = pd.read_csv('GL2018.txt')
    # print('file=======', dir(file))
    # for value in file.values:
    #     print('value=======', value)
    df = pd.DataFrame(file.values, columns=['date', 'number_of_game', 'day_of_week', 'v_name', 'v_league', 'v_game_number', 'h_name', 'h_league',
                                            'h_game_number', 'v_score', 'h_score', 'length_outs', 'day_night', 'completion', 'forefeit', 'protest', 'park_id', 'attendance'
                                            , 'length_minutes', 'v_line_score', 'h_line_score', 'v_at_bats', 'v_hits', 'v_doubles', 'v_triples', 'v_homeruns', 'v_sacrifice_hits',
                                            'v_sacrifice_flies', 'v_hit_by_pitch', 'v_walks', 'v_intentional walks	', 'v_strikeouts', 'v_stolen_bases', 'v_caught_stealing',
                                            'v_grounded_into_double', 'v_first_catcher_interference', 'v_left_on_base', 'v_pitchers_used', 'v_individual_earned_runs',
                                            'v_team_earned_runs', 'v_wild_pitches', 'v_balks', 'v_putouts', 'v_assists', 'v_errors', 'v_passed_balls', 'v_double_plays',
                                            'v_triple_plays', 'h_at_bats', 'h_hits', 'h_doubles', 'h_triples', 'h_homeruns', 'h_sacrifice_hits', 'h_sacrifice_flies', 'h_hit_by_pitch',
                                            'h_walks', 'h_intentional walks', 'h_strikeouts', 'h_stolen_bases', 'h_caught_stealing', 'h_grounded_into_double', 'h_first_catcher_interference',
                                            'h_left_on_base', 'h_pitchers_used', 'h_individual_earned_runs', 'h_team_earned_runs', 'h_wild_pitches', 'h_balks', 'h_putouts',
                                            'h_assists', 'h_errors', 'h_passed_balls', 'h_double_plays', 'h_triple_plays', 'hp_umpire_id', 'hp_umpire_name', '1b_umpire_id',
                                            '1b_umpire_name', '2b_umpire_id', '2b_umpire_name', '3b_umpire_id', '3b_umpire_name', 'lf_umpire_id', 'lf_umpire_name',
                                            'rf_umpire_id', 'rf_umpire_name', 'v_manager_id', 'v_manager_name', 'h_manager_id', 'h_manager_name', 'winning_pitcher_id',
                                            'winning_pitcher_name', 'losing_pitcher_id', 'losing_pitcher_name', 'saving_pitcher_id', 'saving_pitcher_name', 'winning_rbi_batter_id',
                                            'winning_rbi_batter_id_name', 'v_starting_pitcher_id', 'v_starting_pitcher_name', 'h_starting_pitcher_id', 'h_starting_pitcher_name',
                                            'v_player_1_id', 'v_player_1_name', 'v_player_1_def_pos', 'v_player_2_id', 'v_player_2_name', 'v_player_2_def_pos',
                                            'v_player_3_id', 'v_player_3_name', 'v_player_3_def_pos', 'v_player_4_id', 'v_player_4_name', 'v_player_4_def_pos',
                                            'v_player_5_id', 'v_player_5_name', 'v_player_5_def_pos', 'v_player_6_id', 'v_player_6_name', 'v_player_6_def_pos',
                                            'v_player_7_id', 'v_player_7_name', 'v_player_7_def_pos', 'v_player_8_id	', 'v_player_8_name', 'v_player_8_def_pos',
                                            'v_player_9_id', 'v_player_9_name', 'v_player_9_def_pos', 'h_player_1_id', 'h_player_1_name', 'h_player_1_def_pos',
                                            'h_player_2_id', 'h_player_2_name', 'h_player_2_def_pos', 'h_player_3_id', 'h_player_3_name', 'h_player_3_def_pos',
                                            'h_player_4_id', 'h_player_4_name', 'h_player_4_def_pos', 'h_player_5_id', 'h_player_5_name', 'h_player_5_def_pos',
                                            'h_player_6_id', 'h_player_6_name', 'h_player_6_def_pos', 'h_player_7_id', 'h_player_7_name', 'h_player_7_def_pos',
                                            'h_player_8_id', 'h_player_8_name', 'h_player_8_def_pos', 'h_player_9_id', 'h_player_9_name', 'h_player_9_def_pos',
                                            'additional_info', 'acquisition_info'])
    print('df=========', df)

    return file

def get_web(url):
    result = requests.get(url)
    data = pd.read_html(result.text)
    for column in data:
        if '選擇' in column.columns:
            df = pd.DataFrame(column.values, columns=['選擇', '股票代號', '時間', '成交', '買進', '賣出', '漲跌', '張數', '昨收', '開盤', '最高', '最低'])
            print('df=========', df, type(df))
            data = column.values
    df.to_html('templates/classstock/test.html')
    return data

@classstock.route("/class_stock")
def class_stock():
    if current_user.is_authenticated:
        return render_template('classstock/classstock.html')
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))

@classstock.route("/classstock_a", methods=['GET', 'POST'])
def classstock_a():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
        data = get_web(url)
        # file = get_big_data()
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_a_write", methods=['GET', 'POST'])
def classstock_a_write():
    src = "https://tw.stock.yahoo.com/s/list.php?c=%A4%F4%AAd&rr=0.60494800%201544016777"
    html = requests.get(src)
    html.encoding = "cp950"

    sp = BeautifulSoup(html.text, "html.parser")

    data1 = sp.find_all("table")
    # print('data1[5].text======', data1[5].text)
    a = data1[4].text
    # a = datatest[4].table
    # result_list = []
    # for result in a:
    #     result_list.append(result)

    a = a.replace("\n \n\n", "@")
    a = a.replace("\n\n\n\n", "@")
    a = a.replace("\n\n", "\n")
    a = a.replace("\n", ",")
    a = a.replace("@", "\n")
    # print(pdtest)
    file = open('class a.txt', 'a')
    file.write(a)
    file.close()
    return redirect(url_for('classstock.classstock_a'))


@classstock.route("/classstock_b", methods=['GET', 'POST'])
def classstock_b():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AD%B9%AB%7E&rr=0.35528600%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_c", methods=['GET', 'POST'])
def classstock_c():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B6%EC%BD%A6&rr=0.35528700%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_d", methods=['GET', 'POST'])
def classstock_d():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AF%BC%C2%B4&rr=0.35528900%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_e", methods=['GET', 'POST'])
def classstock_e():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_f", methods=['GET', 'POST'])
def classstock_f():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_g", methods=['GET', 'POST'])
def classstock_g():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%BE%F7&rr=0.35529000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_h", methods=['GET', 'POST'])
def classstock_h():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A5%CD%A7%DE%C2%E5%C0%F8&rr=0.35529400%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_i", methods=['GET', 'POST'])
def classstock_i():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AC%C1%BC%FE&rr=0.35529600%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_j", methods=['GET', 'POST'])
def classstock_j():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B3y%AF%C8&rr=0.35529700%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_k", methods=['GET', 'POST'])
def classstock_k():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%BF%FB%C5K&rr=0.35529800%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_l", methods=['GET', 'POST'])
def classstock_l():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%BE%F3%BD%A6&rr=0.35530000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_m", methods=['GET', 'POST'])
def classstock_m():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A8T%A8%AE&rr=0.35530100%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_n", methods=['GET', 'POST'])
def classstock_n():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A5b%BE%C9%C5%E9&rr=0.35530200%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_o", methods=['GET', 'POST'])
def classstock_o():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%B8%A3%B6g%C3%E4&rr=0.35530300%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_p", methods=['GET', 'POST'])
def classstock_p():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A5%FA%B9q&rr=0.35530500%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_q", methods=['GET', 'POST'])
def classstock_q():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B3q%ABH%BA%F4%B8%F4&rr=0.35530600%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_r", methods=['GET', 'POST'])
def classstock_r():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B9s%B2%D5%A5%F3&rr=0.35530700%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_s", methods=['GET', 'POST'])
def classstock_s():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B9q%A4l%B3q%B8%F4&rr=0.35530900%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_t", methods=['GET', 'POST'])
def classstock_t():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B8%EA%B0T%AAA%B0%C8&rr=0.35531000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_u", methods=['GET', 'POST'])
def classstock_u():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5%A6%B9q%A4l&rr=0.35531100%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_v", methods=['GET', 'POST'])
def classstock_v():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%C0%E7%AB%D8&rr=0.35531200%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_w", methods=['GET', 'POST'])
def classstock_w():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AF%E8%B9B&rr=0.35531400%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_x", methods=['GET', 'POST'])
def classstock_x():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%C6%5B%A5%FA&rr=0.35531500%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_y", methods=['GET', 'POST'])
def classstock_y():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AA%F7%BF%C4&rr=0.35531600%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_z", methods=['GET', 'POST'])
def classstock_z():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%B6T%A9%F6%A6%CA%B3f&rr=0.35531700%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_A", methods=['GET', 'POST'])
def classstock_A():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AAo%B9q%BFU%AE%F0&rr=0.35531800%201535770407h"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_B", methods=['GET', 'POST'])
def classstock_B():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%E4%A5L&rr=0.35532000%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_C", methods=['GET', 'POST'])
def classstock_C():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A6s%B0U%BE%CC%C3%D2&rr=0.35532100%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_F", methods=['GET', 'POST'])
def classstock_F():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%AB%FC%BC%C6%C3%FE&rr=0.35532500%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_G", methods=['GET', 'POST'])
def classstock_G():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=ETF&rr=0.35532600%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)

@classstock.route("/classstock_H", methods=['GET', 'POST'])
def classstock_H():
    if current_user.is_authenticated:
        url = "https://tw.stock.yahoo.com/s/list.php?c=%A8%FC%AFq%C3%D2%A8%E9&rr=0.35532700%201535770407"
        data = get_web(url)
    else:
        flash('You need login!', 'warning')
        return redirect(url_for('main.home'))
    return render_template('classstock/data_result.html', data=data)
