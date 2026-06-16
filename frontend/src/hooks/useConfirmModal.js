import {
  useRef,
  useState
} from "react";

function useConfirmModal() {

  const resolverRef =
    useRef(null);

  const [
    modalState,
    setModalState
  ] = useState({
    isOpen: false,
    title: "",
    message: "",
    confirmText: "Confirm",
    cancelText: "Cancel",
    variant: "default"
  });

  const openConfirmModal =
    ({
      title,
      message,
      confirmText = "Confirm",
      cancelText = "Cancel",
      variant = "default"
    }) => {

      return new Promise(
        (resolve) => {

          resolverRef.current =
            resolve;

          setModalState({
            isOpen: true,
            title,
            message,
            confirmText,
            cancelText,
            variant
          });
        }
      );
    };

  const closeModal =
    (result) => {

      if (resolverRef.current) {

        resolverRef.current(
          result
        );
      }

      resolverRef.current =
        null;

      setModalState({
        isOpen: false,
        title: "",
        message: "",
        confirmText: "Confirm",
        cancelText: "Cancel",
        variant: "default"
      });
    };

  const confirmModalProps = {
    ...modalState,

    onConfirm: () =>
      closeModal(true),

    onCancel: () =>
      closeModal(false)
  };

  return {
    confirmModalProps,
    openConfirmModal
  };
}

export default useConfirmModal;