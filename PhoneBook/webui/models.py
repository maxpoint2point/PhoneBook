from django.db import models
from django.contrib.auth.models import User


class Logging(models.Model):
    """Лог действий"""
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now=True)
    log = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.log} [{self.user}]'

    class Meta:
        verbose_name = 'Лог действий'
        verbose_name_plural = 'Логи действий'


class Phones(models.Model):
    """Телефоны"""
    name = models.CharField('Имя контакта', max_length=200)
    phone = models.CharField('Телефон', max_length=50, unique=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    manager = models.CharField("Менеджер", max_length=100, null=True, default=None)

    def save(self, *args, **kwargs):
        if not self.pk:
            log = Logging(
                user=self.user,
                log=f'Create new record {self.__str__()}',
            )
            log.save()
        else:
            log = Logging(
                user=self.user,
                log=f'Change record {self.__str__()}',
            )
            log.save()
        super(Phones, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.name} <{self.phone}>'

    class Meta:
        verbose_name = 'Телефон'
        verbose_name_plural = 'Телефоны'
