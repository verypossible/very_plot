import pytest
import matplotlib.pyplot as plt
import numpy as np

from very_plot import themes


def fig_and_ax():
    fig = plt.figure()
    ax = fig.add_subplot(111)

    return fig, ax


def test_very_axis_plot():
    themes.blog_mpl()

    fig, ax = fig_and_ax()

    ax.plot(np.arange(0, 10))
    ax.plot(np.arange(10, 20))

    for line in ax.get_lines():
        assert line.get_color() == 'k'


def test_very_axis_hist():
    themes.blog_mpl()
    fig, ax = fig_and_ax()

    for loc in np.arange(0, 35, 5):
        x = np.random.normal(loc, 1, 100)
        ax.hist(x)

    for patch in ax.patches:
        assert patch._hatch in themes.VeryAxis.style_cycles["hatch"]
        assert patch._facecolor in themes.VeryAxis.style_cycles["color"]
        assert patch._edgecolor in themes.VeryAxis.style_cycles["edgecolor"]


def test_very_axis_scatter():
    themes.blog_mpl()
    fig, ax = fig_and_ax()

    for loc in np.arange(0, 50, 5):
        x = np.random.normal(loc, 1, 20)
        y = np.random.normal(loc - np.random.random() * loc, 1, 20)
        ax.scatter(x, y, s=50, label=loc)

    for patch in ax.collections:
        print(dir(patch))
        assert all(
            tuple(col) in themes.VeryAxis.style_cycles["color"]
            for col in patch._facecolors)
        assert all(
            tuple(col) in themes.VeryAxis.style_cycles["edgecolor"]
            for col in patch._edgecolors)


def test_very_axis_despine(mocker):
    themes.blog_mpl()
    fig, ax = fig_and_ax()

    despine_patch = mocker.patch("very_plot.themes.sns.despine")

    ax.despine()
    assert despine_patch.call_args[0][0] == fig
    assert despine_patch.call_args[1] == {"trim": True}
