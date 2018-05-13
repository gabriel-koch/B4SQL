# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 01:30:24 2017

@author: Hugo
Edited by: Koch
"""
import math
import pandas as pd  
from sqlalchemy import create_engine


def bendford (table, column,  
              server='mysql://root:@localhost/cadastro', digit=1):
    '''Plots bendfords law for a given SQL table or querry'''
    con = create_engine(server)  #http://docs.sqlalchemy.org/en/latest/core/engines.html get
    df = pd.read_sql(table, con)

    df = df[(df[column] != 0)] #Drop rows with values = 0 or '' 
    sr_frtd = df[column].astype(str).str.slice(digit -1 ,digit) #Creates a series with only the first digit 
    sr_frtd = sr_frtd[(sr_frtd) != '']

    dig_count = sr_frtd.groupby(lambda x: sr_frtd[x]).count().astype(float) #Count how many times each first digit appear
    dig_perc = dig_count.divide(len(sr_frtd)) #Transform it into percent  

    #Create the values for Bendford's Law:   
    if digit==1:
        numbers = [int(n) for n in range(1, 10)] #List from 1 to 10
        benford = [math.log10(1 + 1 / d) for d in numbers] #List with the values proposed by Benford's law 1 to 10    
    if digit==2:
        numbers = [int(n) for n in range(0, 10)] #List from 0 a 10
        benford = [0.11968,0.11389,0.10882,0.10433,0.10031,
                   0.09668,0.09337,0.09035,0.08757,0.08500] #List with the values proposed by Benford's law 0 to 10
    
    df_out = pd.DataFrame({'Data':dig_perc, "Benford's":benford})
    
    return df_out.plot(kind='bar')
    


lists = (('posts','author_id'),
         ('posts','id'))

for a,b in lists:
    bendford(a,b)


