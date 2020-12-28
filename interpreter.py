from pathlib import Path

from macro import Macro


class InterpreterError(Exception):
    pass


__TEMP_PYRMONT__ = []
CURRENT_CONFIG_DIR: Path
CRLF = '\\r\\n'


def e(*args):
    global __TEMP_PYRMONT__
    for arg in args:
        __TEMP_PYRMONT__.append(arg)


def require(module_name):
    from importlib.machinery import SourceFileLoader
    from importlib.util import spec_from_loader, module_from_spec

    global CURRENT_CONFIG_DIR

    module_name = to_python_identifier(module_name)

    file_path = CURRENT_CONFIG_DIR / module_name
    if file_path.suffix != '.py':
        file_path = file_path.with_suffix('.py')

    loader = SourceFileLoader(module_name, str(file_path))
    spec = spec_from_loader(loader.name, loader)
    module = module_from_spec(spec)
    loader.exec_module(module)

    return module


def execute_macro(macro: Macro):
    import sys
    import traceback
    import logging
    from textwrap import indent
    from io import StringIO
    import contextlib

    global CURRENT_CONFIG_DIR, __TEMP_PYRMONT__

    @contextlib.contextmanager
    def exec_io(stdout=None):
        old = sys.stdout
        if stdout is None:
            stdout = StringIO()
        sys.stdout = stdout
        yield stdout
        sys.stdout = old

    CURRENT_CONFIG_DIR = Path(macro.file_path).parent
    __TEMP_PYRMONT__.clear()

    result = {}
    try:
        with exec_io() as s:
            exec(macro.code, globals(), result)

        logging.debug(f"- Output from macro @ line {macro.file_line_offset_start}:")
        logging.debug(indent(s.getvalue(), ' ' * 4) or '<none>')
    except SyntaxError as e:
        error_class = e.__class__.__name__
        details = e.args[0]
        line_number = macro.file_line_offset + e.lineno
    except Exception as e:
        error_class = e.__class__.__name__
        details = e.args[0]
        cl, exc, tb = sys.exc_info()
        line_number = macro.file_line_offset + traceback.extract_tb(tb)[-1][1]
    else:
        return result[macro.OUTPUT_VARIABLE_NAME]

    raise InterpreterError(f"{error_class} at line {line_number:d} of {macro.file_path}: {details}")


def to_python_identifier(string):
    import keyword
    import re

    # create a working copy (and make it lowercase, while we're at it)
    s = string.lower()

    # remove leading and trailing whitespace
    s = s.strip()

    # Make spaces into underscores
    s = re.sub(r'[\s\t\n]+', '_', s)

    # Remove invalid characters
    s = re.sub(r'[^0-9a-zA-Z_]', '', s)

    # Remove leading characters until we find a letter or underscore
    s = re.sub(r'^[^a-zA-Z_]+', '', s)

    # Check that the string is not a python identifier
    while s in keyword.kwlist:
        if re.match(r".*?_\d+$", s):
            i = re.match(r".*?_(\d+)$", s).groups()[0]
            s = s.strip('_' + i) + '_' + str(int(i) + 1)
        else:
            s += '_1'

    return s
