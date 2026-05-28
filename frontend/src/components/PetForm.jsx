function PetForm({

  formData,
  handleChange,
  handleSubmit,
  editingPetId,
  resetForm

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

        <input
          type="number"
          name="owner_id"
          placeholder="Owner ID"
          value={formData.owner_id}
          onChange={handleChange}
          disabled={editingPetId}
        />

        <div className="button-group">

          <button type="submit">

            {editingPetId
              ? "Update Pet"
              : "Create Pet"}

          </button>

          {editingPetId && (

            <button
              type="button"
              onClick={resetForm}
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

export default PetForm;