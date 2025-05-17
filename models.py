from dataclasses import dataclass
from typing import List, Dict

@dataclass
class Stage:
    name: str
    start_month: int
    end_month: int
    resource_needs: Dict[str, int]  # Role: Count

@dataclass
class Project:
    name: str
    start_month: int
    end_month: int
    stages: List[Stage]
