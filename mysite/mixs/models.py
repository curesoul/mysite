from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Customer(models.Model):
    abbreviation = models.CharField(max_length=10, verbose_name='缩写')
    name = models.CharField(max_length=255, verbose_name='公司名称')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '客户'


class Operator(models.Model):
    username = models.OneToOneField(User, on_delete=models.PROTECT)
    name = models.CharField(max_length=50, blank=True, verbose_name='姓名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '操作员'


class Item(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT, verbose_name='客户')
    name = models.CharField(max_length=255, verbose_name='品名')
    mv = models.CharField(max_length=255, verbose_name='门尼')
    mv_min = models.FloatField(verbose_name='最小值')
    mv_max = models.FloatField(verbose_name='最大值')
    temperature = models.IntegerField(default=100, blank=True, verbose_name='温度')
    rotor = models.CharField(max_length=255, default='ML 1+4', verbose_name='转子')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = verbose_name_plural = '品名清单'


class Lot(models.Model):
    lot = models.IntegerField(verbose_name='批号')

    def __str__(self):
        return str(self.lot)

    class Meta:
        verbose_name = verbose_name_plural = '批号'


class ProductionPlan(models.Model):
    item = models.ForeignKey(Item, on_delete=models.PROTECT, verbose_name='品名')
    lot = models.ForeignKey(Lot, on_delete=models.PROTECT, verbose_name='批号')
    created = models.DateField(blank=True, verbose_name='出表时间')

    def __str__(self):
        return str(self.lot.lot) + ' - ' + self.item.name

    def mv_value(self):
        return self.item.mv

    class Meta:
        verbose_name = verbose_name_plural = '素炼成绩表'


class Detail(models.Model):
    plan = models.ForeignKey(ProductionPlan, on_delete=models.PROTECT)
    batch = models.IntegerField(verbose_name='回数')
    mv = models.FloatField(verbose_name='门尼值')
    comment = models.CharField(max_length=255, blank=True, verbose_name='回炼')
    shipment_status = models.BooleanField(default=False, verbose_name='出货状态')

    def __str__(self):
        return str(self.plan)

    class Meta:
        verbose_name = verbose_name_plural = '详细信息'


class DetailChangeLog(models.Model):
    detail = models.ForeignKey(Detail, on_delete=models.PROTECT)
    changed_log = models.CharField(max_length=255, verbose_name='变更记录')

    # def save(self):
