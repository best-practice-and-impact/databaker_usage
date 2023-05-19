import matplotlib.pyplot as plt


def split_data_by_column(df, column_header):
    """Split the data within a dataset based on the unique
    values within a given column

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe of data to split
    column_header : str
        The column header which unique values will split the
        dataset

    Returns
    -------
    dict[any: pd.Dataframe]
        dictionary of unique value to dataframe pairs
    """
    unique_values = df[column_header].unique()
    split_data = {}

    for value in unique_values:
        observations = df.loc[df[column_header] == value]
        split_data[value] = observations

    return split_data


def plot_values(split_data, x_axis_header, y_axis_header, graph_title):
    """Plot multiple datasets from a dictionary

    Parameters
    ----------
    split_data : dict
        key value pairs of group: data
    x_axis_header : str
        The column header for the x-axis data
    y_axis_header : str
        The column header for the y-axis data
    graph_title : str
        The title for the graph
    """
    for value, observations in split_data.items():
        plt.plot(observations[x_axis_header], observations[y_axis_header], label=value)

    plt.xlabel(x_axis_header)
    plt.ylabel(y_axis_header)
    plt.title(graph_title)
    plt.legend()
    plt.show()
