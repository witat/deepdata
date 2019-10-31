import numpy as np
import pandas as pd
import lightgbm as lgb
import seaborn as sns
from sklearn.metrics import mean_squared_log_error
from sklearn.model_selection import StratifiedKFold
import datetime
import os
os.chdir('D:/a_test/techjam/data_pack')


### Read file
demo = pd.read_csv('demographics.csv')
credit = pd.read_csv('cc.csv')
kplus = pd.read_csv('kplus.csv')
train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')

def edit_df(demo, credit, kplus, train, test):
    id_card = demo[['id','cc_no']]
    credit = id_card.merge(credit, 
                            left_on = 'cc_no', 
                            right_on = 'cc_no', 
                            how = 'left')
    # convert dtypes file
    demo['age_ocp'] = demo['age'] + demo['ocp_cd']
    demo.loc[:,['gender','ocp_cd','age']] = demo.loc[:,['age_ocp','gender','ocp_cd','age']].astype('category')
    
    demo['age_ocp'] = demo['age_ocp'].astype('category')
    credit['pos_dt'] = pd.to_datetime(credit['pos_dt'])
    credit = credit.dropna(subset = ['cc_txn_amt'])
    kplus['sunday'] = pd.to_datetime(kplus['sunday'])
    return demo, credit, kplus, train, test

demo, credit, kplus, train, test = edit_df(demo, credit, kplus, train, test)

# credit['week'] = credit.pos_dt.dt.week
# credit['weekday'] = credit.pos_dt.dt.weekday
credit['month'] = credit.pos_dt.dt.month
kplus['month'] = kplus.sunday.dt.month
# kplus_trn = kplus.groupby(['id','month'])['kp_txn_amt'].agg(['sum']).reset_index()
credit_trn = credit.groupby(['id','month'])['cc_txn_amt'].agg(['sum']).reset_index()
credit_trn = credit_trn.groupby(['id'])['sum'].agg(['min','max','mean','median','std']).reset_index()

kplus_trn = kplus.groupby(['id'])['kp_txn_amt'].agg(['min','max','mean','median','std']).reset_index()
# credit monthly


# train data final
demo_ = demo.drop_duplicates(subset = ['id'])

train_df = train.merge(kplus_trn, 
                        left_on = 'id', 
                        right_on = 'id', 
                        how = 'left')
train_df = train_df.merge(credit_trn, 
                        left_on = 'id', 
                        right_on = 'id', 
                        how = 'left',
                        suffixes = ('_kplus','_credit'))
train_df = train_df.merge(demo_, 
                        left_on = 'id', 
                        right_on = 'id', 
                        how = 'left')

test_df = test.merge(kplus_trn, 
                    left_on = 'id', 
                    right_on = 'id', 
                    how = 'left')
test_df = test_df.merge(credit_trn, 
                    left_on = 'id', 
                    right_on = 'id', 
                    how = 'left',
                    suffixes = ('_kplus','_credit'))
test_df = test_df.merge(demo_, 
                        left_on = 'id', 
                        right_on = 'id', 
                        how = 'left')

# train_df = train_df[(train_df.income >= 0) & (train_df.income < 15000)]
# Train model

features = [c for c in train_df.columns if c not in ['income','id','cc_no']]
target = train_df['income']

param = {
    'bagging_freq': 5,          
    'bagging_fraction': 0.8,   
    'boost_from_average':'false',   
    'boost': 'gbdt',             
    'feature_fraction': 1,     
    'learning_rate': 0.005,
    'max_depth': -1,             
    'metric':'mape',                
    'min_data_in_leaf': 20,     
    # 'min_sum_hessian_in_leaf': 10.0,
    'num_leaves': 32,            
    'num_threads': -1,              
    'tree_learner': 'serial',
    'objective': 'regression',
    'reg_alpha': 0.1, 
    'reg_lambda': 0.1,
    'verbosity': 1
}

folds = StratifiedKFold(n_splits=5, shuffle=False, random_state=1)
oof = np.zeros(len(train_df))
predictions = np.zeros(len(test_df))

for fold_, (trn_idx, val_idx) in enumerate(folds.split(train_df.values, target.values)):
    print("Fold {}".format(fold_))
    trn_data = lgb.Dataset(train_df.iloc[trn_idx][features], label=target.iloc[trn_idx])
    val_data = lgb.Dataset(train_df.iloc[val_idx][features], label=target.iloc[val_idx])
    clf = lgb.train(param, trn_data, 1000000, valid_sets = [trn_data, val_data], verbose_eval=5000, early_stopping_rounds = 2000)
    oof[val_idx] = clf.predict(train_df.iloc[val_idx][features], num_iteration=clf.best_iteration)
    # predictions += clf.predict(test_df[features], num_iteration=clf.best_iteration) / folds.n_splits

print("CV score: {:<8.5f}".format(mean_squared_log_error(target, oof)))
lgb.plot_importance(clf, importance_type='gain', max_num_features=20)
