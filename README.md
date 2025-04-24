# nbstrip-empty-cells

[![Downloads](https://static.pepy.tech/badge/nbstrip-empty-cells)](https://pepy.tech/project/nbstrip-empty-cells)
[![PyPI version](https://badge.fury.io/py/nbstrip-empty-cells.svg)](https://badge.fury.io/py/nbstrip-empty-cells)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## Usage with pre-commit

Add to your `.pre-commit-config.yaml`:

```yaml
- repo: https://github.com/Drew5040/nbstrip-empty-cell
  rev: v0.1.0
  hooks:
    - id: nbstrip-empty-cells
```

Then install the pre-commit hook in your local repository:

```bash
pre-commit install
```

You can also run the hook manually on all files:
```bash
pre-commit run --all-files
```

## Downloads

