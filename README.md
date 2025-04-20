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