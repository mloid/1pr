from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import csv
n=0
app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("new_order1.html")

@app.route('/', methods=['POST'])
def making_order():
    n+=0.0001
    id_order = n*10000
    car_type = request.form['car_type']
    #id_car = request.form['id_car']
    #https://overcoder.net/q/3301/%D0%B2%D1%8B%D0%B1%D0%B5%D1%80%D0%B8%D1%82%D0%B5-%D1%81%D1%82%D1%80%D0%BE%D0%BA%D0%B8-%D0%B2-dataframe-%D0%BD%D0%B0-%D0%BE%D1%81%D0%BD%D0%BE%D0%B2%D0%B5-%D0%B7%D0%BD%D0%B0%D1%87%D0%B5%D0%BD%D0%B8%D0%B9-%D0%B2-%D1%81%D1%82%D0%BE%D0%BB%D0%B1%D1%86%D0%B5-%D0%B2-%D0%BF%D0%B0%D0%BD%D0%B4%D0%B0%D1%85
    
    id_driver = request.form['id_driver']
    id_company = request.form['id_company']
    id_person = request.form['id_person']
    id_types = request.form['id_types']
    data = pd.read_csv('templates/orders.csv')
    order = [id_car, id_order, id_driver, id_person, id_company,id_types]
    print(order)#check reading
    filename = order[0] + "_order.csv"
    f = open(filename, 'w')#make table
    return new_order2()
