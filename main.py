from flask import Flask
from flask import request
from flask import render_template
import pandas as pd
import csv

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template("new_order1.html")

@app.route('/', methods=['POST'])
def new_order1():
    id_order = request.form['id_order']
    id_car = request.form['id_car']
    id_driver = request.form['id_driver']
    id_company = request.form['id_company']
    id_person = request.form['id_person']
    id_types = request.form['id_types']
    #data = pd.read_csv('templates/orders.csv')
    order = [id_car, id_order, id_driver, id_person, id_company,id_types]
    print(order)#check reading
    filename = order[0] + "_order.csv"
    f = open(filename, 'w')#make table
    return new_order2()

