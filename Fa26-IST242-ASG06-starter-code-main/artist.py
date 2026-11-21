"""
Represents a musical artist or podcast creator.

This is the simplest class in the hierarchy — no dependencies, no validation.
It introduces two core Python OOP conventions:
  1. The single leading-underscore (_name) signals a non-public attribute.
  2. @property exposes a clean public getter without allowing direct mutation.
"""
class Artist:
    def __init__(self, name, genre):
        self._name = name
        self._genre = genre

    @property
    def name(self):
        return self._name

    @property
    def genre(self):
        return self._genre
    def __str__(self):
        return f"{self.name} ({self.genre})"