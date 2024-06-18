# Copyright (C) 2024 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from conda.common.compat import on_win


# Define the search path for the .condarc file
# See conda's full example:
# https://github.com/conda/conda/blob/32bf03b8ecd99d183f6b1955532dc4acaa96874e/conda/base/constants.py#L28-L62
if on_win:
    CUSTOM_SEARCH_PATH = (
        "C:/ProgramData/conda-restricted/.condarc",
    )
else:
    CUSTOM_SEARCH_PATH = (
        "~/.conda-restricted/.condarc",
    )



def restrict_search_path(command):
    # inline import to prevent circular imports
    from conda.base.context import context, reset_context
    reset_context(search_path=CUSTOM_SEARCH_PATH)
