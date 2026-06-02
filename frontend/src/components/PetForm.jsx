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

      <h2 className="section-title">

        {editingPetId
          ? "Edit Pet"
          : "Create Pet"}

      </h2>

      <form
        onSubmit={handleSubmit}
        className="pet-form"
      >

        <input
          type="text"
          name="name"
          placeholder="Pet Name"
          value={formData.name}
          onChange={handleChange}
        />

        <input
          type="text"
          name="species"
          placeholder="Species"
          value={formData.species}
          onChange={handleChange}
        />

        <input
          type="number"
          name="age"
          placeholder="Age"
          value={formData.age}
          onChange={handleChange}
        />

        <select
          name="owner_id"
          value={formData.owner_id}
          onChange={handleChange}
          disabled={editingPetId || saving}
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

        <div className="button-group">

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