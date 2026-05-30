import OwnerItem from "./OwnerItem";

function OwnerList({

  owners,
  editOwner,
  deleteOwner

}) {

  if (owners.length === 0) {

    return <p>No owners found.</p>;
  }

  return (

    <ul>

      {owners.map((owner) => (

        <OwnerItem
          key={owner.id}
          owner={owner}
          editOwner={editOwner}
          deleteOwner={deleteOwner}
        />

      ))}

    </ul>
  );
}

export default OwnerList;