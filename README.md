![](https://img.shields.io/badge/code%20style-black-000000.svg)

# Development

## Install dev requirements
`pip install -r requirements-dev.txt`

## Formatting
- `black .`

## Linting
- `flake8`

## Run test
- `pytest --cov=hw` run test
- `pytest --cov=hw --cov-report html` run test with html report

## Install pre-commit
- `pip install pre-commit`
- add hooks
  `pre-commit install`
  `pre-commit install --hook-type commit-msg`
- update to the latest versions `pre-commit autoupdate`

Note:
flake8 dependencies are duplicated in the `additional_dependencies` section.
This might be a problem.
