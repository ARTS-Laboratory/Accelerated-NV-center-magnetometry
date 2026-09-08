
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

try:
    import IPython as IP
    ipy = IP.get_ipython()
    if ipy is not None:
        ipy.run_line_magic('reset', '-sf')
except Exception:
    pass

# %% Import modules

import numpy as np
import matplotlib.pyplot as plt

# ---------- Plot formatting ----------

plt.rcParams.update({'text.usetex': True})

plt.rcParams.update({'font.serif': [
    'Times New Roman',
    'Times',
    'DejaVu Serif',
    'Computer Modern Roman'
]})

plt.rcParams.update({'font.family': 'serif'})
plt.rcParams.update({'font.size': 10})

plt.close('all')


# ============================================================
# Load data
# ============================================================

# ---------- Left figure: zero field ----------

data_left = np.loadtxt('32.txt', skiprows=1)

x_left = data_left[:, 0]
y_left = data_left[:, 1]
yfit_left = data_left[:, 2]


# ---------- Right figure: eight dips ----------

data_right = np.loadtxt('8-1.txt', skiprows=1)

x_right = data_right[:, 0]
y_right = data_right[:, 1]
yfit_right = data_right[:, 2]


# ============================================================
# Create figure
# ============================================================

# Each panel is approximately 3.34 inches wide
fig, (ax1, ax2) = plt.subplots(
    1, 2,
    figsize=(6.5, 2.5),
    dpi=300
)


# ============================================================
# (a) Left figure
# ============================================================

ax1.plot(
    x_left,
    y_left,
    linestyle='None',
    marker='o',
    markersize=0.8,
    color='black',
    label='measured data'
)

ax1.plot(
    x_left,
    yfit_left,
    color=plt.cm.tab10(0),
    linewidth=1.0,
    label='fitted curve'
)

# ---------- Legend ----------

leg1 = ax1.legend(
    loc='lower left',
    fontsize=8,
    frameon=True,
    facecolor='white',
    edgecolor='grey',
    framealpha=1.0
)
leg1.get_frame().set_linewidth(0.4)

# ---------- Axes ----------

ax1.set_xlim(2820, 2920)
ax1.set_xticks(np.arange(2820, 2921, 20))

ypad_left = 0.0015

ax1.set_ylim(
    min(y_left.min(), yfit_left.min()) - ypad_left,
    max(y_left.max(), yfit_left.max()) + ypad_left
)

ax1.set_yticks(np.arange(0.92, 1.02, 0.02))

ax1.set_xlabel(
    r'microwave frequency (MHz)',
    labelpad=1
)

ax1.set_ylabel(
    r'normalized lock-in signal',
    labelpad=0.1
)

# ---------- Grid ----------

ax1.grid(
    True,
    which='major',
    linestyle=':',
    linewidth=0.4,
    alpha=0.5
)

# ---------- Ticks ----------

ax1.tick_params(
    axis='both',
    which='major',
    direction='in',
    top=True,
    right=True,
    length=4,
    pad=5
)


# ============================================================
# (b) Right figure
# ============================================================

ax2.plot(
    x_right,
    y_right,
    linestyle='None',
    marker='o',
    markersize=0.8,
    color='black',
    label='measured data'
)

ax2.plot(
    x_right,
    yfit_right,
    color=plt.cm.tab10(0),
    linewidth=1.0,
    label='fitted curve'
)

# ---------- Legend ----------

leg2 = ax2.legend(
    loc='lower right',
    fontsize=8,
    frameon=True,
    facecolor='white',
    edgecolor='grey',
    framealpha=1.0
)

leg2.get_frame().set_linewidth(0.4)

# ---------- Axes ----------

ax2.set_xlim(2720, 3020)
ax2.set_xticks(np.arange(2720, 3021, 50))

ypad_right = 0.0015

ax2.set_ylim(
    min(y_right.min(), yfit_right.min()) - ypad_right,
    max(y_right.max(), yfit_right.max()) + ypad_right
)

ax2.set_ylim(0.955, 1.01)
ax2.set_yticks(np.arange(0.96, 1.011, 0.01))

ax2.set_xlabel(
    r'microwave frequency (MHz)',
    labelpad=1
)

ax2.set_ylabel(
    r'normalized lock-in signal',
    labelpad=0.1
)

# ---------- Grid ----------

ax2.grid(
    True,
    which='major',
    linestyle=':',
    linewidth=0.4,
    alpha=0.5
)

# ---------- Ticks ----------

ax2.tick_params(
    axis='both',
    which='major',
    direction='in',
    top=True,
    right=True,
    length=4,
    pad=5
)


# ============================================================
# Panel labels: (a) and (b)
# ============================================================

ax1.text(
    0.5, -0.25,
    r'(a)',
    transform=ax1.transAxes,
    ha='center',
    va='top',
    fontsize=10
)

ax2.text(
    0.5, -0.25,
    r'(b)',
    transform=ax2.transAxes,
    ha='center',
    va='top',
    fontsize=10
)


# ============================================================
# Layout
# ============================================================

fig.subplots_adjust(
    left=0.09,
    right=0.99,
    bottom=0.25,
    top=0.98,
    wspace=0.28
)


# ============================================================
# Save
# ============================================================

fig.savefig(
    'example-input_spectrum',
    dpi=600,
    bbox_inches='tight',
    pad_inches=0.01
)

plt.show()
 