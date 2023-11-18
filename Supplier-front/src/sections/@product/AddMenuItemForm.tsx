import React, { useState } from "react";
import axios from "axios";
import { useNavigate } from "react-router-dom";
// @mui
import {
  Stack,
  TextField,
  Button,
  Grid,
  Divider,
  Select,
  MenuItem,
  SelectChangeEvent,
  Switch,
} from "@mui/material";
import FormControlLabel from "@mui/material/FormControlLabel";
import CloudUploadIcon from "@mui/icons-material/CloudUpload";
// conf
import { URLCONF } from "../../conf";
// context
import { useAppContext } from "../../hooks/useContext";

// ----------------------------------------------------------------

interface AddMenuItem {
  type: string;
  name: string;
  price: number;
  unit: string;
  hot: boolean;
  desc?: string | null;
  promotions?: string | null;
}

const AddMenuItemForm: React.FC = () => {
  const { uid } = useAppContext();
  const navigate = useNavigate();

  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const [formData, setFormData] = useState<AddMenuItem>({
    type: "staples",
    name: "",
    price: 0,
    unit: "",
    hot: false,
  });

  const handleSelectChange = (event: SelectChangeEvent) => {
    const name = event.target.value as string;
    setFormData({
      ...formData,
      type: name,
    });
  };

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSwitchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFormData({
      ...formData,
      [event.target.name]: event.target.checked,
    });
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];
    if (file && file.type === "image/jpeg") {
      setSelectedFile(file);
    } else {
      setSelectedFile(null);
      alert("Please select a valid .jpg image file.");
    }
  };

  const handleSubmit = (e: React.FormEvent) => {
    const formDataToSend = new FormData();
    formDataToSend.append("name", formData.name);
    formDataToSend.append("type", formData.type);
    formDataToSend.append("price", formData.price.toString());
    formDataToSend.append("unit", formData.unit);
    formDataToSend.append("hot", formData.hot.toString());
    formDataToSend.append("desc", formData.desc || "");
    formDataToSend.append("promotions", formData.promotions || "");

    if (selectedFile) {
      formDataToSend.append("file", selectedFile);
    }

    e.preventDefault();

    axios
      .post(URLCONF.MenuUrl(uid), formDataToSend, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        if (response.status === 201) {
          // navigate(`/dashboard/products`, { replace: true });
          //  危險
          window.location.reload();
        } else {
          // 其他状态码，可能需要处理
        }
      });
  };
  return (
    <>
      <Grid spacing={3}>
        <form onSubmit={handleSubmit}>
          <Stack spacing={2}>
            <Divider sx={{ my: 3 }} />

            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <TextField
                  required
                  label="商品名稱"
                  variant="outlined"
                  name="name"
                  type="text"
                  value={formData.name}
                  onChange={handleChange}
                  fullWidth
                />
              </Stack>
            </Grid>
            <Divider sx={{ my: 3 }}>單位</Divider>
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <TextField
                  required
                  label="價格"
                  variant="outlined"
                  name="price"
                  type="number"
                  value={formData.price}
                  onChange={handleChange}
                  fullWidth
                />
                <TextField
                  required
                  label="單位"
                  variant="outlined"
                  name="unit"
                  type="text"
                  value={formData.unit}
                  onChange={handleChange}
                  fullWidth
                />
              </Stack>
            </Grid>
            <Divider sx={{ my: 3 }}>分類</Divider>
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <Select
                  required
                  value={formData.type}
                  onChange={handleSelectChange}
                  fullWidth
                >
                  <MenuItem value={"staples"}>主食</MenuItem>
                  <MenuItem value={"bento"}>便當</MenuItem>
                  <MenuItem value={"beverages"}>飲料</MenuItem>
                  <MenuItem value={"other"}>其他</MenuItem>
                </Select>
              </Stack>
            </Grid>
            <Divider sx={{ my: 3 }}>可不填寫</Divider>
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <TextField
                  label="產品描述"
                  variant="outlined"
                  name="desc"
                  value={formData.desc}
                  onChange={handleChange}
                  fullWidth
                />
                <TextField
                  label="促銷"
                  variant="outlined"
                  name="promotions"
                  type="text"
                  value={formData.promotions}
                  onChange={handleChange}
                  fullWidth
                />
              </Stack>
            </Grid>
            <Divider sx={{ my: 3 }}>其他</Divider>
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <FormControlLabel
                  control={
                    <Switch
                      checked={formData.hot}
                      onChange={handleSwitchChange}
                      name="hot"
                    />
                  }
                  label="熱門商品"
                />
              </Stack>
            </Grid>
            <Divider sx={{ my: 3 }}>商品圖片</Divider>
            <Grid item xs={12} sm={6} md={3}>
              <Stack direction="row" spacing={2}>
                <div>
                  {selectedFile && (
                    <div>
                      <img
                        src={URL.createObjectURL(selectedFile)}
                        alt="A beautiful landscape"
                        style={{
                          maxWidth: "100px",
                          maxHeight: "100px",
                          borderRadius: "20px",
                        }}
                      />
                    </div>
                  )}
                </div>
                <Stack direction="row" alignItems="center">
                  <input
                    type="file"
                    id="file-input"
                    accept=".jpg"
                    style={{ display: "none" }}
                    onChange={handleFileChange}
                  />
                  <label htmlFor="file-input">
                    <Button
                      component="span"
                      variant="contained"
                      startIcon={<CloudUploadIcon />}
                    >
                      上傳圖片
                    </Button>
                  </label>
                </Stack>
              </Stack>
            </Grid>
            <Button variant="contained" type="submit">
              新增商品
            </Button>
          </Stack>
        </form>
      </Grid>
    </>
  );
};

export default AddMenuItemForm;
