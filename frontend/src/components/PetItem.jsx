import {
  canEditPet,
  canDeletePet
} from "../services/permissionService";

function PetItem({

  pet,
  editPet,
  deletePet,
  deletingId

}) {

  const showActions =
    canEditPet() ||
    canDeletePet();

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

      {showActions && (

        <div className="button-group">

          {canEditPet() && (

            <button
              onClick={() => editPet(pet)}
              disabled={deletingId === pet.id}
            >
              Edit
            </button>

          )}

          {canDeletePet() && (

            <button
              onClick={() => deletePet(pet.id)}
              disabled={deletingId === pet.id}
              className="delete-button"
            >
              {deletingId === pet.id
                ? "Deleting..."
                : "Delete"}
            </button>

          )}

        </div>

      )}

    </div>
  );
}

export default PetItem;