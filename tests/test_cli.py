from tempfile import NamedTemporaryFile
from nbformat import v4, read, write
from remove_empty_cells.cli import remove_empty_cells_from_file

def test_removes_empty_cells():
    # Create a temporary notebook with empty cells
    nb = v4.new_notebook()
    nb.cells = [
        v4.new_code_cell("print('Hello')"),
        v4.new_code_cell(""),
        v4.new_markdown_cell(""),
    ]

    with NamedTemporaryFile(suffix=".ipynb", mode="w+", delete=False) as f:
        write(nb, f)
        test_path = f.name

    # Run cleaner
    result = remove_empty_cells_from_file(test_path)

    # Reload and check
    cleaned_nb = read(open(test_path), as_version=4)

    assert result == 1
    assert len(cleaned_nb.cells) == 1
    assert cleaned_nb.cells[0].source == "print('Hello')"
