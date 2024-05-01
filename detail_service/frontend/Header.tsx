import React, { FC } from "react";
import { AppBar, Toolbar, Typography } from "@mui/material";
import { Link } from "react-router-dom";
import { useAppSelector } from "../../redux/hooks";
import { isValidToken } from "../../utils/functions";
import { UserStatus, UserType } from "../../types/types";
import { LinkButton } from "../LinkButton";

export const Header: FC = () => {
  const token = useAppSelector((state) => state.user.token);
  const user = useAppSelector((state) => state.user.user);

  const isAdmin = () =>
    isValidToken(token) &&
    user &&
    user.status === UserStatus.Confirmed &&
    user.type === UserType.Admin;
  const isDetailL = () =>
    isValidToken(token) &&
    user &&
    user.status === UserStatus.Confirmed &&
    user.type === UserType.DetailL;

  return (
    <AppBar position="static" color="default" elevation={0}>
      <Toolbar sx={{ flexWrap: "wrap" }}>
        <Typography variant="h6" color="inherit" noWrap sx={{ flexGrow: 1 }}>
          <Link to="/">Bolt</Link>
        </Typography>
        {isAdmin() && (
          <LinkButton to="/detailL/new" text="Зарегистрировать деталь" />
        )}
        {isAdmin() && (
          <LinkButton to="/detailL" text="Просмотр списка деталей" />
        )}
        {!isValidToken(token) && <LinkButton to="/signin" text="Войти" />}
        {isValidToken(token) && <LinkButton to="/signout" text="Выйти" />}
      </Toolbar>
    </AppBar>
  );
};
