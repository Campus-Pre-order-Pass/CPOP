from django.conf import settings
from Customer.models import CustomerGroupMembership
from django.http import HttpResponseServerError

def is_in_group(user, group_name):
    return user.groups.filter(name=group_name).exists()



def is_whitelisted(request):
    try:
        path_parts = request.path.split('/')
        uid = path_parts[-1]

        # 使用Django的ORM查询检查uid是否在白名单群组中
        is_whitelisted_customer = CustomerGroupMembership.objects.filter(uid=uid, group__name='WhitelistGroup').exists()

        # 打印或使用结果
        # print(is_whitelisted_customer)

        return is_whitelisted_customer
    except Exception as e:
        # 处理异常，例如打印错误信息
        print(f"Exception in is_whitelisted: {e}")
        # 返回一个适当的 HTTP 响应，例如 500 Internal Server Error
        return HttpResponseServerError("Internal Server Error")


def is_not_blacklisted(user):
    """_summary_
        >>> @user_passes_test(is_whitelisted)
        >>> def your_whitelisted_view(request):

    Args:
        user (_type_): _description_

    Returns:
        _type_: _description_
    """
    return not is_in_group(user, 'BlacklistGroup')

# @user_passes_test(is_whitelisted)
# def your_whitelisted_view(request):
#     # 此處為具有白名單權限的用戶的處理邏輯

# @user_passes_test(is_not_blacklisted)
# def your_blacklist_view(request):
#     # 此處為不在黑名單的用戶的處理邏輯
