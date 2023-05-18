import json

import pandas as pd

from my_package2.analysis.basic_analysis import find_max_per_index, groupby_mean


def run_pipeline():
    """The "main" script for this pipeline. Runs all the api functions
    within the package"""

    with open("analysis_config.json", "r") as f:
        config = json.load(f)

    df = pd.read_csv(config["file_path"], index_col=0)

    month_df = groupby_mean(df, ["Year"], ["Month", "Area"])
    month_destination_dict = find_max_per_index(month_df)

    year_df = groupby_mean(df, ["Month"], ["Year", "Area"])
    year_destination_dict = find_max_per_index(year_df)

    print("The most popular distination for each month was")
    print(month_destination_dict)

    print("The most popular distination for each year was")
    print(year_destination_dict)


if __name__ == "__main__":
    run_pipeline()
