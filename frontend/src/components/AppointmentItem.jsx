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

    <div className="appointment-card">

      <div className="record-main">

        <div className="record-avatar appointment-avatar">
          📅
        </div>

        <div>

          <h3>
            {appointment.pet_name}
          </h3>

          <div className="record-details">

            <span>
              <strong>
                Date:
              </strong>
              {" "}
              {appointment.appointment_date}
            </span>

            <span>
              <strong>
                Reason:
              </strong>
              {" "}
              {appointment.reason}
            </span>

          </div>

        </div>

      </div>

      {showActions && (

        <div className="button-group record-actions">

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
              className="small-button"
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
              className="delete-button small-button"
            >
              {deletingId ===
              appointment.id
                ? "Deleting..."
                : "Delete"}
            </button>

          )}

        </div>

      )}

    </div>
  );
}

export default AppointmentItem;