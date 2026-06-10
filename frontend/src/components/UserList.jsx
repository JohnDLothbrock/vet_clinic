import UserItem from "./UserItem";

function UserList({

  users,
  updatingId,
  handleRoleChange,
  handleActiveChange

}) {

  if (users.length === 0) {

    return (

      <div className="empty-state">

        <div className="empty-state-icon users-empty-icon">
          👥
        </div>

        <h3>
          No users found
        </h3>

        <p>
          Create a new user account to manage staff access.
        </p>

      </div>
    );
  }

  return (

    <div className="table-wrapper">

      <table className="users-table polished-users-table">

        <thead>

          <tr>

            <th>
              ID
            </th>

            <th>
              User
            </th>

            <th>
              Email
            </th>

            <th>
              Role
            </th>

            <th>
              Status
            </th>

            <th>
              Actions
            </th>

          </tr>

        </thead>

        <tbody>

          {users.map(
            (user) => (

              <UserItem
                key={user.id}
                user={user}
                updatingId={updatingId}
                handleRoleChange={
                  handleRoleChange
                }
                handleActiveChange={
                  handleActiveChange
                }
              />

            )
          )}

        </tbody>

      </table>

    </div>
  );
}

export default UserList;