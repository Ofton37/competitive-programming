import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 設定
N = 100  # グリッドサイズ (NxN)
ON = 255 # 生存
OFF = 0  # 死亡
vals = [ON, OFF]

# 1. 初期状態の生成 (ランダム)
grid = np.random.choice(vals, N*N, p=[0.2, 0.8]).reshape(N, N)

def update(frameNum, img, grid, N):
    # グリッドのコピーを作成（計算中に元のデータが変わらないようにするため）
    new_grid = grid.copy()
    
    for i in range(N):
        for j in range(N):
            # 周囲8マスの生存セル数を計算 (トーラス構造: 端と端がつながっている状態)
            total = int((grid[i, (j-1)%N] + grid[i, (j+1)%N] +
                         grid[(i-1)%N, j] + grid[(i+1)%N, j] +
                         grid[(i-1)%N, (j-1)%N] + grid[(i-1)%N, (j+1)%N] +
                         grid[(i+1)%N, (j-1)%N] + grid[(i+1)%N, (j+1)%N]) / 255)

            # ルールの適用
            if grid[i, j] == ON:
                if (total < 2) or (total > 3):
                    new_grid[i, j] = OFF
            else:
                if total == 3:
                    new_grid[i, j] = ON

    # データの更新
    img.set_data(new_grid)
    grid[:] = new_grid[:]
    return img,

# アニメーションの設定
fig, ax = plt.subplots()
img = ax.imshow(grid, interpolation='nearest', cmap='binary')
ani = animation.FuncAnimation(fig, update, fargs=(img, grid, N),
                              frames=10, interval=50, save_count=50)

plt.show()