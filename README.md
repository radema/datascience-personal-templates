# Data Science Project Template

This template has been built after reading the [Medium article by khuyetran1401](https://towardsdatascience.com/how-to-structure-an-ml-project-for-reproducibility-and-maintainability-54d5e53b4c82?sk=c3d05ae5b8ccc95822618d0dacfad8a4).
It would be much simpler to just fork its repo but I prefer to build it by myself to understand each component.
It has been built to be easy and quick to use. 

For 'industrial' or more 'business' projects, I still prefer tools like [Kedro](https://docs.kedro.org/en/stable/).

## Features and Roadmap

:white_check_mark: Automatically build repository structure for DS personal projects

:white_check_mark: Create and Build an environment using conda

:black_square_button: Run Tests automatically

:black_square_button: Manage configuration variables for data pipelines and projects

:white_check_mark: Enforce hints and quality code

:black_square_button: Automatically Document Code

:black_square_button: Automate Code

:white_check_mark: [DVC](https://dvc.org/doc/start) for Data Management and Experiment Management

### To Do
- Automate setup of dvc repo and .gitignore

## Tools used

- [Conda](https://docs.conda.io/en/latest/): Package, dependency and environment management
- [pre-commit](https://pre-commit.com/): framework for managing and maintaining multi-language pre-commit hooks. 

## Template Structure

```bash
.
├── config                       # Project configuration files
│   ├──environment.yml           # Environment file for conda
├── data                         # Local project data (not committed to version control)
│   ├── 01_raw                   # Raw immutable data
│   ├── 02_primary               # Domain model data
│   ├── 03_feature               # Model features
│   ├── 04_model_input           # Often called 'master tables'
│   ├── 05_model_output          # Data generated by model runs
│   ├── 06_reporting             # Ad hoc descriptive cuts
├── docs                         # Project documentation
├── models                       # Project configuration files
├── notebooks                    # Project related Jupyter notebooks (used for experimental code before moving code to src)
├── README.md                    # Project README
└── src                          # Project source code
    └── main.py
```

## How to use this template

Install Cookiecutter:

```bash
pip install cookiecutter
```

Create a project based on the template:

```bash
cookiecutter https://github.com/radema/datascience-personal-templates
```

Set up the environment:
```bash
make setup
make activate
```

To install new PyPI packages, run:
```bash
poetry add <package-name>
```

## Resources and references

- [khuyetran1401/data-sciente-template repository](https://github.com/khuyentran1401/data-science-template/blob/dvc-poetry/README.md)
- [Kedro startes](https://github.com/kedro-org/kedro-starters)
