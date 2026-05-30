import AppointmentItem from "./AppointmentItem";


function AppointmentList({

  appointments,
  editAppointment,
  deleteAppointment

}) {

  if (
    appointments.length === 0
  ) {

    return (
      <p>
        No appointments found.
      </p>
    );
  }

  return (

    <ul>

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
          />

        )
      )}

    </ul>
  );
}

export default AppointmentList;
