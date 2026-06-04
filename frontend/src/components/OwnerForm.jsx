function OwnerForm({

  formData,
  handleChange,
  handleSubmit,
  editingOwnerId,
  resetForm,
  saving

}) {

  return (

    <div>

      <h2>

        {editingOwnerId
          ? "Edit Owner"
          : "Create Owner"}

      </h2>

      <form onSubmit={handleSubmit}>

        <div>

          <input
            type="text"
            name="name"
            placeholder="Owner Name"
            value={formData.name}
            onChange={handleChange}
          />

        </div>

        <br />

        <div>

          <input
            type="text"
            name="phone"
            placeholder="Phone"
            value={formData.phone}
            onChange={handleChange}
          />

        </div>

        <br />

        <button
          type="submit"
          disabled={saving}
        >

          {saving
            ? "Saving..."
            : editingOwnerId
              ? "Update Owner"
              : "Create Owner"}

        </button>

        {editingOwnerId && (

          <button
            type="button"
            onClick={resetForm}
            disabled={saving}
            style={{
              marginLeft: "10px"
            }}
          >
            Cancel
          </button>

        )}

      </form>

    </div>
  );
}

export default OwnerForm;