"""
Project-Abyss Configuration Service

Handles loading, reading and saving application configuration.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


class Config:
    """Central configuration manager."""

    def __init__(self, config_path: str | Path | None = None):
        if config_path is None:
            config_path = (
                Path(__file__).resolve().parent.parent
                / "config"
                / "settings.json"
            )

        self.config_path = Path(config_path)
        self._data: dict[str, Any] = {}

        self.load()

    def load(self) -> None:
        """Load configuration from disk."""

        if not self.config_path.exists():
            raise FileNotFoundError(
                f"Configuration file not found: {self.config_path}"
            )

        with self.config_path.open("r", encoding="utf-8") as file:
            self._data = json.load(file)

    def save(self) -> None:
        """Save configuration to disk."""

        with self.config_path.open("w", encoding="utf-8") as file:
            json.dump(self._data, file, indent=4)

    def get(self, key: str, default: Any = None) -> Any:
        """
        Get a configuration value using dot notation.

        Example:
            config.get("assistant.name")
        """

        value = self._data

        for part in key.split("."):
            if isinstance(value, dict) and part in value:
                value = value[part]
            else:
                return default

        return value

    def set(self, key: str, value: Any) -> None:
        """
        Set a configuration value using dot notation.

        Example:
            config.set("assistant.name", "Friday")
        """

        keys = key.split(".")
        current = self._data

        for part in keys[:-1]:
            current = current.setdefault(part, {})

        current[keys[-1]] = value

    def reload(self) -> None:
        """Reload configuration from disk."""
        self.load()