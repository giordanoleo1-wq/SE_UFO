from dataclasses import dataclass
@dataclass
class State:
    id : str
    name : str
    capital : str
    lat : float
    lng: float
    area : int
    population : int
    neighbors : str

    def __str__(self):
        return f"{self.id} {self.name} {self.lat} {self.lng} {self.neighbors}{self.population} {self.area}"
    def __hash__(self):
        return hash(self.id)

