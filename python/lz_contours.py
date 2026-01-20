import matplotlib.patches as patches, matplotlib.pyplot as plt, numpy as np

# set rcParams
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Libertinus Serif"],
    "text.latex.preamble": r"\usepackage{braket}"
})

# Clockwise and counter-clockwise contours
for clockwise in [False, True]:

    # Parameters
    R, eps, linewidth = 4.0, 0.4, 1.5

    # Create figure and axis
    fig, ax = plt.subplots(figsize=(8, 8))

    # Draw straight line segments
    ax.plot([-R, -eps], [0, 0], "k-", lw=linewidth)
    ax.plot([eps,   R], [0, 0], "k-", lw=linewidth)

    # Draw the large semi-circle
    ax.plot(R * np.cos(np.linspace(-np.pi, 0, 90)), R * np.sin(np.linspace(-np.pi, 0, 90)), "k-", lw=linewidth)

    # Draw the small semi-circle
    ax.plot(eps * np.cos(np.linspace(0, (-1 if clockwise else 1) * np.pi, 90)), eps * np.sin(np.linspace(0, (-1 if clockwise else 1) * np.pi, 90)), "k-", lw=linewidth)

    # Draw arrows indicating direction on the straight line segments
    ax.arrow(-0.6 * R, 0, 0.01, 0, head_width=0.25, head_length=0.3, length_includes_head=True, fc="k", ec="k", lw=linewidth)
    ax.arrow( 0.6 * R, 0, 0.01, 0, head_width=0.25, head_length=0.3, length_includes_head=True, fc="k", ec="k", lw=linewidth)

    # Draw arrows indicating direction on the large semi-circle
    for theta in (np.pi / 4, 3 * np.pi / 4):

        # Determine arrow position and direction
        tip_x, tip_y, dx, dy = R * np.cos(theta), R * np.sin(-theta), -0.01 * np.sin(theta), -0.01 * np.cos(theta)

        # Draw the arrow
        ax.arrow(tip_x - dx, tip_y - dy, dx, dy, head_width=0.25, head_length=0.3, length_includes_head=True, fc="k", ec="k", lw=linewidth)

    # Draw axes lines
    ax.axhline(0, color="k", lw=0.5, zorder=0)
    ax.axvline(0, color="k", lw=0.5, zorder=0)

    # Set axis labels
    ax.text(R + 0.8, -0.5, "$\Re$", ha="left",   va="center", fontsize=30)
    ax.text(-0.5,     0.8, "$\Im$", ha="center", va="bottom", fontsize=30)

    # Set limits
    ax.set_xlim(-R - 1, R + 1); ax.set_ylim(-R - 1, 1); ax.set_aspect("equal")

    # Remove the frame
    for side in ["top", "right", "bottom", "left"]: ax.spines[side].set_visible(False)

    # Remove ticks
    ax.set_xticks([]); ax.set_yticks([])

    # Export the figure as a PDF
    fig.savefig(f"chapters/03-Mixed_Quantum-Classical_Dynamics/sections/images/lz_contour_{'clockwise' if clockwise else 'counterclockwise'}.pdf", bbox_inches="tight")
