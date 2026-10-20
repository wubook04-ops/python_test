import matplotlib
matplotlib.use('Agg')  # 改用 Tkinter 后端，避开 PyQt5 的 DLL 问题
import matplotlib.pyplot as plt
import numpy as np

plt.figure(figsize=(8, 6), dpi=80)
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
C, S = np.cos(X), np.sin(X)
plt.plot(X, C, color='blue', linewidth=1.0, linestyle='-', label='cos(x)')
plt.plot(X, S, color='green', linewidth=1.0, linestyle='-', label='sin(x)')
plt.xlim(-4.0, 4.0)
plt.ylim(-1.0, 1.0)
plt.xticks(np.linspace(-4, 4, 9, endpoint=True))
plt.yticks(np.linspace(-1, 1, 5, endpoint=True))
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('output.png', dpi=100)
print("✅ 图片已保存到 output.png")