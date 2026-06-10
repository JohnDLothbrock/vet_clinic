import {
  canEditOwner,
  canDeleteOwner
} from "../services/permissionService";

function OwnerItem({

  owner,
  editOwner,
  deleteOwner,
  deletingId

}) {

  const showActions =
    canEditOwner() ||
    canDeleteOwner();

  return (

    <div className="owner-card">

      <div className="record-main">

        <div className="record-avatar owner-avatar">
          👤
        </div>

        <div>

          <h3>
            {owner.name}
          </h3>

          <div className="record-details">

            <span>
              <strong>
                Phone:
              </strong>
              {" "}
              {owner.phone}
            </span>

          </div>

        </div>

      </div>

      {showActions && (

        <div className="button-group record-actions">

          {canEditOwner() && (

            <button
              onClick={() =>
                editOwner(
                  owner
                )
              }
              disabled={
                deletingId === owner.id
              }
              className="small-button"
            >
              Edit
            </button>

          )}

          {canDeleteOwner() && (

            <button
              onClick={() =>
                deleteOwner(
                  owner.id
                )
              }
              disabled={
                deletingId === owner.id
              }
              className="delete-button small-button"
            >

              {deletingId === owner.id
                ? "Deleting..."
                : "Delete"}

            </button>

          )}

        </div>

      )}

    </div>
  );
}

export default OwnerItem;