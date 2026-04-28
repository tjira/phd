import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

# Aspect ratio tuned for a taller surface
res = 200
x = np.linspace(-20, 20, res)
y = np.linspace(-25, 25, res) # Taller range
X, Y = np.meshgrid(x, y)

# More dramatic, vertical-friendly potential surface
Z = (4.0 * np.sin(0.15 * X) * np.cos(0.2 * Y) +
     3.0 * np.cos(0.1 * X + 0.3 * Y) +
     2.0 * np.exp(-(X**2 + Y**2) / 150) * 8)

Z -= 3.0 * np.exp(-((X-5)**2 + (Y+10)**2) / 100)
Z += 0.1 * X - 0.05 * Y 

fig = plt.figure(figsize=(15, 20)) # Taller figure
ax = fig.add_subplot(111, projection='3d')
ax.axis("off")

# Set background to transparent
fig.patch.set_alpha(0)
ax.patch.set_alpha(0)

# Sparser grid for a technical look
surf = ax.plot_surface(X, Y, Z, 
                       cmap="PuBu_r", 
                       edgecolor='#0f172a', 
                       linewidth=0.3, 
                       antialiased=True, 
                       alpha=0.98,
                       rcount=25, ccount=15) 

# Dynamic low-angle view
ax.view_init(elev=35, azim=-60)
ax.set_zlim(-15, 20)

import os
os.makedirs("frontmatter/pdf", exist_ok=True)
plt.savefig("frontmatter/pdf/wave.pdf", transparent=True, bbox_inches='tight', pad_inches=0, dpi=400)
plt.close()

