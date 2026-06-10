import {
  useEffect,
  useState
} from "react";

import {
  getAuditLogs
} from "../services/auditLogService";

import "../styles/app.css";

function AuditLogsPage() {

  const [
    auditLogs,
    setAuditLogs
  ] = useState([]);

  const [
    loading,
    setLoading
  ] = useState(true);

  const [
    error,
    setError
  ] = useState("");

  const fetchAuditLogs =
    async () => {

      try {

        setLoading(true);

        const data =
          await getAuditLogs();

        setAuditLogs(
          data
        );

        setError("");

      } catch (error) {

        console.error(
          "Error fetching audit logs:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  useEffect(() => {

    fetchAuditLogs();

  }, []);

  const formatDate =
    (dateValue) => {

      if (!dateValue) {

        return "N/A";
      }

      return new Date(
        dateValue
      ).toLocaleString();
    };

  const getActionClass =
    (action) => {

      if (action === "CREATE") {

        return "audit-action-create";
      }

      if (action === "UPDATE") {

        return "audit-action-update";
      }

      if (action === "DELETE") {

        return "audit-action-delete";
      }

      return "audit-action-default";
    };

  const getActionIcon =
    (action) => {

      if (action === "CREATE") {

        return "＋";
      }

      if (action === "UPDATE") {

        return "✎";
      }

      if (action === "DELETE") {

        return "−";
      }

      return "•";
    };

  if (loading) {

    return (

      <div className="container">

        <div className="page-header">

          <div>

            <h1 className="title">
              Audit Logs
            </h1>

            <p className="page-subtitle">
              Review system activity and administrative changes.
            </p>

          </div>

        </div>

        <div className="card">

          <div className="loading-card">
            Loading audit logs...
          </div>

        </div>

      </div>
    );
  }

  return (

    <div className="container">

      <div className="page-header">

        <div>

          <h1 className="title">
            Audit Logs
          </h1>

          <p className="page-subtitle">
            Review system activity, entity changes, and user actions.
          </p>

        </div>

        <div className="page-summary-card">

          <span className="page-summary-number">
            {auditLogs.length}
          </span>

          <span className="page-summary-label">
            log entries
          </span>

        </div>

      </div>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      <div className="card">

        <div className="list-header">

          <div>

            <h2>
              Activity History
            </h2>

            <p>
              Track create, update, and delete events across the system.
            </p>

          </div>

        </div>

        {auditLogs.length === 0 ? (

          <div className="empty-state">

            <div className="empty-state-icon audit-empty-icon">
              🧾
            </div>

            <h3>
              No audit logs found
            </h3>

            <p>
              Activity will appear here after users create, update, or delete records.
            </p>

          </div>

        ) : (

          <div className="table-wrapper">

            <table className="audit-table polished-audit-table">

              <thead>

                <tr>

                  <th>
                    ID
                  </th>

                  <th>
                    User
                  </th>

                  <th>
                    Action
                  </th>

                  <th>
                    Entity
                  </th>

                  <th>
                    Entity ID
                  </th>

                  <th>
                    Created At
                  </th>

                </tr>

              </thead>

              <tbody>

                {auditLogs.map(
                  (log) => (

                    <tr key={log.id}>

                      <td>
                        <span className="user-id-pill">
                          #{log.id}
                        </span>
                      </td>

                      <td>
                        <span className="audit-user-pill">
                          User {log.user_id}
                        </span>
                      </td>

                      <td>
                        <span
                          className={`audit-action ${getActionClass(log.action)}`}
                        >
                          <span className="audit-action-icon">
                            {getActionIcon(log.action)}
                          </span>

                          {log.action}
                        </span>
                      </td>

                      <td>
                        <span className="audit-entity">
                          {log.entity}
                        </span>
                      </td>

                      <td>
                        <span className="audit-entity-id">
                          {log.entity_id}
                        </span>
                      </td>

                      <td>
                        {formatDate(
                          log.created_at
                        )}
                      </td>

                    </tr>

                  )
                )}

              </tbody>

            </table>

          </div>

        )}

      </div>

    </div>
  );
}

export default AuditLogsPage;