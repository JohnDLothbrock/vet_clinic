function PaginationControls({

  page,
  pageSize,
  total,
  totalPages,
  onPageChange,
  onPageSizeChange

}) {

  const startItem =
    total === 0
      ? 0
      : ((page - 1) * pageSize) + 1;

  const endItem =
    Math.min(
      page * pageSize,
      total
    );

  return (

    <div className="pagination-controls">

      <div className="pagination-summary">

        Showing{" "}

        <strong>
          {startItem}
        </strong>

        {" "}to{" "}

        <strong>
          {endItem}
        </strong>

        {" "}of{" "}

        <strong>
          {total}
        </strong>

        {" "}records

      </div>

      <div className="pagination-actions">

        <select
          value={pageSize}
          onChange={(event) =>
            onPageSizeChange(
              Number(event.target.value)
            )
          }
          className="pagination-page-size"
        >

          <option value={5}>
            5 per page
          </option>

          <option value={10}>
            10 per page
          </option>

          <option value={20}>
            20 per page
          </option>

          <option value={50}>
            50 per page
          </option>

        </select>

        <button
          type="button"
          className="secondary-button"
          disabled={page <= 1}
          onClick={() =>
            onPageChange(
              page - 1
            )
          }
        >
          Previous
        </button>

        <span className="pagination-current-page">

          Page {page} of {totalPages || 1}

        </span>

        <button
          type="button"
          className="secondary-button"
          disabled={
            totalPages === 0 ||
            page >= totalPages
          }
          onClick={() =>
            onPageChange(
              page + 1
            )
          }
        >
          Next
        </button>

      </div>

    </div>
  );
}

export default PaginationControls;
