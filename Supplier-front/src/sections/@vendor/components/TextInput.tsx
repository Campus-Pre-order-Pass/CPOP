import React from "react";
// @mui
import { TextField } from "@mui/material";

// interface
import { TextInputProps } from "./interface";

function TextInput({
  label,
  name,
  value,
  fullWidth,
  handleChange,
  handleBlur,
}: TextInputProps) {
  return (
    <>
      {/* ig */}
      <TextField
        label={label}
        variant="outlined"
        name={name}
        value={value}
        onChange={handleChange}
        onBlur={handleBlur}
        fullWidth={fullWidth}
      />
    </>
  );
}

export default TextInput;
