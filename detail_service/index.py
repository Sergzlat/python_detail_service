from typing import List
from datetime import datetime

from ...types.types import IDetailL

# Mock implementation for example
detail_ls: List[IDetailL] = [
    {"id": "1", "email": "example1@example.com", "password": "password1", "firstName": "John", "lastName": "Doe", "middleName": "Smith", "birthDate": datetime.now()},
    {"id": "2", "email": "example2@example.com", "password": "password2", "firstName": "Jane", "lastName": "Doe", "middleName": "Smith", "birthDate": datetime.now()},
]

async def get_all_detail_ls(token: str) -> List[IDetailL]:
    """
    Get all detail ls from the server using the provided token.
    """
    # Here would usually be the execution of a request to the server to retrieve a list of detail ls using the provided token
    # In this case, we simply return mock data
    return detail_ls

async def create_detail_l(detail_l: IDetailL, token: str) -> IDetailL:
    """
    Create a new detail l on the server using the provided token and detail l data.
    """
    # Here would usually be the execution of a request to the server to create a new detail l using the provided token and detail l data
    # In this case, we simply return mock data
    new_detail_l = {**detail_l, "id": str(len(detail_ls) + 1)}
    detail_ls.append(new_detail_l)
    return new_detail_l

// api/DetailL/index.ts
import { IDetailL } from "../../types/types";

// Моковая реализация для примера
const detailLs: IDetailL[] = [
  { id: "1", email: "example1@example.com", password: "password1", firstName: "John", lastName: "Doe", middleName: "Smith", birthDate: new Date() },
  { id: "2", email: "example2@example.com", password: "password2", firstName: "Jane", lastName: "Doe", middleName: "Smith", birthDate: new Date() },
];

export const GetAllDetailLs = async (token: string): Promise<IDetailL[] | null> => {
  // Здесь обычно было бы выполнение запроса к серверу для получения списка detailLs с использованием переданного токена
  // В данном случае просто возвращаем моковые данные
  return detailLs;
};

export const CreateDetailL = async (detailL: IDetailL, token: string): Promise<IDetailL | null> => {
  // Здесь обычно было бы выполнение запроса к серверу для создания новой детали с использованием переданного токена и данных детали
  // В данном случае просто возвращаем моковые данные
  const newDetailL = { ...detailL, id: String(detailLs.length + 1) };
  detailLs.push(newDetailL);
  return newDetailL;
};

// api/Auth/index.ts
import { IConfirmRequest } from "./types";

// Моковая реализация для примера
export const Confirm = async (confirmRequest: IConfirmRequest): Promise<boolean> => {
  // Здесь обычно было бы выполнение запроса к серверу для подтверждения учетных данных с использованием переданных данных
  // В данном случае просто возвращаем true в качестве успешного подтверждения
  return true;
};

// api/DetailL/index.ts
import { IDetailL, IDetailLCreateRequest } from "./types";

// Моковая реализация для примера
const detailLs: IDetailL[] = [];

// Моковая функция для получения списка деталей
export const GetAllDetailLs = async (token: string): Promise<IDetailL[]> => {
  // Здесь обычно было бы выполнение запроса к серверу для получения списка деталей с использованием переданного токена аутентификации
  // В данном случае просто возвращаем моковый список деталей
  return detailLs;
};

// Моковая функция для создания новой детали
export const CreateDetailL = async (detail: IDetailLCreateRequest, token: string): Promise<boolean> => {
  // Здесь обычно было бы выполнение запроса к серверу для создания новой детали с использованием переданных данных и токена аутентификации
  // В данном случае просто добавляем моковую деталь в список
  const newDetail: IDetailL = {
    id: detailLs.length + 1,
    email: detail.email,
    password: detail.password,
    lastName: detail.lastName,
    firstName: detail.firstName,
    middleName: detail.middleName,
    birthDate: detail.birthDate,
  };
  detailLs.push(newDetail);
  return true;
};
