function AppointmentForm({

  formData,
  handleChange,
  handleSubmit,
  editingAppointmentId,
  resetForm

}) {

  return (

    <div className="card">

      <h2>
        {editingAppointmentId
          ? "Edit Appointment"
          : "Create Appointment"}
      </h2>

      <form onSubmit={handleSubmit}>

        <input
          type="number"
          name="pet_id"
          placeholder="Pet ID"
          value={formData.pet_id}
          onChange={handleChange}
          disabled={editingAppointmentId}
        />

        <input
          type="text"
          name="appointment_date"
          placeholder="Appointment Date"
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