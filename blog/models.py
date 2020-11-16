from django.db import models
from django.contrib.auth.models import User
from DjangoUeditor.models import UEditorField  # 头部增加这行代码导入UEditorField


# 分类
class Category(models.Model):
    name = models.CharField('分类', max_length=50)

    class Meta:
        db_table = 'blog_category'
        verbose_name = '分类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 标签
class Tags(models.Model):
    name = models.CharField('标签', max_length=100)

    class Meta:
        db_table = 'blog_tags'
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 文章
class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    intro = models.TextField('摘要', max_length=200, blank=True)
    # body = models.TextField()

    body = UEditorField('内容', width=800, height=500,
                        toolbars="full", imagePath="upimg/", filePath="upfile/",
                        upload_settings={"imageMaxSize": 1204000},
                        settings={}, command=None, blank=True
                        )

    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='分类', default='1')
    tags = models.ManyToManyField(Tags, blank=True)
    # 存储比较短的字符串可以使用 CharField，但对于文章的正文来说可能会是一大段文本，因此使用 TextField 来存储大段文本。
    # body = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者', default='admin')
    created_time = models.DateTimeField('发布时间', auto_now_add=True)

    class Meta:
        db_table = 'blog_article'
        verbose_name = '文章列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s - %s' % (self.title, self.created_time)
