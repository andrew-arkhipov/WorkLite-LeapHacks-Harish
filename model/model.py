# WorkLite Regression Model

import pandas as pd
import pickle
import random
from sklearn import linear_model
from sklearn.model_selection import train_test_split

def create_data():
    
    columns = ['location', 'severity','ambulance', 'drunk driver', 'pain level', 'emotional distress', \
           'passengers', 'at fault', 'accident type', 'roll over', 'claim']
    location = ['intersection', 'highway', 'stoplight']
    accident_type = ['t-bone', 'head-on', 'rear-end']
    
    data = pd.DataFrame(columns = columns)
    
    for i in range(1001):
        temp = {'location': location[random.randint(0, 2)], 'severity': 0, 
            'ambulance': random.choice([0, 1]), 'drunk driver': random.choice([0, 1]),
            'pain level': round(random.random(), 4), 'emotional distress': round(random.random(), 4),
             'passengers': random.randint(0, 5), 'at fault': random.choice([0, 1]), 'accident type':
             accident_type[random.randint(0, 2)], 'roll over': random.choice([0, 1])}
        data.loc[i] = pd.Series(temp) 
    
    for col in ['location', 'accident type']:
        data = pd.concat([data, pd.get_dummies(data[col], prefix = col)], axis = 1).drop(col, axis = 1)
    
    weights = {'severity': 5000, 'ambulance': 2000, 'drunk driver': 20000, 'pain level': 2000,
           'emotional distress': 500, 'passengers': 100, 'at fault': -10000, 'roll over': 5000,
           'location_highway': 3000, 'location_intersection': 3000, 'location_stoplight': 1500,
           'accident type_head-on': 7000, 'accident type_rear-end': 2000, 'accident type_t-bone': 5000}
    
    for i in range(1001):
        data.loc[i,'claim'] = (data.loc[i,'severity'])*(weights['severity']*random.gauss(1, .1)) + \
                              (data.loc[i,'ambulance'])*(weights['ambulance']) + \
                              (data.loc[i,'drunk driver'])*(weights['drunk driver']*random.gauss(1, .1)) + \
                              (data.loc[i,'pain level'])*(weights['pain level']*random.gauss(1, .1)) + \
                              (data.loc[i,'emotional distress'])*(weights['emotional distress']*random.gauss(1, .1)) + \
                              (data.loc[i,'passengers'])*(weights['passengers']*random.gauss(1, .1)) + \
                              (data.loc[i,'at fault'])*(weights['at fault']*random.gauss(1, .1)) + \
                              (data.loc[i,'roll over'])*(weights['roll over']*random.gauss(1, .1)) + \
                              (data.loc[i,'location_highway'])*(weights['location_highway']*random.gauss(1, .1)) + \
                              (data.loc[i,'location_intersection'])*(weights['location_intersection']*random.gauss(1, .1)) + \
                              (data.loc[i,'location_stoplight'])*(weights['location_stoplight']*random.gauss(1, .1)) + \
                              (data.loc[i,'accident type_head-on'])*(weights['accident type_head-on']*random.gauss(1, .1)) + \
                              (data.loc[i,'accident type_rear-end'])*(weights['accident type_rear-end']*random.gauss(1, .1)) + \
                              (data.loc[i,'accident type_t-bone'])*(weights['accident type_t-bone']*random.gauss(1, .1))
                           
    final_data_df = data.clip(lower = 0)

    return final_data_df

def train_model(data):
    
    X_train, X_test, y_train, y_test = train_test_split(data.drop(['claim'], axis = 1),
                                   data['claim'], random_state = 42, test_size = .2)
    ols = linear_model.LinearRegression()
    model = ols.fit(X_train, y_train)
    
    pickle.dump(model, open('modelparams.sav', 'wb'))

  
def main():
    
    data = create_data()
    train_model(data)
    
main()
    