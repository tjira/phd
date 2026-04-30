import matplotlib.pyplot as plt, numpy as np

# Grid of points
X, Y = np.meshgrid(np.linspace(-20, 20, 256), np.linspace(-25, 25, 256))

# Complex wave function
Z = 4.0 * np.sin(0.15 * X) * np.cos(0.2 * Y) + 3.0 * np.cos(0.1 * X + 0.3 * Y) + 16.0 * np.exp(-(X**2 + Y**2) / 150)

# Add some localized features
Z -= 3.0 * np.exp(-((X - 5)**2 + (Y + 10)**2) / 100); Z += 0.1 * X - 0.05 * Y 

# Set up the 3D plot
fig, ax = plt.subplots(figsize=(15, 20), subplot_kw=dict(projection="3d"), constrained_layout=True)

# Remove axes
ax.axis("off")

# Sparser grid for a technical look
surf = ax.plot_surface(X, Y, Z, cmap="PuBu_r", edgecolor='#0f172a', linewidth=0.3, antialiased=True, alpha=0.98, rcount=25, ccount=15) 

# Dynamic low-angle view
ax.view_init(elev=35, azim=-60); ax.set_zlim(-15, 20)

# Save the figure with a transparent background and tight layout
plt.savefig("frontmatter/pdf/wave.pdf", transparent=True, bbox_inches="tight", pad_inches=0)
