# -*- coding: utf-8 -*-
#
# Usage: Load all Taiwan stock code info from csv file
#
# TWSE equities = 上市證券
# TPEx equities = 上櫃證券
#

import csv
import os
import sys
from collections import namedtuple

if hasattr(sys, '_MEIPASS'):
# PyInstaller会创建临时文件夹temp
# 并把路径存储在_MEIPASS中
    #self.appPath = os.path.dirname(os.path.realpath(sys.executable))
    PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(sys.executable))
    TPEX_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'tpex_equities.csv')
    TWSE_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'twse_equities.csv')
else:
    #self.appPath, filename = os.path.split(os.path.abspath( __file__))
    PACKAGE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
    TPEX_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'codes', 'tpex_equities.csv')
    TWSE_EQUITIES_CSV_PATH = os.path.join(PACKAGE_DIRECTORY, 'codes', 'twse_equities.csv')

ROW = namedtuple('StockCodeInfo', ['type', 'code', 'name', 'ISIN', 'start',
                                   'market', 'group', 'CFI'])







codes = {}
tpex = {}
twse = {}


def read_csv(path, types):
    global codes, twse, tpex
    with open(path, newline='', encoding='utf_8') as csvfile:
        reader = csv.reader(csvfile)
        csvfile.readline()
        for row in reader:
            row = ROW(*(item.strip() for item in row))
            codes[row.code] = row
            if types == 'tpex':
                tpex[row.code] = row
            else:
                twse[row.code] = row


read_csv(TPEX_EQUITIES_CSV_PATH, 'tpex')
read_csv(TWSE_EQUITIES_CSV_PATH, 'twse')
