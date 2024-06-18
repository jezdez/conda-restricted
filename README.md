# conda-restricted

A conda plugin to restrict the `SEARCH_PATH` for conda configuration files

## How?

- Install this conda plugin into your conda base environments:

  ```
  $ conda activate base
  $ (base) pip install "conda-restricted @ https://github.com/jezdez/conda-restricted/archive/refs/heads/main.zip"
  ```

- The only config files loades are the ones from `~/.conda-restricted/.condarc` (POSIX) and `C:/ProgramData/conda-restricted/.condarc` (Windows).
