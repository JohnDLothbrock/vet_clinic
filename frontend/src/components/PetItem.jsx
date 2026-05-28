function PetItem({

  pet,
  editPet,
  deletePet

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