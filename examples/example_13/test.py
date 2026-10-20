import os, sys, numpy as np, matplotlib
print("解释器 :", sys.executable)
print("后端   :", matplotlib.get_backend())
print("PATH 里有 Library\\bin 吗 :",
      any("Library" in p and "bin" in p for p in os.environ["PATH"].split(os.pathsep)))
print("np.dot :", np.dot(np.eye(3), np.eye(3))[0][0])
