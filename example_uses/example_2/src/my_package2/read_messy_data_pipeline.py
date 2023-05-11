import json

from my_package2.read_data.read_messy_data import create_conversion_segment, load_table


def run_pipeline():
    """The "main" script for this pipeline. Runs all the api functions
    within the package"""

    with open("read_data_config.json", "r") as f:
        config = json.load(f)

    table = load_table(config)
    conversion_segment = create_conversion_segment(table, config)
    df = conversion_segment.topandas()

    df.to_csv("data/tidy_data.csv")
    print(df)


if __name__ == "__main__":
    run_pipeline()
