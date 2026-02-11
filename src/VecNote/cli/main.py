from pydantic_settings import BaseSettings, CliApp, SettingsConfigDict, CliSubCommand
from VecNote.cli.note import NoteCommands

class VecNote(BaseSettings):
    """
    VecNote basic settings
    """
    note: CliSubCommand[NoteCommands]

    model_config = SettingsConfigDict(
        cli_prog_name="VectNote",
        cli_parse_args=True,
    )

    def cli_cmd(self):
        CliApp.run_subcommand(self)


def start() -> None:
    """
    Starting point for the code
    """
    CliApp.run(VecNote)


if __name__ == "__main__":
    start()
