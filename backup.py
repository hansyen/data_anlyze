#     # print(result_info, type(result_info))
#     # # result_info['High'].plot()
#     # plt.plot.result_info('High')
#     # plt.ylabel('date')
#     # picture = plt.show()
#     return render_template('stock_plot.html', data=picture)
# lable=tk.Label(win, text="high is the highest price of the stock on that trading day")
# lable.grid(column=1,row=1)
#
# button=tk.Button(win,text="High",command=highplot)
# button.grid(column=0,row=1,padx=5,pady=5)
   
# def lowplot():
#     result['Low'].plot()
#
#     plt.show()

# lable=tk.Label(win, text="low is the lowest price of the stock on that trading day")
# lable.grid(column=1,row=2)

# button=tk.Button(win,text="Low",command=lowplot)
# button.grid(column=0,row=2,padx=5,pady=5)
    
# def openplot():
#     result['Open'].plot()
#
#     plt.show()

# lable=tk.Label(win, text="Open is the price of the stock at the beginning of the trading day (it need not be the closing price of the previous trading day)")
# lable.grid(column=1,row=3)

# button=tk.Button(win,text="Open",command=openplot)
# button.grid(column=0,row=3,padx=5,pady=5)

# def closeplot():
#     result['Close'].plot()
#
#     plt.show()

# lable=tk.Label(win, text="close is the price of the stock at closing time.")
# lable.grid(column=1,row=4)

# button=tk.Button(win,text="Close",command=closeplot)
# button.grid(column=0,row=4,padx=5,pady=5)

# def volumeplot():
#     result['Volume'].plot()
#
#     plt.show()
    
# lable=tk.Label(win, text="Volume indicates how many stocks were traded")
# lable.grid(column=1,row=5)

# button=tk.Button(win,text="Volume",command=volumeplot)
# button.grid(column=0,row=5,padx=5,pady=5)


# def adjcloseplot():
#     result['Adj Close'].plot()
#
#     plt.show()

# lable=tk.Label(win, text="Adjusted close is the closing price of the stock that adjusts the price of the stock for corporate actions")
# lable.grid(column=1,row=6)

# button=tk.Button(win,text="Adj Close",command=adjcloseplot)
# button.grid(column=0,row=6,padx=5,pady=5)