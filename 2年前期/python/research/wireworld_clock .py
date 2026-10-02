import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- パラメータ設定 ---
N = 40
EMPTY, HEAD, TAIL, WIRE = 0, 1, 2, 3

# 色の設定: 背景(黒), 電子頭(青), 電子尾(赤), 導体(黄)
cmap = ListedColormap(['#000000', '#0077ff', '#ff4500', '#ffd700'])

# --- グリッドの構築 ---
grid = np.zeros((N, N), dtype=int)

# 1. クロック（ループ構造）の作成
# 5x5の正方形ループを作成
grid[10:15, 10] = WIRE
grid[10:15, 14] = WIRE
grid[10, 10:15] = WIRE
grid[14, 10:15] = WIRE

# 2. 出力ワイヤー（クロックから信号を引き出す）
grid[12, 14:35] = WIRE

# 3. 初期信号の注入 (ループの中に電子を1つ置く)
grid[10, 10] = HEAD
grid[10, 11] = TAIL

# --- 描画準備 ---
fig, ax = plt.subplots(figsize=(8, 4))
img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
ax.axis('off')
ax.set_title("Wireworld: Clock Generator")

def update(frame):
    global grid
    new_grid = grid.copy()
    
    # 電子の頭の数をカウント (周囲8マス)
    head_mask = (grid == HEAD).astype(int)
    total_heads = (
        np.roll(head_mask,  1, axis=0) + np.roll(head_mask, -1, axis=0) +
        np.roll(head_mask,  1, axis=1) + np.roll(head_mask, -1, axis=1) +
        np.roll(head_mask, (1, 1), axis=(0, 1)) + np.roll(head_mask, (1, -1), axis=(0, 1)) +
        np.roll(head_mask, (-1, 1), axis=(0, 1)) + np.roll(head_mask, (-1, -1), axis=(0, 1))
    )
    
    # ルール適用
    # 頭 -> 尾
    new_grid[grid == HEAD] = TAIL
    # 尾 -> 導体
    new_grid[grid == TAIL] = WIRE
    # 導体 -> 頭 (周囲に頭が1つか2つある場合のみ)
    wire_mask = (grid == WIRE)
    new_grid[wire_mask & ((total_heads == 1) | (total_heads == 2))] = HEAD
    
    img.set_data(new_grid)
    grid = new_grid
    return img,

ani = animation.FuncAnimation(fig, update, frames=200, interval=100, blit=True)
plt.show()