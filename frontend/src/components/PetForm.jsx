function PetForm({

  formData,
  handleChange,
  handleSubmit,
  editingPetId,
  resetForm,
  owners,
  saving

}) {

  return (

    <div>

      <div className="form-header">

        <div>

          <h2 className="section-title">

            {editingPetId
              ? "Edit Pet"
              : "Create Pet"}

          </h2>

          <p>
            {editingPetId
              ? "Update the selected pet record."
              : "Register a new pet and assign it to an owner."}
          </p>

        </div>

      </div>

      <form
        onSubmit={handleSubmit}
        className="pet-form form-grid"
      >

        <div className="form-field">

          <label>
            Pet Name
          </label>

          <input
            type="text"
            name="name"
            placeholder="Example: Luna"
            value={formData.name}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Species
          </label>

          <input
            type="text"
            name="species"
            placeholder="Example: Dog, Cat, Rabbit"
            value={formData.species}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Age
          </label>

          <input
            type="number"
            name="age"
            placeholder="Example: 4"
            value={formData.age}
            onChange={handleChange}
            disabled={saving}
            min="0"
          />

        </div>

        <div className="form-field">

          <label>
            Owner
          </label>

          <select
            name="owner_id"
            value={formData.owner_id}
            onChange={handleChange}
            disabled={
              editingPetId ||
              saving
            }
          >

            <option value="">
              Select Owner
            </option>

            {owners.map((owner) => (

              <option
                key={owner.id}
                value={owner.id}
              >
                {owner.name}
              </option>

            ))}

          </select>

        </div>

        <div className="form-actions">

          <button
            type="submit"
            disabled={saving}
          >

            {saving
              ? "Saving..."
              : editingPetId
                ? "Update Pet"
                : "Create Pet"}

          </button>

          {editingPetId && (

            <button
              type="button"
              onClick={resetForm}
              className="secondary-button"
              disabled={saving}
            >
              Cancel
            </button>

          )}

        </div>

      </form>

    </div>
  );
}

export default PetForm;