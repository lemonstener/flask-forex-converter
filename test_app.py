from flask import Flask, flash, request, redirect, render_template
from forex_python.converter import CurrencyRates, CurrencyCodes
from unittest import TestCase
from app import app, c, cc, convert, currencies

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class forex_test(TestCase):
    def test_homepage(self):
        '''Making sure homepage loads as intended'''
        with app.test_client() as client:
            res = client.get('/')
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            self.assertIn('<button>CONVERT</button>', html)

    def test_redirection(self):
        '''Making sure /convert redirects back to home page'''
        with app.test_client() as client:
            res = client.post(
                '/convert', data={'from': 'USD', 'to': 'USD', 'amount': '10'})

            self.assertEqual(res.status_code, 302)
            self.assertEqual(res.location, 'http://localhost/')

    def test_redirection__followed_success(self):
        '''Continuing from test_redirect'''
        with app.test_client() as client:
            res = client.post(
                '/convert', data={'from': 'USD', 'to': 'USD', 'amount': '10'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            self.assertEqual(res.status_code, 200)
            '''Making sure application works as intended'''
            self.assertIn(
                '<p class="success"><b>US$ 10 amounts to US$ 10.0</b></p>', html)

    def test_redirection__followed_capitalization(self):
        with app.test_client() as client:
            res = client.post(
                '/convert', data={'from': 'usD', 'to': 'usd', 'amount': '10'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            '''Making sure the application capitalizes all letters in the prompts'''
            self.assertIn(
                '<p class="success"><b>US$ 10 amounts to US$ 10.0</b></p>', html)

    def test_redirection_followed_error(self):
        with app.test_client() as client:
            res = client.post(
                '/convert', data={'from': 'beep', 'to': 'bop', 'amount': 'BOOP'}, follow_redirects=True)
            html = res.get_data(as_text=True)

            '''Making sure all flash error messages display properly'''
            self.assertIn(
                '<p class="error"><b>Invalid currency code to convert from: &#34;BEEP&#34;</b></p>', html)
            self.assertIn(
                '<p class="error"><b>Invalid currency code to convert to: &#34;BOP&#34;</b></p>', html)
            self.assertIn(
                '<p class="error"><b>Invalid amount: &#34;BOOP&#34;</b></p>', html)

            res2 = client.post(
                '/convert', data={'from': 'USD', 'to': 'BGN', 'amount': 'BOOP'}, follow_redirects=True)
            html2 = res2.get_data(as_text=True)

            '''Making sure flash error messages trigger appropriately'''
            self.assertNotIn(
                '<p class="error"><b>Invalid currency code to convert from: &#34;USD&#34;</b></p>', html2)
            self.assertNotIn(
                '<p class="error"><b>Invalid currency code to convert to: &#34;BGN&#34;</b></p>', html2)
            self.assertIn(
                '<p class="error"><b>Invalid amount: &#34;BOOP&#34;</b></p>', html2)

            '''Making sure the convert function will not run if even one input is invalid'''
            self.assertNotIn(
                '<p class="success"><b>US$ BOOP amounts to US$ BOOP</b></p>', html)
