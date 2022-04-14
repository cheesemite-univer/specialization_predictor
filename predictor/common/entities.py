from dataclasses import dataclass
from dataclasses import field

@dataclass
class Grades(object):
    id: int = field(init=False)
    pupil_id: int = field(init=False)
    math: int
    physics: int
    biology: int
    chemistry: int
    economics: int
    history: int
    english: int
    art: int

@dataclass
class Wages(object):
    id: int = field(init=False)
    speciality_id: int = field(init=False)
    math: int
    physics: int
    biology: int
    chemistry: int
    economics: int
    history: int
    english: int
    art: int

@dataclass
class Pupil(object):
    id: int = field(init=False)
    name: str
    fullname: str
    grades: Grades = field()

@dataclass
class Speciality(object):
    id: int = field(init=False)
    name: str
    wages: Wages = field()

