import numpy as np
import pandas as pd
from itertools import product
from math import sqrt
import xlrd

import gurobipy as gp
from gurobipy import GRB


fra_u_c = pd.read_excel('Utility_Chemical.xlsx', sheet_name='fra')
dpl_u_c = pd.read_excel('Utility_Chemical.xlsx', sheet_name='dpl')
upg_u_c = pd.read_excel('Utility_Chemical.xlsx', sheet_name='upg')



df_b = pd.read_excel('Price_Cost.xlsx', sheet_name='feedstock')
df_fra = pd.read_excel('Price_Cost.xlsx', sheet_name='bp-fra')
df_dpl = pd.read_excel('Price_Cost.xlsx', sheet_name='bp-dpl')
df_upg = pd.read_excel('Price_Cost.xlsx', sheet_name='bp-upg')
df_fp = pd.read_excel('Price_Cost.xlsx', sheet_name='final products')


df_c_fra =  pd.read_excel('Price_Cost.xlsx', sheet_name='cap-fra')
df_c_dpl =  pd.read_excel('Price_Cost.xlsx', sheet_name='cap-dpl')
df_c_upg =  pd.read_excel('Price_Cost.xlsx', sheet_name='cap-upg')


# read yield data

def excel2matrix(path,page):
    data = xlrd.open_workbook(path)
    table = data.sheets()[page]
    nrows = table.nrows  
    ncols = table.ncols
    datamatrix = np.zeros((nrows, ncols))
    for i in range(ncols):
        cols = table.col_values(i)
        datamatrix[:, i] = cols
    return datamatrix
