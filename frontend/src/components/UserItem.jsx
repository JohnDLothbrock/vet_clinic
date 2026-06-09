function UserItem({

  user,
  updatingId,
  handleRoleChange,
  handleActiveChange

}) {

  const getRoleName =
    (roleId) => {

      if (roleId === 1) {

        return "Admin";
      }

      if (roleId === 2) {

        return "Veterinarian";
      }

      if (roleId === 3) {

        return "Receptionist";
      }

      return "Unknown";
    };

  return (

    <tr>

      <td>
        {user.id}
      </td>

      <td>
        {user.username}
      </td>

      <td>
        {user.email}
      </td>

      <td>
        <select
          value={user.role_id}
          onChange={(event) =>
            handleRoleChange(
              user.id,
              Number(event.target.value)
            )
          }
          disabled={updatingId === user.id}
        >

          <option value="1">
            Admin
          </option>

          <option value="2">
            Veterinarian
          </option>

          <option value="3">
            Receptionist
          </option>

        </select>

        <span className="role-label">
          {getRoleName(user.role_id)}
        </span>

      </td>

      <td>
        <span
          className={
            user.active
              ? "status-active"
              : "status-inactive"
          }
        >
          {user.active
            ? "Active"
            : "Inactive"}
        </span>
      </td>

      <td>

        <button
          type="button"
          onClick={() =>
            handleActiveChange(
              user.id,
              !user.active
            )
          }
          disabled={updatingId === user.id}
          className={
            user.active
              ? "delete-button"
              : "secondary-button"
          }
        >

          {updatingId === user.id
            ? "Updating..."
            : user.active
              ? "Deactivate"
              : "Activate"}

        </button>

      </td>

    </tr>
  );
}

export default UserItem;