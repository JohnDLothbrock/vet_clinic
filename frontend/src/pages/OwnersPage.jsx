import { useEffect, useState } from "react";

import OwnerForm from "../components/OwnerForm";
import OwnerList from "../components/OwnerList";

import {

  getOwners,
  createOwner,
  updateOwner,
  deleteOwner

} from "../services/ownerService";

import "../styles/app.css";


function OwnersPage() {

  const [owners, setOwners] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    phone: ""
  });

  const [editingOwnerId, setEditingOwnerId] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  // LOAD OWNERS
  const fetchOwners = async () => {

    try {

      setLoading(true);

      const data = await getOwners();

      setOwners(data);

      setError("");

    } catch (error) {

      console.error(
        "Error fetching owners:",
        error
      );

      setError(
        "Failed to load owners."
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchOwners();

  }, []);

  // HANDLE INPUTS
  const handleChange = (event) => {

    setFormData({
      ...formData,
      [event.target.name]: event.target.value
    });
  };

  // CREATE / UPDATE
  const handleSubmit = async (event) => {

    event.preventDefault();

    try {

      if (editingOwnerId) {

        await updateOwner(
          editingOwnerId,
          formData
        );

      } else {

        await createOwner(formData);
      }

      resetForm();

      fetchOwners();

    } catch (error) {

      console.error(
        "Error saving owner:",
        error
      );

      setError(
        "Failed to save owner."
      );
    }
  };

  // DELETE
  const handleDeleteOwner = async (
    ownerId
  ) => {

    const confirmed = window.confirm(
      "Are you sure you want to delete this owner?"
    );

    if (!confirmed) {

      return;
    }

    try {

      await deleteOwner(ownerId);

      fetchOwners();

    } catch (error) {

      console.error(
        "Error deleting owner:",
        error
      );

      setError(
        "Failed to delete owner."
      );
    }
  };

  // EDIT
  const handleEditOwner = (owner) => {

    setEditingOwnerId(owner.id);

    setFormData({
      name: owner.name,
      phone: owner.phone
    });

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  };

  // RESET
  const resetForm = () => {

    setEditingOwnerId(null);

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
        />

      </div>

      <div className="card">

        <h2>Owner List</h2>

        {loading ? (

          <p>Loading owners...</p>

        ) : (

          <OwnerList
            owners={owners}
            editOwner={handleEditOwner}
            deleteOwner={handleDeleteOwner}
          />

        )}

      </div>

    </div>
  );
}

export default OwnersPage;