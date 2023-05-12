import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def _get_headers(self) -> dict:
        return {
            'Content-Type': 'application/json',
            'Authorization': f'OAuth {self.token}'
        }

    def _get_link_to_upload(self, file_path) -> str:
        """Get link for upload files"""
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self._get_headers()
        params = {'path': file_path, 'overwrite': True}
        response = requests.get(upload_url, headers=headers, params=params)
        return response.json().get('href', '')

    def upload_file_to_disk(self, file_path: str, file_list: list[str]):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        try:
            for filename in file_list:
                href = self._get_link_to_upload(file_path + filename)
                requests.put(href, data=open(filename, 'rb'))
            print('Successful upload for all files')
        except Exception as e:
            print(f'Error: {e}')


TOKEN = ''

if __name__ == '__main__':
    yd = YaUploader(token=TOKEN)
    yd.upload_file_to_disk("Netology/test/", ["test1.txt", "test2.txt"])