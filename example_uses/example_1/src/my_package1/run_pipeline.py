import json

from my_package1.analysis.basic_analysis import plot_values, split_data_by_column
from my_package1.data_handling.read_messy_data import (
    create_conversion_segment,
    load_table,
)


def run_pipeline():
    "The main run script for the package"
    with open("pipeline_config.json", "r") as f:
        config = json.load(f)

    table = load_table(config)
    conversion_segment = create_conversion_segment(table, config)
    df = conversion_segment.topandas()

    split_data = split_data_by_column(df, "Age")
    plot_values(split_data, "Years", "OBS", config["graph_title"])


if __name__ == "__main__":
    run_pipeline()
