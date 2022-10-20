# -*- coding: utf-8 -*-
"""
Created on Thu Aug 25 18:35:58 2022

@author: hp
"""

import numpy as np
from flask import Flask,request,render_template,jsonify
import pickle
app=Flask(__name__)
@app.route('/')
def home():
    return render_template(nindex.html)