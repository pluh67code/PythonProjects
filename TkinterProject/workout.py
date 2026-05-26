from exercise import Exercise
from dataclasses import dataclass, field

@dataclass
class Workout:
    name: str = "N/A"
    exercises: list[Exercise] = field(default_factory=list)

