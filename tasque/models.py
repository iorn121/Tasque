from django.db import models
import uuid


class TaskTag(models.Model):
    name = models.CharField(max_length=100, verbose_name="タグ")
    # sort_order = models.PositiveSmallIntegerField(verbose_name="ソート順")

    def __int__(self):
        return self.id

    def __str__(self):
        return self.name


class TaskStatus(models.IntegerChoices):
    TODO = 0, "TODO"
    DONE = 1, "完了"
    CANCELLED = 2, "期限切れ"


class Task(models.Model):
    class Meta:
        ordering = ['-created_at']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(verbose_name='タスク名', max_length=100)
    detail = models.TextField(
        verbose_name='詳細', max_length=200, blank=True, null=True)
    status = models.PositiveSmallIntegerField(
        verbose_name="ステータス", choices=TaskStatus.choices, default=0)
    tag = models.ForeignKey(
        TaskTag, on_delete=models.PROTECT, verbose_name='タグ', default=1)
    due_date = models.DateField(verbose_name='期限', blank=True, null=True)
    created_at = models.DateTimeField(verbose_name='作成日時', auto_now_add=True)
    finished_at = models.DateTimeField(
        verbose_name='完了日時', blank=True, null=True)

    def __str__(self):
        return self.title
