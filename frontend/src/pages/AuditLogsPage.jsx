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

  if (loading) {

    return (

      <div className="container">

        <p>
          Loading audit logs...
        </p>

      </div>
    );
  }

  return (

    <div className="container">

      <h1 className="title">
        Audit Logs
      </h1>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      <div className="card">

        {auditLogs.length === 0 ? (

          <p>
            No audit logs found.
          </p>

        ) : (

          <table className="audit-table">

            <thead>

              <tr>

                <th>
                  ID
                </th>

                <th>
                  User ID
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
                      {log.id}
                    </td>

                    <td>
                      {log.user_id}
                    </td>

                    <td>
                      <span className="audit-action">
                        {log.action}
                      </span>
                    </td>

                    <td>
                      {log.entity}
                    </td>

                    <td>
                      {log.entity_id}
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

        )}

      </div>

    </div>
  );
}

export default AuditLogsPage;