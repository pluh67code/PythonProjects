from dataclasses import dataclass

@dataclass
class Exercise:
    name: str = "N/A"
    sets: int = 3
    reps: int = 5
