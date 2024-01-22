from django.db import models
from django.utils import timezone


class BaseStatusModel(models.Model):
    @classmethod
    def get_today_status(cls, vendor_id: int) -> models.Model:
        today = timezone.now().date()

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

    @classmethod
    def base_get_today_status(cls, id: int, related_models: models.Model):
        today = date.today()
        try:
            m = related_models.objects.get(id=id)
            status = cls.objects.get(related_models=m, date=today)
        except cls.DoesNotExist as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.base_get_today_status")
        except Exception as e:
            raise Exception(
                f"{str(e)} in {cls.__class__.__name__}.base_get_today_status")

        return status

    class Meta:
        abstract = True
