import alibi
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from alibi_detect.cd import TabularDrift
import pandas as pd

wine_data = load_wine()
feature_names = wine_data.feature_names
X,y =wine_data.data, wine_data.target
X_ref, X_test, y_ref, y_test = train_test_split(X, y, test_size=0.50, random_state= 42)

cd = TabularDrift(X_ref = X_ref, p_val= .05)
preds = cd.predict(X_test)
labels = ['No', 'Yes']
print('Drift: {}'.format(labels[preds['data']['is_drift']]))

from alibi_detect.cd import MMDDriftOnline
ert = 50
window_size = 10
cd = MMDDriftOnline(X_ref, ert, window_size, backend='pytorch', n_bootstraps= 2500)
