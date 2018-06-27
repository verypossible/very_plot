import pytest
import matplotlib.pyplot as plt
import numpy as np

from very_plot import formatters


def test_blog_figure(mocker):
    despine_patch = mocker.patch("very_plot.formatters.sns.despine")

    fig = plt.figure()
    fig.add_subplot(121)
    fig.add_subplot(122)

    fig = formatters.blog_figure(fig)

    assert np.array_equal(fig.get_size_inches(), (8, 6))
    assert despine_patch.call_args[0][0] == fig
    assert despine_patch.call_args[1] == {"trim": True}
