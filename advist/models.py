from django.db import models
from django.utils import timezone


# Create your models here.
class Advistments(models.Model):
    title = models.CharField(max_length=40, verbose_name='Товар')
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True,
                    verbose_name='Цена товара')
    published = models.DateTimeField(auto_now_add=True, db_index=True)
    rubric = models.ForeignKey('Rubric', null=True,
                               on_delete=models.PROTECT, verbose_name='Рубрика')
    class Meta:
        verbose_name_plural = 'Обьявления'
        verbose_name = 'Обьявление'
        ordering = ['-published']

    def __str__(self):
        return self.title


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
                            verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']

