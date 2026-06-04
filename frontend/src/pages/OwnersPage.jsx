import { useEffect, useState } from "react";

import toast from "react-hot-toast";

import OwnerForm from "../components/OwnerForm";
import OwnerList from "../components/OwnerList";

import {
  getOwners,
  searchOwners,
  createOwner,
  updateOwner,
  deleteOwner
} from "../services/ownerService";

import "../styles/app.css";

function OwnersPage() {

  const [owners, setOwners] =
    useState([]);

  const [searchTerm, setSearchTerm] =
    useState("");

  const [formData, setFormData] =
    useState({
      name: "",
      phone: ""
    });

  const [editingOwnerId,
    setEditingOwnerId] =
    useState(null);

  const [loading,
    setLoading] =
    useState(true);

  const [saving,
    setSaving] =
    useState(false);

  const [deletingId,
    setDeletingId] =
    useState(null);

  const [error,
    setError] =
    useState("");

  const fetchOwners =
    async () => {

      try {

        setLoading(true);

        const data =
          await getOwners();

        setOwners(data);

        setError("");

      } catch (error) {

        console.error(
          "Error fetching owners:",
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

    fetchOwners();

  }, []);

  const handleSearch =
    async () => {

      setError("");

      if (!searchTerm.trim()) {

        fetchOwners();

        return;
      }

      try {

        setLoading(true);

        const data =
          await searchOwners(
            searchTerm
          );

        setOwners(data);

      } catch (error) {

        console.error(
          "Error searching owners:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setLoading(false);
      }
    };

  const handleChange =
    (event) => {

      setError("");

      setFormData({
        ...formData,
        [event.target.name]:
          event.target.value
      });
    };

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      if (saving) {

        return;
      }

      if (!formData.name.trim()) {

        setError(
          "Owner name is required."
        );

        return;
      }

      if (!formData.phone.trim()) {

        setError(
          "Phone is required."
        );

        return;
      }

      try {

        setSaving(true);

        if (editingOwnerId) {

          await updateOwner(
            editingOwnerId,
            formData
          );

          toast.success(
            "Owner updated successfully."
          );

        } else {

          await createOwner(
            formData
          );

          toast.success(
            "Owner created successfully."
          );
        }

        setError("");

        resetForm();

        await fetchOwners();

      } catch (error) {

        console.error(
          "Error saving owner:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setSaving(false);
      }
    };

  const handleDeleteOwner =
    async (ownerId) => {

      const confirmed =
        window.confirm(
          "Are you sure you want to delete this owner?"
        );

      if (!confirmed) {

        return;
      }

      try {

        setDeletingId(
          ownerId
        );

        await deleteOwner(
          ownerId
        );

        toast.success(
          "Owner deleted successfully."
        );

        setError("");

        await fetchOwners();

      } catch (error) {

        console.error(
          "Error deleting owner:",
          error
        );

        setError(
          error.message
        );

      } finally {

        setDeletingId(
          null
        );
      }
    };

  const handleEditOwner =
    (owner) => {

      setEditingOwnerId(
        owner.id
      );

      setFormData({
        name: owner.name,
        phone: owner.phone
      });

      window.scrollTo({
        top: 0,
        behavior: "smooth"
      });
    };

  const resetForm =
    () => {

      setEditingOwnerId(
        null
      );

      setFormData({
        name: "",
        phone: ""
      });
    };

  return (

    <div className="container">

      <h1 className="title">
        Owners Management
      </h1>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      <div className="card">

        <OwnerForm
          formData={formData}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          editingOwnerId={editingOwnerId}
          resetForm={resetForm}
          saving={saving}
        />

      </div>

      <div className="card">

        <h2>
          Owner List
        </h2>

        <div
          style={{
            display: "flex",
            gap: "10px",
            marginBottom: "20px"
          }}
        >

          <input
            type="text"
            placeholder="Search owner by name..."
            value={searchTerm}
            onChange={(event) => {

              setError("");

              setSearchTerm(
                event.target.value
              );

            }}
          />

          <button
            onClick={handleSearch}
          >
            Search
          </button>

          <button
            onClick={() => {

              setSearchTerm("");

              fetchOwners();
            }}
          >
            Clear
          </button>

        </div>

        {loading ? (

          <p>
            Loading owners...
          </p>

        ) : (

          <OwnerList
            owners={owners}
            editOwner={handleEditOwner}
            deleteOwner={handleDeleteOwner}
            deletingId={deletingId}
          />

        )}

      </div>

    </div>
  );
}

export default OwnersPage;