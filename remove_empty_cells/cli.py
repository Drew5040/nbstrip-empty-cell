import sys
import nbformat

def remove_empty_cells_from_file(file_path):


    # Read in noteboook
    with open(file_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    # Count & filter empty cells
    original_count = len(nb.cells)
    nb.cells = [cell for cell in nb.cells if cell.source and cell.source.strip()]
    removed = original_count - len(nb.cells)

    # Test for removed cells
    if removed > 0:
        with open(file_path, "w", encoding="utf-8") as f:
            nbformat.write(nb, f)
        print(f"{file_path}: Removed {removed} empty cell(s)")
        return 1
    else:
        return 0

def main():

    # Test & iterate over file paths
    exit_code = 0
    for file_path in sys.argv[1:]:
        if file_path.endswith(".ipynb"):
            result = remove_empty_cells_from_file(file_path)
            exit_code = exit_code or result
    sys.exit(exit_code)

# Run as script
if __name__ == "__main__":
    main()
