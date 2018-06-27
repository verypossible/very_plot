import pytest
import matplotlib.pyplot as plt
import numpy as np

from very_plot import themes


def test_blog_mpl_bw(mocker):
    themes.blog_mpl_bw()

    fig = plt.figure()
    ax = fig.add_subplot(121)

    ax.plot(np.arange(0, 10))
    ax.plot(np.arange(10, 20))

    for line in ax.get_lines():
        assert line.get_color() == 'k'
