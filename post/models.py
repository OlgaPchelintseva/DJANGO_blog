from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', help_text='Введите заголовок поста')
    content = models.TextField( verbose_name='Содержание', help_text='Введите текст поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  #auto_now_add - фиксирует один раз дату при создании, при обновлении записи значение не обновляется
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления') #auto_now - фиксирует дату каждый раз при обновлении записи
    
    def __str__(self):
        return self.title 
    
    class Meta:
        # для того, чтобы в админке модель читалась
        verbose_name = 'Пост' # ед.число
        verbose_name_plural = 'Посты' # мн.число

        ordering = ['-created_at'] # сортировка по полю дата создания, новые сверху
        