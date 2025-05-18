class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []

    def pets(self):
        # Return all pets owned by this owner
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        # Check that pet is an instance of Pet
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        # Assign owner to pet
        pet.owner = self
        # Optionally, add pet to owner's pet list if maintaining a list
        if pet not in self._pets:
            self._pets.append(pet)

    def get_sorted_pets(self):
        # Return pets sorted by name
        return sorted(self.pets(), key=lambda p: p.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        # Validate pet_type
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet_type: {pet_type}")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        self.set_owner(owner)
        Pet.all.append(self)

    def set_owner(self, owner):
        # Validate owner type if provided
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an Owner instance")
        self.owner = owner
        # If owner provided, add pet to owner's list
        if owner is not None:
            owner.add_pet(self)