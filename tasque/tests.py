
import datetime
from django.test import TestCase
from .models import Task, TaskStatus, TaskTag


class TaskModelTests(TestCase):

    def test_create_tag(self):
        """
        タグを作成できているか確認
        """
        TaskTag.objects.create(name='test_tag')
        actual_tag = TaskTag.objects.get(name='test_tag')
        self.assertEqual(actual_tag.name, 'test_tag')

    def test_task_has_date(self):
        """
        作成したデータに日付が付与されているか確認
        """
        TaskTag.objects.create(name='test_tag')
        Task.objects.create(title='test_title')
        actual_task = Task.objects.get(title='test_title')
        self.assertIsInstance(actual_task.created_at, datetime.datetime)

    def test_save_and_retrieve(self):
        """
        データの保存と取得を確認
        """
        TaskTag.objects.create(name='test_tag')
        Task.objects.create(title='test_title')
        actual_task = Task.objects.get(title='test_title')
        self.assertEqual(actual_task.title, 'test_title')
