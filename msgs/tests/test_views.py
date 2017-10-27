# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import Client, TestCase
from django.core.urlresolvers import reverse


class BaseTest(TestCase):

    def setUp(self):
        self.client = Client()


class ViewsTest(BaseTest):

    def setUp(self):
        super().setUp()

    def test_frontpage_render_succeeds(self):
        resp = self.client.get(reverse('frontpage'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed('index.html')
