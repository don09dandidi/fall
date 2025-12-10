from dataclasses import dataclass


@dataclass
class Car:
    """Car model"""
    id: int
    type: str  # "ELECTRIC" or "GAS"
    passengers: str  # "PEOPLE" or "ROBOTS"
    is_dining: bool
    consumption: int
    
    @classmethod
    def from_dict(cls, data: dict) -> 'Car':
        """Create Car from dictionary"""
        return cls(
            id=data['id'],
            type=data['type'],
            passengers=data['passengers'],
            is_dining=data['isDining'],
            consumption=data['consumption']
        )
