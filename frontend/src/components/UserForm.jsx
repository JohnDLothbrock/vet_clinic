function UserForm({

  formData,
  handleChange,
  handleSubmit,
  saving

}) {

  return (

    <div>

      <div className="form-header">

        <div>

          <h2 className="section-title">
            Create User
          </h2>

          <p>
            Add a new staff account and assign the correct system role.
          </p>

        </div>

      </div>

      <form
        onSubmit={handleSubmit}
        className="user-form form-grid"
      >

        <div className="form-field">

          <label>
            Username
          </label>

          <input
            type="text"
            name="username"
            placeholder="Example: vet1"
            value={formData.username}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Email
          </label>

          <input
            type="email"
            name="email"
            placeholder="Example: vet1@clinic.com"
            value={formData.email}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Temporary Password
          </label>

          <input
            type="password"
            name="password"
            placeholder="Minimum 8 characters"
            value={formData.password}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Role
          </label>

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

        </div>

        <div className="form-actions">

          <button
            type="submit"
            disabled={saving}
          >

            {saving
              ? "Creating..."
              : "Create User"}

          </button>

        </div>

      </form>

    </div>
  );
}

export default UserForm;