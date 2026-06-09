import {
  useState
} from "react";

import {
  useNavigate
} from "react-router-dom";

import toast from "react-hot-toast";

import {
  login
} from "../services/authService";

import "../styles/app.css";

function LoginPage() {

  const navigate =
    useNavigate();

  const [
    formData,
    setFormData
  ] = useState({
    username: "",
    password: ""
  });

  const [
    loading,
    setLoading
  ] = useState(false);

  const [
    error,
    setError
  ] = useState("");

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

      if (!formData.username.trim()) {

        setError(
          "Username is required."
        );

        return;
      }

      if (!formData.password.trim()) {

        setError(
          "Password is required."
        );

        return;
      }

      try {

        setLoading(true);

        await login(
          formData.username,
          formData.password
        );

        toast.success(
          "Login successful."
        );

        navigate(
          "/",
          {
            replace: true
          }
        );

      } catch (error) {

        console.error(
          "Login error:",
          error
        );

        setError(
          "Invalid username or password."
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="login-page">

      <div className="login-card">

        <h1>
          Veterinary Clinic
        </h1>

        <p className="login-subtitle">
          Sign in to continue
        </p>

        {error && (

          <p className="error-message">
            {error}
          </p>

        )}

        <form onSubmit={handleSubmit}>

          <input
            type="text"
            name="username"
            placeholder="Username"
            value={formData.username}
            onChange={handleChange}
            disabled={loading}
          />

          <input
            type="password"
            name="password"
            placeholder="Password"
            value={formData.password}
            onChange={handleChange}
            disabled={loading}
          />

          <button
            type="submit"
            disabled={loading}
            className="full-width-button"
          >

            {loading
              ? "Signing in..."
              : "Login"}

          </button>

        </form>

        <p className="login-help-text">
          Forgot password will be added in Phase 2.
        </p>

      </div>

    </div>
  );
}

export default LoginPage;