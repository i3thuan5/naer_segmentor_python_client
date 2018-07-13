# -*- coding: utf-8 -*-
from unittest.case import TestCase

from naer import segment


class 國教院斷詞用戶端整合試驗(TestCase):

    def test_語句斷一句話(self):
        斷詞結果 = segment('市面上很少有「教科書設計」的專書')
        self.assertEqual(斷詞結果[0],  ["市面", "Nc"])
