# `example_2`

An example pipeline/package that uses the databaker package

```{warning}
Where this documentation refers to the root folder we mean where this README.md is
located.
```

## Getting started

It's suggested that you install this package and it's requirements within a virtual environment.

### Installing the package

Whilst in the root folder, in the command prompt, you can install the package and it's dependencies
using:

```shell
pip install -e .
```

This installs an editable version of the package. Meaning, if you update the
package code, you do not have to reinstall it for the changes to take effect.
(This saves a lot of time when you test your code)

Remember to update the setup and requirement files inline with any changes to your
package. The inital files contain the bare minimum to get you started.

## Running the pipeline scripts
### Read the messy csv

This package has two pipeline scripts. The first is `read_messy_data_pipeline.py`. This script reads in a messy csv (a csv that would be difficult to read in another way. e.g. using pandas) and saves a tidy version as a csv.

To use this pipeline script you must amend the `read_data_config.json` to reflect the data you wish to scrape (if you are directly using this example no changes are required). After this you can run the pipeline, from the root of this example (inside the example_2 folder), by entering the following into the terminal.

```shell
python src/my_package2/read_messy_data_pipeline.py
```

The second pipeline script is the `analysis_pipeline.py`. This is a basic analysis on the tidy data to show an example usage. Before running the script change the `analysis_config.json` file to match your requirements (if you are directly using this example no changes are required). After that you can run the pipeline using the following command in the terminal.

```shell
python src/my_package2/analysis_pipeline.py
```

Alternatively, most Python IDE's allow you to run the code directly from the IDE using a `run` button.

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].
