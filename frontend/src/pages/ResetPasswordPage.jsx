import {
  useState
} from "react";

import {
  Link,
  useNavigate,
  useSearchParams
} from "react-router-dom";

import toast from "react-hot-toast";

import {
  resetPassword
} from "../services/authService";

import "../styles/app.css";

function ResetPasswordPage() {

  const navigate =
    useNavigate();

  const [
    searchParams
  ] = useSearchParams();

  const token =
    searchParams.get("token");

  const [
    formData,
    setFormData
  ] = useState({
    newPassword: "",
    confirmPassword: ""
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

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      setError("");
      setMessage("");

      if (!token) {

        setError(
          "Password reset token is missing."
        );

        return;
      }

      if (!formData.newPassword.trim()) {

        setError(
          "New password is required."
        );

        return;
      }

      if (
        formData.newPassword.length < 8
      ) {

        setError(
          "Password must contain at least 8 characters."
        );

        return;
      }

      if (
        formData.newPassword !==
        formData.confirmPassword
      ) {

        setError(
          "Passwords do not match."
        );

        return;
      }

      try {

        setLoading(true);

        const response =
          await resetPassword(
            token,
            formData.newPassword
          );

        setMessage(
          response.message
        );

        toast.success(
          "Password reset successfully."
        );

        setTimeout(
          () => {

            navigate(
              "/login",
              {
                replace: true
              }
            );

          },
          1500
        );

      } catch (error) {

        console.error(
          "Reset password error:",
          error
        );

        setError(
          "Invalid or expired password reset link."
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="login-page">

      <div className="login-card">

        <h1>
          Reset Password
        </h1>

        <p className="login-subtitle">
          Create a new password for your account.
        </p>

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

        <form onSubmit={handleSubmit}>

          <input
            type="password"
            name="newPassword"
            placeholder="New password"
            value={formData.newPassword}
            onChange={handleChange}
            disabled={loading}
          />

          <input
            type="password"
            name="confirmPassword"
            placeholder="Confirm new password"
            value={formData.confirmPassword}
            onChange={handleChange}
            disabled={loading}
          />

          <button
            type="submit"
            disabled={loading}
            className="full-width-button"
          >

            {loading
              ? "Resetting..."
              : "Reset Password"}

          </button>

        </form>

        <p className="login-help-text">

          <Link to="/login">
            Back to login
          </Link>

        </p>

      </div>

    </div>
  );
}

export default ResetPasswordPage;