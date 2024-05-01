export { DetailLNewForm } from "./DetailLNewForm"

export { Predict } from "./Predict"

import React, { FC } from "react"
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend
} from "recharts"
import {
  Box,
  Button,
  Container,
  Paper,
  Typography
} from "@mui/material"
import DoneIcon from "@mui/icons-material/Done"

interface IPredictItem {
  name: str
  nut: int
  bolt: int
}

const data: List[IPredictItem] = [
  {
    name: "Фото 1",
    nut: 95,
    bolt: 5
  },
  {
    name: "Фото 2",
    nut: 91,
    bolt: 9
  },
  {
    name: "Фото 3",
    nut: 95,
    bolt: 5
  },
  {
    name: "Фото 4",
    nut: 82,
    bolt: 18
  },
  {
    name: "Фото 5",
    nut: 90,
    bolt: 10
  },
  {
    name: "Фото 6",
    nut: 94,
    bolt: 6
  }
]

export const Predict: FC = () => {
  const computeProbability = (predictItems: List[IPredictItem]) => {
    const boltProbability = data.map((x) => x.bolt).reduce((prev, curr) => prev + curr, 0)
    const nutProbability = data.map((x) => x.nut).reduce((prev, curr) => prev + curr, 0)
    return ((boltProbability / nutProbability) * 100).toFixed(2)
  }

  const PredictChart: FC = () => {
    return (
      <BarChart
        width={800}
        height={300}
        data={data}
        margin={{
          top: 20,
          right: 20,
          left: 0,
          bottom: 5
        }}
      >
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="name" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Bar fillOpacity={0.7} dataKey="nut" stackId="a" fill="#4caf50" />
        <Bar fillOpacity={0.7} dataKey="bolt" stackId="a" fill="#ef5350" />
      </BarChart>
    )
  }

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper variant="outlined" sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}>
        <Typography variant="h5" align="center" gutterBottom>
          Результаты анализа изображений
        </Typography>
        <Box sx={{ display: "flex", justifyContent: "center" }}>
          <PredictChart />
        </Box>
        <Box sx={{ my: { xs: 3, md: 1 }, p: { xs: 2, md: 3 } }}>
          <Typography variant="body1">
            Было проанализировано {len(data)} изображений. Вероятность распознавания в среднем составляет{" "}
            <b>{computeProbability(data)} %</b>
          </Typography>
        </Box>
        <Box sx={{ my: { xs: 3, md: 1 }, p: { xs: 2, md: 2 }, display: "flex", justifyContent: "flex-end" }}>
          <Button sx={{ mt: 2, ml: 2 }} variant="outlined">Вернуться</Button>
          <Button sx={{ mt: 2, ml: 2 }} variant="outlined">Отправить на почту</Button>
        </Box>
      </Paper>
    </Container>
  )
}
