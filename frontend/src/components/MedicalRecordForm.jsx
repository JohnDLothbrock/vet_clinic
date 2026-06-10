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

      <div className="form-header">

        <div>

          <h2 className="section-title">
            {editingMedicalRecordId
              ? "Edit Medical Record"
              : "Create Medical Record"}
          </h2>

          <p>
            {editingMedicalRecordId
              ? "Update clinical details for the selected visit."
              : "Add diagnosis, treatment, and visit notes for a pet."}
          </p>

        </div>

      </div>

      <form
        onSubmit={handleSubmit}
        className="medical-record-form form-grid"
      >

        <div className="form-field">

          <label>
            Pet
          </label>

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

        </div>

        <div className="form-field">

          <label>
            Visit Date
          </label>

          <input
            type="datetime-local"
            name="visit_date"
            value={formData.visit_date}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field">

          <label>
            Weight
          </label>

          <input
            type="number"
            step="0.01"
            name="weight"
            placeholder="Example: 12.5"
            value={formData.weight}
            onChange={handleChange}
            disabled={saving}
            min="0"
          />

        </div>

        <div className="form-field">

          <label>
            Diagnosis
          </label>

          <input
            type="text"
            name="diagnosis"
            placeholder="Example: Ear infection"
            value={formData.diagnosis}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field form-field-full">

          <label>
            Treatment
          </label>

          <textarea
            name="treatment"
            placeholder="Describe treatment, medication, or recommended care..."
            value={formData.treatment}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field form-field-full">

          <label>
            Notes
          </label>

          <textarea
            name="notes"
            placeholder="Optional additional clinical notes..."
            value={formData.notes}
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