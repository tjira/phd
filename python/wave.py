import matplotlib.pyplot as plt, numpy as np

# High density for fine detail in the oscillations
X, Y = np.meshgrid(np.linspace(-11, 11, 512), np.linspace(-11, 11, 512))

# Wavefunction combining multiple sine and cosine waves with Gaussian peaks for visual interest
Z = (
    2.5 * np.sin(0.7 * X) * np.cos(0.5 * Y) +
    1.5 * np.cos(0.4 * X + 0.8 * Y) +
    1.0 * np.sin(1.2 * X) * np.sin(0.2 * Y) +
    6.0 * np.exp(-(X**2 + Y**2) / 800) +
    4.0 * np.exp(-((X - 45)**2 + (Y - 10)**2) / 400) +
    4.0 * np.exp(-((X + 45)**2 + (Y + 10)**2) / 400)
)

# Set up the 3D plot with a very wide aspect ratio
fig, ax = plt.subplots(figsize=(24, 8), subplot_kw={"projection": "3d"})

# Remove axes
ax.axis("off")

# Plot the surface
surf = ax.plot_surface(X, Y, Z, cmap="PuBu_r", edgecolor='#0f172a', linewidth=0.1, antialiased=True, alpha=1, rcount=30, ccount=30)

# Low-angle "horizon" view
ax.view_init(elev=18, azim=-75); ax.set_zlim(-8, 15)

# Save the figure with a transparent background
plt.savefig("frontmatter/pdf/wave.pdf", transparent=True, bbox_inches="tight", pad_inches=0)
