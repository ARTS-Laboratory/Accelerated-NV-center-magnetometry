#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import IPython as IP
    ipy = IP.get_ipython()
    if ipy is not None:
        ipy.run_line_magic("reset", "-sf")
except Exception:
    pass

# %% imports

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# %% plotting style

plt.rcParams.update({"text.usetex": True})
plt.rcParams.update({"image.cmap": "viridis"})
plt.rcParams.update({
    "font.serif": [
        "Times New Roman", "Times", "DejaVu Serif",
        "Bitstream Vera Serif", "Computer Modern Roman",
        "New Century Schoolbook", "Century Schoolbook L",
        "Utopia", "ITC Bookman", "Bookman",
        "Nimbus Roman No9 L", "Palatino",
        "Charter", "serif"
    ]
})
plt.rcParams.update({"font.family": "serif"})
plt.rcParams.update({"font.size": 10})
plt.rcParams.update({"mathtext.rm": "serif"})
plt.rcParams.update({"mathtext.fontset": "custom"})

cc = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.close("all")

# ============================================================
# SETTINGS
# ============================================================

zero_field_csv = "32_plot_6_fit_evolution_data.csv"
eight_dip_csv = "eight_dip_plot_9_fit_evolution_data.csv"

# ============================================================
# LEFT PANEL (a): ZERO-FIELD SETTINGS
# ============================================================

zero_selected_iterations = [10, 12, 15, 20, 30, 50]

zero_x_min = 2820
zero_x_max = 2920

zero_y_min = 0.87
zero_y_max = 1.02

zero_x_major_step = 20
zero_y_major_step = 0.02

zero_experimental_marker_size = 0.8
zero_reference_linewidth = 1.0
zero_adaptive_linewidth = 1.0

# ============================================================
# RIGHT PANEL (b): EIGHT-DIP SETTINGS
# ============================================================

eight_selected_iterations = [30, 40, 50, 60, 70, 80, 90]

eight_x_min = 2720
eight_x_max = 3022

eight_y_min = 0.895
eight_y_max = 1.01

eight_x_major_step = 45
eight_y_major_step = 0.02

eight_experimental_marker_size = 1.0
eight_reference_linewidth = 1.0
eight_adaptive_linewidth = 1.0

# ============================================================
# COMMON FIGURE SETTINGS
# ============================================================

figure_width = 6.5
figure_height = 2.7
figure_dpi = 300

legend_fontsize = 5.5
legend_location = "lower right"

panel_label_fontsize = 10

# ============================================================
# LOAD ZERO-FIELD DATA
# ============================================================

zero_data = pd.read_csv(zero_field_csv)

zero_frequency = zero_data["frequency_MHz"].to_numpy()
zero_experimental = zero_data["experimental_data"].to_numpy()
zero_reference_fit = zero_data["reference_fit"].to_numpy()

# ============================================================
# LOAD EIGHT-DIP DATA
# ============================================================

eight_data = pd.read_csv(eight_dip_csv)

eight_frequency = eight_data["frequency_MHz"].to_numpy()
eight_experimental = eight_data["experimental_data"].to_numpy()
eight_reference_fit = eight_data["reference_full_data_fit"].to_numpy()

# ============================================================
# LEGEND FUNCTION
# ============================================================

def grey_legend(ax, fontsize=5.5, loc="lower right"):
    legend = ax.legend(
        loc=loc,
        fontsize=fontsize,
        frameon=True
    )

    legend.get_frame().set_facecolor("white")
    legend.get_frame().set_alpha(1.0)
    legend.get_frame().set_edgecolor("grey")
    legend.get_frame().set_linewidth(0.5)

    return legend


# ============================================================
# CREATE SIDE-BY-SIDE FIGURE
# ============================================================

fig, (ax1, ax2) = plt.subplots(
    1,
    2,
    figsize=(figure_width, figure_height),
    dpi=figure_dpi
)

# ============================================================
# LEFT PANEL (a): ZERO-FIELD SPECTRUM
# ============================================================

ax1.plot(
    zero_frequency,
    zero_experimental,
    "o",
    color="black",
    markersize=zero_experimental_marker_size,
    linestyle="None",
    label="experimental data"
)

ax1.plot(
    zero_frequency,
    zero_reference_fit,
    "-",
    color=cc[1],
    linewidth=zero_reference_linewidth,
    label="reference full-data fit"
)

for i, n_points in enumerate(zero_selected_iterations):

    column_name = f"adaptive_fit_{n_points}_points"

    if column_name not in zero_data.columns:
        print(
            f"Warning: {column_name} "
            f"was not found in {zero_field_csv}."
        )
        continue

    adaptive_fit = zero_data[column_name].to_numpy()

    ax1.plot(
        zero_frequency,
        adaptive_fit,
        "-",
        color=cc[(i + 2) % len(cc)],
        linewidth=zero_adaptive_linewidth,
        label=f"{n_points} points"
    )

# Axis ranges
ax1.set_xlim(zero_x_min, zero_x_max)
ax1.set_ylim(zero_y_min, zero_y_max)

# Axis labels
ax1.set_xlabel("microwave frequency (MHz)")
ax1.set_ylabel("normalized intensity")

# Major tick spacing
ax1.xaxis.set_major_locator(
    MultipleLocator(zero_x_major_step)
)

ax1.yaxis.set_major_locator(
    MultipleLocator(zero_y_major_step)
)

# Major ticks only
ax1.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax1.minorticks_off()

# Grid
ax1.grid(
    True,
    which="major",
    alpha=0.3
)

# Legend
grey_legend(
    ax1,
    fontsize=legend_fontsize,
    loc=legend_location
)

# ============================================================
# RIGHT PANEL (b): EIGHT-DIP SPECTRUM
# ============================================================

ax2.plot(
    eight_frequency,
    eight_experimental,
    "o",
    color="black",
    markersize=eight_experimental_marker_size,
    linestyle="None",
    label="experimental data"
)

ax2.plot(
    eight_frequency,
    eight_reference_fit,
    "-",
    color=cc[1],
    linewidth=eight_reference_linewidth,
    label="reference full-data fit"
)

for i, n_points in enumerate(eight_selected_iterations):

    column_name = f"adaptive_fit_{n_points}_points"

    if column_name not in eight_data.columns:
        print(
            f"Warning: {column_name} "
            f"was not found in {eight_dip_csv}."
        )
        continue

    adaptive_fit = eight_data[column_name].to_numpy()

    ax2.plot(
        eight_frequency,
        adaptive_fit,
        "-",
        color=cc[(i + 2) % len(cc)],
        linewidth=eight_adaptive_linewidth,
        label=f"{n_points} points"
    )

# Axis ranges
ax2.set_xlim(eight_x_min, eight_x_max)
ax2.set_ylim(eight_y_min, eight_y_max)

# Axis labels
ax2.set_xlabel("microwave frequency (MHz)")
ax2.set_ylabel("normalized intensity")

# Major tick spacing
ax2.xaxis.set_major_locator(
    MultipleLocator(eight_x_major_step)
)

ax2.yaxis.set_major_locator(
    MultipleLocator(eight_y_major_step)
)

# Major ticks only
ax2.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax2.minorticks_off()

# Grid
ax2.grid(
    True,
    which="major",
    alpha=0.3
)

# Legend
grey_legend(
    ax2,
    fontsize=legend_fontsize,
    loc=legend_location
)

# ============================================================
# PANEL LABELS
# ============================================================

ax1.text(
    0.5,
    -0.25,
    "(a)",
    transform=ax1.transAxes,
    ha="center",
    va="top",
    fontsize=panel_label_fontsize
)

ax2.text(
    0.5,
    -0.25,
    "(b)",
    transform=ax2.transAxes,
    ha="center",
    va="top",
    fontsize=panel_label_fontsize
)

# ============================================================
# FIGURE LAYOUT
# ============================================================

fig.subplots_adjust(
    left=0.10,
    right=0.995,
    bottom=0.26,
    top=0.98,
    wspace=0.24
)

# ============================================================
# SAVE MAIN FIGURE
# ============================================================

fig.savefig(
    "adaptive_fit_evolution_zero_field_and_eight_dip.png",
    dpi=figure_dpi,
    bbox_inches="tight",
    pad_inches=0.01
)

plt.show()


# ============================================================
# SEPARATE ZOOMED FIGURE FOR ZERO-FIELD SPECTRUM 32
# ============================================================

# Zoomed figure settings
zero_zoom_figure_width = 1
zero_zoom_figure_height = 1.5

zero_zoom_x_min = 2860
zero_zoom_x_max = 2880

zero_zoom_y_min = 0.935
zero_zoom_y_max = 1.00

zero_zoom_x_major_step = 20
zero_zoom_y_major_step = 0.02

# ============================================================
# CREATE ZERO-FIELD ZOOMED FIGURE
# ============================================================

fig_zoom, ax_zoom = plt.subplots(
    figsize=(
        zero_zoom_figure_width,
        zero_zoom_figure_height
    ),
    dpi=figure_dpi
)

# Experimental data
ax_zoom.plot(
    zero_frequency,
    zero_experimental,
    "o",
    color="black",
    markersize=zero_experimental_marker_size,
    linestyle="None",
    label="experimental data"
)

# Reference full-data fit
ax_zoom.plot(
    zero_frequency,
    zero_reference_fit,
    "-",
    color=cc[1],
    linewidth=zero_reference_linewidth,
    label="reference full-data fit"
)

# Adaptive fits
for i, n_points in enumerate(zero_selected_iterations):

    column_name = f"adaptive_fit_{n_points}_points"

    if column_name not in zero_data.columns:
        print(
            f"Warning: {column_name} "
            f"was not found in {zero_field_csv}."
        )
        continue

    adaptive_fit = zero_data[column_name].to_numpy()

    ax_zoom.plot(
        zero_frequency,
        adaptive_fit,
        "-",
        color=cc[(i + 2) % len(cc)],
        linewidth=zero_adaptive_linewidth,
        label=f"{n_points} points"
    )

# Axis range
ax_zoom.set_xlim(
    zero_zoom_x_min,
    zero_zoom_x_max
)

ax_zoom.set_ylim(
    zero_zoom_y_min,
    zero_zoom_y_max
)

# No axis labels
ax_zoom.set_xlabel("")
ax_zoom.set_ylabel("")

# Major tick spacing
ax_zoom.xaxis.set_major_locator(
    MultipleLocator(zero_zoom_x_major_step)
)

ax_zoom.yaxis.set_major_locator(
    MultipleLocator(zero_zoom_y_major_step)
)

# Major ticks only
ax_zoom.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax_zoom.minorticks_off()

# Grid
ax_zoom.grid(
    True,
    which="major",
    alpha=0.3
)

# No legend
# grey_legend(
#     ax_zoom,
#     fontsize=legend_fontsize,
#     loc=legend_location
# )

# Layout
fig_zoom.tight_layout(
    pad=0.1
)

# Save
fig_zoom.savefig(
    "32_adaptive_fit_selected_zoomed_separate.png",
    dpi=figure_dpi,
    bbox_inches="tight",
    pad_inches=0.01
)

plt.show()


# ============================================================
# SEPARATE ZOOMED FIGURE FOR EIGHT-DIP SPECTRUM
# ============================================================

# Zoomed figure settings
eight_zoom_figure_width = 1
eight_zoom_figure_height = 1

eight_zoom_x_min = 2857
eight_zoom_x_max = 2897

eight_zoom_y_min = 0.98
eight_zoom_y_max = 1.005

eight_zoom_x_major_step = 20
eight_zoom_y_major_step = 0.01

# ============================================================
# CREATE EIGHT-DIP ZOOMED FIGURE
# ============================================================

fig_zoom_eight, ax_zoom_eight = plt.subplots(
    figsize=(
        eight_zoom_figure_width,
        eight_zoom_figure_height
    ),
    dpi=figure_dpi
)

# Experimental data
ax_zoom_eight.plot(
    eight_frequency,
    eight_experimental,
    "o",
    color="black",
    markersize=eight_experimental_marker_size,
    linestyle="None",
    label="experimental data"
)

# Reference full-data fit
ax_zoom_eight.plot(
    eight_frequency,
    eight_reference_fit,
    "-",
    color=cc[1],
    linewidth=eight_reference_linewidth,
    label="reference full-data fit"
)

# Adaptive fits
for i, n_points in enumerate(eight_selected_iterations):

    column_name = f"adaptive_fit_{n_points}_points"

    if column_name not in eight_data.columns:
        print(
            f"Warning: {column_name} "
            f"was not found in {eight_dip_csv}."
        )
        continue

    adaptive_fit = eight_data[column_name].to_numpy()

    ax_zoom_eight.plot(
        eight_frequency,
        adaptive_fit,
        "-",
        color=cc[(i + 2) % len(cc)],
        linewidth=eight_adaptive_linewidth,
        label=f"{n_points} points"
    )

# ============================================================
# AXIS RANGE
# ============================================================

ax_zoom_eight.set_xlim(
    eight_zoom_x_min,
    eight_zoom_x_max
)

ax_zoom_eight.set_ylim(
    eight_zoom_y_min,
    eight_zoom_y_max
)

# ============================================================
# NO X OR Y AXIS LABELS
# ============================================================

ax_zoom_eight.set_xlabel("")
ax_zoom_eight.set_ylabel("")

# ============================================================
# MAJOR TICK SPACING
# ============================================================

ax_zoom_eight.xaxis.set_major_locator(
    MultipleLocator(eight_zoom_x_major_step)
)

ax_zoom_eight.yaxis.set_major_locator(
    MultipleLocator(eight_zoom_y_major_step)
)

# Major ticks only
ax_zoom_eight.tick_params(
    axis="both",
    which="major",
    direction="in",
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax_zoom_eight.minorticks_off()

# ============================================================
# GRID
# ============================================================

ax_zoom_eight.grid(
    True,
    which="major",
    alpha=0.3
)

# ============================================================
# NO LEGEND
# ============================================================

# grey_legend(
#     ax_zoom_eight,
#     fontsize=legend_fontsize,
#     loc=legend_location
# )

# ============================================================
# LAYOUT
# ============================================================

fig_zoom_eight.tight_layout(
    pad=0.1
)

# ============================================================
# SAVE
# ============================================================

fig_zoom_eight.savefig(
    "eight_dip_zoomed_separate.png",
    dpi=figure_dpi,
    bbox_inches="tight",
    pad_inches=0.01
)

plt.show()