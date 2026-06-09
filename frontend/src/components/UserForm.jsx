function UserForm({

  formData,
  handleChange,
  handleSubmit,
  saving

}) {

  return (

    <div>

      <h2>
        Create User
      </h2>

      <form
        onSubmit={handleSubmit}
        className="user-form"
      >

        <input
          type="text"
          name="username"
          placeholder="Username"
          value={formData.username}
          onChange={handleChange}
          disabled={saving}
        />

        <input
          type="email"
          name="email"
          placeholder="Email"
          value={formData.email}
          onChange={handleChange}
          disabled={saving}
        />

        <input
          type="password"
          name="password"
          placeholder="Temporary password"
          value={formData.password}
          onChange={handleChange}
          disabled={saving}
        />

        <select
          name="role_id"
          value={formData.role_id}
          onChange={handleChange}
          disabled={saving}
        >

          <option value="">
            Select Role
          </option>

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

        <button
          type="submit"
          disabled={saving}
        >

          {saving
            ? "Creating..."
            : "Create User"}

        </button>

      </form>

    </div>
  );
}

export default UserForm;