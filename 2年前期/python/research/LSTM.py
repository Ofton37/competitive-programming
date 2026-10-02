import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from sklearn.preprocessing import MinMaxScaler

# 1. サンプルデータの作成（サイン波）
data = np.sin(np.linspace(0, 100, 1000))
data = data.reshape(-1, 1)

# 2. データの正規化（LSTMは0~1の範囲にスケールするのが一般的）
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_data = scaler.fit_transform(data)

# 3. 学習用データの作成（過去50ステップから次を予測）
def create_dataset(dataset, look_back=50):
    X, Y = [], []
    for i in range(len(dataset) - look_back):
        X.append(dataset[i:(i + look_back), 0])
        Y.append(dataset[i + look_back, 0])
    return np.array(X), np.array(Y)

look_back = 50
X, y = create_dataset(scaled_data, look_back)

# LSTMの入力形式 [サンプル数, タイムステップ, 特徴量数] に変換
X = np.reshape(X, (X.shape[0], X.shape[1], 1))

# 4. モデルの構築
model = Sequential([
    LSTM(50, activation='tanh', input_shape=(look_back, 1)),
    Dense(1) # 出力層（次の値を1つ予測）
])

model.compile(optimizer='adam', loss='mse')

# 5. 学習
model.fit(X, y, epochs=20, batch_size=32, verbose=1)

print("モデルの構築と学習が完了しました！")