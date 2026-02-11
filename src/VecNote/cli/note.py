import subprocess

from pydantic import BaseModel
from pydantic_settings import CliApp, CliSubCommand
from VecNote.note import Note
from VecNote.config import Dir_path, file_name_format, editior
from pathlib import Path


class NoteCreate(BaseModel):
    """
    Create a new note.
    """

    def cli_cmd(self):
        print("Creating the a new empty note.")
        dire_path = Dir_path
        note = Note.create_empty(dire_path, file_name_format)
        print(f"Note was create successfully.: {note.path.as_posix()}")



class NoteEdit(BaseModel):
    """
    Edit a new note.
    """
    path: Path | None = None


    def cli_cmd(self):
        print("editing the Note")
        path = self.path or Note.last_created_file
        if path is None:
            print("No path was given to create")
            return
        note = Note.from_path(path)
        subprocess.run([editior, note.path.as_posix()])


class NoteCommands(BaseModel):
    """
    List of Note commands
    """
    create: CliSubCommand[NoteCreate]
    edit: CliSubCommand[NoteEdit]

    def cli_cmd(self):
        CliApp.run_subcommand(self)
