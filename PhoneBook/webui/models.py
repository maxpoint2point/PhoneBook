from django.db import models
from django.contrib.auth.models import User


class Logging(models.Model):
    """Лог действий"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    log = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.user} <{self.log}>'

    class Meta:
        verbose_name = 'Лог действий'
        verbose_name_plural = 'Логи действий'


class Phones(models.Model):
    """Телефоны"""
    name = models.CharField('Имя контакта', max_length=200)
    phone = models.CharField('Телефон', max_length=50, unique=True)
    updated = models.ManyToManyField(Logging, related_name='phones_logging', null=True)

    def __str__(self):
        return f'{self.name} <{self.phone}>'

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
