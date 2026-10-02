import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 設定
N = 100
STEPS_PER_FRAME = 5  # 少し遅くして動きを見やすくしました

grid = np.zeros((N, N))
x, y = N // 2, N // 2
direction = 0  # 0:上, 1:右, 2:下, 3:左

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

fig, ax = plt.subplots()
img = ax.imshow(grid, cmap='binary', interpolation='nearest')

# 蟻を「赤い点」として追加
ant_dot, = ax.plot(x, y, 'ro', markersize=5) 

def update(frame):
    global x, y, direction
    
    for _ in range(STEPS_PER_FRAME):
        if grid[y, x] == 0:
            direction = (direction + 1) % 4
            grid[y, x] = 1
        else:
            direction = (direction - 1) % 4
            
        
        x = (x + dx[direction]) % N
        y = (y + dy[direction]) % N

    # 盤面の更新
    img.set_data(grid)
    # 蟻の位置を更新
    ant_dot.set_data([x], [y])
    
    return img, ant_dot

ani = animation.FuncAnimation(fig, update, frames=200, interval=10, blit=True)
plt.show()