# 在您的应用的 views.py 文件中

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import CSPReport


@csrf_exempt
def handle_csp_report(request):
    if request.method == 'POST':
        # 从请求中提取报告数据
        report_data = request.body.decode('utf-8')

        # 在这里解析报告数据并将其保存到数据库
        # 这只是一个示例，实际上您可能需要使用 JSON 解析器或其他方法来处理报告数据
        CSPReport.objects.create(document_uri=report_data.get('document_uri'),
                                 referrer=report_data.get('referrer'),
                                 blocked_uri=report_data.get('blocked_uri'))
        return HttpResponse(status=204)

    return HttpResponse(status=400)  # 非 POST 请求返回 400 Bad Request
