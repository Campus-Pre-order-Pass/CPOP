import os
from PIL import Image, ImageDraw, ImageFont
from escpos.printer import Network


class OrderInvoiceGenerator:

    # 初始化
    def __init__(self, IP):
        self.printer_ip = IP
        self.width = 600
        self.font_size = 50
        self.line_height = 55
        self.table_width = 400
        self.background_color = (255, 255, 255)
        self.y_position = 0
        script_dir = os.path.dirname(os.path.abspath(__file__))
        self.logo_folder = os.path.join(script_dir, 'Logo')
        self.font_folder = os.path.join(script_dir, 'Font')
        self.save_folder = os.path.join(script_dir, 'Temp')
        self.font_path = os.path.join(self.font_folder, 'test2.TTF')
        self.font = ImageFont.truetype(self.font_path, self.font_size)

    # 生成發票
    def generate_invoice(self, shop, order_details, print_invoice=False, show_invoice=False):
        self.order_details = order_details
        self.draw_init(shop)
        self.draw_logo()
        self.draw_order_time()
        self.draw_order_number()
        self.draw_table_header()
        self.draw_order_information()
        self.draw_total_amount()
        self.save_invoice()
        if show_invoice:
            self.show_invoice()
        if print_invoice:
            self.print_invoice()

    # 店家設定
    def draw_init(self, shop):
        # 根據店家選擇設定相應的印表機和標誌
        self.set_shop_configuration(shop)
        # 圖片和字型初始化
        self.logo_image = Image.open(self.logo_path)
        self.logo_width, self.logo_height = self.logo_image.size
        self.image_height = (
            self.logo_height
            + 40
            + (len(self.order_details) + 1) * self.line_height
            + 15
        )
        self.image = Image.new(
            'RGB', (self.width, self.image_height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)
        filename = self.order_details[1][1] + ".jpg"
        self.save_path = os.path.join(self.save_folder, filename)

    # 畫店家標誌
    def draw_logo(self):
        image_x = (self.width - self.logo_width) - 50
        self.y_position = 0
        self.image.paste(self.logo_image, (image_x, self.y_position))

    # 畫訂單時間
    def draw_order_time(self):
        time_text = self.order_details[0][0] + self.order_details[0][1]
        x = (self.width - self.table_width) - 150
        self.y_position = self.logo_height + 2 * self.line_height - 100 - 10
        self.draw.text((x, self.y_position), time_text,
                       fill=(0, 0, 0), font=self.font)

    # 畫訂單編號
    def draw_order_number(self):
        number_text = self.order_details[1][0] + self.order_details[1][1]
        x = (self.width - self.table_width) - 150
        self.y_position = self.logo_height + 2 * self.line_height - 50 - 10
        self.draw.text((x, self.y_position), number_text,
                       fill=(0, 0, 0), font=self.font)

    # 畫訂單表頭
    def draw_table_header(self):
        title_row = ["項目", "數量"]
        x = (self.width - self.table_width)
        self.y_position = self.logo_height + 4 * self.line_height - 50 - 20
        cell_x_positions = [x - 50, x + 300, x - 30]
        for i, title in enumerate(title_row):
            cell_x = cell_x_positions[i]
            line_text = title
            self.draw.text((cell_x-100, self.y_position - 50),
                           line_text, fill=(0, 0, 0), font=self.font)
        self.y_position += self.line_height - 20

    # 畫訂單詳細信息
    def draw_order_information(self):
        x = (self.width - self.table_width)
        cell_x_positions = [x - 50, x + 300, x - 30]
        for detail in self.order_details[3:99]:
            for i, cell in enumerate(detail):
                cell_x = cell_x_positions[i]
                line_text = cell
                if line_text and i == 2:  # 內容
                    self.y_position += 42
                    font = ImageFont.truetype(
                        self.font_path, self.font_size - 24)
                    self.draw.text((cell_x-100, self.y_position-20),
                                   line_text, fill=(0, 0, 0), font=font)
                    self.y_position -= 38
                else:  # 備註
                    self.y_position -= 4
                    font = ImageFont.truetype(
                        self.font_path, self.font_size - 10)
                    self.draw.text((cell_x-90, self.y_position-20),
                                   line_text, fill=(0, 0, 0), font=font)
            self.y_position += self.line_height + 10

    # 畫總金額
    def draw_total_amount(self):
        total_text = self.order_details[2][0] + self.order_details[2][1]
        self.y_position += self.line_height
        x = (self.width - self.table_width)
        self.draw.text((x-40, self.y_position-50), total_text,
                       fill=(0, 0, 0), font=self.font)

    # 儲存發票
    def save_invoice(self):
        self.image.save(self.save_path)

    # 顯示發票
    def show_invoice(self):
        self.image.show()

    # 列印發票
    def print_invoice(self):
        printer = Network(host=self.printer_ip, port=self.printer_port)
        printer.codepage = 'CP950'
        printer.image(self.save_path)
        printer.cut()
        printer.close()

    # 根據店家設定印表機和標誌
    def set_shop_configuration(self, shop):
        if shop == "A":
            print("好吃A!")
            self.printer_port = 1000
            self.logo_path = os.path.join(self.logo_folder, 'bbb.png')
        elif shop == "B":
            print("好吃B!")
            self.printer_port = 1001
            self.logo_path = os.path.join(self.logo_folder, 'example.png')
        else:
            # 可以添加其他店家的配置
            print("#####未知的店家#####")
            print("#####未知的店家#####")
            print("#####未知的店家#####")


# 使用示例
order_details_example = [
    ["時間: ", "11-05 10:30", ""],
    ["平台: ", "888", ""],
    ["總金額: ", "1000", ""],
    ["波士頓龍蝦蛋餅", "1", ""],
    ["雙色吐司", "1", "巧克力/奶酥"],
    ["紅茶", "1", "去冰"]
]
invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
invoice_generator.generate_invoice(
    shop="A", order_details=order_details_example, print_invoice=False, show_invoice=True)
