from pydantic import BaseModel

class NoteCreate(BaseModel):
    """
    Create a new note.
    """
    def cli_cmd(self):
        print("Creating the a new empty note.")
