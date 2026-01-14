import datetime
from dataclasses import dataclass
@dataclass
class Sighting:
    id :int
    s_datetime : datetime.datetime
    city : str
    state : str
    country: str
    shape: str
    duration : int
    duration_hm : str
    comments: str
    date_posted : datetime.datetime
    latitude : float
    longitude : float
    def __str__(self):
        return f"{self.state} {self.shape} {self.latitude:.2f} {self.longitude:.2f}{self.s_datetime}{self.id}{self.comments}{self.date_posted}"

    def __hash__(self):
        return hash(self.id)

    def __lt__(self, other):
        return self.s_datetime.year < other.s_datetime.year