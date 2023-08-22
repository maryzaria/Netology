from unittest import TestCase

from ..API_Yandex import YandexDiscUpload


class TestAPIYandex(TestCase):
    yd = YandexDiscUpload()

    def test_create_folder(self):
        # создаем новую папку с именем 'new_folder'
        result_code = self.yd.create_new_folder('new_folder')
        self.assertIn(result_code, (200, 201))

        # создаем уже существующую папку: re.compile(r'По указанному пути .* уже существует папка с таким именем')
        result_code = self.yd.create_new_folder('new_folder')
        self.assertEqual(result_code, 409)

    def test_auth(self):
        """Не авторизован."""
        new_yd = YandexDiscUpload(yd_token='')
        res = new_yd.create_new_folder('new_folder')
        self.assertEqual(res, 401)

    def test_correct_data(self):
        """Некорректные данные."""
        res = self.yd.create_new_folder(list())
        self.assertEqual(res, 400)

    def test_correct_url(self):
        """Ресурс не найден."""
        res = self.yd.create_new_folder('folder', url='https://cloud-api.yandex.net/v1')
        self.assertEqual(res, 404)
