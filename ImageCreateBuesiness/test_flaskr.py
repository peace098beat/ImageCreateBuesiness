# -*- coding: utf-8 -*-

import unittest

import flaskr


class TestFlaskHello(unittest.TestCase):

    def setUp(self):
        self.app = flaskr.app.test_client()

    def test_get(self):
        response = self.app.get('/test')
        assert response.status_code == 200
        assert response.data == 'Hello, World!'



if __name__ == '__main__':
    unittest.main()