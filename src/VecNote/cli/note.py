from pydantic import BaseModel
from VecNote.note import Note
from VecNote.config import Dir_path,file_name_format

class NoteCreate(BaseModel):
    """
    Create a new note.
    """
    def cli_cmd(self):
        print("Creating the a new empty note.")
        dire_path = Dir_path
        note = Note.create_empty(dire_path,file_name_format)
        print("Note was create successfully.")
