import React, { FC, useEffect, useState } from "react";
import {
  Button,
  Card,
  CardContent,
  Container,
  Grid,
  TextField,
  Typography,
} from "@mui/material";
import { getFullName } from "../../../utils/functions";
import { EmptyDetailL, IDetailL } from "../../../types/types";
import { useAppSelector } from "../../../redux/hooks";
import { useParams } from "react-router-dom";
import { LocalizationProvider } from "@mui/x-date-pickers";
import { AdapterMoment } from "@mui/x-date-pickers/AdapterMoment";
import { DesktopDatePicker } from "@mui/x-date-pickers/DesktopDatePicker";

export const DetailLAccount: FC = () => {
  const params = useParams<any>();
  const detailLs = useAppSelector((state) => state.detailL.detailLs);

  const [detailL, setDetailL] = useState<IDetailL>(EmptyDetailL);
  const [viewMode, setViewMode] = useState<boolean>(true);

  useEffect(() => {
    const model = detailLs.find(
      (d) => d.id === (params && params.detailLId ? parseInt(params.detailLId) : 0)
    );
    if (model) {
      setDetailL(model);
    }
  }, []);

  const handleUpdateButton = () => {
    setViewMode(!viewMode);
  };

  return (
    <Container component="main" maxWidth="md" sx={{ my: 3 }}>
      <Card>
        <CardContent>
          <Grid container sx={{ my: 3, mx: 0 }}>
            <Grid item xs={10}>
              <Typography
                noWrap
                variant="h5"
                component="div"
                sx={{ flexGrow: 1 }}
              >
                {getFullName(detailL)}
              </Typography>
              <Typography
                variant="body2"
                component="div"
                color="text.secondary"
              >
                {detailL.birthDate?.toLocaleDateString("ru-ru")}
              </Typography>
            </Grid>
            <Grid item xs={2}>
              <Button size="large" onClick={handleUpdateButton}>
                {viewMode ? "Редактировать" : "Сохранить"}
              </Button>
            </Grid>
          </Grid>
          <Grid container sx={{ my: 3, mx: 0 }}>
            <Typography variant="h6" gutterBottom>
              Информация о детали
            </Typography>
            <Grid container spacing={3}>
              <Grid item md={3} sm={6} xs={12}>
                <TextField
                  disabled={viewMode}
                  required
                  label="Вид"
                  fullWidth
                  variant="standard"
                  value={detailL.lastName}
                  onChange={(e) =>
                    setDetailL({ ...detailL, lastName: e.target.value })
                  }
                />
              </Grid>
              <Grid item md={3} sm={6} xs={12}>
                <TextField
                  disabled={viewMode}
                  required
                  label="Наименование"
                  fullWidth
                  variant="standard"
                  value={detailL.firstName}
                  onChange={(e) =>
                    setDetailL({ ...detailL, firstName: e.target.value })
                  }
                />
              </Grid>
              <Grid item md={3} sm={6} xs={12}>
                <TextField
                  disabled={viewMode}
                  required
                  label="Классификация"
                  fullWidth
                  variant="standard"
                  value={detailL.middleName}
                  onChange={(e) =>
                    setDetailL({ ...detailL, middleName: e.target.value })
                  }
                />
              </Grid>
              <Grid item md={3} sm={6} xs={12}>
                <LocalizationProvider dateAdapter={AdapterMoment}>
                  <DesktopDatePicker
                    disabled={viewMode}
                    label="Дата изготовления"
                    inputFormat="DD.MM.YYYY"
                    value={detailL.birthDate}
                    onChange={(date) =>
                      setDetailL({ ...detailL, birthDate: date })
                    }
                    mask="__.__.____"
                    renderInput={(params) => (
                      <TextField
                        required
                        fullWidth
                        variant="standard"
                        {...params}
                      />
                    )}
                  />
                </LocalizationProvider>
              </Grid>
            </Grid>
          </Grid>
        </CardContent>
      </Card>
    </Container>
  );
};
