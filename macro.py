import textwrap
import logging
from pathlib import Path
from typing import List


class Macro:
    OUTPUT_VARIABLE_NAME = "pyrmont_macro_output"

    def __init__(self, file_line_offset: int, code_lines: List[str], indent_size: int, pyrm_path: Path):
        self.file_path = pyrm_path
        self.indent_size = indent_size
        self.file_line_offset_start = file_line_offset
        self.file_line_offset = file_line_offset - len(code_lines) + 3

        logging.debug(f"- Macro @ line {self.file_line_offset_start}")

        self.code = textwrap.dedent("".join(code_lines)) + f"{self.OUTPUT_VARIABLE_NAME} = __TEMP_PYRMONT__"
