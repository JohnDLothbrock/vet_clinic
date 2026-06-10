function AppointmentForm({

  formData,
  handleChange,
  handleSubmit,
  editingAppointmentId,
  resetForm,
  pets,
  saving

}) {

  return (

    <div className="card">

      <div className="form-header">

        <div>

          <h2 className="section-title">

            {editingAppointmentId
              ? "Edit Appointment"
              : "Create Appointment"}

          </h2>

          <p>
            {editingAppointmentId
              ? "Update the selected appointment date or reason."
              : "Schedule a new visit for a registered pet."}
          </p>

        </div>

      </div>

      <form
        onSubmit={handleSubmit}
        className="appointment-form form-grid"
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
              editingAppointmentId ||
              saving
            }
          >

            <option value="">
              Select Pet
            </option>

            {pets.map((pet) => (

              <option
                key={pet.id}
                value={pet.id}
              >
                {pet.name} ({pet.owner_name})
              </option>

            ))}

          </select>

        </div>

        <div className="form-field">

          <label>
            Appointment Date
          </label>

          <input
            type="datetime-local"
            name="appointment_date"
            value={formData.appointment_date}
            onChange={handleChange}
            disabled={saving}
          />

        </div>

        <div className="form-field form-field-full">

          <label>
            Reason
          </label>

          <input
            type="text"
            name="reason"
            placeholder="Example: Annual checkup"
            value={formData.reason}
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
              ? editingAppointmentId
                ? "Updating..."
                : "Creating..."
              : editingAppointmentId
                ? "Update Appointment"
                : "Create Appointment"}

          </button>

          {editingAppointmentId && (

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

export default AppointmentForm;