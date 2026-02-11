from pydantic import BaseModel
from pathlib import Path
from datetime import datetime
from typing import Self


class Note(BaseModel):
    """
    Note model structure
    """
    path: Path
    """ Path to the Note file"""
    content: str | None = None
    """ Content"""

    @classmethod
    def create_empty(cls, dir_path: Path, file_name_format: str) -> Self:
        """
        Create a empty note given a directory.
        :param dir_path: path
        :param file_name: filename
        """
        now = datetime.now().strftime(file_name_format)
        note_path = dir_path.joinpath(f"{now}.md")
        note_path.touch(exist_ok=True)
        return cls(path=note_path)

    @classmethod
    def from_path(cls, path: Path) -> Self:
        """
        Load the nate from the path
        """
        note = cls(path=path)
        note.load()
        return note

    def load(self) -> None:
        """
        loads the note contains
        """
        text = self.path.read_text()
        self.content = text
