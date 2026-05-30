function PetItem({

  pet,
  editPet,
  deletePet

}) {

  console.log(
    "PET ITEM:",
    pet
  );

  return (

    <div className="pet-card">

      <div>

        <h3>{pet.name}</h3>

        <p>
          Species: {pet.species}
        </p>

        <p>
          Age: {pet.age}
        </p>

        <p>
          Owner: {pet.owner_name}
        </p>

      </div>

      <div className="button-group">

        <button
          onClick={() => editPet(pet)}
        >
          Edit
        </button>

        <button
          onClick={() => deletePet(pet.id)}
          className="delete-button"
        >
          Delete
        </button>

      </div>

    </div>
  );
}

export default PetItem;