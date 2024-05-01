// api/DetailL.ts
// ...

// Интерфейс запроса на создание детали
export interface IDetailLCreateRequest {
  email: string;
  password: string;
  lastName: string;
  firstName: string;
  middleName: string;
  birthDate: Date | null;
}

// Объект запроса на создание детали по умолчанию
export const defaultDetailLCreateRequest: IDetailLCreateRequest = {
  email: "",
  password: "",
  lastName: "",
  firstName: "",
  middleName: "",
  birthDate: null,
};

// Функция для создания детали
export const CreateDetailL = async (
  data: IDetailLCreateRequest,
  token: string
): Promise<any> => {
  // Отправка запроса на создание детали
};
