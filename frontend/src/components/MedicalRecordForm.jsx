function MedicalRecordForm({

  formData,
  handleChange,
  handleSubmit,
  editingMedicalRecordId,
  resetForm,
  pets,
  saving

}) {

  return (

    <div>

      <h2>
        {editingMedicalRecordId
          ? "Edit Medical Record"
          : "Create Medical Record"}
      </h2>

      <form
        onSubmit={handleSubmit}
        className="medical-record-form"
      >

        <select
          name="pet_id"
          value={formData.pet_id}
          onChange={handleChange}
          disabled={
            editingMedicalRecordId ||
            saving
          }
        >

          <option value="">
            Select Pet
          </option>

          {pets.map(
            (pet) => (

              <option
                key={pet.id}
                value={pet.id}
              >
                {pet.name} ({pet.owner_name})
              </option>

            )
          )}

        </select>

        <input
          type="datetime-local"
          name="visit_date"
          value={formData.visit_date}
          onChange={handleChange}
          disabled={saving}
        />

        <input
          type="number"
          step="0.01"
          name="weight"
          placeholder="Weight"
          value={formData.weight}
          onChange={handleChange}
          disabled={saving}
        />

        <input
          type="text"
          name="diagnosis"
          placeholder="Diagnosis"
          value={formData.diagnosis}
          onChange={handleChange}
          disabled={saving}
        />

        <textarea
          name="treatment"
          placeholder="Treatment"
          value={formData.treatment}
          onChange={handleChange}
          disabled={saving}
        />

        <textarea
          name="notes"
          placeholder="Notes"
          value={formData.notes}
          onChange={handleChange}
          disabled={saving}
        />

        <div className="button-group">

          <button
            type="submit"
            disabled={saving}
          >

            {saving
              ? "Saving..."
              : editingMedicalRecordId
                ? "Update Medical Record"
                : "Create Medical Record"}

          </button>

          {editingMedicalRecordId && (

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

export default MedicalRecordForm;