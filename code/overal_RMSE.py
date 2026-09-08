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

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FixedLocator

# %% plotting style

plt.rcParams.update({"text.usetex": True})
plt.rcParams.update({"image.cmap": "viridis"})
plt.rcParams.update({"font.serif": ["Times New Roman", "Times", "DejaVu Serif", "Bitstream Vera Serif", "Computer Modern Roman", "New Century Schoolbook", "Century Schoolbook L", "Utopia", "ITC Bookman", "Bookman", "Nimbus Roman No9 L", "Palatino", "Charter", "serif"]})
plt.rcParams.update({"font.family": "serif"})
plt.rcParams.update({"font.size": 10})
plt.rcParams.update({"mathtext.rm": "serif"})
plt.rcParams.update({"mathtext.fontset": "custom"})

cc = plt.rcParams["axes.prop_cycle"].by_key()["color"]

plt.close("all")

# ============================================================
# SETTINGS
# ============================================================

zero_csv = "all_zero_field_spectra_RMSE_raw.csv"
eight_csv = "eight_dip_all27_RMSE_raw.csv"

figure_width = 6.5
figure_height = 2.5
figure_dpi = 300

horizontal_space = 0.25

# ============================================================
# LEFT PANEL SETTINGS: ZERO FIELD
# ============================================================

left_x_min = 8
left_x_max = 52

left_y_min = -0.001
left_y_max = 0.020

left_plot_start = 10
left_plot_end = 50
left_plot_step = 5

left_major_x_ticks = np.arange(10, 51, 5)
left_y_major_step = 0.005

left_shadow_marker_size = 4.0
left_shadow_alpha = 0.10

left_mean_marker_size = 3.5
left_mean_linewidth = 1.2

left_legend_fontsize = 8
left_legend_location = "upper right"

# ============================================================
# RIGHT PANEL SETTINGS: EIGHT DIPS
# ============================================================

right_x_min = 28
right_x_max = 72

right_y_min = -0.001
right_y_max = 0.020

right_plot_start = 30
right_plot_end = 70
right_plot_step = 5

right_major_x_ticks = np.arange(30, 71, 5)
right_y_major_step = 0.005

right_shadow_marker_size = 4.0
right_shadow_alpha = 0.10

right_mean_marker_size = 3.5
right_mean_linewidth = 1.2

right_legend_fontsize = 8
right_legend_location = "upper right"

# ============================================================
# PANEL LABEL SETTINGS
# ============================================================

left_panel_label = "(a)"
right_panel_label = "(b)"

panel_label_y = -0.24
panel_label_fontsize = 10

# ============================================================
# LOAD DATA
# ============================================================

zero_data = pd.read_csv(zero_csv)
eight_data = pd.read_csv(eight_csv)

print("\nZero-field columns:")
print(zero_data.columns.tolist())

print("\nEight-dip columns:")
print(eight_data.columns.tolist())

# ============================================================
# FILTER ZERO-FIELD DATA
# ============================================================

zero_data = zero_data[(zero_data["n_points"] >= left_plot_start) & (zero_data["n_points"] <= left_plot_end)].copy()
zero_data = zero_data[((zero_data["n_points"] - left_plot_start) % left_plot_step) == 0].copy()

# ============================================================
# FILTER EIGHT-DIP DATA
# ============================================================

eight_data = eight_data[(eight_data["n_points"] >= right_plot_start) & (eight_data["n_points"] <= right_plot_end)].copy()
eight_data = eight_data[((eight_data["n_points"] - right_plot_start) % right_plot_step) == 0].copy()

# ============================================================
# CALCULATE MEAN RMSE
# ============================================================

zero_summary = zero_data.groupby(["method", "n_points"], as_index=False).agg(mean_rmse=("rmse", "mean"), std_rmse=("rmse", "std"), n_spectra=("scan_index", "count"))

eight_summary = eight_data.groupby(["method", "n_points"], as_index=False).agg(mean_rmse=("rmse", "mean"), std_rmse=("rmse", "std"), n_spectra=("scan_number", "count"))

# ============================================================
# SAVE SUMMARY CSV FILES
# ============================================================

zero_summary.to_csv("zero_field_RMSE_10To50_summary.csv", index=False)
eight_summary.to_csv("eight_dip_RMSE_30To70_summary.csv", index=False)

# ============================================================
# METHOD SETTINGS
# ============================================================

method_settings = {
    "Adaptive": {"color": cc[0], "marker": "o", "linestyle": "-", "label": "adaptive"},
    "Uniform": {"color": cc[1], "marker": "s", "linestyle": "--", "label": "uniform"},
    "Random": {"color": cc[2], "marker": "d", "linestyle": "-.", "label": "random"}
}

# ============================================================
# CREATE FIGURE
# ============================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(figure_width, figure_height), dpi=figure_dpi)

# ============================================================
# LEFT PANEL: ZERO-FIELD SHADOW POINTS
# ============================================================

for method in ["Adaptive", "Uniform", "Random"]:
    settings = method_settings[method]
    method_data = zero_data[zero_data["method"] == method]

    ax1.plot(method_data["n_points"], method_data["rmse"], linestyle="None", marker=settings["marker"], markersize=left_shadow_marker_size, markerfacecolor=settings["color"], markeredgecolor="none", alpha=left_shadow_alpha, zorder=1)

# ============================================================
# LEFT PANEL: ZERO-FIELD MEAN CURVES
# ============================================================

for method in ["Adaptive", "Uniform", "Random"]:
    settings = method_settings[method]
    mean_data = zero_summary[zero_summary["method"] == method].sort_values("n_points")

    ax1.plot(mean_data["n_points"], mean_data["mean_rmse"], linestyle=settings["linestyle"], marker=settings["marker"], color=settings["color"], markersize=left_mean_marker_size, linewidth=left_mean_linewidth, label=settings["label"], zorder=5)

# ============================================================
# LEFT PANEL AXIS SETTINGS
# ============================================================

ax1.set_xlim(left_x_min, left_x_max)
ax1.set_ylim(left_y_min, left_y_max)

ax1.set_xlabel("number of sampled points")
ax1.set_ylabel("RMSE")

ax1.xaxis.set_major_locator(FixedLocator(left_major_x_ticks))
ax1.yaxis.set_major_locator(MultipleLocator(left_y_major_step))

ax1.tick_params(axis="both", which="major", direction="in", length=4, width=0.8, top=False, right=False)
ax1.minorticks_off()

ax1.grid(True, which="major", alpha=0.3)

legend1 = ax1.legend(loc=left_legend_location, fontsize=left_legend_fontsize, frameon=True)

legend1.get_frame().set_facecolor("white")
legend1.get_frame().set_alpha(1.0)
legend1.get_frame().set_edgecolor("grey")
legend1.get_frame().set_linewidth(0.5)

# ============================================================
# RIGHT PANEL: EIGHT-DIP SHADOW POINTS
# ============================================================

for method in ["Adaptive", "Uniform", "Random"]:
    settings = method_settings[method]
    method_data = eight_data[eight_data["method"] == method]

    ax2.plot(method_data["n_points"], method_data["rmse"], linestyle="None", marker=settings["marker"], markersize=right_shadow_marker_size, markerfacecolor=settings["color"], markeredgecolor="none", alpha=right_shadow_alpha, zorder=1)

# ============================================================
# RIGHT PANEL: EIGHT-DIP MEAN CURVES
# ============================================================

for method in ["Adaptive", "Uniform", "Random"]:
    settings = method_settings[method]
    mean_data = eight_summary[eight_summary["method"] == method].sort_values("n_points")

    ax2.plot(mean_data["n_points"], mean_data["mean_rmse"], linestyle=settings["linestyle"], marker=settings["marker"], color=settings["color"], markersize=right_mean_marker_size, linewidth=right_mean_linewidth, label=settings["label"], zorder=5)

# ============================================================
# RIGHT PANEL AXIS SETTINGS
# ============================================================

ax2.set_xlim(right_x_min, right_x_max)
ax2.set_ylim(right_y_min, right_y_max)

ax2.set_xlabel("number of sampled points")
ax2.set_ylabel("RMSE")

ax2.xaxis.set_major_locator(FixedLocator(right_major_x_ticks))
ax2.yaxis.set_major_locator(MultipleLocator(right_y_major_step))

ax2.tick_params(axis="both", which="major", direction="in", length=4, width=0.8, top=False, right=False)
ax2.minorticks_off()

ax2.grid(True, which="major", alpha=0.3)

legend2 = ax2.legend(loc=right_legend_location, fontsize=right_legend_fontsize, frameon=True)

legend2.get_frame().set_facecolor("white")
legend2.get_frame().set_alpha(1.0)
legend2.get_frame().set_edgecolor("grey")
legend2.get_frame().set_linewidth(0.5)

# ============================================================
# PANEL LABELS
# ============================================================

ax1.text(0.5, panel_label_y, left_panel_label, transform=ax1.transAxes, ha="center", va="top", fontsize=panel_label_fontsize)
ax2.text(0.5, panel_label_y, right_panel_label, transform=ax2.transAxes, ha="center", va="top", fontsize=panel_label_fontsize)

# ============================================================
# LAYOUT
# ============================================================

fig.subplots_adjust(left=0.10, right=0.995, bottom=0.22, top=0.98, wspace=horizontal_space)

# ============================================================
# SAVE FIGURE
# ============================================================

fig.savefig("overal_RMSE.png", dpi=figure_dpi, bbox_inches="tight", pad_inches=0.01)

plt.show()

# ============================================================
# PRINT SUMMARY
# ============================================================

print("\n========================================")
print("ZERO-FIELD MEAN RMSE")
print("========================================")
print(zero_summary.to_string(index=False))

print("\n========================================")
print("EIGHT-DIP MEAN RMSE")
print("========================================")
print(eight_summary.to_string(index=False))

print("\n========================================")
print("FILES SAVED")
print("========================================")

print("overal_RMSE.png")