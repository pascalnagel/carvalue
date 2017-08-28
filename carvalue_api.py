import pickle
import xgboost as xgb
import pandas as pd
import numpy as np
from scipy import stats

model = pickle.load(open("web_1_model.p", "rb"))

eps = 200
carspecs = pd.DataFrame(data=[{'seller': 'privat',
                                'offerType': 'Angebot',
                                'abtest': 'test',
                                'vehicleType': 'limousine',
                                'gearbox': 'manuell',
                                'powerPS': 156,
                                'model': 'a_klasse',
                                'kilometer': 25000+i*eps,
                                'fuelType': 'benzin',
                                'brand': 'mercedes_benz',
                                'notRepairedDamage': 'nein',
                                'age': 1037} for i in range(1000)], index=['predcar'+str(i) for i in range(1000)])

lbl = pickle.load(open("labelencoder.p", "rb"))

count = 0
for f in ['seller', 'offerType', 'abtest', 'vehicleType', 'gearbox', 'model', 'fuelType', 'brand', 'notRepairedDamage']:
    carspecs[f] = lbl[count].transform(list(carspecs[f].values))
    count += 1


predX = xgb.DMatrix(carspecs[['seller',
                              'offerType',
                              'abtest',
                              'vehicleType',
                              'gearbox',
                              'powerPS',
                              'model',
                              'kilometer',
                              'fuelType',
                              'brand',
                              'notRepairedDamage',
                              'age']])
predprice = np.exp(model.predict(predX))

slope, intercept, r_value, p_value, std_err = stats.linregress(np.linspace(25000,225000,1000), predprice)

print(-slope)
