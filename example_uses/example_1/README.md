# `example_1`

An example pipeline/package that uses the databaker package. This example looks at how internet users in different age groups change between 2013 to 2020.

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

## Running the pipeline script

To run this example pipeline, first ensure the `pipeline_config.json` file is updated to match any changes you've made (if no changes are made after the git clone the config should work without changes). After this run the following command from the root of this example (inside the example_1 folder):

```shell
python src/my_package1/run_pipeline.py
```

Alternatively, most Python IDE's allow you to run the code directly from the IDE using a `run` button.

## Licence

Unless stated otherwise, the codebase is released under the MIT License. This covers
both the codebase and any sample code in the documentation. The documentation is ©
Crown copyright and available under the terms of the Open Government 3.0 licence.

## Acknowledgements

[This project structure is based on the `govcookiecutter` template
project][govcookiecutter].
