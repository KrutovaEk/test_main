import unittest
from unittest import TestCase
import requests



class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def ivk(self, paths):
        per= 'https://cloud-api.yandex.net/v1/disk/resources'
        fer= {'Authorization': 'OAuth ' + self.token}
        path={'path': paths}
        res=requests.put(per, headers=fer, params=path)
        return res.status_code






# if __name__ == '__main__':

#     token =  # токен Яндекс Диска
#     uploader = YaUploader(token)
#     result = print(uploader.ivk("RE"))
   

    










