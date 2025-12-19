from django.contrib.auth import get_user_model
from django.db import models

from .constants import MAX_TITLE_LENGTH


User = get_user_model()


class AbstractPublished(models.Model):
    is_published = models.BooleanField(
        "Опубликовано",
        default=True,
        help_text="Снимите галочку, чтобы скрыть публикацию."
    )
    created_at = models.DateTimeField(
        "Добавлено",
        auto_now_add=True,
    )

    class Meta:
        abstract = True


class Category(AbstractPublished):
    title = models.CharField(
        "Заголовок",
        max_length=MAX_TITLE_LENGTH,
    )
    description = models.TextField(
        "Описание"
    )
    slug = models.SlugField(
        "Идентификатор",
        unique=True,
        help_text="Идентификатор страницы для URL; "
                  "разрешены символы латиницы, "
                  "цифры, дефис и подчёркивание."
    )

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "категория"

    def __str__(self):
        return self.title[:20]


class Location(AbstractPublished):
    name = models.CharField(
        "Название места",
        max_length=MAX_TITLE_LENGTH,
    )

    class Meta:
        verbose_name_plural = "Местоположения"
        verbose_name = "местоположение"

    def __str__(self):
        return self.name[:20]


class Post(AbstractPublished):
    title = models.CharField(
        "Заголовок",
        max_length=MAX_TITLE_LENGTH,
    )
    text = models.TextField(
        "Текст"
    )
    pub_date = models.DateTimeField(
        "Дата и время публикации",
        help_text="Если установить дату и время в будущем — "
                  "можно делать отложенные публикации."
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
        related_name='posts',
        verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name="Местоположение"
    )
    category = models.ForeignKey(
        Category,
        null=True,
        on_delete=models.SET_NULL,
        related_name='posts',
        verbose_name="Категория"
    )

    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "публикация"
        ordering = ['-pub_date']

    def __str__(self):
        return self.title[:20]
