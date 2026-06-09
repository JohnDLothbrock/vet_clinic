import UserItem from "./UserItem";

function UserList({

  users,
  updatingId,
  handleRoleChange,
  handleActiveChange

}) {

  if (users.length === 0) {

    return (
      <p>
        No users found.
      </p>
    );
  }

  return (

    <table className="users-table">

      <thead>

        <tr>

          <th>
            ID
          </th>

          <th>
            Username
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
  );
}

export default UserList;