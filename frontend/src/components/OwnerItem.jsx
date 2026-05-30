function OwnerItem({

  owner,
  editOwner,
  deleteOwner

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

      <div style={{ marginTop: "5px" }}>

        <button
          onClick={() => editOwner(owner)}
        >
          Edit
        </button>

        <button
          onClick={() => deleteOwner(owner.id)}
          style={{
            marginLeft: "10px"
          }}
        >
          Delete
        </button>

      </div>

    </li>
  );
}

export default OwnerItem;