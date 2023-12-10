import requests
import unittest
from unittest import TestCase
from ja_disk import YaUploader



class TestSummarinize(TestCase):

    def test_2(self):
        token = # токен Яндекс Диска
        uploader = YaUploader(token)
        result = uploader.ivk('Папка')
        expected = 201
        self.assertEqual(result, expected)  

    @unittest.expectFailure
    def test_3(self):
        token =  # токен Яндекс Диска
        uploader = YaUploader(token)
        result = uploader.ivk('Папка')
        expected = 400
        self.assertE(result, expected)  

    @unittest.expectFailure
    def test_4(self):
        token =  # токен Яндекс Диска
        uploader = YaUploader(token)
        result = uploader.ivk('Папка')
        expected = 401
        self.assertE(result, expected) 

    @unittest.expectFailure
    def test_5(self):
        token =  # токен Яндекс Диска
        uploader = YaUploader(token)
        result = uploader.ivk('Папка')
        expected = 409
        self.assertE(result, expected)  
 






