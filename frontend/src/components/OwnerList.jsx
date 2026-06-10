import OwnerItem from "./OwnerItem";

function OwnerList({

  owners,
  editOwner,
  deleteOwner,
  deletingId

}) {

  if (owners.length === 0) {

    return (

      <div className="empty-state">

        <div className="empty-state-icon">
          👤
        </div>

        <h3>
          No owners found
        </h3>

        <p>
          Try clearing the search or create a new owner record.
        </p>

      </div>
    );
  }

  return (

    <div className="owner-list">

      {owners.map((owner) => (

        <OwnerItem
          key={owner.id}
          owner={owner}
          editOwner={editOwner}
          deleteOwner={deleteOwner}
          deletingId={deletingId}
        />

      ))}

    </div>
  );
}

export default OwnerList;