# Copyright (C) 2024 Anaconda, Inc
# SPDX-License-Identifier: BSD-3-Clause
from conda import plugins

from .restricted import restrict_search_path


# TODO get this list of commands programmatically
@plugins.hookimpl
def conda_pre_commands():
    yield plugins.CondaPreCommand(
        name="restrict-search-path",
        action=restrict_search_path,
        run_for={
            "activate",
            "build",
            "clean",
            "compare",
            "config",
            "content",
            "convert",
            "create",
            "deactivate",
            "debug",
            "develop",
            "doctor",
            "export",
            "index",
            "info",
            "init",
            "inspect",
            "install",
            "list",
            "metapackage",
            "notices",
            "package",
            "remove",
            "rename",
            "render",
            "repoquery",
            "run",
            "search",
            "skeleton",
            "update",
        },
    )
