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

  const getRoleClass =
    (roleId) => {

      if (roleId === 1) {

        return "role-badge-admin";
      }

      if (roleId === 2) {

        return "role-badge-vet";
      }

      if (roleId === 3) {

        return "role-badge-receptionist";
      }

      return "role-badge-default";
    };

  return (

    <tr>

      <td>
        <span className="user-id-pill">
          #{user.id}
        </span>
      </td>

      <td>

        <div className="user-cell">

          <div className="user-avatar">
            {user.username
              .charAt(0)
              .toUpperCase()}
          </div>

          <div>

            <strong>
              {user.username}
            </strong>

            <span>
              Staff account
            </span>

          </div>

        </div>

      </td>

      <td>
        {user.email}
      </td>

      <td>

        <div className="role-control">

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

          <span
            className={`role-badge ${getRoleClass(user.role_id)}`}
          >
            {getRoleName(user.role_id)}
          </span>

        </div>

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
              ? "delete-button small-button"
              : "secondary-button small-button"
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