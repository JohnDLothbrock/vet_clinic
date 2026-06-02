function PetItem({

  pet,
  editPet,
  deletePet,
  deletingId

}) {

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
          disabled={deletingId === pet.id}
        >
          Edit
        </button>

        <button
          onClick={() => deletePet(pet.id)}
          disabled={deletingId === pet.id}
          className="delete-button"
        >
          {deletingId === pet.id
            ? "Deleting..."
            : "Delete"}
        </button>

      </div>

    </div>
  );
}

export default PetItem;