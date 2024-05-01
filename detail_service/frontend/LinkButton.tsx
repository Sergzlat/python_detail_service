import React, { FC } from "react";
import { Link as RouterLink } from "react-router-dom";
import Button, { ButtonProps } from "@mui/material/Button";

export interface LinkButtonProps extends ButtonProps {
  to: string;
}

export const LinkButton: FC<LinkButtonProps> = ({ to, ...buttonProps }) => (
  <Button component={RouterLink} to={to} {...buttonProps} />
);
import React, { FC } from "react";
import { Link } from "react-router-dom";
import { Button } from "@mui/material";

export interface ILinkButtonProps {
  to: string;
  text: string;
}

export const LinkButton: FC<ILinkButtonProps> = ({ to, text }) => (
  <Link to={to}>
    <Button variant="outlined" sx={{ my: 1, mx: 1.5 }}>
      {text}
    </Button>
  </Link>
);
// components/LinkButton.tsx
import React, { FC } from "react";
import { Link as RouterLink } from "react-router-dom";
import Button, { ButtonProps } from "@mui/material/Button";

export interface LinkButtonProps extends ButtonProps {
  to: string;
}

export const LinkButton: FC<LinkButtonProps> = ({ to, ...buttonProps }) => (
  <Button component={RouterLink} to={to} {...buttonProps} />
);
