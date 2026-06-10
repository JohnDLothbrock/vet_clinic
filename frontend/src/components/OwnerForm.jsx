function OwnerForm({

  formData,
  handleChange,
  handleSubmit,
  editingOwnerId,
  resetForm,
  saving

}) {

  return (

    <div>

      <div className="form-header">

        <div>

          <h2 className="section-title">

            {editingOwnerId
              ? "Edit Owner"
              : "Create Owner"}

          </h2>

          <p>
            {editingOwnerId
              ? "Update the selected client record."
              : "Register a new owner before assigning pets."}
          </p>

        </div>

      </div>

      <form
        onSubmit={handleSubmit}
        className="owner-form form-grid"
      >

        <div className="form-field">

          <label>
            Owner Name
          </label>

          <input
            type="text"
            name="name"
            placeholder="Example: Maria Rodriguez"
            value={formData.name}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Phone
          </label>

          <input
            type="text"
            name="phone"
            placeholder="Example: +506 8888 8888"
            value={formData.phone}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-actions">

          <button
            type="submit"
            disabled={saving}
          >

            {saving
              ? "Saving..."
              : editingOwnerId
                ? "Update Owner"
                : "Create Owner"}

          </button>

          {editingOwnerId && (

            <button
              type="button"
              onClick={resetForm}
              disabled={saving}
              className="secondary-button"
            >
              Cancel
            </button>

          )}

        </div>

      </form>

    </div>
  );
}

export default OwnerForm;