from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse_lazy

from ..models import Diary


class LoggedInTestCase(TestCase):
    """各クラスで使う処理をoverrideしたTast Caseクラス"""

    def setUp(self):
        """テスト前事前設定"""
        self.password = ''
        self.test_user = get_user_model().objects.create_user(
            username='',
            email='',
            password=self.password
        )
        self.client.login(email=self.test_user.email, password=self.password)


class TestDiaryCreateView(LoggedInTestCase):
    """DiaryCreateViewテスト"""

    def test_create_diary_success(self):
        """作成成功検証"""
        params = {
            'title': 'テキストタイトル',
            'content': '本文',
            'photo1': '',
            'photo2': '',
            'photo3': '',
        }
        response = self.client.post()

    def test_create_diary_failure(self):
        """作成失敗検証"""
        pass


class TestDiaryUpdateView(LoggedInTestCase):
    """DiaryUpdateViewテスト"""

    def test_update_diary_success(self):
        """編集成功検証"""
        pass

    def test_update_diary_failure(self):
        """編集失敗検証"""
        pass


class TestDiaryDeleteView(LoggedInTestCase):
    """DiaryDeleteViewテスト"""

    def test_dedlete_diary_success(self):
        """編集成功検証"""
        pass

    def test_delete_diary_failure(self):
        """編集失敗検証"""
        pass
