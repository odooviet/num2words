# Copyright (c) 2013, Savoir-faire Linux inc.  All Rights Reserved.

# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA

from unittest import TestCase

from num2words import num2words

class Num2WordsENTest(TestCase):
    def test_and_join_199(self):
        self.assertEqual(num2words(187), "сто вісімдесят сім")

    def test_cardinal_for_float_number(self):
        self.assertEqual(num2words(12.40), "дванадцять кома сорок")
        self.assertEqual(num2words(17.31), "сімнадцять кома тридцять один")
        self.assertEqual(num2words(14.13), "чотирнадцять кома тринадцять")
        self.assertEqual(num2words(12.31), "дванадцять кома тридцять один")
