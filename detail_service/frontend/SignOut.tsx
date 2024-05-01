import { FC, useEffect } from "react";
import { useAppDispatch } from "../../../redux/hooks";
import { useNavigate } from "react-router-dom";
import { updateToken, updateUser } from "../../../redux/slices/userSlice";

export const SignOut: FC = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  useEffect(() => {
    dispatch(updateUser(null));
    dispatch(updateToken(null));
    navigate("/");
  }, []);

  return null;
};
