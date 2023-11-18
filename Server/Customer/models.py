from django.db import models

# Create your models here.


class Customer(models.Model):
    """Customer model"""
    uid = models.CharField(max_length=255, unique=True, verbose_name="唯一識別碼")
    name = models.CharField(max_length=255, verbose_name="姓名")
    contact = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="聯絡電話")
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True, verbose_name="電子郵件")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "顧客"
        verbose_name_plural = "顧客列表"

    def __str__(self):
        return self.name
