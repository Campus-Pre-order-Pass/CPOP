# import datetime
# from django.db import models
# from django.core.exceptions import ValidationError
# from django.db.models import UniqueConstraint


# from .validators import non_negative_validator

# # models that
# from Shop.vendor import Vendor
# from Shop.models.menuItem import MenuItem

# # Mixin包含TotalUsers和DailyNewUsers的字段和方法


# class CountModelMixin(models.Model):
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator])
#     date = models.DateField()

#     class Meta:
#         abstract = True

#     def __str__(self):
#         return f'{self._meta.verbose_name} Count for {self.date}'

#     @classmethod
#     def increase_count(cls, v: Vendor, current_date):
#         obj, created = cls.objects.get_or_create(
#             vendor=v, date=current_date, defaults={'count': 0}
#         )
#         obj.count += 1
#         obj.save()
#         return obj

#     @classmethod
#     def get_quarter_start_date(cls, date):
#         # 计算日期所属的季度的开始日期
#         quarter_month = ((date.month - 1) // 3) * 3 + 1
#         return datetime.date(date.year, quarter_month, 1)

#     @classmethod
#     def increase_total_count(cls, v: Vendor, current_date):
#         # 计算季度开始日期
#         quarter_start_date = cls.get_quarter_start_date(current_date)

#         # 使用供应商、季度开始日期来查找或创建对象
#         obj, created = cls.objects.get_or_create(
#             vendor=v, date=quarter_start_date, defaults={'count': 0}
#         )
#         obj.count += 1
#         obj.save()
#         return obj

#     # money =================================================================

#     @classmethod
#     def increase_money(cls, v: Vendor, money, current_date):
#         obj, created = cls.objects.get_or_create(
#             vendor=v, date=current_date, defaults={'count': 0}
#         )
#         obj.count += money
#         obj.save()

#     @classmethod
#     def increase_total_money(cls, v: Vendor, money,  current_date):
#         # 计算季度开始日期
#         quarter_start_date = cls.get_quarter_start_date(current_date)

#         # 使用供应商、季度开始日期来查找或创建对象
#         obj, created = cls.objects.get_or_create(
#             vendor=v, date=quarter_start_date, defaults={'count': 0}
#         )
#         obj.count += money
#         obj.save()
#         return obj

# # TotalUsers和DailyNewUsers继承CountModelMixin


# class TotalUsers(CountModelMixin):
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='total_users_count')

#     def __str__(self):
#         return f'Total Users Count for {self.date}'


# class DailyNewUsers(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='daily_new_users')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='daily_new_users_count')

#     class Meta:
#         verbose_name = "新使用者"
#         verbose_name_plural = "新使用者"

#     def __str__(self):
#         return f'Daily New Users Count for {self.date}'


# class ActiveUsers(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='active_users')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='active_users_count')

#     def __str__(self):
#         return f'Active Users Count for {self.date}'


# class DailyActiveUsers(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='daily_active_users')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='daily_active_users_count')

#     def __str__(self):
#         return f'Daily Active Users Count for {self.date}'

# # order


# class TotalOrders(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='total_orders')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='total_orders_count')

#     def __str__(self):
#         return f'Total Orders Count for {self.date}'


# class DailyOrders(CountModelMixin):

#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='daily_total_orders')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='daily_total_orders_count')

#     class Meta:
#         verbose_name = "訂單數"
#         verbose_name_plural = "訂單數"

#     def __str__(self):
#         return f'Daily Orders Count for {self.date}'

# # money


# class TotalSales(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='total_sales')
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='total_sales_count')

#     def __str__(self):
#         return f'Total Sales Count for {self.date}'


# class DailySales(CountModelMixin):
#     vendor = models.ForeignKey(
#         Vendor, on_delete=models.CASCADE, related_name='daily_sales')

#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='daily_sales_count')

#     class Meta:
#         verbose_name = "銷售額"
#         verbose_name_plural = "銷售額"

#     def __str__(self):
#         return f'Daily Sales Count for {self.date}'

# # views


# class VisitsandPageViews(models.Model):
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator], verbose_name='visitsandPageViews_count')
#     date = models.DateField(unique=True)

#     class Meta:
#         verbose_name = "瀏覽人數"
#         verbose_name_plural = "瀏覽人數"

#     def __str__(self):
#         return f'Visits and Page Views Count for {self.date}'


# class ConversionRate(models.Model):
#     conversion_rate = models.DecimalField(max_digits=5, decimal_places=2)
#     date = models.DateField(unique=True)

#     def __str__(self):
#         return f'Conversion Rate for {self.date}'

# # 圓餅圖


# class MostPopularStore(models.Model):
#     vendor = models.OneToOneField(
#         Vendor, on_delete=models.CASCADE, related_name='most_popular', primary_key=True,  default="")
#     count = models.PositiveIntegerField(
#         default=0, validators=[non_negative_validator])
#     date = models.DateField(unique=True)

#     def __str__(self):
#         return f'Most Popular Store for {self.Vendor.name} on {self.date}'


# # Dashbroad使用CountModelMixin来共享字段和方法


# class Dashbroad(CountModelMixin):
#     pass
