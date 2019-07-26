import numpy as np
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://ubuntu@18.218.203.43:5432/metis-project-3')

f_name = 'bank-additional-full.csv  bank-additional.csv  bank-full.csv  bank.csv'.replace('.csv', '').split('  ')


for i in f_name:
    df = pd.read_csv('~/metis-project-3/data/{}.csv'.format(i), sep=';')
#     engine = create_engine('postgresql://ubuntu@18.218.203.43:5432/metis-project-3')
    df.to_sql('{}'.format(i.replace('-', '_')), engine)
    