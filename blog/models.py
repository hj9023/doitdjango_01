from django.db import models


# Create your models here.
class Post(models.Model):
    objects = None
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='blog/images/%Y/%m/%d/',blank=True)
    file_upload = models.FileField(upload_to='blog/files/%Y/%m/%d/', blank=True)
    # 현재시간을 새로 작성할 때 바로 넣기
    created_at = models.DateTimeField(auto_now_add=True)
    # 수정시간 업데이트
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'[{self.pk}]{self.title}'


    def get_absolute_url(self):
        return f'/blog/{self.pk}'