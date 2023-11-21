from escpos.printer import Network
from PIL import Image

# 替换成你的网络打印机的IP地址和端口

# printer_ip = '192.168.123.100'
# printer_port = 9100

printer_ip = '10.0.0.11'
printer_port = 1000

# 创建网络打印机对象
printer = Network(host=printer_ip, port=printer_port)
printer.codepage = 'CP950'

# 打印图片
image_path = 'order_info.jpg'
printer.image(image_path)

# 切纸（如果支持）
printer.cut()

# 关闭连接
printer.close()
