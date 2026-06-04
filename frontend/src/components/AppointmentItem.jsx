function AppointmentItem({

  appointment,
  editAppointment,
  deleteAppointment,
  deletingId

}) {

  return (

    <li className="list-item">

      <strong>
        Pet:
      </strong>
      {" "}
      {appointment.pet_name}

      <br />

      <strong>
        Date:
      </strong>
      {" "}
      {appointment.appointment_date}

      <br />

      <strong>
        Reason:
      </strong>
      {" "}
      {appointment.reason}

      <div>

        <button
          onClick={() =>
            editAppointment(
              appointment
            )
          }
          disabled={
            deletingId ===
            appointment.id
          }
        >
          Edit
        </button>

        <button
          onClick={() =>
            deleteAppointment(
              appointment.id
            )
          }
          disabled={
            deletingId ===
            appointment.id
          }
        >
          {deletingId ===
          appointment.id
            ? "Deleting..."
            : "Delete"}
        </button>

      </div>

    </li>
  );
}

export default AppointmentItem;