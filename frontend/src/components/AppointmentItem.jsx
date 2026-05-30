function AppointmentItem({

  appointment,
  editAppointment,
  deleteAppointment

}) {

  return (

    <li className="list-item">

      <strong>
        Pet ID:
      </strong>
      {" "}
      {appointment.pet_id}

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
        >
          Edit
        </button>

        <button
          onClick={() =>
            deleteAppointment(
              appointment.id
            )
          }
        >
          Delete
        </button>

      </div>

    </li>
  );
}

export default AppointmentItem;