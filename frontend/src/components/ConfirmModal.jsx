import {
  useEffect
} from "react";

function ConfirmModal({

  isOpen,
  title,
  message,
  confirmText,
  cancelText,
  variant,
  onConfirm,
  onCancel

}) {

  useEffect(() => {

    const handleEscape =
      (event) => {

        if (
          event.key === "Escape" &&
          isOpen
        ) {

          onCancel();
        }
      };

    document.addEventListener(
      "keydown",
      handleEscape
    );

    return () => {

      document.removeEventListener(
        "keydown",
        handleEscape
      );
    };

  }, [
    isOpen,
    onCancel
  ]);

  if (!isOpen) {

    return null;
  }

  const confirmButtonClass =
    variant === "danger"
      ? "delete-button"
      : "confirm-modal-primary-button";

  return (

    <div
      className="confirm-modal-backdrop"
      onClick={onCancel}
    >

      <div
        className="confirm-modal"
        onClick={(event) =>
          event.stopPropagation()
        }
      >

        <div className="confirm-modal-icon">

          {variant === "danger"
            ? "⚠️"
            : "✅"}

        </div>

        <h2>
          {title}
        </h2>

        <p>
          {message}
        </p>

        <div className="confirm-modal-actions">

          <button
            type="button"
            className="secondary-button"
            onClick={onCancel}
          >
            {cancelText || "Cancel"}
          </button>

          <button
            type="button"
            className={confirmButtonClass}
            onClick={onConfirm}
          >
            {confirmText || "Confirm"}
          </button>

        </div>

      </div>

    </div>
  );
}

export default ConfirmModal;