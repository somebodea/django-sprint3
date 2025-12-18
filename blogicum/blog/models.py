from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()


class PublishedAndCreated(models.Model):
    is_published = models.BooleanField(
        default=True,
        blank=False,
        verbose_name="Опубликовано",
        help_text="Снимите галочку, чтобы скрыть публикацию."
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        blank=False,
        verbose_name="Добавлено"
    )

    class Meta:
        abstract = True


class Category(PublishedAndCreated):
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Заголовок"
    )
    description = models.TextField(
        blank=False,
        verbose_name="Описание"
    )
    slug = models.SlugField(
        blank=False,
        unique=True,
        verbose_name="Идентификатор",
        help_text="Идентификатор страницы для URL; "
                  "разрешены символы латиницы, "
                  "цифры, дефис и подчёркивание."
    )

    class Meta:
        verbose_name_plural = "Категории"
        verbose_name = "категория"

    def __str__(self):
        return self.title


class Location(PublishedAndCreated):
    name = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Название места"
    )

    class Meta:
        verbose_name_plural = "Местоположения"
        verbose_name = "местоположение"

    def __str__(self):
        return self.name


class Post(PublishedAndCreated):
    title = models.CharField(
        max_length=256,
        blank=False,
        verbose_name="Заголовок"
    )
    text = models.TextField(
        blank=False,
        verbose_name="Текст"
    )
    pub_date = models.DateTimeField(
        blank=False,
        verbose_name="Дата и время публикации",
        help_text="Если установить дату и время в будущем — "
                  "можно делать отложенные публикации."
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=False,
        verbose_name="Автор публикации"
    )
    location = models.ForeignKey(
        Location,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Местоположение"
    )
    category = models.ForeignKey(
        Category,
        blank=False,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="Категория"
    )

    class Meta:
        verbose_name_plural = "Публикации"
        verbose_name = "публикация"

    def __str__(self):
        return self.title
