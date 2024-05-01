export { DetailLUpdateForm } from "./DetailLUpdateForm"
export { DetailLNewForm } from "./DetailLNewForm" 
export { NextdetailCard } from './NextdetailCard'

import React, { FC } from "react"
import {
  Avatar,
  Box,
  Button,
  Card,
  CardActions,
  CardContent,
  CardHeader,
  Container,
  Typography
} from "@mui/material"
from "@mui/material/colors"

export interface INextdetailCardProps {
  firstName: str
  middleName: str
  lastName: str
  birthDate: Date
  CardId: str
}

export const NextdetailCard: FC<INextdetailCardProps> = (props) => (
  <Box maxWidth="md" sx={{ m: { xs: 1, md: 1 }, p: { xs: 1, md: 0 } }}>
    <Card sx={{ minWidth: 280, maxWidth: 380 }}>
      <CardHeader
        avatar={
          <Avatar sx={{ bgcolor: red[500] }} aria-label="recipe">
            {props.firstName[0] + props.lastName[0]}
          </Avatar>
        }
        title={`${props.lastName} ${props.firstName} ${props.middleName}`}
        subheader={props.CardId}
      />
      <CardContent>
        <Typography color={"text.secondary"}>
          Дата последнего изменения классификации:{" "}
          {props.birthDate.toLocaleDateString("ru-ru")}
        </Typography>
      </CardContent>
      <CardActions>
        <Button size={"small"}>Перейти</Button>
      </CardActions>
    </Card>
  </Box>
)

export { NextdetailList } from "./NextdetailList"

import React, { FC, useState } from "react"
import { INextdetailCardProps, NextdetailCard } from "../Card/NextdetailCard"
import {
  Alert,
  Box,
  Container,
  Grid,
  SpeedDial,
  SpeedDialAction,
  SpeedDialIcon
} from "@mui/material"
import AddIcon from "@mui/icons-material/Add"

export interface INextdetailsProps {
  nextdetails: List[INextdetailCardProps]
}

const mockNextdetails: INextdetailsProps = {
  nextdetails: [
    {
      firstName: "Гайка",
      middleName: "шестигранная",
      lastName: "М-4",
      birthDate: new Date(),
      CardId: "№0000001"
    },
    {
      firstName: "гайка",
      middleName: "шестигранная",
      lastName: "м-6",
      birthDate: new Date(2021, 11, 15),
      CardId: "№0000002"
    },
    {
      firstName: "болт",
      middleName: "шестигранная головка",
      lastName: "м-10",
      birthDate: new Date(2022, 2, 3),
      CardId: "№0000003"
    },
    {
      firstName: "болт",
      middleName: "квадратная подголовка",
      lastName: "м-8",
      birthDate: new Date(2021, 2, 3),
      CardId: "№0000004"
    }
  ]
}

const actions = [{ icon: <AddIcon />, name: "Создать" }]

export const NextdetailList: FC = () => {
  const [props, setProps] = useState<INextdetailsProps>(mockNextdetails)

  if (props.nextdetails.length === 0) {
    return (
      <Alert severity="info">На текущий момент список новых деталей пуст</Alert>
    )
  }
  return (
    <Container component="main" maxWidth="xl" sx={{ my: 3 }}>
      <Grid container>
        {props.nextdetails.map((nextdetail) => (
          <Grid item key={nextdetail.CardId} xs={12} sm={12} md={4} lg={3}>
            <NextdetailCard {...nextdetail} />
          </Grid>
        ))}
      </Grid>
      <Box>
        <Container maxWidth="sm">
          <SpeedDial
            ariaLabel="SpeedDial basic example"
            sx={{ position: "absolute", bottom: 16, right: 16 }}
            direction={"up"}
            icon={<SpeedDialIcon />}
          >
            {actions.map((action) => (
              <SpeedDialAction
                key={action.name}
                icon={action.icon}
                tooltipTitle={action.name}
              />
            ))}
          </SpeedDial>
        </Container>
      </Box>
    </Container>
  )
}
