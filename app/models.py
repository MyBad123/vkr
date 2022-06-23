from operator import mod
from django.db import models


class ProductModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя продукта')
    price = models.IntegerField(verbose_name='Цена продукта')
    number = models.IntegerField(verbose_name='Количество продукта')
    about = models.TextField(verbose_name='Описание продукта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductPhotoModel(models.Model):
    photo = models.ImageField(upload_to='uploads/', verbose_name='Фото продукта')
    product = models.ForeignKey(ProductModel, on_delete=models.CASCADE, verbose_name='Продукт')

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фото'


class QuestionModel(models.Model):
    question = models.TextField(verbose_name='Вопрос')
    responce = models.TextField(verbose_name='Ответ')

    class Meta:
        verbose_name = 'Вопросы и ответы'
        verbose_name_plural = 'Вопросы и ответы'


class MailModel(models.Model):
    mail = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name = 'Почта'
        verbose_name_plural = 'Почта'


class СommunicationModel(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    phone = models.CharField(max_length=200, verbose_name='Телефон')
    mail = models.EmailField(verbose_name='Почта')
    text = models.TextField(verbose_name='Текст')

    class Meta:
        verbose_name = 'Связь'
        verbose_name_plural = 'Связь'
