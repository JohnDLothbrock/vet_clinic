function AppointmentForm({

  formData,
  handleChange,
  handleSubmit,
  editingAppointmentId,
  resetForm,
  pets

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
          disabled={editingAppointmentId}
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
        />

        <input
          type="text"
          name="reason"
          placeholder="Reason"
          value={formData.reason}
          onChange={handleChange}
        />

        <button type="submit">

          {editingAppointmentId
            ? "Update Appointment"
            : "Create Appointment"}

        </button>

        {editingAppointmentId && (

          <button
            type="button"
            onClick={resetForm}
          >
            Cancel
          </button>

        )}

      </form>

    </div>
  );
}

export default AppointmentForm;