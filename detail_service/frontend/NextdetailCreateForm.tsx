import React, { FC } from "react";
import { FC } from "react";
import { Grid, TextField, Typography } from "@mui/material";
import { LocalizationProvider } from "@mui/x-date-pickers";
import AdapterMoment from "@mui/lab/AdapterMoment";
import DesktopDatePicker from "@mui/lab/DesktopDatePicker";
import { INextdetailCreateRequest } from "../../../../api/Nextdetail/requests";

export interface INextdetailCreateFormProps {
  /**
   * Данные
   */
  data: INextdetailCreateRequest;
  /**
   * Событие обновления введенных данных на форме
   */
  onChange: (newData: INextdetailCreateRequest) => void;
}

export const NextdetailCreateForm: FC<INextdetailCreateFormProps> = ({
  data,
  onChange,
}) => (
  <>
    <Typography variant="h6" gutterBottom>
      Данные новой детали
    </Typography>
    <Grid container spacing={3}>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Вид"
          fullWidth
          variant="standard"
          value={data.type}
          onChange={(e) => onChange({ ...data, type: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Наименование"
          fullWidth
          variant="standard"
          value={data.name}
          onChange={(e) => onChange({ ...data, name: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Классификация"
          fullWidth
          variant="standard"
          value={data.classification}
          onChange={(e) => onChange({ ...data, classification: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <LocalizationProvider dateAdapter={AdapterMoment}>
          <DesktopDatePicker
            label="Дата изготовления"
            inputFormat="DD.MM.YYYY"
            value={data.manufactureDate}
            onChange={(date) => onChange({ ...data, manufactureDate: date })}
            renderInput={(params) => (
              <TextField required fullWidth variant="standard" {...params} />
            )}
          />
        </LocalizationProvider>
      </Grid>
    </Grid>
  </>
);
import React, { FC } from "react";
import { FC } from "react";
import { Grid, TextField, Typography } from "@mui/material";
import { LocalizationProvider } from "@mui/x-date-pickers";
import AdapterMoment from "@mui/lab/AdapterMoment";
import DesktopDatePicker from "@mui/lab/DesktopDatePicker";
import { INextdetailCreateRequest } from "../../../../api/Nextdetail/requests";

export interface INextdetailCreateFormProps {
  /**
   * Данные
   */
  data: INextdetailCreateRequest;
  /**
   * Событие обновления введенных данных на форме
   */
  onChange: (newData: INextdetailCreateRequest) => void;
}

export const NextdetailCreateForm: FC<INextdetailCreateFormProps> = ({
  data,
  onChange,
}) => (
  <>
    <Typography variant="h6" gutterBottom>
      Данные новой детали
    </Typography>
    <Grid container spacing={3}>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Вид"
          fullWidth
          variant="standard"
          value={data.type}
          onChange={(e) => onChange({ ...data, type: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Наименование"
          fullWidth
          variant="standard"
          value={data.name}
          onChange={(e) => onChange({ ...data, name: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <TextField
          required
          label="Классификация"
          fullWidth
          variant="standard"
          value={data.classification}
          onChange={(e) => onChange({ ...data, classification: e.target.value })}
        />
      </Grid>
      <Grid item md={6} sm={6} xs={12}>
        <LocalizationProvider dateAdapter={AdapterMoment}>
          <DesktopDatePicker
            label="Дата изготовления"
            inputFormat="DD.MM.YYYY"
            value={data.manufactureDate}
            onChange={(date) => onChange({ ...data, manufactureDate: date })}
            renderInput={(params) => (
              <TextField required fullWidth variant="standard" {...params} />
            )}
          />
        </LocalizationProvider>
      </Grid>
    </Grid>
  </>
);


from typing import Dict, Callable
from datetime import datetime
from dataclasses import dataclass
from flask import Flask, request, jsonify

app = Flask(__name__)

@dataclass
class INextdetailCreateRequest:
    firstName: str
    middleName: str
    lastName: str
    birthDate: datetime
    email: str
    password: str

@dataclass
class IConfirmRequest:
    confirmCode: str
    email: str

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    password = data.get("password")
    type = data.get("type")
    # Process signup logic here
    # Assuming SignUpResponse is returned with Id, Email, and Message fields
    response = {"Id": 1, "Email": email, "Message": "Signup successful"}
    return jsonify(response), 200

@app.route("/confirm", methods=["POST"])
def confirm():
    data = request.json
    email = data.get("email")
    confirm_code = data.get("confirmCode")
    # Process confirmation logic here
    # Assuming ConfirmResponse is returned with Id, Email, and Message fields
    response = {"Id": 1, "Email": email, "Message": "Confirmation successful"}
    return jsonify(response), 200

@app.route("/nextdetail", methods=["POST"])
def create_nextdetail():
    data = request.json
    # Assuming CreateNextdetail is a function to create a new detail
    # This function would use the provided data to create a new detail
    # and return a response indicating success or failure
    return jsonify({"message": "Nextdetail created successfully"}), 200

if __name__ == "__main__":
    app.run(debug=True)
