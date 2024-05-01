import { FC, useState } from "react";
import {
  Alert,
  Collapse,
  Grid,
  IconButton,
  TextField,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import { IConfirmRequest } from "../../../../api/Auth";

export interface IVerifyCodeFormProps {
  data: IConfirmRequest;
  onChange: (newData: IConfirmRequest) => void;
}

export const VerifyForm: FC<IVerifyCodeFormProps> = ({ data, onChange }) => {
  const [open, setOpen] = useState<boolean>(true);

  return (
    <>
      <Collapse in={open}>
        <Alert
          severity="info"
          sx={{ mb: 2 }}
          action={
            <IconButton
              aria-label="close"
              color="inherit"
              size="small"
              onClick={() => {
                setOpen(false);
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }
        >
          На электронную почту был отправлен код подтверждения
        </Alert>
      </Collapse>
      <Typography variant="h6" gutterBottom>
        Учетные данные детали
      </Typography>
      <Grid container spacing={3}>
        <Grid item md={6} sm={6} xs={12}>
          <TextField
            required
            label="Код подтверждения"
            fullWidth
            variant="standard"
            value={data.confirmCode}
            onChange={(e) => onChange({ ...data, confirmCode: e.target.value })}
          />
        </Grid>
      </Grid>
    </>
  );
};

export * from "./FormStepper";
export * from "./EmailForm";
export { PersonalForm } from "./PersonalForm";
export { VerifyForm } from "./VerifyForm"; // Новый экспорт

import { FC, useState } from "react";
import {
  Alert,
  Collapse,
  Grid,
  IconButton,
  TextField,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";
import { IConfirmRequest } from "../../../../api/Auth";

export interface IVerifyCodeFormProps {
  data: IConfirmRequest;
  onChange: (newData: IConfirmRequest) => void;
}

export const VerifyForm: FC

import { FC, useState } from "react";
import { IConfirmRequest } from "../../../../api/Auth";
import {
  Alert,
  Collapse,
  Grid,
  IconButton,
  TextField,
  Typography,
} from "@mui/material";
import CloseIcon from "@mui/icons-material/Close";

export interface IVerifyCodeFormProps {
  /**
   * Данные
   */
  data: IConfirmRequest;
  /**
   * Событие обновления введенных данных на форме
   */
  onChange: (newData: IConfirmRequest) => void;
}

export const VerifyForm: FC<IVerifyCodeFormProps> = ({ data, onChange }) => {
  const [open, setOpen] = useState<boolean>(true);

  return (
    <>
      <Collapse in={open}>
        <Alert
          severity="info"
          sx={{ mb: 2 }}
          action={
            <IconButton
              aria-label="close"
              color="inherit"
              size="small"
              onClick={() => {
                setOpen(false);
              }}
            >
              <CloseIcon fontSize="inherit" />
            </IconButton>
          }
        >
          На электронную почту <i>{data.email}</i> был отправлен код
          подтверждения
        </Alert>
      </Collapse>
      <Typography variant="h6" gutterBottom>
        Данные уч. записи
      </Typography>
      <Grid container spacing={3}>
        <Grid item md={6} sm={6} xs={12}>
          <TextField
            required
            label="Код подтверждения"
            fullWidth
            variant="standard"
            value={data.confirmCode}
            onChange={(e) => onChange({ ...data, confirmCode: e.target.value })}
          />
        </Grid>
      </Grid>
    </>
  );
};

