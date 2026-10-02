import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

# --- 設定 ---
N = 60
EMPTY, HEAD, TAIL, WIRE = 0, 1, 2, 3
cmap = ListedColormap(['#000000', '#0077ff', '#ff4500', '#ffd700'])

# --- グリッドの構築 ---
grid = np.zeros((N, N), dtype=int)

# 1. マスタークロック (中央のループ)
grid[25:30, 10] = WIRE
grid[25:30, 14] = WIRE
grid[25, 10:15] = WIRE
grid[29, 10:15] = WIRE

# 2. 信号の分岐 (T字路)
grid[27, 14:25] = WIRE # メインワイヤー
grid[10:45, 25] = WIRE # 垂直方向の分岐

# 3. 二つの同期した出力先へのワイヤー
grid[10, 25:50] = WIRE # 出力1
grid[45, 25:50] = WIRE # 出力2

# 4. 初期信号
grid[25, 10] = HEAD
grid[25, 11] = TAIL

# --- 描画 ---
fig, ax = plt.subplots(figsize=(10, 6))
img = ax.imshow(grid, cmap=cmap, vmin=0, vmax=3, interpolation='nearest')
ax.axis('off')
ax.set_title("Synchronized Dual Clocks (Wireworld)")

def update(frame):
    global grid
    new_grid = grid.copy()
    head_mask = (grid == HEAD).astype(int)
    
    # 周囲8マスのヘッドをカウント (np.rollによる高速計算)
    total_heads = (
        np.roll(head_mask, 1, 0) + np.roll(head_mask, -1, 0) +
        np.roll(head_mask, 1, 1) + np.roll(head_mask, -1, 1) +
        np.roll(head_mask, (1, 1), (0, 1)) + np.roll(head_mask, (1, -1), (0, 1)) +
        np.roll(head_mask, (-1, 1), (0, 1)) + np.roll(head_mask, (-1, -1), (0, 1))
    )
    
    # ワイヤーワールド基本ルール
    new_grid[grid == HEAD] = TAIL
    new_grid[grid == TAIL] = WIRE
    wire_mask = (grid == WIRE)
    new_grid[wire_mask & ((total_heads == 1) | (total_heads == 2))] = HEAD
    
    img.set_data(new_grid)
    grid = new_grid
    return img,

ani = animation.FuncAnimation(fig, update, frames=200, interval=80, blit=True)
plt.show()