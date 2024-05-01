// api/Auth.ts
// ...

// Интерфейс запроса на подтверждение учетных данных
export interface IConfirmRequest {
  email: string;
  confirmCode: string;
}

// Объект запроса на подтверждение учетных данных по умолчанию
export const defaultConfirmRequest: IConfirmRequest = {
  email: "",
  confirmCode: "",
};

// Функция для отправки запроса на подтверждение учетных данных
export const Confirm = async (data: IConfirmRequest): Promise<any> => {
  // Отправка запроса на подтверждение учетных данных
};
