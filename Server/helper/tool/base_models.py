from django.db import models
from datetime import date


class BaseStatusModel(models.Model):
    @classmethod
    def get_today_status(cls, vendor_id: int) -> any:
        today = date.today()

        try:
            # 尝试获取当天的商店状态记录
            status = cls.objects.get(id=vendor_id, date=today)
        except cls.DoesNotExist as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.get_today_status")
        except Exception as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.get_today_status")

        return status

    class Meta:
        abstract = True
