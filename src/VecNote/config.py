from pathlib import Path
from typing import Any

from platformdirs import user_config_path
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_settings.sources import (
    PydanticBaseSettingsSource,
    TomlConfigSettingsSource,
)
import rtoml

Dir_path = Path("./")
file_name_format = "%Y%m%d%H%M%S"
# editior = "edit"
lastfile_path = None
config_file = "config.toml"
config_dir = user_config_path() / "VecNote"
config_path = config_dir / config_file


# config_path.touch()


class Setting(BaseSettings):
    """Tool settings"""
    last_file_creation_name: str = ""
    """ Store last file name create from create command to use in edit command"""
    editor: str = "edit"  # default one in windows 11 onwards
    """Text editor to be use"""

    model_config = SettingsConfigDict(toml_file=config_path)

    def model_post_init(self, __context: Any) -> None:
        if not config_path.exists():
            config_dir.mkdir(parents=True, exist_ok=True)
            config_path.touch()
            self.save()

    @classmethod
    def settings_customise_sources(
            cls,
            settings_cls: type[BaseSettings],
            init_settings: PydanticBaseSettingsSource,
            env_settings: PydanticBaseSettingsSource,
            dotenv_settings: PydanticBaseSettingsSource,
            file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        return (TomlConfigSettingsSource(settings_cls), init_settings)

    def save(self):
        """Save the settings"""
        config_path.write_text(rtoml.dumps(
            self.model_dump(), pretty=True, none_value=None
        ))


setting = Setting()
# print(setting.last_file_creation_name, setting.editor)
