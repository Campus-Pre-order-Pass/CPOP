
import { Helmet } from 'react-helmet-async';
import { useState, useEffect } from 'react';
import axios from 'axios';
// @mui
import {
    Container,
    Stack,
    TextField,
    Box,
    Divider,
    Grid,
    MenuItem,
    Select,
    Paper,
    Skeleton,
} from '@mui/material';
import { styled } from '@mui/material/styles';
// components
import Iconify from '../components/iconify/index';
// texts
import TEXTS from '../locales/text';
// conf
import { URLCONF } from '../conf';
// context
import { useAppContext } from '../hooks/useContext';

// ----------------------------------------------------------------


const DemoPaper = styled(Paper)(({ theme }) => ({
    margin: 20,
    background: "rgba(128, 128, 128, 0.2)",
    padding: theme.spacing(2),
    ...theme.typography.body2,
    textAlign: 'center',
}));

export default function VendorPage() {
    const { uid } = useAppContext();

    const [selectedFile, setSelectedFile] = useState(null);
    const [name, setName] = useState(null);
    const [value, setValue] = useState(null);
    const [formData, setFormData] = useState({
        uid: '', // 这个字段通常由后端生成
        name: '',
        principal: '',
        email: '',
        contact: '',
        campus_name: '建功校區',
        open_time: '',
        close_time: '',
        rest_open_time: '',
        rest_close_time: '',
        vendor_img_url: '',
        desc: '',
        promotions: '',
        shop_url: '',
        ig_url: '',
        fd_url: '',
        preorder_qty: 0,
    });


    useEffect(() => {

        axios.get(URLCONF.RegisterUrl(uid))
            .then((response) => {
                setFormData(response.data);
                // console.log(
                //     `${URLCONF.BaseUrl}${formData.vendor_img_url}`);
            })
            .catch((error) => {
                console.error('Error:', error);
                // 在这里处理请求错误，可以显示错误信息或采取其他措施
            });

    }, []);


    const handleChange = (e) => {
        const { name, value } = e.target;
        setValue(value);
        setName(name);

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

    const handleBlur = () => {


        axios.put(URLCONF.RegisterUrl(uid), { [name]: value })
            .then((response) => {
                // 处理成功响应
                console.log('Success:', response.data);
            })
    };



    return (<>
        <Helmet>
            <title> {TEXTS.Vendorpage.name} | {TEXTS.projName}</title>
        </Helmet>
        {formData.email === "" ?
            (<Skeleton variant="rounded" width={"100%"} height={"100%"} />)
            : (
                <DemoPaper variant="outlined" >

                    <Container>

                        <Stack direction="row" spacing={2} alignItems="center" margin={2} >

                            <Box
                                component="img" // 指定子组件为图像
                                src={`${URLCONF.BaseUrl}${formData.vendor_img_url}`}
                                alt="img"
                                sx={{
                                    maxWidth: '100%', // 默认最大宽度
                                    width: '50px', // 在小屏幕上的宽度
                                    height: '50px', // 图像的高度与宽度相等，以实现圆形效果
                                    borderRadius: '50%', // 将边框半径设置为50%以创建圆形效果

                                }}
                            />


                            <TextField
                                required
                                label="廠商名"
                                variant="outlined"
                                name="name"
                                value={formData.name}
                                onChange={handleChange}
                                onBlur={handleBlur}

                            />

                        </Stack>

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
                        </Stack>
                        <Divider sx={{ my: 3 }}>

                        </Divider>

                        {/* body */}
                        <Stack direction={"column"} spacing={4}>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>
                                    <TextField
                                        label="負責人"
                                        variant="outlined"
                                        name="principal"
                                        type="text"
                                        value={formData.principal}
                                        required
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                    />

                                </Stack>

                            </Grid>
                            <Divider sx={{ my: 3 }}>
                                聯絡方式
                            </Divider>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>

                                    <TextField
                                        label="信箱"
                                        variant="outlined"
                                        name="email"
                                        value={formData.email}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        required
                                        fullWidth
                                    />

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
                                </Stack>

                            </Grid>
                            <Divider sx={{ my: 3 }}>
                                營業時間
                            </Divider>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>

                                    <TextField
                                        label="開業時間"
                                        variant="outlined"
                                        name="open_time"
                                        type="time" // 设置输入类型为时间
                                        value={formData.open_time}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        InputLabelProps={{
                                            shrink: true, // 让标签缩小，以适应时间输入
                                        }}
                                        required
                                        fullWidth
                                    />
                                    <TextField
                                        label="歇業時間"
                                        variant="outlined"
                                        name="close_time"
                                        type="time"
                                        value={formData.close_time}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        InputLabelProps={{
                                            shrink: true, // 让标签缩小，以适应时间输入
                                        }}
                                        required
                                        fullWidth
                                    />
                                </Stack>

                            </Grid>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>

                                    <TextField
                                        label="休息開始時間"
                                        variant="outlined"
                                        name="rest_open_time"
                                        type="time" // 设置输入类型为时间
                                        value={formData.rest_open_time}
                                        onChange={handleChange}
                                        InputLabelProps={{
                                            shrink: true, // 让标签缩小，以适应时间输入
                                        }}
                                        onBlur={handleBlur}
                                        required
                                        fullWidth
                                    />
                                    <TextField
                                        label="休息結束時間"
                                        variant="outlined"
                                        name="rest_close_time"
                                        type="time"
                                        value={formData.rest_close_time}
                                        onChange={handleChange}
                                        InputLabelProps={{
                                            shrink: true, // 让标签缩小，以适应时间输入
                                        }}
                                        onBlur={handleBlur}
                                        required
                                        fullWidth
                                    />
                                </Stack>

                            </Grid>
                            <Divider sx={{ my: 3 }}>
                                其他
                            </Divider>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>
                                    <TextField
                                        label="每小時最大預購數量"
                                        variant="outlined"
                                        name="preorder_qty"
                                        type="number"
                                        value={formData.preorder_qty}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        fullWidth
                                        required
                                    />

                                </Stack>
                            </Grid>
                            <Divider sx={{ my: 3 }}>
                                優惠標語
                            </Divider>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2}>
                                    <TextField
                                        label="優惠內容"
                                        variant="outlined"
                                        name="promotions"
                                        type="text"
                                        value={formData.promotions}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        fullWidth
                                        required
                                    />

                                </Stack>
                            </Grid>


                            <Divider sx={{ my: 3 }}>
                                連結
                            </Divider>

                            <Grid container spacing={2}>
                                <Grid item xs={12} sm={6} md={4} >
                                    <div>
                                        <Stack direction="row" sx={{ '& > *:not(:last-child)': { marginRight: 1 } }} >
                                            {/* ig */}
                                            <Iconify icon="icon-park:web-page" width={55} />
                                            <TextField
                                                label="餐廳外部連結"
                                                variant="outlined"
                                                name="shop_url"
                                                type="url"
                                                value={formData.shop_url}
                                                onChange={handleChange}
                                                onBlur={handleBlur}
                                                required
                                                fullWidth
                                            />

                                        </Stack>
                                    </div>

                                </Grid>
                                <Grid item xs={12} sm={6} md={4} >
                                    <div>
                                        <Stack direction="row" sx={{ '& > *:not(:last-child)': { marginRight: 1 } }} >
                                            {/* ig */}
                                            <Iconify icon="skill-icons:instagram" width={55} />
                                            <TextField
                                                label="餐廳ig連結"
                                                variant="outlined"
                                                name="ig_url"
                                                type="url"
                                                value={formData.ig_url}
                                                onChange={handleChange}
                                                onBlur={handleBlur}
                                                required
                                                fullWidth
                                            />

                                        </Stack>
                                    </div>

                                </Grid>

                                <Grid item xs={12} sm={6} md={4} >
                                    <div>
                                        <Stack direction="row" sx={{ '& > *:not(:last-child)': { marginRight: 1 } }} >
                                            {/* ig */}
                                            <Iconify icon="logos:facebook" width={55} />
                                            <TextField
                                                label="餐廳fd連結"
                                                variant="outlined"
                                                name="fd_url"
                                                type="url"
                                                value={formData.fd_url}
                                                onChange={handleChange}
                                                onBlur={handleBlur}
                                                required
                                                fullWidth
                                            />

                                        </Stack>
                                    </div>

                                </Grid>
                            </Grid>
                            <Divider sx={{ my: 3 }}>
                                參數
                            </Divider>

                            <Grid item xs={12} sm={6} md={3} >
                                <Stack direction="row" spacing={2}>
                                    <TextField
                                        label="每小時最大預購數量"
                                        variant="outlined"
                                        name="preorder_qty"
                                        type="url"
                                        value={formData.preorder_qty}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        required
                                        sx={{ width: '100%' }} // 设置宽度为100%
                                    />
                                </Stack>
                            </Grid>




                            <Divider sx={{ my: 3 }}>
                                校區
                            </Divider>
                            <Grid item xs={12} sm={6} md={3}>
                                <Stack direction="row" spacing={2} >

                                    <Select
                                        required
                                        value={formData.campus_name || '建功校區'}
                                        onChange={handleChange}
                                        onBlur={handleBlur}
                                        fullWidth
                                    >
                                        <MenuItem value={'建功校區'}>建功校區</MenuItem>
                                        <MenuItem value={'第一校區'}>第一校區</MenuItem>
                                        <MenuItem value={'燕巢校區'}>燕巢校區</MenuItem>
                                    </Select>

                                </Stack>

                            </Grid>
                        </Stack>
                    </Container >
                </DemoPaper >
            )
        }
    </>);
}