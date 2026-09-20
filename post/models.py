from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок', help_text='Введите заголовок поста')
    content = models.TextField( verbose_name='Содержание', help_text='Введите текст поста')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')  #auto_now_add - фиксирует один раз дату при создании, при обновлении записи значение не обновляется
    update_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления') #auto_now - фиксирует дату каждый раз при обновлении записи
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='posts', null=True, blank=True) # может быть пустым # user.posts.all() # может быть null

    def __str__(self):
        return self.title 
    
    class Meta:
        # для того, чтобы в админке модель читалась
        verbose_name = 'Пост' # ед.число
        verbose_name_plural = 'Посты' # мн.число
        ordering = ['-created_at'] # сортировка по полю дата создания, новые сверху
        
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments') #post.comments.all()
    text = models.TextField(verbose_name='Текст комментария')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', related_name='comments') #user.comments.all() 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f'Комментарий от {self.author} к "{self.post.title}"'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментаии'
        ordering = ['-created_at']