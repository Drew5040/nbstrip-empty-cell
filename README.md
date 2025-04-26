# nbstrip-empty-cells
[![Downloads](https://static.pepy.tech/badge/nbstrip-empty-cells)](https://pepy.tech/project/nbstrip-empty-cells)
[![PyPI version](https://badge.fury.io/py/nbstrip-empty-cells.svg)](https://badge.fury.io/py/nbstrip-empty-cells)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


## v0.1.2
- Minor edits to documentation and README formatting.

## What this Hook Does
This hook automatically removes empty code and markdown cells from Jupyter notebooks before they are committed. 
It helps keep your notebooks clean and version control diffs minimal.

## Why use this Tool:
- Avoid noisy diffs from empty cells.
- Keep your notebooks clean and readable, especially in version control.
- Seamlessly integrates with your Git workflow via pre-commit
- Safe to run on mixed repositories — non-.ipynb files are ignored.

## Example usage with pre-commit & pip
Add to your `.pre-commit-config.yaml` in your notebook repository:

```yaml
- repo: https://github.com/Drew5040/nbstrip-empty-cell
  rev: v0.1.1
  hooks:
    - id: nbstrip-empty-cells
```

Then install pre-commit in your local repository:

```bash
pre-commit install
```

Update all hook versions:

```bash
pre-commit autoupdate
```

Then run the hook (nbstrip-empty-cells) manually on all files (safe to do so):
```bash
pre-commit run --all-files
```

Installation & Usage via pip & CLI (Optional)
```bash
pip install nbstrip-empty-cells

nbstrip-empty-cells notebook1.ipynb notebook2.ipynb 
```


