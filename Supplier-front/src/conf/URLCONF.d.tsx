const http = "http";
const ip = "localhost";
const port = "8000";
const v = "v0";
const BaseApiUrl = `${http}://${ip}:${port}/${v}/api`;
const BaseUrl = `${http}://${ip}:${port}`;

function RegisterUrl(uid: string) {
  return `${BaseApiUrl}/auth/vendor/${uid}`;
}

function MenuUrl(uid: string) {
  return `${BaseApiUrl}/shop/menu/${uid}`;
}
function FileUrl(uid: string) {
  return `${BaseApiUrl}/shop/file/${uid}`;
}

function CurrentStateUrl(uid: string) {
  return `${BaseApiUrl}/shop/current/${uid}`;
}

function TrackUrl(uid: string) {
  return `${BaseApiUrl}/track/merchant/${uid}`;
}
const OrtherUrl = { FileUrl };

const URLCONF = {
  BaseUrl,
  BaseApiUrl,
  RegisterUrl,
  MenuUrl,
  OrtherUrl,
  CurrentStateUrl,
  TrackUrl,
};

export default URLCONF;
