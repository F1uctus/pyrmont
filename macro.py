import textwrap
from pathlib import Path
from typing import List


class Macro:
    def __init__(self, code_lines: List[str], indent_size: int, pyrm_path: Path):
        code_lines = textwrap.dedent("".join(code_lines))
        cur_path = pyrm_path.parent
        self.indent_size = indent_size
        self.code = "\r\n".join([
            "__temp__pyrmont__ = []",
            f"CURRENTPATH = '{cur_path}'",
            "crlf = '\\r\\n'",
            "def e(*args):",
            "    global __temp__pyrmont__",
            "    for arg in args:",
            "        __temp__pyrmont__.append(arg)",
            "def require(file_name):",
            "    global CURRENTPATH",
            "    import importlib.util as imp",
            "    from os.path import join, abspath",
            "    spec = imp.spec_from_file_location(",
            "        'module.name',",
            "        abspath(join(CURRENTPATH, file_name + '.py'))",
            "    )",
            "    module = imp.module_from_spec(spec)",
            "    spec.loader.exec_module(module)",
            "    return module",
            code_lines,
            "pyrmont_macro_output = __temp__pyrmont__",
            ""
        ])
        print(self.code)
