from databaker import framework
from databaker.framework import ConversionSegment, loadxlstabs
from databaker.jupybakehtml import HDim


def load_table(config):
    """Load the desired table using the table number and file path in config

    Parameters
    ----------
    config : dict
        dictionary containing a file path and table number

    Returns
    -------
    databaker cellbag
        cellbag containing all the cells from the table
    """
    tables = loadxlstabs(config["file_path"])
    table = tables[config["table_number"]]

    return table


def create_dimension(table, dim_title, dim_settings):
    """Create a dimension for your observations. E.g. row or column headers

    Parameters
    ----------
    table : cell bag
        cell bag of all the cells in the table
    dim_title : str
        The title for the dimension
    dim_settings : dict
        Configurations for the dimension

    Returns
    -------
    Databaker HDim
        Databaker dimension with the configured values
    """
    cells = (
        table.excel_ref(dim_settings["cell_range"]).is_not_blank().is_not_whitespace()
    )
    search_type = getattr(framework, dim_settings["search_type"])
    direction = getattr(framework, dim_settings["direction"])
    dim = HDim(cells, dim_title, search_type, direction)

    return dim


def create_conversion_segment(table, config):
    """Create a databaker conversion segment using a config

    Parameters
    ----------
    table : Cell bag
        Cell bag of all the cells within a table
    config : dict
        configuration needed to extract data from cell bag

    Returns
    -------
    Databaker ConversionSegment
        A ConversionSegment with the extracted values
    """
    dimensions = []
    for dim_title, dim_settings in config["dimensions"].items():
        dim = create_dimension(table, dim_title, dim_settings)
        dimensions.append(dim)

    observations = (
        table.excel_ref(config["observation_range"]).is_not_blank().is_not_whitespace()
    )
    conversion_segment = ConversionSegment(observations, dimensions)

    return conversion_segment


def load_and_create_dataframe(config):
    """Load data, extract useful information and convert data to pandas dataframe

    Parameters
    ----------
    config : dict
        configuration to extract data from messy csv

    Returns
    -------
    Dataframe
        Pandas dataframe with a row per observation and column per dimension.
    """
    table = load_table(config)
    conversion_segment = create_conversion_segment(table, config)
    df = conversion_segment.topandas()

    return df


def reduce_string_len(string, length=3):
    """Reduce the length of a string to a given length

    Parameters
    ----------
    string : str
        string to shorten
    length : int, optional
        The length to shorten a string to, by default 3

    Returns
    -------
    str
        The shortened string
    """
    return string[:length]


def clean_data(df):
    """Clean the data of special characters and bring string data
    down to a common length

    Parameters
    ----------
    df : pd.Dataframe
        Dataframe to clean

    Returns
    -------
    pd.Dataframe
        Cleaned data
    """
    df["Month"] = df["Month"].str.replace("¹", "", regex=True)
    df["Month"] = df["Month"].str.replace("†", "", regex=True)

    df["Month"] = df["Month"].apply(reduce_string_len)

    return df
