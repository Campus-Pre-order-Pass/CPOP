import { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
// @mui
import {
    Stack,
    TextField,
    Button,
    MenuItem,
    Select,
    Input,
    Grid,
    Divider
} from '@mui/material';
// conf
import { URLCONF } from '../../../conf';


// ----------------------------------------------------------------------

export default function RegisterFrom({ setCurrentStep, uid, email, displayName }) {
    const navigate = useNavigate();




    const [selectedFile, setSelectedFile] = useState(null);


    const [formData, setFormData] = useState({
        email: email,
        name: "",
        principal: displayName,
        contact: '',
        campus_name: '建功校區',
        open_time: '',
        close_time: '',
        vendor_img_url: "",
        preorder_qty: 0,

    });

    const handleChange = (event) => {
        const { name, value } = event.target;
        setFormData({
            ...formData,
            [name]: value,
        });
    };



    const handleFileChange = (e) => {
        const file = e.target.files[0];
        if (file && file.type === 'image/jpeg') {
            setSelectedFile(file);
        } else {
            setSelectedFile(null);
            alert('Please select a valid .jpg image file.');
        }
    };




    const handleSubmit = (e) => {

        const formDataToSend = new FormData();
        formDataToSend.append('email', formData.email);
        // formDataToSend.append('password', formData.password);
        formDataToSend.append('name', formData.name);
        formDataToSend.append('principal', formData.principal);
        formDataToSend.append('contact', formData.contact);
        formDataToSend.append('campus_name', formData.campus_name);
        formDataToSend.append('open_time', formData.open_time);
        formDataToSend.append('close_time', formData.close_time);

        if (selectedFile) {
            formDataToSend.append('file', selectedFile);
        }



        e.preventDefault();



        axios.post(URLCONF.RegisterUrl(uid),
            formDataToSend
            , {
                headers: {
                    'Content-Type': 'multipart/form-data',
                },
            })
            .then((response) => {
                if (response.status === 201) {
                    // 成功，执行导航操作
                    navigate(`/login`, { replace: true });
                } else {
                    // 其他状态码，可能需要处理
                }
            })



    };

    return (
        <>
            <Grid spacing={3}>

                <form onSubmit={handleSubmit}>
                    <Stack spacing={2}>
                        <Grid item xs={12} sm={6} md={3}>
                            <Stack direction="row" spacing={2}>
                                <TextField
                                    required
                                    label="信箱"
                                    variant="outlined"
                                    name="email"
                                    value={formData.email}
                                    onChange={handleChange}
                                    fullWidth
                                />

                            </Stack>

                        </Grid>
                        <Grid item xs={12} sm={6} md={3}>
                            <Stack direction="row" spacing={2}>

                                <TextField
                                    required
                                    label="廠商名"
                                    variant="outlined"
                                    name="name"
                                    value={formData.name}
                                    onChange={handleChange}
                                    fullWidth
                                />
                                <TextField
                                    required
                                    label="負責人"
                                    variant="outlined"
                                    name="principal"
                                    type="text"
                                    value={formData.principal}
                                    onChange={handleChange}
                                    fullWidth
                                />

                            </Stack>

                        </Grid>
                        <Grid item xs={12} sm={6} md={3}>
                            <Stack direction="row" spacing={2}>

                                <TextField
                                    required
                                    label="開業時間"
                                    variant="outlined"
                                    name="open_time"
                                    type="time" // 设置输入类型为时间
                                    value={formData.open_time}
                                    onChange={handleChange}
                                    InputLabelProps={{
                                        shrink: true, // 让标签缩小，以适应时间输入
                                    }}
                                    fullWidth
                                />
                                <TextField
                                    required
                                    label="歇業時間"
                                    variant="outlined"
                                    name="close_time"
                                    type="time"
                                    value={formData.close_time}
                                    onChange={handleChange}
                                    InputLabelProps={{
                                        shrink: true, // 让标签缩小，以适应时间输入
                                    }}
                                    fullWidth
                                />
                            </Stack>

                        </Grid>
                        <Grid item xs={12} sm={6} md={3}>
                            <Stack direction="row" spacing={2} >

                                <TextField
                                    required
                                    label="電話"
                                    variant="outlined"
                                    name="contact"
                                    type='number'
                                    value={formData.contact}
                                    onChange={handleChange}
                                    fullWidth
                                />

                                <Select
                                    required
                                    value={formData.campus_name || '建功校區'}
                                    onChange={handleChange}
                                    fullWidth
                                >
                                    <MenuItem value={'建功校區'}>建功校區</MenuItem>
                                    <MenuItem value={'第一校區'}>第一校區</MenuItem>
                                    <MenuItem value={'燕巢校區'}>燕巢校區</MenuItem>
                                </Select>
                            </Stack>

                        </Grid>

                        <Divider sx={{ my: 3 }}>
                            商店圖片
                        </Divider>
                        <Grid item xs={12} sm={6} md={3}>
                            <Stack direction="row" spacing={2}>
                                <div>
                                    {selectedFile && (
                                        <div>
                                            <img
                                                src={URL.createObjectURL(selectedFile)}
                                                alt="A beautiful landscape"
                                                style={{
                                                    maxWidth: '200px',
                                                    maxHeight: '200px',
                                                    borderRadius: '20px' // 设置圆角半径，以像素为单位
                                                }} />
                                        </div>
                                    )}
                                </div>
                                <Input
                                    required
                                    type="file"
                                    inputProps={{ accept: '.jpg' }}
                                    onChange={handleFileChange}
                                />
                            </Stack>

                        </Grid>
                        <Button variant="contained" type="submit">
                            註冊！
                        </Button>
                    </Stack>


                </form>
            </Grid >

        </>
    );
}


