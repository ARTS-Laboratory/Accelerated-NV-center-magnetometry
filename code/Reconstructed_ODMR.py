#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import IPython as IP
    ipy = IP.get_ipython()
    if ipy is not None:
        ipy.run_line_magic('reset', '-sf')
except Exception:
    pass

# %% import modules

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator

# %% plot formatting

plt.rcParams.update({'text.usetex': True})
plt.rcParams.update({'image.cmap': 'viridis'})

plt.rcParams.update({
    'font.serif': [
        'Times New Roman', 'Times', 'DejaVu Serif',
        'Bitstream Vera Serif', 'Computer Modern Roman',
        'New Century Schoolbook', 'Century Schoolbook L',
        'Utopia', 'ITC Bookman', 'Bookman',
        'Nimbus Roman No9 L', 'Palatino',
        'Charter', 'serif'
    ]
})

plt.rcParams.update({'font.family': 'serif'})
plt.rcParams.update({'font.size': 10})
plt.rcParams.update({'mathtext.rm': 'serif'})
plt.rcParams.update({'mathtext.fontset': 'custom'})

cc = plt.rcParams['axes.prop_cycle'].by_key()['color']

plt.close('all')

# ============================================================
# SETTINGS
# ============================================================

# CSV files
zero_csv = '32_plot_5_final_fit_data.csv'
eight_csv = 'eight_dip_plot_2_final_adaptive_fit_data.csv'

# Overall figure size
figure_width = 6.5
figure_height = 2.5
figure_dpi = 300

# Space between the two panels
horizontal_space = 0.25

# ============================================================
# LEFT PANEL SETTINGS: ZERO-FIELD / SPECTRUM 32
# ============================================================

left_x_min = 2820
left_x_max = 2920

left_y_min = 0.928
left_y_max = 1.01

left_x_major_step = 20
left_y_major_step = 0.02

left_experimental_linewidth = 1.0
left_reference_linewidth = 1.2
left_adaptive_linewidth = 1.2

left_sample_marker_size = 15
left_sample_marker_linewidth = 1.0

left_legend_fontsize = 6
left_legend_location = 'best'

# ============================================================
# RIGHT PANEL SETTINGS: EIGHT-DIP
# ============================================================

right_x_min = 2720
right_x_max = 3020

right_y_min = 0.948
right_y_max = 1.01

# Explicit ticks are used below so that both 2720 and 3020 appear
right_x_major_step = 50
right_y_major_step = 0.01

right_experimental_linewidth = 1.0
right_reference_linewidth = 1.0
right_adaptive_linewidth = 1.0

right_sample_marker_size = 15
right_sample_marker_linewidth = 1.0

right_legend_fontsize = 6
right_legend_location = 'best'

# ============================================================
# PANEL LABEL SETTINGS
# ============================================================

left_panel_label = '(a)'
right_panel_label = '(b)'

panel_label_y = -0.24
panel_label_fontsize = 10

# ============================================================
# LOAD DATA
# ============================================================

zero_data = pd.read_csv(zero_csv)
eight_data = pd.read_csv(eight_csv)

print('\nZero-field columns:')
print(zero_data.columns.tolist())

print('\nEight-dip columns:')
print(eight_data.columns.tolist())

# ============================================================
# ZERO-FIELD DATA
# ============================================================

zero_frequency = zero_data['frequency_MHz'].to_numpy()
zero_experimental = zero_data['experimental_normalized'].to_numpy()
zero_reference = zero_data['reference_fit'].to_numpy()
zero_adaptive = zero_data['final_adaptive_fit'].to_numpy()
zero_sampled = zero_data['adaptive_sampled_points'].to_numpy()

zero_sample_mask = np.isfinite(zero_sampled)

# ============================================================
# EIGHT-DIP DATA
# ============================================================

eight_frequency = eight_data['frequency_MHz'].to_numpy()
eight_experimental = eight_data['experimental_data'].to_numpy()
eight_reference = eight_data['reference_full_data_fit'].to_numpy()
eight_adaptive = eight_data['final_adaptive_fit'].to_numpy()
eight_sampled = eight_data['adaptive_sampled_points'].to_numpy()

eight_sample_mask = np.isfinite(eight_sampled)

# ============================================================
# LEGEND FUNCTION
# ============================================================

def white_legend(ax, fontsize, loc='best'):
    legend = ax.legend(fontsize=fontsize, loc=loc, frameon=True)
    legend.get_frame().set_facecolor('white')
    legend.get_frame().set_alpha(1.0)
    legend.get_frame().set_edgecolor('grey')
    legend.get_frame().set_linewidth(0.2)
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
# LEFT PANEL
# ZERO-FIELD / SPECTRUM 32
# ============================================================

# Experimental data: blue solid line
ax1.plot(
    zero_frequency,
    zero_experimental,
    '-',
    color=cc[0],
    linewidth=left_experimental_linewidth,
    label='experimental data'
)

# Reference full-data fit
ax1.plot(
    zero_frequency,
    zero_reference,
    '-',
    color=cc[1],
    linewidth=left_reference_linewidth,
    label='reference full-data fit'
)

# Final adaptive fit
ax1.plot(
    zero_frequency,
    zero_adaptive,
    '--',
    color=cc[2],
    linewidth=left_adaptive_linewidth,
    label='52-point adaptive fit'
)

# Adaptive sampled points
ax1.scatter(
    zero_frequency[zero_sample_mask],
    zero_sampled[zero_sample_mask],
    s=left_sample_marker_size,
    marker='o',
    facecolors='none',
    edgecolors='black',
    linewidths=left_sample_marker_linewidth,
    label='adaptive sampled points'
)

# Horizontal reference line at normalized intensity = 1
ax1.axhline(
    1.0,
    linestyle=':',
    linewidth=1.0
)

# ============================================================
# LEFT PANEL AXES
# ============================================================

ax1.set_xlim(left_x_min, left_x_max)
ax1.set_ylim(left_y_min, left_y_max)

ax1.set_xlabel('microwave frequency (MHz)')
ax1.set_ylabel('normalized intensity')

ax1.xaxis.set_major_locator(MultipleLocator(left_x_major_step))
ax1.yaxis.set_major_locator(MultipleLocator(left_y_major_step))

ax1.tick_params(
    axis='both',
    which='major',
    direction='in',
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax1.minorticks_off()

ax1.grid(
    True,
    which='major',
    alpha=0.3
)

white_legend(
    ax1,
    fontsize=left_legend_fontsize,
    loc=left_legend_location
)

# ============================================================
# RIGHT PANEL
# EIGHT-DIP
# ============================================================

# Experimental data
ax2.plot(
    eight_frequency,
    eight_experimental,
    '-',
    color=cc[0],
    linewidth=right_experimental_linewidth,
    label='experimental data'
)

# Reference full-data fit
ax2.plot(
    eight_frequency,
    eight_reference,
    '-',
    color=cc[1],
    linewidth=right_reference_linewidth,
    label='reference full-data fit'
)

# Final adaptive fit
ax2.plot(
    eight_frequency,
    eight_adaptive,
    '--',
    color=cc[2],
    linewidth=right_adaptive_linewidth,
    label='final adaptive fit'
)

# Adaptive sampled points
ax2.scatter(
    eight_frequency[eight_sample_mask],
    eight_sampled[eight_sample_mask],
    s=right_sample_marker_size,
    marker='o',
    facecolors='none',
    edgecolors='black',
    linewidths=right_sample_marker_linewidth,
    label='adaptive sampled points'
)

# Horizontal reference line
ax2.axhline(
    1.0,
    linestyle=':',
    linewidth=1.0
)

# ============================================================
# RIGHT PANEL AXES
# ============================================================

ax2.set_xlim(right_x_min, right_x_max)
ax2.set_ylim(right_y_min, right_y_max)

ax2.set_xlabel('microwave frequency (MHz)')
ax2.set_ylabel('normalized intensity')

# Explicit x ticks so both 2720 and 3020 are shown
ax2.set_xticks([
    2720,
    2770,
    2820,
    2870,
    2920,
    2970,
    3020
])

# Y-axis tick spacing
ax2.yaxis.set_major_locator(
    MultipleLocator(right_y_major_step)
)

ax2.tick_params(
    axis='both',
    which='major',
    direction='in',
    length=4,
    width=0.8,
    top=False,
    right=False
)

ax2.minorticks_off()

ax2.grid(
    True,
    which='major',
    alpha=0.3
)

white_legend(
    ax2,
    fontsize=right_legend_fontsize,
    loc=right_legend_location
)

# ============================================================
# PANEL LABELS
# ============================================================

ax1.text(
    0.5,
    panel_label_y,
    left_panel_label,
    transform=ax1.transAxes,
    ha='center',
    va='top',
    fontsize=panel_label_fontsize
)

ax2.text(
    0.5,
    panel_label_y,
    right_panel_label,
    transform=ax2.transAxes,
    ha='center',
    va='top',
    fontsize=panel_label_fontsize
)

# ============================================================
# FIGURE LAYOUT
# ============================================================

fig.subplots_adjust(
    left=0.10,
    right=0.995,
    bottom=0.22,
    top=0.98,
    wspace=horizontal_space
)

# ============================================================
# SAVE FIGURE
# ============================================================

fig.savefig(
    'zero_field_and_eight_dip_final_adaptive_fit.png',
    dpi=figure_dpi,
    bbox_inches='tight',
    pad_inches=0.01
)

plt.show()