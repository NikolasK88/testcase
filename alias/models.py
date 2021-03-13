from django.db import models


class Alias(models.Model):
    alias = models.TextField(verbose_name="Alias", null=True, blank=True)
    target = models.CharField(max_length=24, verbose_name='Slug', null=True,
                              blank=True)
    start = models.DateTimeField(verbose_name="Start", null=True, blank=True)
    end = models.DateTimeField(verbose_name="End", default=None, null=True,
                               blank=True)

    class Meta:
        verbose_name = "Alias"
        verbose_name_plural = "Alias"

    def __str__(self):
        return str(f'Alias: {self.id}')
