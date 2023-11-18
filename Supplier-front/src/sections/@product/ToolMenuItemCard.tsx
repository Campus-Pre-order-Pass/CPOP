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
// firebase
// context
import { useAppContext } from "../../hooks/useContext";

// ----------------------------------------------------------------

interface AddMenuItem {
  product_id: string;
  type: string;
  name: string;
  price: number;
  unit: string;
  hot: boolean;
  menu_img_url: null;
  desc?: string | null;
  promotions?: string | null;
}

// 导入AddMenuItemForm组件
const ToolMenuItemCard: React.FC<{ props: AddMenuItem }> = ({ props }) => {
  const { uid } = useAppContext();
  const navigate = useNavigate();
  const [selectedFile, setSelectedFile] = useState<File | null>(null);

  const [formData, setFormData] = useState<AddMenuItem>(props);

  const [name, setName] = useState<any>();
  const [value, setValue] = useState<any>();

  const handleSelectChange = (event: SelectChangeEvent) => {
    const value = event.target.value as string;

    setName("type");
    setValue(value);
    setFormData({
      ...formData,
      type: value,
    });
  };
  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = e.target;

    setName(name);
    setValue(value);

    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSwitchChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setName(event.target.name);
    setValue(event.target.checked);
    setFormData({
      ...formData,
      [event.target.name]: event.target.checked,
    });
  };

  const handleFileChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0];

    setName("file");
    setValue(file);
    if (file && file.type === "image/jpeg") {
      setSelectedFile(file);
    } else {
      setSelectedFile(null);
      alert("必須使用 .jpg 照片");
    }
  };

  const handleSubmit = () => {
    const formDataToSend = new FormData();
    console.log(name, value);
    formDataToSend.append(name, value);

    axios
      .put(URLCONF.MenuUrl(formData.product_id), formDataToSend, {
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

  const handleSubmitFile = () => {
    const formDataToSend = new FormData();
    if (selectedFile) {
      formDataToSend.append("file", selectedFile);
    } else {
      return;
    }

    axios
      .put(URLCONF.OrtherUrl.FileUrl(formData.product_id), formDataToSend, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        if (response.status === 201) {
          // navigate(`/dashboard/products`, { replace: true });
          //  危險
          // window.location.reload();
        } else {
          // 其他状态码，可能需要处理
        }
      });
  };

  const handleDelete = () => {
    axios
      .put(URLCONF.MenuUrl(formData.product_id), {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        if (response.status === 201) {
          // navigate(`/dashboard/products`, { replace: true });
          //  危險
          // window.location.reload();
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
                  onBlur={handleSubmit}
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
                  onBlur={handleSubmit}
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
                  onBlur={handleSubmit}
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
                  onBlur={handleSubmit}
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
                  onBlur={handleSubmit}
                  fullWidth
                />
                <TextField
                  label="促銷"
                  variant="outlined"
                  name="promotions"
                  type="text"
                  value={formData.promotions}
                  onChange={handleChange}
                  onBlur={handleSubmit}
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
                      onBlur={handleSubmit}
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
                  <div>
                    <img
                      src={
                        selectedFile
                          ? URL.createObjectURL(selectedFile)
                          : `${URLCONF.BaseUrl}${formData.menu_img_url}`
                      }
                      alt="A beautiful landscape"
                      style={{
                        maxWidth: "100px",
                        maxHeight: "100px",
                        borderRadius: "20px",
                      }}
                    />
                  </div>
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
                      onBlur={handleSubmit}
                    >
                      更改圖片
                    </Button>
                  </label>
                </Stack>
              </Stack>
            </Grid>
            <Button
              color="error"
              variant="contained"
              type="submit"
              onClick={handleDelete}
            >
              取消商品
            </Button>
          </Stack>
        </form>
      </Grid>
    </>
  );
};

export default ToolMenuItemCard;
