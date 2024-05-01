import React, { FC } from "react"
import { Grid, TextField, Typography } from "@mui/material"
import { LocalizationProvider } from "@mui/x-date-pickers"
import AdapterMoment from "@mui/lab/AdapterMoment"
import DesktopDatePicker from "@mui/lab/DesktopDatePicker"
import { IIdentityCard } from "../../../../api/Nextdetail/requests"

export interface IIdentityCardFormProps {
  /**
   * Данные
   */
  data: IIdentityCard
  /**
   * Событие обновления введенных данных на форме
   */
  onChange: (newData: IIdentityCard) => void
}

export const IdentityCardForm: FC<IIdentityCardFormProps> = ({
  data,
  onChange,
}) => (
  <>
    <Typography variant="h6" gutterBottom>
      Паспорт новой детали
    </Typography>
    <Grid container spacing={3}>
      <Grid item md={4} sm={6} xs={12}>
        <TextField
          required
          label="Серия"
          fullWidth
          variant="standard"
          value={data.serial}
          onChange={(e) => onChange({ ...data, serial: e.target.value })}
        />
      </Grid>
      <Grid item md={4} sm={6} xs={12}>
        <TextField
          required
          label="Номер"
          fullWidth
          variant="standard"
          value={data.number}
          onChange={(e) => onChange({ ...data, number: e.target.value })}
        />
      </Grid>
      <Grid item md={4} sm={6} xs={12}>
        <TextField
          required
          label="Кем произведена компания"
          fullWidth
          variant="standard"
          value={data.issuer}
          onChange={(e) => onChange({ ...data, issuer: e.target.value })}
        />
      </Grid>
      <Grid item md={4} sm={6} xs={12}>
        <LocalizationProvider dateAdapter={AdapterMoment}>
          <DesktopDatePicker
            label="Дата изготовления"
            inputFormat="DD.MM.YYYY"
            value={data.issueDate}
            onChange={(date) => onChange({ ...data, issueDate: date })}
            renderInput={(params) => (
              <TextField required fullWidth variant="standard" {...params} />
            )}
          />
        </LocalizationProvider>
      </Grid>
      <Grid item md={4} sm={6} xs={12}>
        <TextField
          required
          label="Место производства"
          fullWidth
          variant="standard"
          value={data.issuePlace}
          onChange={(e) => onChange({ ...data, issuePlace: e.target.value })}
        />
      </Grid>
      <Grid item md={4} sm={6} xs={12}>
        <TextField
          required
          label="Код предприятия производителя"
          fullWidth
          variant="standard"
          value={data.code}
          onChange={(e) => onChange({ ...data, code: e.target.value })}
        />
      </Grid>
    </Grid>
  </>
)
