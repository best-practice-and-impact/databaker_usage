def groupby_mean(df, drop_cols, groupby_cols):
    """Drop unused columns and group given columns

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe with columns to drop and columns to group on
    drop_cols : list[str]
        List of column headers to drop
    groupby_cols : list[str]
        list of columns to group on

    Returns
    -------
    pd.Dataframe
        Grouped dataframe
    """
    df = df.drop(drop_cols, axis=1)
    df = df.groupby(groupby_cols).mean()

    return df


def find_max_per_index(df):
    """Create a dictionary of level 0 indicies pairied with the max
    value in the level 1 index.

    Parameters
    ----------
    df : pd.Dataframe
        Pandas dataframe with multiIndex

    Returns
    -------
    dict
        dictionary of level 0 index paired with the max value from the
        level 1 index
    """
    level_0_max_pair = {}
    level_0_index_list = df.index.get_level_values(0).unique().to_numpy()

    for index in level_0_index_list:
        max_value = df.loc[index].max().to_numpy()[0]
        max_level_1_index = (
            df.loc[df["OBS"] == max_value].index.get_level_values(1).to_numpy()[0]
        )
        level_0_max_pair[index] = max_level_1_index

    return level_0_max_pair
