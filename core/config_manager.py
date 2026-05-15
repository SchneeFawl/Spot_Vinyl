import json
from pathlib import Path

class ConfigManager:
    def __init__(self, config_path) -> None:
        self.path = Path(config_path)
        self.config = self._load_config()

    def _load_config(self):
        if self.path.exists():
            try:
                with open(self.path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass        # if file corrupted then fall bnack to defaults

        # default values
        return {
            "discord_webhook_url": "",
            "discord_enabled": False,
            "always_on_top": False,
            "theme": "Classic"
        }

    def save(self) -> None:
        with open(self.path, "w") as f:
            json.dump(self.config, f, indent=4)
    
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value) -> None:
        self.config[key] = value
        self.save()
