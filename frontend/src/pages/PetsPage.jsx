import { useEffect, useState } from "react";
import toast from "react-hot-toast";

import PetForm from "../components/PetForm";
import PetList from "../components/PetList";

import {
  getPetsWithOwner,
  createPet,
  updatePet,
  deletePet,
  searchPets
} from "../services/petService";

import {
  getOwners
} from "../services/ownerService";

import "../styles/app.css";

function PetsPage() {

  const [pets, setPets] = useState([]);

  const [owners, setOwners] =
    useState([]);

  const [searchTerm, setSearchTerm] =
    useState("");

  const [formData, setFormData] = useState({
    name: "",
    species: "",
    age: "",
    owner_id: ""
  });

  const [editingPetId, setEditingPetId] =
    useState(null);

  const [loading, setLoading] =
    useState(true);

  const [saving, setSaving] =
    useState(false);

  const [deletingId, setDeletingId] =
    useState(null);

  const [error, setError] =
    useState("");

  const fetchPets = async () => {

    try {

      setLoading(true);

      const data =
        await getPetsWithOwner();

      setPets(data);

      setError("");

    } catch (error) {

      console.error(
        "Error fetching pets:",
        error
      );

      setError(
        error.message
      );

    } finally {

      setLoading(false);
    }
  };

  const fetchOwners = async () => {

    try {

      const data =
        await getOwners();

      setOwners(data);

    } catch (error) {

      console.error(
        "Error fetching owners:",
        error
      );

      setError(
        error.message
      );
    }
  };

  const handleSearch = async () => {

    setError("");

    if (!searchTerm.trim()) {

      fetchPets();

      return;
    }

    try {

      setLoading(true);

      const data =
        await searchPets(
          searchTerm
        );

      setPets(data);

    } catch (error) {

      console.error(
        "Error searching pets:",
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

    const loadData = async () => {

      await Promise.all([
        fetchPets(),
        fetchOwners()
      ]);

    };

    loadData();

  }, []);

  const handleChange = (event) => {

    setError("");

    setFormData({
      ...formData,
      [event.target.name]:
        event.target.value
    });
  };

  const handleSubmit = async (event) => {

    event.preventDefault();

    if (saving) {

      return;
    }

    if (!formData.name.trim()) {

      setError(
        "Pet name is required."
      );

      return;
    }

    if (!formData.species.trim()) {

      setError(
        "Species is required."
      );

      return;
    }

    if (!formData.age) {

      setError(
        "Age is required."
      );

      return;
    }

    if (!formData.owner_id) {

      setError(
        "Owner is required."
      );

      return;
    }

    const payload = {
      name: formData.name,
      species: formData.species,
      age: Number(formData.age),
      owner_id: Number(formData.owner_id)
    };

    try {

      setSaving(true);

      const isEditing =
        editingPetId !== null;

      if (isEditing) {

        await updatePet(
          editingPetId,
          {
            name: payload.name,
            species: payload.species,
            age: payload.age
          }
        );

        toast.success(
          "Pet updated successfully!"
        );

      } else {

        await createPet(
          payload
        );

        toast.success(
          "Pet created successfully!"
        );
      }

      setError("");

      resetForm();

      await fetchPets();

    } catch (error) {

      console.error(
        "Error saving pet:",
        error
      );

      setError(
        error.message
      );

    } finally {

      setSaving(false);
    }
  };

  const handleDeletePet = async (
    petId
  ) => {

    const confirmed =
      window.confirm(
        "Are you sure you want to delete this pet?"
      );

    if (!confirmed) {

      return;
    }

    try {

      setDeletingId(
        petId
      );

      await deletePet(
        petId
      );

      toast.success(
        "Pet deleted successfully!"
      );

      setError("");

      await fetchPets();

    } catch (error) {

      console.error(
        "Error deleting pet:",
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

  const handleEditPet = (pet) => {

    setEditingPetId(
      pet.id
    );

    setFormData({
      name: pet.name,
      species: pet.species,
      age: pet.age,
      owner_id: pet.owner_id
    });

    window.scrollTo({
      top: 0,
      behavior: "smooth"
    });
  };

  const resetForm = () => {

    setEditingPetId(
      null
    );

    setFormData({
      name: "",
      species: "",
      age: "",
      owner_id: ""
    });
  };

  return (

    <div className="container">

      <h1 className="title">
        Veterinary Clinic App
      </h1>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      <div className="card">

        <PetForm
          formData={formData}
          handleChange={handleChange}
          handleSubmit={handleSubmit}
          editingPetId={editingPetId}
          resetForm={resetForm}
          owners={owners}
          saving={saving}
        />

      </div>

      <div className="card">

        <h2>Pet List</h2>

        <div
          style={{
            display: "flex",
            gap: "10px",
            marginBottom: "20px"
          }}
        >

          <input
            type="text"
            placeholder="Search pet by name..."
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

              setError("");

              setSearchTerm("");

              fetchPets();
            }}
          >
            Clear
          </button>

        </div>

        {loading ? (

          <p>
            Loading pets...
          </p>

        ) : (

          <PetList
            pets={pets}
            editPet={handleEditPet}
            deletePet={handleDeletePet}
            deletingId={deletingId}
          />

        )}

      </div>

    </div>
  );
}

export default PetsPage;