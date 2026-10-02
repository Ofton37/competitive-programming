#Machine Learning competition
# Set up code checking
from learntools.core import binder
binder.bind(globals())
from learntools.machine_learning.ex7 import *

# Set up filepaths
import os
if not os.path.exists("../input/train.csv"):
    os.symlink("../input/home-data-for-ml-course/train.csv", "../input/train.csv")  
    os.symlink("../input/home-data-for-ml-course/test.csv", "../input/test.csv") 
    
    # Import helpful libraries
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split

# Load the data, and separate the target
iowa_file_path = '../input/train.csv'
home_data = pd.read_csv(iowa_file_path)
y = home_data.SalePrice

# Create X (After completing the exercise, you can return to modify this line!)
features = ['LotArea', 'YearBuilt', '1stFlrSF', '2ndFlrSF', 'FullBath', 'BedroomAbvGr', 'TotRmsAbvGrd']

# Select columns corresponding to features, and preview the data
X = home_data[features]
X.head()

# Split into validation and training data
train_X, val_X, train_y, val_y = train_test_split(X, y, random_state=1)

# Define a random forest model
rf_model = RandomForestRegressor(random_state=1)
rf_model.fit(train_X, train_y)
rf_val_predictions = rf_model.predict(val_X)
rf_val_mae = mean_absolute_error(rf_val_predictions, val_y)

print("Validation MAE for Random Forest Model: {:,.0f}".format(rf_val_mae))

# To improve accuracy, create a new Random Forest model which you will train on all training data
rf_model_on_full_data = RandomForestRegressor(random_state = 1)

# fit rf_model_on_full_data on all data from the training data
rf_model_on_full_data.fit(X,y)

import pandas as pd

# 1. パスの指定（エラーが出る場合はここをフルパスに書き換えます）
# 例: r'C:\Users\mngwd\OneDrive\デスクトップ\プログラマ\python\kaggle\input\test.csv'
test_data_path = '../input/test.csv'

# 2. ファイルの読み込み
test_data = pd.read_csv(test_data_path)

# 3. 特徴量の抽出
# ※注: 事前に features = ['LotArea', 'YearBuilt', ...] のように定義されている必要があります
test_X = test_data[features]

# 4. 予測の実行
# ※注: 事前に学習済みの rf_model が存在している必要があります
test_preds = rf_model.predict(test_X)