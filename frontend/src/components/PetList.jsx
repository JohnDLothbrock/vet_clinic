import PetItem from "./PetItem";

function PetList({

  pets,
  editPet,
  deletePet

}) {

  if (pets.length === 0) {

    return (
      <p className="empty-message">
        No pets found.
      </p>
    );
  }

  return (

    <div className="pet-list">

      {pets.map((pet) => (

        <PetItem
          key={pet.id}
          pet={pet}
          editPet={editPet}
          deletePet={deletePet}
        />

      ))}

    </div>
  );
}

export default PetList;