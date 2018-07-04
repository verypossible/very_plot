import matplotlib
import matplotlib.axes._axes
import matplotlib.pyplot as plt
import seaborn as sns
from cycler import cycler


def blog_mpl():
    """
    Apply black and white blog theme for matplotlib.

    Usage:
    ```
    from very_plot import themes

    themes.blog_mpl_bw()
    ```

    All plots after this import will follow this theme.
    """
    matplotlib.rcParams["axes.grid"] = True

    monochrome = (cycler('color', ['k']) * \
                  cycler('marker', ['', '.']) * \
                  cycler('linestyle', ['-', '--', ':', '-.']) * \
                  cycler('alpha', [1.0]))

    plt.rc(
        'axes',
        prop_cycle=monochrome,
    )

    sns.set_style('ticks')

    matplotlib.projections.register_projection(VeryAxis)


class VeryAxis(matplotlib.axes._axes.Axes):

    style_cycles = {
        "hatch": ["", "", ".", "*", "o", "/", "x", "+"],
        "marker": ["o", "o", "*", "*", "v", "v", "s", "s", "D", "D"],
        "color": [(0, 0, 0, 1), (1, 1, 1, 1)],
        "edgecolor": [(1, 1, 1, 1), (0, 0, 0, 1)]
    }

    def __init__(self, *args, **kwargs):
        self.hist_calls = 0
        self.scatter_calls = 0
        self.despined = False

        super(VeryAxis, self).__init__(*args, **kwargs)
        super(VeryAxis, self).grid()

    def plot(self, *args, **kwargs):
        result = super(VeryAxis, self).plot(*args, **kwargs)

        return result

    def hist(self, *args, despine=True, **kwargs):
        hist_args = ["color", "edgecolor", "hatch"]

        self.__set_kwargs(hist_args, kwargs, self.hist_calls)
        self.hist_calls += 1
        result = super(VeryAxis, self).hist(*args, **kwargs)

        return result

    def scatter(self, *args, **kwargs):
        scatter_args = ["color", "edgecolor", "marker"]

        self.__set_kwargs(scatter_args, kwargs, self.scatter_calls)
        self.scatter_calls += 1
        result = super(VeryAxis, self).scatter(*args, **kwargs)

        return result

    def __set_kwargs(self, overrides, kwargs, index):
        for arg in overrides:
            opts = self.style_cycles[arg]
            kwargs[arg] = kwargs.get(arg, opts[index % len(opts)])

    def despine(self):
        sns.despine(self.figure, trim=True)
