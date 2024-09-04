from django.db import models
from django.contrib.postgres.fields import ArrayField, DateTimeRangeField
from django.contrib.postgres.indexes import GistIndex
from django.contrib.postgres.constraints import ExclusionConstraint
from django.contrib.postgres.validators import RangeMinValueValidator, RangeMaxValueValidator
from datetime import datetime
from markupfield.fields import MarkupField
from precise_bbcode.fields import BBCodeTextField
from easy_thumbnails.fields import ThumbnailerImageField  # Импортирую миниатюры

class Amenity(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название удобства")
    description = models.TextField(verbose_name="Описание")
    description_bbcode = BBCodeTextField(verbose_name="Описание BBCode", blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")
    # Меняю ImageField на ThumbnailerImageField для поддержки миниатюр
    image = ThumbnailerImageField(upload_to='amenities/', blank=True, null=True, verbose_name="Изображение")
    file = models.FileField(upload_to='amenities/files/', blank=True, null=True, verbose_name="Документ (xlsx/pdf)")
    tags = ArrayField(
        base_field=models.CharField(max_length=50),
        verbose_name="Теги",
        blank=True,
        default=list
    )
    available_times = DateTimeRangeField(
        verbose_name="Доступное время",
        validators=[
            RangeMinValueValidator(datetime(2022, 1, 1)),
            RangeMaxValueValidator(datetime(2030, 12, 31))
        ],
        default=(datetime(2022, 1, 1), datetime(2022, 1, 1))
    )

    class Meta:
        verbose_name = "Удобство"
        verbose_name_plural = "Удобства"
        indexes = [
            GistIndex(fields=['available_times']),
        ]
        constraints = [
            ExclusionConstraint(
                name='exclude_overlapping_times',
                expressions=[
                    ('available_times', '&&'),
                ],
            ),
        ]

    def __str__(self):
        return self.name

class EnhancedAmenity(models.Model):
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE, verbose_name="Основное удобство")
    unique_code = models.CharField(max_length=20, verbose_name="Уникальный код", unique=True)
    vip_service = models.BooleanField(default=False, verbose_name="VIP Услуга")
    additional_features = ArrayField(
        base_field=models.CharField(max_length=100),
        verbose_name="Дополнительные особенности",
        blank=True,
        default=list
    )

    class Meta:
        verbose_name = "Расширенное Удобство"
        verbose_name_plural = "Расширенные Удобства"

    def __str__(self):
        return f"{self.amenity.name} - {self.unique_code}"

