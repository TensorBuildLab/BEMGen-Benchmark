"""v2.0 paper figures. usage: python make_figures_v2.py <analysis_dir> <fig_dir>"""
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.image as mpimg  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

A, F = Path(sys.argv[1]), Path(sys.argv[2])
BLUE, ORANGE, AQUA, YELLOW = "#2a78d6", "#eb6834", "#1baf7a", "#eda100"
INK, INK2, GRID = "#0b0b0b", "#52514e", "#e4e3df"
plt.rcParams.update({"font.family": "DejaVu Sans", "font.size": 8, "axes.edgecolor": INK2, "axes.labelcolor": INK,
                     "xtick.color": INK2, "ytick.color": INK2, "axes.spines.top": False, "axes.spines.right": False,
                     "savefig.dpi": 400})


def fig_documents():
    """Example inputs: M plan, M schedules, P change order."""
    ims = [(A / "runs/20261107-build_m2.0/tasks/T2-test-01/package/A-101_plan.png", "(a) M: A-101 floor plan"),
           (A / "runs/20261107-build_m2.0/tasks/T2-test-01/package/G-001_schedules.png", "(b) M: G-001 schedules"),
           (A / "runs/20261107-build_p2.0.1/tasks/P2-test-10/package/CO-1_glazing.png", "(c) P: CO-1 change order")]
    fig, axs = plt.subplots(1, 3, figsize=(7.1, 2.6))
    for ax, (p, t) in zip(axs, ims):
        ax.imshow(mpimg.imread(p))
        ax.set_title(t, fontsize=8, loc="left", color=INK)
        ax.axis("off")
    fig.tight_layout()
    fig.savefig(F / "fig_v2_documents.png")


def fig_conditions():
    d = pd.read_csv(A / "results/v2_analysis/conditions.csv")
    conds = ["text (v1.1.3 run)", "text (same-session rerun)", "multimodal M"]
    labels = ["Text,\nearlier run", "Text,\nrerun", "Multimodal\nM"]
    systems = ["Claude Haiku 5.5", "Claude Sonnet 5.5", "Claude Opus 5.5"]
    cols = [YELLOW, AQUA, BLUE]
    fig, axs = plt.subplots(1, 2, figsize=(7.1, 2.8), gridspec_kw={"width_ratios": [3, 1.3]})
    ax = axs[0]
    w = 0.26
    x = np.arange(len(conds))
    for i, (s, c) in enumerate(zip(systems, cols)):
        g = d[d.system == s].set_index("condition").reindex(conds)
        xs = x + (i - 1) * w
        ax.bar(xs, g["pass"], w * 0.92, color=c, label=s.replace("Claude ", ""), zorder=3)
        ax.scatter(xs, g["repaired_pass"], marker="_", s=120, color=INK, linewidths=1.6, zorder=4,
                   label="after syntax repair (diagnostic)" if i == 0 else None)
    ax.set_xticks(x, labels)
    ax.set_ylabel("Tasks passed (of 40)")
    ax.set_ylim(0, 50)
    ax.set_yticks(range(0, 41, 10))
    ax.yaxis.grid(True, color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    ax.set_title("(a) Text vs multimodal, same 40 v1.1.3 test tasks", fontsize=8, loc="left")
    ax.legend(fontsize=6.5, frameon=False, loc="upper center", ncol=4, bbox_to_anchor=(0.55, 1.0))
    ax = axs[1]
    p = d[d.condition == "DOE edits P"].set_index("system").reindex(systems)
    ax.bar(range(3), p["pass"], 0.6, color=cols, zorder=3)
    lo, hi = p["wilson_lo"] * 32, p["wilson_hi"] * 32
    ax.errorbar(range(3), p["pass"], yerr=[p["pass"] - lo, hi - p["pass"]], fmt="none", ecolor=INK2, lw=0.8,
                capsize=2, zorder=4)
    ax.set_xticks(range(3), [s.split()[1] for s in systems])
    ax.set_ylim(0, 34)
    ax.set_ylabel("Tasks passed (of 32)")
    ax.yaxis.grid(True, color=GRID, lw=0.6)
    ax.set_axisbelow(True)
    ax.set_title("(b) DOE prototype edits P", fontsize=8, loc="left")
    fig.tight_layout()
    fig.savefig(F / "fig_v2_results.png")


def fig_metrics():
    s1 = pd.read_csv(A / "results/v2_metrics/controls_summary.csv")
    s2 = pd.read_csv(A / "results/v2_metrics/controls_summary2.csv")
    crit = [(s2, "L3", "Annual end uses (L3)"), (s1, "L3h", "Load shape + peaks (L3h)"),
            (s2, "L3b", "Heat balance (L3b)"), (s2, "MR1", "Climate swap (MR1)"),
            (s2, "L3 and L3b and MR1", "L3 and L3b and MR1"), (s1, "G14h", "G14 hourly"), (s1, "EUI10", "Total EUI ±10%")]
    fig, axs = plt.subplots(1, 2, figsize=(7.1, 3.3), sharey=True)
    for ax, st, t in zip(axs, ["text", "P"], ["(a) Text tasks (320 valid, 457 mutants)",
                                              "(b) DOE edits P (≈135 valid, ≈175 mutants)"]):
        def rate(src, c, kind):
            g = src[(src.set == st) & (src.criterion == c) & (src.kind == kind)]
            return float(g["rate"].iloc[0]) if len(g) else None
        far = [rate(src, c, "mutant") for src, c, _ in crit]
        frr = [rate(src, c, "variant") for src, c, _ in crit]
        y = np.arange(len(crit))[::-1]
        ax.barh(y + 0.18, far, 0.34, color=ORANGE, label="false-accept (mutants)", zorder=3)
        ax.barh(y - 0.18, [v or 0 for v in frr], 0.34, color=BLUE, label="false-reject (valid variants)", zorder=3)
        for yy, v in zip(y, far):
            ax.text(v + 0.01, yy + 0.18, f"{v:.0%}", va="center", fontsize=6.3, color=INK)
        for yy, v in zip(y, frr):
            ax.text((v or 0) + 0.01, yy - 0.18, "–" if v is None else f"{v:.1%}" if 0 < v < 0.1 else f"{v:.0%}",
                    va="center", fontsize=6.3, color=INK)
        ax.set_yticks(y, [n for _, _, n in crit])
        ax.set_xlim(0, 1.12)
        ax.xaxis.grid(True, color=GRID, lw=0.6)
        ax.set_axisbelow(True)
        ax.set_title(t, fontsize=8, loc="left")
        ax.set_xlabel("Rate (energy criterion alone)")
    h, l = axs[0].get_legend_handles_labels()
    fig.legend(h, l, fontsize=6.5, frameon=False, loc="lower center", ncol=2)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    fig.savefig(F / "fig_v2_metrics.png")


fig_documents()
fig_conditions()
fig_metrics()
print("ok")
