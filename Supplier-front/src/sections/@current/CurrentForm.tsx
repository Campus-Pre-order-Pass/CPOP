import React, { useState } from "react";
import axios from "axios";
// @mui
import {
  Stack,
  Grid,
  Switch,
  Card,
  Typography,
  CardContent,
  InputLabel,
  Input,
  FormHelperText,
  FormControl,
  TextField,
} from "@mui/material";
import FormControlLabel from "@mui/material/FormControlLabel";
import { URLCONF } from "../../conf";
import auth from "../../firebase/firebase";
// conf
// context

// ----------------------------------------------------------------

interface State {
  current_number: number;
  wait_number: number;
  is_closed: boolean;
  is_delivery_available: boolean;
}

function submit_state(name: string, value: any): void {
  const uid = auth.currentUser?.uid || "test";
  axios
    .put(URLCONF.CurrentStateUrl(uid), { [name]: value })
    .then((response) => {
      // Handle the response here if needed
    })
    .catch((error) => {
      // Handle errors here if needed
      console.log(error);
    });
}
export default function CurrentForm({ currentState }: { currentState: State }) {
  const [localState, setLocalState] = useState(currentState);

  const handleSwitchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const newValue = event.target.checked;
    const propertyName = event.target.name;

    // Use the spread operator to create a new object based on currentState
    // and update the specified property
    setLocalState((prevState) => ({
      ...prevState,
      [propertyName]: newValue,
    }));

    // Optionally, you can make an API call to update the server with the new value
    // Example: axios.post(URLCONF.UpdateSwitchUrl, { [propertyName]: newValue });
    submit_state(propertyName, newValue);
  };

  const handleTextChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setLocalState((prevData) => ({
      ...prevData,
      [name]: value,
    }));
    submit_state(name, value);
  };

  return (
    <Card>
      <CardContent>
        {" "}
        <Typography gutterBottom variant="h5" component="div">
          餐廳狀態
        </Typography>
      </CardContent>
      <Grid spacing={3}>
        <form>
          <Stack spacing={2} margin={2}>
            {/* <Divider sx={{ my: 3 }} /> */}
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <FormControlLabel
                  control={
                    <Switch
                      checked={localState.is_closed}
                      onChange={(event) => handleSwitchChange(event)}
                      name="is_closed"
                    />
                  }
                  label="開業狀態"
                />
                <FormControlLabel
                  control={
                    <Switch
                      checked={localState.is_delivery_available}
                      onChange={(event) => handleSwitchChange(event)}
                      name="is_delivery_available"
                    />
                  }
                  label="外送"
                />
                <TextField
                  margin={"dense"}
                  label={"現在號碼"}
                  type="number"
                  variant="outlined"
                  name="current_number"
                  value={localState.current_number}
                  onChange={handleTextChange}
                />
                <TextField
                  margin={"dense"}
                  label="等待人數"
                  type="number"
                  variant="outlined"
                  name="wait_number"
                  value={localState.wait_number}
                  onChange={handleTextChange}
                />
              </Stack>
            </Grid>
            {/* <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}></Stack>
            </Grid> */}
          </Stack>
        </form>
      </Grid>
    </Card>
  );
}
