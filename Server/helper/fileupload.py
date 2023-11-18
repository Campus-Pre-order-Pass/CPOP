import shutil
import os
from django.core.files.storage import FileSystemStorage


def upload_file(request, vendor_id, filename):
    if request.method == 'POST' and request.data["file"]:
        # 获取上传的图片文件
        uploaded_file = request.data["file"]

        # 检查文件是否有效
        if uploaded_file:
            # 构造保存路径
            vendor_image_path = os.path.join(
                "static", 'vendor', vendor_id, filename)

            # 如果文件已经存在，删除旧文件
            if os.path.exists(vendor_image_path):
                os.remove(vendor_image_path)

            # 将文件保存到静态文件夹
            fs = FileSystemStorage()
            fs.save(vendor_image_path, uploaded_file)

            # 返回成功响应
            return True

    # 返回失败响应
    return False


def delete_folder(folder_path):
    try:
        # 使用 shutil.rmtree 删除整个文件夹及其内容
        shutil.rmtree(folder_path)
        return True
    except Exception as e:
        # 处理删除文件夹时可能发生的异常
        print(f"删除文件夹失败：{str(e)}")
        return False
