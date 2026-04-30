import matplotlib.pyplot as plt, numpy as np

# High density for fine detail
X, Y = np.meshgrid(np.linspace(-25, 25, 600), np.linspace(-20, 20, 600))

# Base wave pattern
Z_wave = 0.9 * np.sin(0.5 * X) * np.cos(0.4 * Y) * np.exp(-(X**2 + Y**2) / 800)

# Left side features (back cover)
Z_left = (
    6.0 * np.exp(-((X + 18)**2 + (Y - 8)**2) / 30) +
    5.5 * np.exp(-((X + 15)**2 + (Y + 9)**2) / 25) +
    4.5 * np.exp(-((X + 12)**2 + (Y - 2)**2) / 20)
)

# Middle features (spine)
Z_middle = (
    2.0 * np.exp(-((X + 6)**2 + (Y - 12)**2) / 20) +
    2.5 * np.exp(-((X)**2 + (Y - 10)**2) / 20) +
    6.0 * np.exp(-((X)**2 + (Y + 10)**2) / 20)
)

# Right side features (front cover)
Z_right = (
    5.0 * np.exp(-((X - 8)**2 + (Y - 6)**2) / 15) +
    13.0 * np.exp(-((X - 16)**2 + (Y - 4)**2) / 12)
)

# Combine all components
Z = Z_wave + Z_left + Z_right + Z_middle

# Set up the plot
fig, ax = plt.subplots(subplot_kw={"projection": "3d"}, figsize=(24, 12), facecolor="#020617")

# Remove axes for a cleaner look
ax.axis("off")

# Plot the surface
ax.plot_surface(X, Y, Z, cmap="PuBu_r", edgecolor="#0f172a", linewidth=0.4, shade=False, rcount=60, ccount=60, antialiased=True)

# View adjustment
ax.view_init(elev=22, azim=-85); ax.set_zlim(-3, 16)

# Remove margins and save
plt.savefig("frontmatter/pdf/wave.pdf", transparent=True, bbox_inches="tight", pad_inches=0, dpi=300)
