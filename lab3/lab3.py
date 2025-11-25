import json
import os

class Individual:
    #reprezentareIndivid (day 1)
    def __init__(self, id, is_humanoid, planet, age, traits):
        self.__id = id
        self.__is_humanoid = is_humanoid
        self.__planet = planet
        self.__age = age
        self.__traits = traits if traits else []
    
    @property
    def id(self):
        return self.__id
    
    @property
    def is_humanoid(self):
        return self.__is_humanoid
    
    @property
    def planet(self):
        return self.__planet
    
    @property
    def age(self):
        return self.__age
    
    @property
    def traits(self):
        return self.__traits
    
    def to_dict(self):
        return {
            "id": self.__id,
            "isHumanoid": self.__is_humanoid,
            "originPlanet": self.__planet,
            "age": self.__age,
            "physicalTraits": self.__traits if self.__traits else None
        }
    
    def __repr__(self):
        return f"Individual(id={self.__id}, planet={self.__planet})"


class Universe:
    def __init__(self, name):
        self.__name = name
        self.__individuals = []
    
    @property
    def name(self):
        return self.__name
    
    @property
    def individuals(self):
        return self.__individuals
    
    def add_individual(self, individual):
        self.__individuals.append(individual)
    
    def get_count(self):
        return len(self.__individuals)


class Classifier:
    #clasificare (day 4)
    
    @staticmethod
    def classify(individual):
        
        planet = individual.planet
        traits = set(individual.traits)
        
        if planet in ["KASHYYYK", "ENDOR"]:
            return "starwars"
        
        if planet == "BETELGEUSE":
            return "hitchhiker"
        if planet == "VOGSPHERE":
            return "hitchhiker"
        if {"EXTRA_ARMS", "EXTRA_HEAD"}.intersection(traits):
            return "hitchhiker"
        
        if "POINTY_EARS" in traits:
            return "rings"
        if {"SHORT", "BULKY"}.issubset(traits) and individual.is_humanoid:
            return "rings"
        
        # Marvel - Asgardians
        if planet == "ASGARD":
            return "marvel"
        if {"BLONDE", "TALL"}.issubset(traits) and individual.age and individual.age > 200:
            return "marvel"
        
        return None


class FileHandler:
    #citire/scriere fișiere (day 2/ day 5)
    
    @staticmethod
    def read_input(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Error: File not found at {file_path}")
            return []
        except json.JSONDecodeError:
            print(f"Error: Invalid JSON in {file_path}")
            return []
    
    @staticmethod
    def write_output(universe, output_path):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        data = [ind.to_dict() for ind in universe.individuals]
        
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"✓ Written {universe.get_count()} individuals to {output_path}")


def main():
    # inițializareUniversuri
    universes = {
        "starwars": Universe("Star Wars"),
        "hitchhiker": Universe("Hitchhiker's Guide"),
        "rings": Universe("Lord of the Rings"),
        "marvel": Universe("Marvel")
    }
    
    unclassified = Universe("Unclassified")
    
    # citireImputday 2)
    input_path = os.path.join("resources", "input.json")
    data = FileHandler.read_input(input_path)
    
    if not data:
        print("No data to process!")
        return
    
    # Mapare JSON -> Oobiecte (day 3)
    individuals = []
    for item in data:
        ind = Individual(
            id=item.get("id"),
            is_humanoid=item.get("isHumanoid"),
            planet=item.get("originPlanet"),
            age=item.get("age"),
            traits=item.get("physicalTraits")
        )
        individuals.append(ind)
    
    print(f"✓ Loaded {len(individuals)} individuals")
    
    # clasificare(day 4)
    for ind in individuals:
        universe_name = Classifier.classify(ind)
        
        if universe_name and universe_name in universes:
            universes[universe_name].add_individual(ind)
        else:
            unclassified.add_individual(ind)
    
    # afișareStatistici
    print("\n=== Classification Results ===")
    for name, universe in universes.items():
        print(f"{name.capitalize()}: {universe.get_count()} individuals")
    print(f"Unclassified: {unclassified.get_count()} individuals")
    
    # scriereOutput(day 5)
    output_dir = os.path.join("resources", "output")
    output_files = {
        "starwars": "star-wars.json",
        "hitchhiker": "hitchhiker.json",
        "rings": "rings.json",
        "marvel": "marvel.json"
    }
    
    print("\n=== Writing Output Files ===")
    for name, filename in output_files.items():
        output_path = os.path.join(output_dir, filename)
        FileHandler.write_output(universes[name], output_path)
    
    if unclassified.get_count() > 0:
        FileHandler.write_output(
            unclassified, 
            os.path.join(output_dir, "unclassified.json")
        )


if __name__ == "__main__":
    main()