import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://ubuntu@13.58.184.120:5432/project-3')

f_name = '2018_h1.csv  H2017.csv  Master_H1b.csv  Master_H1b_utf8.csv'.replace('.csv', '').split('  ')


for i in f_name:
    df = pd.read_csv('~/data/{}.csv'.format(i), sep=';')
    df.to_sql('{}'.format(i.replace('-', '_')), engine)
    