# project/tests/main/test_main.py


import unittest

from project.tests.base import BaseTestCaseMain


class TestMainBlueprint(BaseTestCaseMain):

    def test_index(self):
        # Ensure Flask is setup.
        self.client.get('/logout', follow_redirects=True)
        response = self.client.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Welcome!', response.data)
        self.assertIn(b'Register/Login', response.data)

    def test_about(self):
        # Ensure about route behaves correctly.
        response = self.client.get('/about', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'About', response.data)

    def test_404(self):
        # Ensure 404 error is handled.
        response = self.client.get('/404')
        self.assert404(response)
        self.assertTemplateUsed('errors/404.html')


if __name__ == '__main__':
    unittest.main()