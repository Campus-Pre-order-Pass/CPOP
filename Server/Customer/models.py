from django.db import models

from django.contrib.auth.models import Group
# Create your models here.

class Customer(models.Model):
    """Customer model"""
    uid = models.CharField(max_length=255, unique=True, verbose_name="唯一識別碼")
    name = models.CharField(max_length=255, verbose_name="姓名")
    contact = models.CharField(
        max_length=15, null=True, blank=True, verbose_name="聯絡電話")
    email = models.EmailField(
        max_length=255, unique=True, null=True, blank=True, verbose_name="電子郵件")
    
    # whitelist_groups = models.ManyToManyField(Group, related_name='whitelist_users' , verbose_name="白名單" , help_text="黑名單")
    # blacklist_groups = models.ManyToManyField(Group, related_name='blacklist_users'  , verbose_name="黑名單"  ,help_text="黑名單")

    created_at = models.DateTimeField(auto_now_add=True, verbose_name="創建時間")

    class Meta:
        verbose_name = "顧客"
        verbose_name_plural = "顧客列表"

    def __str__(self):
        return "%s | %s" % (self.name, self.uid)
    
    
class CustomerGroupMembership(models.Model):
    uid = models.CharField(max_length=255, unique=True, verbose_name="唯一識別碼")
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='customer_memberships' ,verbose_name="群組")
    class Meta:
        verbose_name = "顧客群組"
        verbose_name_plural = "顧客群組"

    def __str__(self):
        return "%s | %s" % (self.uid, self.group)
