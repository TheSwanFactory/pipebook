# pipebook
Next-generation notebook for resilient, production-ready data pipelines

A graphical user interface based on [The Data Config](https://benn.substack.com/p/the-data-config) design pattern using [FRIDAAY](https://github.com/TheSwanFactory/fridaay)

See the introductory [PipeBook](https://ihack.us/2022/06/30/pipebook-yml-reimagining-notebooks-as-resilient-data-pipelines/) blog post.

## Usage

Use `poetry` to manage both dependencies and the virtual environment:
```
$ poetry install # or '$ poetry update'
$ poetry run python3 -m pipebook
```
## Development

```
$ poetry env use python3
$ poetry run pytest
$ poetry run ptw
```
## Implementation

Uses the [Toga GUI Toolkit](https://toga.readthedocs.io/en/latest/index.html) for Python. For more details, see the [PipeBook UX Design Brief](https://ihack.us/2022/07/09/pipebook-ux-design-brief/).
