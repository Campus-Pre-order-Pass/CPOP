# from order.core.module.base import BaseClass


class Configuration():
    # ok
    SUCESS_CODE = 200

    # format error
    FORMAT_ERROR = 303

    # models error
    MODELS_ERROR = 307
    MODELS_NOT_FOUND = 308

    # 新增与订单验证相关的错误码
    VAILD_ERROR = 399
    BUSINESS_HOURS_ERROR = 400
    INVENTORY_ERROR = 401
    USER_PURCHASE_LIMIT_ERROR = 402
    DAILY_PURCHASE_LIMIT_ERROR = 403

    # 廠商條件error
    VENDOR_VAILD_ERROR = 606

    # general error
    ERROR_CODE = 500

    #  user setting
    MAX_USER_PURCHASE_LIMIT = 2

    # other settings
    NOT_POSIT_ERROR = 501

    # print error
    PRINTER_ERROR = 502


C = Configuration()
