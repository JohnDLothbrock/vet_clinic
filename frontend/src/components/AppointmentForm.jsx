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

      <h2>

        {editingAppointmentId
          ? "Edit Appointment"
          : "Create Appointment"}

      </h2>

      <form onSubmit={handleSubmit}>

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

        <input
          type="datetime-local"
          name="appointment_date"
          value={formData.appointment_date}
          onChange={handleChange}
          disabled={saving}
        />

        <input
          type="text"
          name="reason"
          placeholder="Reason"
          value={formData.reason}
          onChange={handleChange}
          disabled={saving}
        />

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
          >
            Cancel
          </button>

        )}

      </form>

    </div>
  );
}

export default AppointmentForm;