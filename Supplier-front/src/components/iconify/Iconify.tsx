import { forwardRef, HTMLAttributes } from "react";
import { Icon } from "@iconify/react";
import { Box, BoxProps } from "@mui/material";
import React from "react";

interface IconifyProps extends HTMLAttributes<HTMLDivElement> {
  icon: string;
  width?: number | string;
  sx?: BoxProps["sx"];
}

const Iconify = forwardRef<HTMLDivElement, IconifyProps>((props, ref) => {
  const { icon, width = 20, sx, ...other } = props;

  return (
    <Box
      ref={ref}
      component={Icon}
      icon={icon}
      sx={{ width, height: width, ...sx }}
    />
  );
});

export default Iconify;
