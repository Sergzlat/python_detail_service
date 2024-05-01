// api/DetailL/requests.ts
import { Moment } from "moment";

// Интерфейс запроса на создание детали
export interface IDetailLCreateRequest {
  lastName: string;
  firstName: string;
  middleName: string;
  birthDate: Moment;
  email: string;
  password: string;
}

// Объект запроса на создание детали по умолчанию
export const defaultDetailLCreateRequest: IDetailLCreateRequest = {
  lastName: "",
  firstName: "",
  middleName: "",
  birthDate: null as any,
  email: "",
  password: "",
};
