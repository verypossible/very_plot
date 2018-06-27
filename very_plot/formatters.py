import seaborn.apionly as sns


def blog_figure(fig, size=(8, 6), grid=True):
    """
    Formate a blog figure

    Usage:
    ```
    import matplotlib.pyplot as plt
    from very_plot import formatters

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(data)

    fig = formatters.blog_mpl_bw(fig, size=(width_inches,
                                            height_inches), grid=True)
    ```

    This will format the plot nicely for you.
    """

    fig.set_size_inches(*size)
    sns.despine(fig, trim=True)

    if grid:
        for ax in fig.axes:
            ax.grid()

    return fig
