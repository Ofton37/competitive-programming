import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# 1. データの読み込み
iris = load_iris()
X = iris.data
y = iris.target

# 2. 学習データとテストデータに分割
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. モデルの作成と学習
# n_estimators: 作成する決定木の数
# max_depth: 木の深さの最大値
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# 4. 予測と評価
y_pred = model.predict(X_test)

print(f"正解率: {accuracy_score(y_test, y_pred):.2f}")
print("\n分類レポート:")
print(classification_report(y_test, y_pred, target_names=iris.target_names))