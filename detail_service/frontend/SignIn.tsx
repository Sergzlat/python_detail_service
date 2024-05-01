import React, { FC, useState } from "react";
import { Button, Container, Grid, Paper, TextField, Typography } from "@mui/material";
import { useNavigate } from "react-router-dom";
import { useAppDispatch } from "../../../redux/hooks";
import { updateToken, updateUser } from "../../../redux/slices/userSlice";
import * as AuthApi from "../../../api/Auth";
import { ISignInRequest } from "../../../api/Auth";

export const SignIn: FC = () => {
  const dispatch = useAppDispatch();
  const navigate = useNavigate();

  const [request, setRequest] = useState<ISignInRequest>({
    email: "",
    password: "",
  });

  const handleSignInButtonClick = () => {
    AuthApi.SignIn(request).then((r) => {
      if (r != null) {
        dispatch(updateUser({
          email: r.data.email,
          status: r.data.status,
          type: r.data.type,
        }));
        dispatch(updateToken({ jwtToken: r.data.jwtToken }));
        navigate("/");
      }
    });
  };

  return (
    <Container component="main" maxWidth="sm" sx={{ mb: 4 }}>
      <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
        <Typography component="h1" variant="h4" align="center">
          Войти
        </Typography>
        <Grid container spacing={3}>
          <Grid item md={12} sm={12} xs={12}>
            <TextField
              required
              label="Адрес изготовителя"
              fullWidth
              variant="standard"
              type="email"
              value={request.email}
              onChange={(e) => setRequest({ ...request, email: e.target.value })}
            />
          </Grid>
          <Grid item md={12} sm={12} xs={12}>
            <TextField
              required
              label="Пароль"
              fullWidth
              variant="standard"
              type="password"
              value={request.password}
              onChange={(e) => setRequest({ ...request, password: e.target.value })}
            />
          </Grid>
          <Grid item md={4} sm={4} xs={4}>
            <Button fullWidth variant="outlined" onClick={handleSignInButtonClick}>
              Войти
            </Button>
          </Grid>
        </Grid>
      </Paper>
    </Container>
  );
};

from typing import Callable
from dataclasses import dataclass
from tkinter import messagebox, Button, Entry, Frame, Label

@dataclass
class IConfirmRequest:
    email: str
    confirmCode: str

class VerifyForm(Frame):
    def __init__(self, master: Frame, data: IConfirmRequest, onChange: Callable[[IConfirmRequest], None], **kwargs):
        super().__init__(master, **kwargs)
        self.data = data
        self.onChange = onChange
        self.open = True

        collapse = Label(self, text="На электронную почту " + data.email + " был отправлен код подтверждения", fg="blue")
        collapse.pack()

        close_button = Button(self, text="Закрыть", command=self.close)
        close_button.pack()

        label = Label(self, text="Данные уч. записи", font=("Helvetica", 16))
        label.pack()

        code_label = Label(self, text="Код подтверждения", font=("Helvetica", 12))
        code_label.pack()

        self.code_entry = Entry(self)
        self.code_entry.pack()

    def close(self):
        self.open = False
        self.destroy()
