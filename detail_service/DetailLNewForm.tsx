import { FC, useEffect, useState } from "react";
import { Box, Button, Container, Paper, Typography } from "@mui/material";
import { EmailForm } from "./components/EmailForm";
import { FormStepper } from "./components/FormStepper";
import * as DetailLApi from "../../../api/DetailL";
import {
  defaultDetailLCreateRequest,
  IDetailLCreateRequest,
} from "../../../api/DetailL";
import { useAppSelector } from "../../../redux/hooks";
import { isValidToken } from "../../../utils/functions";
import { defaultConfirmRequest, IConfirmRequest } from "../../../api/Auth";
import * as AuthApi from "../../../api/Auth";
import { PersonalForm } from "./components/PersonalForm";
import { VerifyForm } from "./components/VerifyForm";
import DoneIcon from "@mui/icons-material/Done";
import { Link } from "react-router-dom";

const steps = [
  "Персонализация детали",
  "Учетные данные детали",
  "Подтверждение учетных данных",
];

export const DetailLNewForm: FC = () => {
  const token = useAppSelector((state) => state.user.token);
  const [createRequest, setCreateRequest] = useState<IDetailLCreateRequest>(
    defaultDetailLCreateRequest
  );
  const [confirmRequest, setConfirmRequest] = useState<IConfirmRequest>(
    defaultConfirmRequest
  );
  const [activeStep, setActiveStep] = useState<number>(0);

  useEffect(() => {
    if (activeStep === 2) {
      DetailLApi.CreateDetailL(createRequest, token?.jwtToken ?? "").then(
        (response) => console.log(response)
      );
    }
    if (activeStep === 3) {
      AuthApi.Confirm({ ...confirmRequest, email: createRequest.email }).then(
        (response) => console.log(response)
      );
    }
  }, [activeStep]);

  const getStepContent = (step: number) => {
    if (step === 0) {
      return <PersonalForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 1) {
      return <EmailForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 2) {
      return <VerifyForm data={confirmRequest} onChange={setConfirmRequest} />;
    }

    throw new Error("Unknown step");
  };

  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper
        variant="outlined"
        sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}
      >
        <Typography component="h1" variant="h4" align="center">
          Регистрация новой детали
        </Typography>
        <FormStepper activeStep={activeStep} steps={steps} />
        <>
          {activeStep === steps.length ? (
            <>
              <Typography component="h5" variant="h5" align="center">
                Регистрация завершена успешно!
              </Typography>
              <Box sx={{ display: "flex", justifyContent: "center" }}>
                <DoneIcon color={"success"} fontSize={"large"} />
              </Box>
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                <Link to="/">
                  <Button
                    variant="outlined"
                    onClick={handleNext}
                    sx={{ mt: 3, ml: 1 }}
                  >
                    На главную
                  </Button>
                </Link>
              </Box>
            </>
          ) : (
            <>
              {getStepContent(activeStep)}
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                {activeStep !== 0 && (
                  <Button sx={{ mt: 3, ml: 1 }} onClick={handleBack}>
                    Назад
                  </Button>
                )}
                <Button
                  variant="outlined"
                  onClick={handleNext}
                  sx={{ mt: 3, ml: 1 }}
                >
                  {activeStep === steps.length - 1 ? "Подтвердить" : "Далее"}
                </Button>
              </Box>
            </>
          )}
        </>
      </Paper>
    </Container>
  );
};
import React, { FC, useEffect, useState } from "react";
import { Box, Button, Container, Paper, Typography } from "@mui/material";
import { EmailForm } from "./components/EmailForm";
import { FormStepper } from "./components/FormStepper";
import * as DetailLApi from "../../../api/DetailL";
import {
  defaultDetailLCreateRequest,
  IDetailLCreateRequest,
} from "../../../api/DetailL";
import { useAppSelector } from "../../../redux/hooks";
import { isValidToken } from "../../../utils/functions";
import { defaultConfirmRequest, IConfirmRequest } from "../../../api/Auth";
import * as AuthApi from "../../../api/Auth";
import { PersonalForm } from "./components/PersonalForm";
import { VerifyForm } from "./components/VerifyForm";
import DoneIcon from "@mui/icons-material/Done";
import { Link } from "react-router-dom";

const steps = [
  "Персонализация детали",
  "Учетные данные детали",
  "Подтверждение учетных данных",
];

export const DetailLNewForm: FC = () => {
  const token = useAppSelector((state) => state.user.token);
  const [createRequest, setCreateRequest] = useState<IDetailLCreateRequest>(
    defaultDetailLCreateRequest
  );
  const [confirmRequest, setConfirmRequest] = useState<IConfirmRequest>(
    defaultConfirmRequest
  );
  const [activeStep, setActiveStep] = useState<number>(0);

  useEffect(() => {
    if (activeStep === 2) {
      DetailLApi.CreateDetailL(createRequest, token?.jwtToken ?? "").then(
        (response) => console.log(response)
      );
    }
    if (activeStep === 3) {
      AuthApi.Confirm({ ...confirmRequest, email: createRequest.email }).then(
        (response) => console.log(response)
      );
    }
  }, [activeStep]);

  const getStepContent = (step: number) => {
    if (step === 0) {
      return <PersonalForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 1) {
      return <EmailForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 2) {
      return <VerifyForm data={confirmRequest} onChange={setConfirmRequest} />;
    }

    throw new Error("Unknown step");
  };

  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper
        variant="outlined"
        sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}
      >
        <Typography component="h1" variant="h4" align="center">
          Регистрация новой детали
        </Typography>
        <FormStepper activeStep={activeStep} steps={steps} />
        <>
          {activeStep === steps.length ? (
            <>
              <Typography component="h5" variant="h5" align="center">
                Регистрация завершена успешно!
              </Typography>
              <Box sx={{ display: "flex", justifyContent: "center" }}>
                <DoneIcon color={"success"} fontSize={"large"} />
              </Box>
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                <Link to="/">
                  <Button
                    variant="outlined"
                    onClick={handleNext}
                    sx={{ mt: 3, ml: 1 }}
                  >
                    На главную
                  </Button>
                </Link>
              </Box>
            </>
          ) : (
            <>
              {getStepContent(activeStep)}
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                {activeStep !== 0 && (
                  <Button sx={{ mt: 3, ml: 1 }} onClick={handleBack}>
                    Назад
                  </Button>
                )}
                <Button
                  variant="outlined"
                  onClick={handleNext}
                  sx={{ mt: 3, ml: 1 }}
                >
                  {activeStep === steps.length - 1 ? "Подтвердить" : "Далее"}
                </Button>
              </Box>
            </>
          )}
        </>
      </Paper>
    </Container>
  );
};

import { FC, useEffect, useState } from "react";
import { useAppSelector } from "../../../redux/hooks";
import {
  defaultIdentityCard,
  defaultNextdetailCreateRequest,
  INextdetailCreateRequest,
} from "../../../api/Nextdetail";
import { PersonalForm } from "./components/PersonalForm";
import { isValidToken } from "../../../utils/functions";
import { Box, Button, Container, Paper, Typography } from "@mui/material";
import { FormStepper } from "./components/FormStepper";
import { EmailForm } from "./components/EmailForm";
import { VerifyForm } from "./components/VerifyForm";
import { defaultConfirmRequest, IConfirmRequest } from "../../../api/Auth";
import { IdentityCardForm } from "./components/IdentityCardForm";
import DoneIcon from "@mui/icons-material/Done";
import { Link } from "react-router-dom";
import * as NextdetailApi from "../../../api/Nextdetail";
import * as AuthApi from "../../../api/Auth";
import { INextdetail } from "../../types/types";

const steps = [
  "Информация о новой детали",
  "Паспортные данные новой детали",
  "Данные уч. записи",
  "Подтверждение уч. записи",
];

export const NextdetailNewForm: FC = () => {
  const token = useAppSelector((state) => state.user.token);
  const [createRequest, setCreateRequest] = useState<INextdetailCreateRequest>(
    defaultNextdetailCreateRequest
  );
  const [confirmRequest, setConfirmRequest] = useState<IConfirmRequest>(
    defaultConfirmRequest
  );
  const [identityCard, setIdentityCard] =
    useState<INextdetail>(defaultIdentityCard);
  const [activeStep, setActiveStep] = useState<number>(0);

  useEffect(() => {
    setCreateRequest({ ...createRequest, identityCard });
  }, [identityCard]);

  useEffect(() => {
    if (activeStep === 3) {
      NextdetailApi.CreateNextdetail(createRequest, token?.jwtToken ?? "").then(
        (r) => r
      );
    }
    if (activeStep === 4) {
      AuthApi.Confirm({ ...confirmRequest, email: createRequest.email }).then(
        (r) => r
      );
    }
  }, [activeStep]);

  const getStepContent = (step: number) => {
    if (step === 0) {
      return <PersonalForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 1) {
      return (
        <IdentityCardForm data={identityCard} onChange={setIdentityCard} />
      );
    }
    if (step === 2) {
      return <EmailForm data={createRequest} onChange={setCreateRequest} />;
    }
    if (step === 3) {
      return <VerifyForm data={confirmRequest} onChange={setConfirmRequest} />;
    }

    throw new Error("Unknown step");
  };

  const handleNext = () => {
    setActiveStep(activeStep + 1);
  };

  const handleBack = () => {
    setActiveStep(activeStep - 1);
  };

  if (!isValidToken(token)) return <></>;

  return (
    <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
      <Paper
        variant="outlined"
        sx={{ my: { xs: 3, md: 6 }, p: { xs: 2, md: 3 } }}
      >
        <Typography component="h1" variant="h4" align="center">
          Регистрация новой детали
        </Typography>
        <FormStepper activeStep={activeStep} steps={steps} />
        <>
          {activeStep === steps.length ? (
            <>
              <Typography component="h5" variant="h5" align="center">
                Регистрация завершена успешно!
              </Typography>
              <Box sx={{ display: "flex", justifyContent: "center" }}>
                <DoneIcon color={"success"} fontSize={"large"} />
              </Box>
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                <Link to="/">
                  <Button
                    variant="outlined"
                    sx={{ mt: 3, ml: 1 }}
                  >
                    На главную
                  </Button>
                </Link>
              </Box>
            </>
          ) : (
            <>
              {getStepContent(activeStep)}
              <Box sx={{ display: "flex", justifyContent: "flex-end" }}>
                {activeStep !== 0 && (
                  <Button sx={{ mt: 3, ml: 1 }} onClick={handleBack}>
                    Назад
                  </Button>
                )}
                <Button
                  variant="outlined"
                  onClick={handleNext}
                  sx={{ mt: 3, ml: 1 }}
                >
                  {activeStep === steps.length - 1 ? "Подтвердить" : "Далее"}
                </Button>
              </Box>
            </>
          )}
        </>
      </Paper>
    </Container>
  );
};

export { NextdetailUpdateForm } from "./NextdetailUpdateForm";

import { FC } from "react";

export const NextdetailUpdateForm: FC = () => {
  return <></>;
};
