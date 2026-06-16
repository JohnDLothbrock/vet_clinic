import {
  useEffect,
  useState
} from "react";

import PaginationControls from "../components/PaginationControls";

import {
  getPaginatedAuditLogs
} from "../services/auditLogService";

import "../styles/app.css";

function AuditLogsPage() {

  const [
    auditLogs,
    setAuditLogs
  ] = useState([]);

  const [
    actionFilter,
    setActionFilter
  ] = useState("");

  const [
    entityFilter,
    setEntityFilter
  ] = useState("");

  const [
    userIdFilter,
    setUserIdFilter
  ] = useState("");

  const [
    dateFrom,
    setDateFrom
  ] = useState("");

  const [
    dateTo,
    setDateTo
  ] = useState("");

  const [
    page,
    setPage
  ] = useState(1);

  const [
    pageSize,
    setPageSize
  ] = useState(10);

  const [
    total,
    setTotal
  ] = useState(0);

  const [
    totalPages,
    setTotalPages
  ] = useState(0);

  const [
    loading,
    setLoading
  ] = useState(true);

  const [
    error,
    setError
  ] = useState("");

  const buildDateFromFilter =
    (value) => {

      if (!value) {

        return "";
      }

      return `${value} 00:00:00`;
    };

  const buildDateToFilter =
    (value) => {

      if (!value) {

        return "";
      }

      return `${value} 23:59:59`;
    };

  const fetchAuditLogs =
    async (
      pageToLoad = page,
      filtersOverride = null
    ) => {

      try {

        setLoading(true);

        const filters =
          filtersOverride || {
            action: actionFilter,
            entity: entityFilter,
            user_id: userIdFilter,
            date_from: buildDateFromFilter(
              dateFrom
            ),
            date_to: buildDateToFilter(
              dateTo
            )
          };

        const data =
          await getPaginatedAuditLogs({
            page: pageToLoad,
            page_size: pageSize,
            action: filters.action,
            entity: filters.entity,
            user_id: filters.user_id,
            date_from: filters.date_from,
            date_to: filters.date_to
          });

        setAuditLogs(
          data.items
        );

        setTotal(
          data.total
        );

        setTotalPages(
          data.total_pages
        );

        setPage(
          data.page
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

    fetchAuditLogs(
      page
    );

  }, [
    page,
    pageSize
  ]);

  const handleSearch =
    async () => {

      setError("");

      const filters = {
        action: actionFilter,
        entity: entityFilter,
        user_id: userIdFilter,
        date_from: buildDateFromFilter(
          dateFrom
        ),
        date_to: buildDateToFilter(
          dateTo
        )
      };

      await fetchAuditLogs(
        1,
        filters
      );
    };

  const handleClearFilters =
    async () => {

      setError("");

      setActionFilter("");
      setEntityFilter("");
      setUserIdFilter("");
      setDateFrom("");
      setDateTo("");

      await fetchAuditLogs(
        1,
        {
          action: "",
          entity: "",
          user_id: "",
          date_from: "",
          date_to: ""
        }
      );
    };

  const handlePageChange =
    (newPage) => {

      setPage(
        newPage
      );
    };

  const handlePageSizeChange =
    (newPageSize) => {

      setPageSize(
        newPageSize
      );

      setPage(1);
    };

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
            {total}
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
              Filter create, update, and delete events across the system.
            </p>

          </div>

        </div>

        <div className="advanced-filter-grid">

          <select
            value={actionFilter}
            onChange={(event) => {

              setError("");

              setActionFilter(
                event.target.value
              );

            }}
          >

            <option value="">
              All actions
            </option>

            <option value="CREATE">
              CREATE
            </option>

            <option value="UPDATE">
              UPDATE
            </option>

            <option value="DELETE">
              DELETE
            </option>

          </select>

          <select
            value={entityFilter}
            onChange={(event) => {

              setError("");

              setEntityFilter(
                event.target.value
              );

            }}
          >

            <option value="">
              All entities
            </option>

            <option value="Pet">
              Pet
            </option>

            <option value="Owner">
              Owner
            </option>

            <option value="Appointment">
              Appointment
            </option>

            <option value="MedicalRecord">
              MedicalRecord
            </option>

            <option value="User">
              User
            </option>

          </select>

          <input
            type="number"
            placeholder="User ID"
            value={userIdFilter}
            onChange={(event) => {

              setError("");

              setUserIdFilter(
                event.target.value
              );

            }}
          />

          <input
            type="date"
            value={dateFrom}
            onChange={(event) => {

              setError("");

              setDateFrom(
                event.target.value
              );

            }}
          />

          <input
            type="date"
            value={dateTo}
            onChange={(event) => {

              setError("");

              setDateTo(
                event.target.value
              );

            }}
          />

          <button
            type="button"
            onClick={handleSearch}
          >
            Apply
          </button>

          <button
            type="button"
            onClick={handleClearFilters}
            className="secondary-button"
          >
            Clear
          </button>

        </div>

        {loading ? (

          <div className="loading-card">
            Loading audit logs...
          </div>

        ) : auditLogs.length === 0 ? (

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

          <>

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

            <PaginationControls
              page={page}
              pageSize={pageSize}
              total={total}
              totalPages={totalPages}
              onPageChange={handlePageChange}
              onPageSizeChange={handlePageSizeChange}
            />

          </>

        )}

      </div>

    </div>
  );
}

export default AuditLogsPage;