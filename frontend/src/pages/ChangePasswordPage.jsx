import {
  useState
} from "react";

import toast from "react-hot-toast";

import {
  changeMyPassword
} from "../services/userService";

import "../styles/app.css";

function ChangePasswordPage() {

  const [
    formData,
    setFormData
  ] = useState({
    current_password: "",
    new_password: "",
    confirm_password: ""
  });

  const [
    loading,
    setLoading
  ] = useState(false);

  const [
    error,
    setError
  ] = useState("");

  const [
    message,
    setMessage
  ] = useState("");

  const handleChange =
    (event) => {

      setError("");
      setMessage("");

      setFormData({
        ...formData,
        [event.target.name]:
          event.target.value
      });
    };

  const resetForm =
    () => {

      setFormData({
        current_password: "",
        new_password: "",
        confirm_password: ""
      });
    };

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      setError("");
      setMessage("");

      if (!formData.current_password.trim()) {

        setError(
          "Current password is required."
        );

        return;
      }

      if (!formData.new_password.trim()) {

        setError(
          "New password is required."
        );

        return;
      }

      if (
        formData.new_password.length < 8
      ) {

        setError(
          "New password must contain at least 8 characters."
        );

        return;
      }

      if (
        formData.new_password !==
        formData.confirm_password
      ) {

        setError(
          "New password and confirmation do not match."
        );

        return;
      }

      try {

        setLoading(true);

        const response =
          await changeMyPassword({
            current_password:
              formData.current_password,

            new_password:
              formData.new_password
          });

        setMessage(
          response.message
        );

        toast.success(
          "Password changed successfully."
        );

        resetForm();

      } catch (error) {

        console.error(
          "Error changing password:",
          error
        );

        setError(
          error.response?.data?.error ||
          "Unable to change password."
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="container">

      <h1 className="title">
        Change Password
      </h1>

      {error && (

        <p className="error-message">
          {error}
        </p>

      )}

      {message && (

        <p className="success-message">
          {message}
        </p>

      )}

      <div className="card change-password-card">

        <form
          onSubmit={handleSubmit}
          className="change-password-form"
        >

          <input
            type="password"
            name="current_password"
            placeholder="Current password"
            value={formData.current_password}
            onChange={handleChange}
            disabled={loading}
          />

          <input
            type="password"
            name="new_password"
            placeholder="New password"
            value={formData.new_password}
            onChange={handleChange}
            disabled={loading}
          />

          <input
            type="password"
            name="confirm_password"
            placeholder="Confirm new password"
            value={formData.confirm_password}
            onChange={handleChange}
            disabled={loading}
          />

          <button
            type="submit"
            disabled={loading}
          >

            {loading
              ? "Changing..."
              : "Change Password"}

          </button>

        </form>

      </div>

    </div>
  );
}

export default ChangePasswordPage;