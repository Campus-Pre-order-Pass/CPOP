import os
from PIL import Image, ImageDraw, ImageFont
from escpos.printer import Network

printer_ip = '10.0.0.11'
printer_port = 1000
width = 600
font_size = 50
script_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(script_dir)
logo_folder = os.path.join(parent_dir, 'Logo')
font_folder = os.path.join(parent_dir, 'Font')
save_folder = os.path.join(parent_dir, 'Temp')
logo_path = os.path.join(logo_folder, '666.png')
font_path = os.path.join(font_folder, 'test2.TTF')
logo_image = Image.open(logo_path)
logo_width, logo_height = logo_image.size

order_details = [
    ["時間: ", "11-05 10:30",""],
    ["平台: ", "346",""],
    ["總金額: ", "1000",""],
    ["波士頓龍蝦蛋餅", "1",""],
    ["雙色吐司", "1","巧克力/奶酥"],
    ["鍋燒意麵", "1","加蛋"],
    ["紅茶", "1","去冰"]    
]
line_height = 55
table_width = 400
image_height = logo_height + 40 + (len(order_details) + 1) * line_height + 50
background_color = (255, 255, 255)
image = Image.new('RGB', (width, image_height), background_color)
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_path, font_size)
image_x = (width - logo_width) // 2
image_y = 0
image.paste(logo_image, (image_x, image_y))

time_text = order_details[0][0] + order_details[0][1]
x = (width - table_width) // 2
y = image_y + logo_height
draw.text((x-50, y), time_text, fill=(0, 0, 0), font=font)
y += 2 * line_height - 10

number_text = order_details[1][0] + order_details[1][1]
draw.text((x-50, y-40), number_text, fill=(0, 0, 0), font=font)

title_row = ["項目", "數量"]
x = (width - table_width) // 2
y += 2 * line_height - 50 -20

cell_x_positions = [x-50, x+300, x-30]

for i, title in enumerate(title_row):
    cell_x = cell_x_positions[i]
    line_text = title
    draw.text((cell_x, y -20 ), line_text, fill=(0, 0, 0), font=font)
y += line_height - 20 

for detail in order_details[3:99]:
    for i, cell in enumerate(detail):
        cell_x = cell_x_positions[i]
        line_text = cell
        if(line_text and  i ==2) :
            y += 42
            font = ImageFont.truetype(font_path, font_size-24)
            draw.text((cell_x, y), line_text, fill=(0, 0, 0), font= font)
            y -= 38
        else:
            y -= 4
            font = ImageFont.truetype(font_path, font_size-10)
            draw.text((cell_x, y), line_text, fill=(0, 0, 0), font= font)
    y += line_height + 10
font = ImageFont.truetype(font_path, font_size)

total_text = order_details[2][0] + order_details[2][1]
y += line_height
draw.text((x + 30, y), total_text, fill=(0, 0, 0), font=font)

str = order_details[1][1] + ".jpg" 
save_path = os.path.join(save_folder, str)
image.save(save_path)
image.show()
printer = Network(host=printer_ip, port=printer_port)
printer.codepage = 'CP950'
printer.image(save_path)
printer.cut()
printer.close()
