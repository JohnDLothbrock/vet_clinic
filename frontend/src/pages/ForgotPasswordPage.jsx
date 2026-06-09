import {
  useState
} from "react";

import {
  Link
} from "react-router-dom";

import toast from "react-hot-toast";

import {
  requestPasswordReset
} from "../services/authService";

import "../styles/app.css";

function ForgotPasswordPage() {

  const [
    email,
    setEmail
  ] = useState("");

  const [
    loading,
    setLoading
  ] = useState(false);

  const [
    message,
    setMessage
  ] = useState("");

  const [
    error,
    setError
  ] = useState("");

  const handleSubmit =
    async (event) => {

      event.preventDefault();

      setError("");
      setMessage("");

      if (!email.trim()) {

        setError(
          "Email is required."
        );

        return;
      }

      try {

        setLoading(true);

        const response =
          await requestPasswordReset(
            email.trim()
          );

        setMessage(
          response.message
        );

        toast.success(
          "Password reset request processed."
        );

      } catch (error) {

        console.error(
          "Forgot password error:",
          error
        );

        setError(
          "Unable to process password reset request."
        );

      } finally {

        setLoading(false);
      }
    };

  return (

    <div className="login-page">

      <div className="login-card">

        <h1>
          Forgot Password
        </h1>

        <p className="login-subtitle">
          Enter your email to receive a reset link.
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
            type="email"
            name="email"
            placeholder="Email address"
            value={email}
            onChange={(event) => {

              setError("");
              setMessage("");
              setEmail(
                event.target.value
              );
            }}
            disabled={loading}
          />

          <button
            type="submit"
            disabled={loading}
            className="full-width-button"
          >

            {loading
              ? "Sending..."
              : "Send Reset Link"}

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

export default ForgotPasswordPage;