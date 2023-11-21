
# Order Invoice Generator

這是一個訂單發票生成器，    
用於生成、顯示和列印訂單發票。   
可以根據不同店家的配置生成相應的發票。

### 環境
```
pip install escpos
pip install pywin32
pip install Pillow
```

### 範例
初始化 OrderInvoiceGenerator 時需提供印表機的 IP 地址。    
請根據實際情況修改 order_details_example 和 IP 變數。    

```
order_details_example = [
    ["時間: ", "11-05 10:30", ""],
    ["平台: ", "888", ""],
    ["總金額: ", "1000", ""],
    ["波士頓龍蝦蛋餅", "1", ""],
    ["雙色吐司", "1", "巧克力/奶酥"],
    ["紅茶", "1", "去冰"]
]
invoice_generator = OrderInvoiceGenerator(IP="10.0.0.11")
invoice_generator.generate_invoice(shop="A", order_details=order_details_example, print_invoice=False, show_invoice=True)
```

## 解釋
- **generate_invoice**: 生成發票，可選擇是否顯示或列印。
- **show_invoice**: 顯示發票。
- **print_invoice**: 列印發票。


## 設定店家配置
在 set_shop_configuration 方法中，   
根據不同店家的需求配置印表機和標誌。    
```
def set_shop_configuration(self, shop):
    if shop == "A":
        print("唯美食棧")
        self.printer_port = 1000
        self.logo_path = os.path.join(self.logo_folder, 'A001.jpg')
    elif shop == "B":
        print("茶壹")
        self.printer_port = 1001
        self.logo_path = os.path.join(self.logo_folder, 'B001.jpg')
    else:
        # 可以添加其他店家的配置
        print("#####未知的店家#####")
        print("#####未知的店家#####")
        print("#####未知的店家#####")
        print("#####未知的店家#####")
        print("#####未知的店家#####")
```

## 貢獻
歡迎提供建議和改進！請隨時發送問題或拉取請求。


