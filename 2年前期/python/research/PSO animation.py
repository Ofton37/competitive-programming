import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- 1. 最適化対象の関数 (Ackley Function: 局所解が多くて難しい関数) ---
def objective_function(x, y):
    return -20.0 * np.exp(-0.2 * np.sqrt(0.5 * (x**2 + y**2))) - \
           np.exp(0.5 * (np.cos(2 * np.pi * x) + np.cos(2 * np.pi * y))) + np.e + 20

# --- 2. PSOのパラメータ設定 ---
N_PARTICLES = 30
W, C1, C2 = 0.9, 0.8, 0.1
LIMIT = 5  # 探索範囲 (-5 から 5)

# 粒子の初期化
pos = np.random.uniform(-LIMIT, LIMIT, (N_PARTICLES, 2))
vel = np.random.standard_normal((N_PARTICLES, 2)) * 0.1
pbest = pos.copy()
pbest_score = np.array([objective_function(p[0], p[1]) for p in pos])
gbest = pbest[np.argmin(pbest_score)]
gbest_score = np.min(pbest_score)

# --- 3. 描画の準備 ---
fig, ax = plt.subplots(figsize=(8, 6))
# 背景に等高線を描画
x_range = np.linspace(-LIMIT, LIMIT, 100)
y_range = np.linspace(-LIMIT, LIMIT, 100)
X, Y = np.meshgrid(x_range, y_range)
Z = objective_function(X, Y)
ax.contourf(X, Y, Z, levels=20, cmap='viridis', alpha=0.6)

# 粒子の描画 (散布図)
scat = ax.scatter(pos[:, 0], pos[:, 1], color='red', edgecolors='white', label='Particles')
gbest_dot = ax.plot(gbest[0], gbest[1], 'b*', markersize=15, label='Global Best')[0]
ax.set_title("Particle Swarm Optimization (PSO)")
ax.legend()

# --- 4. 更新関数 ---
def update(frame):
    global pos, vel, pbest, pbest_score, gbest, gbest_score
    
    r1, r2 = np.random.rand(2)
    # 速度と位置の更新
    vel = W * vel + C1 * r1 * (pbest - pos) + C2 * r2 * (gbest - pos)
    pos += vel
    
    # 範囲外に出ないように制限
    pos = np.clip(pos, -LIMIT, LIMIT)

    # 評価とベストの更新
    for i in range(N_PARTICLES):
        score = objective_function(pos[i, 0], pos[i, 1])
        if score < pbest_score[i]:
            pbest_score[i] = score
            pbest[i] = pos[i].copy()
            if score < gbest_score:
                gbest_score = score
                gbest = pos[i].copy()

    # 描画データの更新
    scat.set_offsets(pos)
    gbest_dot.set_data([gbest[0]], [gbest[1]])
    return scat, gbest_dot

# アニメーション実行
ani = animation.FuncAnimation(fig, update, frames=100, interval=50, blit=True)
plt.show()