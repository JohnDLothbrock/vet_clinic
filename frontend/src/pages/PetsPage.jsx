import { useEffect, useState } from "react";

import PetForm from "../components/PetForm";
import PetList from "../components/PetList";

import {

  getPets,
  createPet,
  updatePet,
  deletePet

} from "../services/petService";

import "../App.css";


function PetsPage() {

  const [pets, setPets] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    species: "",
    age: "",
    owner_id: ""
  });

  const [editingPetId, setEditingPetId] = useState(null);

  const [loading, setLoading] = useState(true);

  const [error, setError] = useState("");

  // LOAD PETS
  const fetchPets = async () => {

    try {

      setLoading(true);

      const data = await getPets();

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

  useEffect(() => {

    fetchPets();

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

    const payload = {
      name: formData.name,
      species: formData.species,
      age: Number(formData.age),
      owner_id: Number(formData.owner_id)
    };

    try {

      // UPDATE
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

        // CREATE
        await createPet(payload);
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

    const confirmed = window.confirm(
      "Are you sure you want to delete this pet?"
    );

    if (!confirmed) {

      return;
    }

    try {

      await deletePet(petId);

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

    setEditingPetId(pet.id);

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

    setEditingPetId(null);

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
        />

      </div>

      <div className="card">

        <h2>Pet List</h2>

        {loading ? (

          <p>Loading pets...</p>

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