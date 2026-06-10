import AppointmentItem from "./AppointmentItem";

function AppointmentList({

  appointments,
  editAppointment,
  deleteAppointment,
  deletingId

}) {

  if (
    appointments.length === 0
  ) {

    return (

      <div className="empty-state">

        <div className="empty-state-icon appointment-empty-icon">
          📅
        </div>

        <h3>
          No appointments found
        </h3>

        <p>
          Create a new appointment to schedule a clinic visit.
        </p>

      </div>
    );
  }

  return (

    <div className="appointment-list">

      {appointments.map(
        (appointment) => (

          <AppointmentItem
            key={appointment.id}
            appointment={appointment}
            editAppointment={
              editAppointment
            }
            deleteAppointment={
              deleteAppointment
            }
            deletingId={
              deletingId
            }
          />

        )
      )}

    </div>
  );
}

export default AppointmentList;