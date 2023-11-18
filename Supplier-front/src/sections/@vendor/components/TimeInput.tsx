import React from "react";
import { Stack, TextField } from "@mui/material";
import { UrlInputProps } from "./interface";

function TimeInput({
  label,
  name,
  value,
  fullWidth,
  onChange,
  onBlur,
}: UrlInputProps) {
  return (
    <div>
      <Stack
        direction="row"
        sx={{ "& > *:not(:last-child)": { marginRight: 1 } }}
      >
        <TextField
          label={label}
          variant="outlined"
          name={name}
          type="time"
          value={value}
          onChange={onChange}
          onBlur={onBlur}
          fullWidth={fullWidth}
          required
          sx={{ width: "100%" }}
        />
      </Stack>
    </div>
  );
}

export default TimeInput;
