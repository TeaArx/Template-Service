from django.db import models
import uuid


class ApplicationType(models.Model):
    """Класс, описывающий тип заявки"""

    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    name = models.CharField(verbose_name="Названия заявки", max_length=250)

    class Meta:
        verbose_name = "Типы заявок"
        verbose_name_plural = "Типы заявок"

    def __str__(self):
        return self.name


class Pattern(models.Model):
    """Класс, описывающий шаблон"""

    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4, unique=True
    )
    name = models.CharField(verbose_name="Наименования шаблона", max_length=250)
    activity = models.BooleanField(verbose_name="Активность шаблона")
    notes = models.TextField(verbose_name="Премечания заявки", blank=True)
    pattern = models.JSONField(verbose_name="Шаблон заявки", blank=True)
    application_type = models.ForeignKey(
        ApplicationType, on_delete=models.PROTECT, verbose_name="Тип заявки"
    )

    class Meta:
        verbose_name = "Шаблон"
        verbose_name_plural = "Шаблоны"

    def __str__(self):
        return self.name
