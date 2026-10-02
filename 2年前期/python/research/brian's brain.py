import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- 設定 ---
N = 100
INTERVAL = 50

# 状態の定義
READY = 0      # 生存（次に興奮できる状態）
FIRING = 1     # 興奮（光っている状態）
REFRACTORY = 2 # 休息（興奮が終わって休んでいる状態）

# 色の設定: [0:黒(背景), 1:白(興奮), 2:青(休息)]
cmap = ListedColormap(['#1a1a1a', '#ffffff', '#0077ff'])

# --- 初期状態の生成 ---
# ランダムに配置
grid = np.random.choice([READY, FIRING, REFRACTORY], N*N, p=[0.85, 0.1, 0.05]).reshape(N, N)

fig, ax = plt.subplots(figsize=(8, 8))
img = ax.imshow(grid, cmap=cmap, interpolation='nearest', vmin=0, vmax=2)
ax.axis('off')
ax.set_title("Brian's Brain")

# --- 更新関数 ---
def update(frame):
    global grid
    new_grid = grid.copy()
    
    # 周囲8マスの「興奮(FIRING)」状態の数をカウントする
    # ライフゲームと同じようにロール（ずらし）を使って高速に計算
    firing_neighbors = (
        (grid == FIRING).astype(int)
    )
    
    # 上下左右斜めの合計を計算
    total_firing = (
        np.roll(firing_neighbors,  1, axis=0) + np.roll(firing_neighbors, -1, axis=0) +
        np.roll(firing_neighbors,  1, axis=1) + np.roll(firing_neighbors, -1, axis=1) +
        np.roll(firing_neighbors, ( 1,  1), axis=(0, 1)) + np.roll(firing_neighbors, ( 1, -1), axis=(0, 1)) +
        np.roll(firing_neighbors, (-1,  1), axis=(0, 1)) + np.roll(firing_neighbors, (-1, -1), axis=(0, 1))
    )

    # ルールの適用
    # 1. 興奮(FIRING) -> 休息(REFRACTORY)
    mask_firing = (grid == FIRING)
    new_grid[mask_firing] = REFRACTORY
    
    # 2. 休息(REFRACTORY) -> 生存(READY)
    mask_refractory = (grid == REFRACTORY)
    new_grid[mask_refractory] = READY
    
    # 3. 生存(READY) かつ 周囲の興奮が2つ -> 興奮(FIRING)
    mask_ready = (grid == READY)
    new_grid[mask_ready & (total_firing == 2)] = FIRING

    img.set_data(new_grid)
    grid = new_grid
    return img,

ani = animation.FuncAnimation(fig, update, frames=200, interval=INTERVAL, blit=True)
plt.show()