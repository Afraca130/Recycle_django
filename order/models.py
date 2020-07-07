from django.db import models

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(
        'user.User', verbose_name='사용자', on_delete=models.CASCADE)
    product = models.ForeignKey(
        'product.Product', verbose_name='상품', on_delete=models.CASCADE)
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')


class Meta:
    db_table = 'recycle_product'
    verbose_name = '상품'
    verbose_name_plural = '상품'
