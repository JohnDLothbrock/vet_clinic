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

    <li
      style={{
        marginBottom: "15px"
      }}
    >

      <strong>{owner.name}</strong>
      {" - "}
      {owner.phone}

      {showActions && (

        <div
          style={{
            marginTop: "5px"
          }}
        >

          {canEditOwner() && (

            <button
              onClick={() => editOwner(owner)}
              disabled={
                deletingId === owner.id
              }
            >
              Edit
            </button>

          )}

          {canDeleteOwner() && (

            <button
              onClick={() => deleteOwner(owner.id)}
              disabled={
                deletingId === owner.id
              }
              style={{
                marginLeft: "10px"
              }}
            >

              {deletingId === owner.id
                ? "Deleting..."
                : "Delete"}

            </button>

          )}

        </div>

      )}

    </li>
  );
}

export default OwnerItem;