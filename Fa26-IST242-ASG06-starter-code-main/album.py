"""
Represents a music album or podcast series, including the years it was active.

Key concepts to implement:
  • Input validation in __init__ (fail-fast with a clear ValueError).
  • Defensive copy on both input and output so external code cannot corrupt
    the internal years list.
  • A *derived* property (debut_year) that computes its value from stored data
    rather than keeping a second field in sync.
"""
class Album:
    def __init__(self, title, active, years):
        if not years:
            raise ValueError("years list cannot be empty")

        self._title = title
        self._active = active
        self._years = years.copy()  

    @property
    def title(self):
        return self._title

    @property
    def active(self):
        return self._active

    @property
    def debut_year(self):
        return self._years[0]

    @property
    def years(self):
        return self._years.copy()

    def __str__(self):
        return f"{self.title} active = {self._active},  debut year: {self.debut_year}"