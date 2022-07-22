# pipebook
### Next-generation notebook for resilient, production-ready data pipelines

A graphical user interface based on [The Data Config](https://benn.substack.com/p/the-data-config) design pattern, using the [FRIDAAY](https://github.com/TheSwanFactory/fridaay) data format.

See the introductory [PipeBook](https://ihack.us/2022/06/30/pipebook-yml-reimagining-notebooks-as-resilient-data-pipelines/) blog post.

## Usage

Use `[poetry](https://python-poetry.org/docs/)` to manage both dependencies and the virtual environment:

### Installing Poetry

```
$ curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
# WINDOWS: (Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -
```

### Running PipeBook

```
$ poetry install # OR: '$ poetry update'
$ poetry run python -m pipebook
```
## Development

```
$ poetry env use python
$ poetry run pytest
$ poetry run ptw
```

## Releases
```
$ poetry version patch
$ poetry build && poetry publish
$ poetry version prepatch
```

## Implementation

Uses the [Toga GUI Toolkit](https://toga.readthedocs.io/en/latest/index.html) for Python. For more details, see the [PipeBook UX Design Brief](https://ihack.us/2022/07/09/pipebook-ux-design-brief/).
