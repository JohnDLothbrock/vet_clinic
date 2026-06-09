import {
  getUserRoleId
} from "./tokenService";

export const ROLE_IDS = {
  ADMIN: 1,
  VETERINARIAN: 2,
  RECEPTIONIST: 3
};

export function isAdmin() {

  return getUserRoleId() === ROLE_IDS.ADMIN;
}

export function isVeterinarian() {

  return getUserRoleId() === ROLE_IDS.VETERINARIAN;
}

export function isReceptionist() {

  return getUserRoleId() === ROLE_IDS.RECEPTIONIST;
}

export function canViewDashboard() {

  return true;
}

export function canViewPets() {

  return true;
}

export function canCreatePet() {

  return (
    isAdmin() ||
    isReceptionist()
  );
}

export function canEditPet() {

  return (
    isAdmin() ||
    isReceptionist()
  );
}

export function canDeletePet() {

  return isAdmin();
}

export function canViewOwners() {

  return true;
}

export function canCreateOwner() {

  return (
    isAdmin() ||
    isReceptionist()
  );
}

export function canEditOwner() {

  return (
    isAdmin() ||
    isReceptionist()
  );
}

export function canDeleteOwner() {

  return isAdmin();
}

export function canViewAppointments() {

  return true;
}

export function canCreateAppointment() {

  return true;
}

export function canEditAppointment() {

  return true;
}

export function canDeleteAppointment() {

  return isAdmin();
}

export function canViewAuditLogs() {

  return isAdmin();
}

export function canViewUsers() {

  return isAdmin();
}

export function canCreateUser() {

  return isAdmin();
}

export function canUpdateUserRole() {

  return isAdmin();
}

export function canUpdateUserActive() {

  return isAdmin();
}

export function canViewMedicalRecords() {

  return true;
}

export function canCreateMedicalRecord() {

  return (
    isAdmin() ||
    isVeterinarian()
  );
}

export function canEditMedicalRecord() {

  return (
    isAdmin() ||
    isVeterinarian()
  );
}

export function canDeleteMedicalRecord() {

  return isAdmin();
}