import matplotlib as mpl, matplotlib.pyplot as plt, numpy as np

# Use PGF
mpl.use("pgf")

# Update matplotlib parameters
plt.rcParams.update({
    "pgf.texsystem": "lualatex",
    "pgf.preamble": "\n".join([
        r"\usepackage{braket}",
        r"\usepackage{unicode-math}",
        r"\setmainfont{Libertinus Serif}",
        r"\setmathfont{Libertinus Math}",
        r"\setsansfont{Libertinus Sans}"
    ]),
    "pgf.rcfonts": False
})

# Point of tangency
P = [0.5, 0]

# Manifold function
def f_manifold(x, y):
    return -1.0 * (x**2 + y**2)

def df_manifold_dx(x, y):
    return -1.0 * 2 * x

def df_manifold_dy(x, y):
    return -1.0 * 2 * y

# Tangent function
def f_tangent(x, y):
    return f_manifold(*P) + df_manifold_dx(*P) * (x - P[0]) + df_manifold_dy(*P) * (y - P[1])

# Tangent point
point = np.array([P[0], P[1], f_manifold(*P)])

# Create a grid of points
x_m, y_m = np.linspace(-1.5, 1.5, 64), np.linspace(-1.5, 1.5, 64); X_m, Y_m = np.meshgrid(x_m, y_m)
x_t, y_t = np.linspace(-0.8, 1.5,  2), np.linspace(-1.2, 1.5,  2); X_t, Y_t = np.meshgrid(x_t, y_t)

# Set up the 3D plot
fig, ax = plt.subplots(subplot_kw=dict(projection="3d"), constrained_layout=True); ax.set_axis_off()

# Plot the surface
ax.plot_surface(X_m, Y_m, f_manifold(X_m, Y_m), color="gray", alpha=0.6, rstride=1, cstride=1, linewidth=0)

# Plot the tangent plane
ax.plot_surface(X_t, Y_t, f_tangent(X_t, Y_t), color="lightblue", alpha=0.95, rstride=5, cstride=5, edgecolor="black", linewidth=0.5)

# Calculate the other two points on the plot
line1_end = np.array([P[0] - 0.8, P[1] + 0.8, f_tangent(P[0] - 0.8, P[1] + 0.8) + 0.0])
line2_end = np.array([P[0] - 0.8, P[1] + 0.8, f_tangent(P[0] - 0.8, P[1] + 0.8) + 8.0])

# Highlight the point of tangency
ax.plot3D([point[0]], [point[1]], [point[2]], color="black", marker="o", ms=3, zorder=10)

# Highlight the other points
ax.plot3D([line1_end[0]], [line1_end[1]], [line1_end[2]], color="black", marker="o", ms=3, zorder=10)
ax.plot3D([line2_end[0]], [line2_end[1]], [line2_end[2]], color="black", marker="o", ms=3, zorder=10)

# Draw lines between the points
ax.plot3D([point[0],     line1_end[0]], [point[1],     line1_end[1]], [point[2],     line1_end[2]], color="black", linewidth=1, linestyle="-",  zorder=10)
ax.plot3D([point[0],     line2_end[0]], [point[1],     line2_end[1]], [point[2],     line2_end[2]], color="black", linewidth=1, linestyle="-",  zorder=10)
ax.plot3D([line1_end[0], line2_end[0]], [line1_end[1], line2_end[1]], [line1_end[2], line2_end[2]], color="black", linewidth=1, linestyle="--",  zorder=10)

# Add labels for the manifold and tangent plane
ax.text(1.8,  2.0, -2.1, "$\mathcal{M}$",         fontsize=12, zorder=10)
ax.text(1.2, -0.8,  3.3, "$T_{\Psi}\mathcal{M}$", fontsize=12, zorder=10)

# Add labels for the points
ax.text(point[0] + 0.2, point[1] - 0.2, point[2] - 1.5, r"$\ket{\Psi(\symbf{\alpha})}$", fontsize=12, zorder=10)
ax.text(line1_end[0] + 0.3, line1_end[1] - 0.2, line1_end[2] - 1.7, r"$\partial_t\ket{\Psi(\symbf{\alpha})}$", fontsize=12, zorder=10)
ax.text(line2_end[0] + 0.5, line2_end[1] + 0.6, line2_end[2] + 1.3, r"$-iH\ket{\Psi(\symbf{\alpha})}$", fontsize=12, zorder=10)

# Adjust the view
ax.view_init(elev=25, azim=45); ax.set_zlim(-1, 0); ax.set_box_aspect((1, 1.1, 0.05))

# Save the figure
plt.savefig("chapters/02-Time_Evolution_in_Quantum_Mechanics/sections/images/dfvp_schema.pdf", bbox_inches="tight", pad_inches=0)
