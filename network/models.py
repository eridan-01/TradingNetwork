from django.db import models
from users.models import NULLABLE


class NetworkNode(models.Model):
    LEVELS = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(
        max_length=255,
        verbose_name='Название организации',
        help_text='Введите название организации'
    )

    email = models.EmailField(
        verbose_name='Email',
        help_text='Введите вашу электронную почту'
    )

    country = models.CharField(
        max_length=100,
        verbose_name='Страна',
        help_text='Введите страну'
    )

    city = models.CharField(
        max_length=100,
        verbose_name='Город',
        help_text='Введите город'
    )

    street = models.CharField(
        max_length=100,
        verbose_name='Улица',
        help_text='Введите улицу'
    )

    house_number = models.CharField(
        max_length=10,
        verbose_name='Номер дома',
        help_text='Введите номер дома'
    )

    product_name = models.CharField(
        max_length=255,
        verbose_name='Название продукта',
        help_text='Введите название продукта'
    )

    product_model = models.CharField(
        max_length=255,
        verbose_name='Модель продукта',
        help_text='Введите модель продукта'
    )

    product_release_date = models.DateField(
        verbose_name='Дата выпуска продукта',
        help_text='Введите дату выпуска продукта'
    )

    supplier = models.ForeignKey(
        'self',
        **NULLABLE,
        on_delete=models.SET_NULL,
        related_name='clients',
        verbose_name='Поставщик',
        help_text='Выберите поставщика'
    )

    debt = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Долг',
        help_text='Введите текущий долг'
    )

    level = models.IntegerField(
        choices=LEVELS,
        verbose_name='Уровень организации',
        help_text='Выберите уровень организации'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания',
        help_text='Время создания записи'
    )

    class Meta:
        verbose_name = 'Торговая сеть'
        verbose_name_plural = 'Торговые сети'

    def __str__(self):
        return self.name

