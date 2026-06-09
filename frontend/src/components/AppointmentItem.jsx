import {
  canEditAppointment,
  canDeleteAppointment
} from "../services/permissionService";

function AppointmentItem({

  appointment,
  editAppointment,
  deleteAppointment,
  deletingId

}) {

  const showActions =
    canEditAppointment() ||
    canDeleteAppointment();

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

      {showActions && (

        <div>

          {canEditAppointment() && (

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

          )}

          {canDeleteAppointment() && (

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

          )}

        </div>

      )}

    </li>
  );
}

export default AppointmentItem;