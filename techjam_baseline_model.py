import numpy as np
import pandas as pd
import datetime
import os
os.chdir('D:/a_test/techjam/data_pack')

### Read file
demo = pd.read_csv('demographics.csv').drop_duplicates(subset = ['id'])
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

# Concat data

train_df = train.merge(demo, left_on = 'id', right_on = 'id', how = 'left')
test_df = test.merge(demo, left_on = 'id', right_on = 'id', how = 'left')

model = pd.DataFrame(train_df.groupby(['age','ocp_cd'])['income'].median()).reset_index()

sub = test_df.merge(model, 
                    left_on = ['age', 'ocp_cd'],
                    right_on = ['age', 'ocp_cd'],
                    how = 'left')
