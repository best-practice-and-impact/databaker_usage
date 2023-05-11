from databaker import framework
from databaker.framework import ConversionSegment, loadxlstabs, warnings, xypath
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


def DuplicateCellValueOverride(self, cells_to_override, cell_to_duplicate):
    """Duplicate a chosen value across a range of cells

    Parameters
    ----------
    cells_to_override : str
        The range of cells to override with the duplicate value. string in the
        form 'A7:A8'
    cell_to_duplicate : str
        Cell to duplicate across range
    """

    if isinstance(cell_to_duplicate, xypath.xypath.Bag):
        assert len(cell_to_duplicate) == 1, "Can only duplicate a single cell"
        cell_to_duplicate = cell_to_duplicate._cell
        duplicate_value = cell_to_duplicate.value

    for overridecell in cells_to_override:

        overridecell = overridecell._cell

        # add the cell into the base set of cells if it's new
        if overridecell not in self.hbagset.unordered_cells:
            if not self.bhbagsetCopied:
                self.hbagset = self.hbagset | (
                    self.hbagset.by_index(1) if len(self.hbagset) else self.hbagset
                )  # force copy by adding element from itself
                self.bhbagsetCopied = (
                    True  # avoid inefficient copying every single time
                )
            self.hbagset.add(overridecell)
            self.samerowlookup = None  # abolish any caching
        else:
            if overridecell in self.cellvalueoverride:
                if self.cellvalueoverride[overridecell] != duplicate_value:
                    warnings.warn(
                        "Cell %s was already overridden by value %s; is this a mistake?"
                        % (overridecell, self.cellvalueoverride[overridecell])
                    )

        assert duplicate_value is None or isinstance(
            duplicate_value, (str, float, int)
        ), "Override from value should only be str,float,int,None (%s)" % type(
            duplicate_value
        )
        self.cellvalueoverride[overridecell] = duplicate_value


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
    setattr(HDim, "DuplicateCellValueOverride", DuplicateCellValueOverride)

    if "override_cells" in dim_settings:
        for cell, new_value in dim_settings["override_cells"].items():
            dim.AddCellValueOverride(table.excel_ref(cell), new_value)

    if "duplicate_cells" in dim_settings:
        for cells, new_value in dim_settings["duplicate_cells"].items():
            dim.DuplicateCellValueOverride(
                table.excel_ref(cells), table.excel_ref(new_value)
            )

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
