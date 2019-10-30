from django.db import models


# Create your models here.
class Topic(models.Model):
    """用户学习的主题"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text


class Entry(models.Model):
    """学到的某个主题的具体知识"""
    # 外键，建立联系
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # 这个不限制长度
    text = models.TextField()
    # 按照创建时间呈现条目
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """返回模型的字符串表示"""
        return self.text[:50] + '...'

