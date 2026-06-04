function OwnerItem({

  owner,
  editOwner,
  deleteOwner,
  deletingId

}) {

  return (

    <li
      style={{
        marginBottom: "15px"
      }}
    >

      <strong>{owner.name}</strong>
      {" - "}
      {owner.phone}

      <div
        style={{
          marginTop: "5px"
        }}
      >

        <button
          onClick={() => editOwner(owner)}
          disabled={
            deletingId === owner.id
          }
        >
          Edit
        </button>

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

      </div>

    </li>
  );
}

export default OwnerItem;