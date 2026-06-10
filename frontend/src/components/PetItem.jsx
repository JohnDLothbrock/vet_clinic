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

      <div className="record-main">

        <div className="record-avatar">
          🐾
        </div>

        <div>

          <h3>
            {pet.name}
          </h3>

          <div className="record-details">

            <span>
              <strong>
                Species:
              </strong>
              {" "}
              {pet.species}
            </span>

            <span>
              <strong>
                Age:
              </strong>
              {" "}
              {pet.age}
            </span>

            <span>
              <strong>
                Owner:
              </strong>
              {" "}
              {pet.owner_name}
            </span>

          </div>

        </div>

      </div>

      {showActions && (

        <div className="button-group record-actions">

          {canEditPet() && (

            <button
              onClick={() => editPet(pet)}
              disabled={deletingId === pet.id}
              className="small-button"
            >
              Edit
            </button>

          )}

          {canDeletePet() && (

            <button
              onClick={() => deletePet(pet.id)}
              disabled={deletingId === pet.id}
              className="delete-button small-button"
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