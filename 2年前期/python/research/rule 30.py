import numpy as np
import matplotlib.pyplot as plt

# 設定
width = 101   # 横幅（奇数にすると中心から始めやすい）
steps = 50    # 何世代進めるか（縦の長さ）

# グリッドの初期化 (全 0)
# cells[世代, 位置]
cells = np.zeros((steps, width), dtype=int)

# 初期状態：真ん中のセルだけを 1 (黒) にする
cells[0, width // 2] = 1

# Rule 30 の定義 (バイナリを数値に変換した時の対応表)
# (左, 中, 右) のパターン -> 次の世代の中央の値
# 111->0, 110->0, 101->0, 100->1, 011->1, 010->1, 001->1, 000->0
rules = {
    (1, 1, 1): 0,
    (1, 1, 0): 0,
    (1, 1, 1): 0, # 重複修正: 101->0
    (1, 0, 1): 0,
    (1, 0, 0): 1,
    (0, 1, 1): 1,
    (0, 1, 0): 1,
    (0, 0, 1): 1,
    (0, 0, 0): 0,
}

# 世代交代の計算
for i in range(steps - 1):
    for j in range(width):
        # 左右の隣接セルを取得（端は 0 とみなす）
        left  = cells[i, (j - 1) % width]
        mid   = cells[i, j]
        right = cells[i, (j + 1) % width]
        
        # ルールを適用して次の行を決定
        cells[i + 1, j] = rules[(left, mid, right)]

# 描画
plt.figure(figsize=(10, 5))
plt.imshow(cells, cmap='binary', interpolation='nearest')
plt.axis('off')
plt.title("Wolfram Rule 30")
plt.show()