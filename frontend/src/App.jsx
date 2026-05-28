import { useEffect, useState } from "react";

function App() {

  const API_URL = "http://127.0.0.1:8000/api/v1/pets";

  const [pets, setPets] = useState([]);

  const [formData, setFormData] = useState({
    name: "",
    species: "",
    age: "",
    owner_id: ""
  });

  const [editingPetId, setEditingPetId] = useState(null);

  // LOAD PETS
  const fetchPets = async () => {

    try {

      const response = await fetch(API_URL);

      const data = await response.json();

      setPets(data);

    } catch (error) {

      console.error(
        "Error fetching pets:",
        error
      );
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

  // CREATE OR UPDATE
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

        await fetch(
          `${API_URL}/${editingPetId}`,
          {
            method: "PUT",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify({
              name: payload.name,
              species: payload.species,
              age: payload.age
            })
          }
        );

      } else {

        // CREATE
        await fetch(
          API_URL,
          {
            method: "POST",
            headers: {
              "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
          }
        );
      }

      resetForm();

      fetchPets();

    } catch (error) {

      console.error(
        "Error saving pet:",
        error
      );
    }
  };

  // DELETE
  const deletePet = async (petId) => {

    try {

      await fetch(
        `${API_URL}/${petId}`,
        {
          method: "DELETE"
        }
      );

      fetchPets();

    } catch (error) {

      console.error(
        "Error deleting pet:",
        error
      );
    }
  };

  // EDIT
  const editPet = (pet) => {

    setEditingPetId(pet.id);

    setFormData({
      name: pet.name,
      species: pet.species,
      age: pet.age,
      owner_id: pet.owner_id
    });
  };

  // RESET FORM
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

    <div style={{ padding: "20px" }}>

      <h1>Veterinary Clinic App</h1>

      <h2>
        {editingPetId
          ? "Edit Pet"
          : "Create Pet"}
      </h2>

      <form onSubmit={handleSubmit}>

        <div>
          <input
            type="text"
            name="name"
            placeholder="Pet Name"
            value={formData.name}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <input
            type="text"
            name="species"
            placeholder="Species"
            value={formData.species}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <input
            type="number"
            name="age"
            placeholder="Age"
            value={formData.age}
            onChange={handleChange}
          />
        </div>

        <br />

        <div>
          <input
            type="number"
            name="owner_id"
            placeholder="Owner ID"
            value={formData.owner_id}
            onChange={handleChange}
            disabled={editingPetId}
          />
        </div>

        <br />

        <button type="submit">

          {editingPetId
            ? "Update Pet"
            : "Create Pet"}

        </button>

        {editingPetId && (

          <button
            type="button"
            onClick={resetForm}
            style={{ marginLeft: "10px" }}
          >
            Cancel
          </button>

        )}

      </form>

      <hr />

      <h2>Pet List</h2>

      {pets.length === 0 ? (

        <p>No pets found.</p>

      ) : (

        <ul>

          {pets.map((pet) => (

            <li
              key={pet.id}
              style={{
                marginBottom: "15px"
              }}
            >

              <strong>{pet.name}</strong>
              {" - "}
              {pet.species}
              {" - Age: "}
              {pet.age}

              <div style={{ marginTop: "5px" }}>

                <button
                  onClick={() => editPet(pet)}
                >
                  Edit
                </button>

                <button
                  onClick={() => deletePet(pet.id)}
                  style={{
                    marginLeft: "10px"
                  }}
                >
                  Delete
                </button>

              </div>

            </li>

          ))}

        </ul>

      )}

    </div>
  );
}

export default App;