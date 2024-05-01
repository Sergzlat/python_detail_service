  // utils/functions.ts
import { IDetailL } from "../types/types";

// Функция для получения полного имени детали
export const getFullName = (detail: IDetailL): string => {
  return `${detail.lastName} ${detail.firstName} ${detail.middleName}`;
};

