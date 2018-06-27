import matplotlib.pyplot as plt
import seaborn.apionly as sns
from cycler import cycler


def blog_mpl_bw():
    """
    Apply black and white blog theme for matplotlib.

    Usage:
    ```
    from very_plot import themes

    themes.blog_mpl_bw()
    ```

    All plots after this import will follow this theme.
    """
    monochrome = (cycler('color', ['k']) * cycler('marker', ['', '.']) *
                  cycler('linestyle', ['-', '--', ':', '-.']))
    plt.rc('axes', prop_cycle=monochrome)

    sns.set_style('ticks')
