
from jinja2 import Template
import os

# 读取模板文件
template_path = 'drf_template.jinja'
with open(template_path, 'r') as file:
    template_content = file.read()

# 创建 Jinja2 模板对象
template = Template(template_content)

# 定义模板中的变量
drf_imports = 'from rest_framework.views import APIView\n'
mark_imports = 'from Order.OrderLogic.test.mark import MarkData\n'
base_config_imports = 'from helper.base.drf_yasg_base import BaseAPIViewDRFConfig\n'
serializer_imports = 'from Order.serializers import OrderItemSerializer, OrderRequestBodySerializer, OrderSerializer\n'
uid_param_name = 'uid'
uid_param_description = '顧客 `UID`'
uid_param_example = 'test'
base_class = 'BaseAPIViewDRFConfig'  # 可以根据实际情况更改

drf_methods = '''
def get(self, request, uid):
    # Your GET method logic here
    pass

def post(self, request, uid):
    # Your POST method logic here
    pass
'''

# 渲染模板
rendered_code = template.render(
    drf_imports=drf_imports,
    mark_imports=mark_imports,
    base_config_imports=base_config_imports,
    serializer_imports=serializer_imports,
    uid_param_name=uid_param_name,
    uid_param_description=uid_param_description,
    uid_param_example=uid_param_example,
    base_class=base_class,
    drf_methods=drf_methods,
)

# 确定生成代码的保存路径
output_path = 'generated_drf.py'

# 将生成的代码写入文件
with open(output_path, 'w') as output_file:
    output_file.write(rendered_code)

print(f"DRF code generated successfully. Saved to {output_path}")
