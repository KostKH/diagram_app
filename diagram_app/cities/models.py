from django.db import models


class City(models.Model):
    """Класс City создает БД SQL для хранения списка городов."""

    name = models.CharField(
        verbose_name='Название города',
        unique=True,
        blank=False,
        max_length=60,
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.name


class PlanFact(models.Model):
    """Класс Plan создает БД SQL для хранения плановых
    и фактических данных."""

    year = models.PositiveSmallIntegerField(
        verbose_name='Год',
    )
    plan = models.PositiveSmallIntegerField(
        verbose_name='План',
        default=0,
    )
    fact = models.PositiveSmallIntegerField(
        verbose_name='Факт',
        default=0,
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        related_name='plan',
        verbose_name='Город: план',
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['city', 'year'],
                name='unique_city_year'
            )
        ]
        ordering = ('id',)

    def __str__(self):
        return f'{self.city}_{self.year}_{self.plan}_{self.fact}'
