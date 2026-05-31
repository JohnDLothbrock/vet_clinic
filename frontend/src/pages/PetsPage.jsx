import { useEffect, useState } from "react";

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

  const [error, setError] =
    useState("");

  // LOAD PETS
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
        "Failed to load pets."
      );

    } finally {

      setLoading(false);
    }
  };

  // LOAD OWNERS
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
    }
  };

  // SEARCH PETS
  const handleSearch = async () => {

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
        "Failed to search pets."
      );

    } finally {

      setLoading(false);
    }
  };

  useEffect(() => {

    fetchPets();
    fetchOwners();

  }, []);

  // HANDLE INPUTS
  const handleChange = (event) => {

    setFormData({
      ...formData,
      [event.target.name]:
        event.target.value
    });
  };

  // CREATE / UPDATE
  const handleSubmit = async (event) => {

    event.preventDefault();

    const payload = {
      name: formData.name,
      species: formData.species,
      age: Number(formData.age),
      owner_id: Number(formData.owner_id)
    };

    try {

      if (editingPetId) {

        await updatePet(
          editingPetId,
          {
            name: payload.name,
            species: payload.species,
            age: payload.age
          }
        );

      } else {

        await createPet(
          payload
        );
      }

      resetForm();

      fetchPets();

    } catch (error) {

      console.error(
        "Error saving pet:",
        error
      );

      setError(
        "Failed to save pet."
      );
    }
  };

  // DELETE
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

      await deletePet(
        petId
      );

      fetchPets();

    } catch (error) {

      console.error(
        "Error deleting pet:",
        error
      );

      setError(
        "Failed to delete pet."
      );
    }
  };

  // EDIT
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

  // RESET
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
            onChange={(event) =>
              setSearchTerm(
                event.target.value
              )
            }
          />

          <button
            onClick={handleSearch}
          >
            Search
          </button>

          <button
            onClick={() => {

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
          />

        )}

      </div>

    </div>
  );
}

export default PetsPage;