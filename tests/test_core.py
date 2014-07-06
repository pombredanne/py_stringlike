#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from six import text_type
from unittest import main, TestCase

from stringlike import StringLike


class StringMock(StringLike):
    """
    A simple mock of built-in strings using the StringLike class.
    """
    def __init__(self, string):
        """
        Take a string and use it as the representation of this class.
        """
        self.string = string

    def __str__(self):
        """
        Just return whatever we got during construction.
        """
        return text_type(self.string)


class TestStringLikeMagicMethods(TestCase):
    def test_str(self):
        self.assertEqual(str(StringMock('abc')), 'abc')
        self.assertEqual(text_type(StringMock('абв')), 'абв')

    def test_eq(self):
        self.assertEqual(StringMock(''), '')
        self.assertEqual(StringMock('abc'), 'abc')
        self.assertEqual(StringMock('вгд'), 'вгд')

    def test_ne(self):
        self.assertNotEqual(StringMock(''), 'abc')
        self.assertNotEqual(StringMock('abc'), '')

        self.assertNotEqual(StringMock(''), 'вгд')
        self.assertNotEqual(StringMock('вгд'), '')

    def test_lt(self):
        self.assertTrue(StringMock('a') < 'b')
        self.assertTrue('a' < StringMock('b'))
        self.assertTrue(StringMock('a') < StringMock('b'))

        # test unicode
        self.assertTrue(StringMock('в') < 'г')
        self.assertTrue('в' < StringMock('г'))
        self.assertTrue(StringMock('в') < StringMock('г'))

    def test_le(self):
        self.assertTrue(StringMock('a') <= 'b')
        self.assertTrue('a' <= StringMock('b'))
        self.assertTrue(StringMock('a') <= StringMock('b'))

        # test unicode
        self.assertTrue(StringMock('в') <= 'г')
        self.assertTrue('в' <= StringMock('г'))
        self.assertTrue(StringMock('в') <= StringMock('г'))

    def test_gt(self):
        self.assertTrue(StringMock('b') > 'a')
        self.assertTrue('b' > StringMock('a'))
        self.assertTrue(StringMock('b') > StringMock('a'))

        # test unicode
        self.assertTrue(StringMock('г') > 'в')
        self.assertTrue('г' > StringMock('в'))
        self.assertTrue(StringMock('г') > StringMock('в'))

    def test_ge(self):
        self.assertTrue(StringMock('b') >= 'a')
        self.assertTrue('b' >= StringMock('a'))
        self.assertTrue(StringMock('b') >= StringMock('a'))

        # test unicode
        self.assertTrue(StringMock('г') >= 'в')
        self.assertTrue('г' >= StringMock('в'))
        self.assertTrue(StringMock('г') >= StringMock('в'))

    def test_concat(self):
        self.assertEqual(StringMock('a') + 'bc', 'abc')
        self.assertEqual('a' + StringMock('bc'), 'abc')
        self.assertEqual(StringMock('a') + StringMock('bc'), 'abc')

        # test unicode
        self.assertEqual(StringMock('в') + 'гд', 'вгд')
        self.assertEqual('в' + StringMock('гд'), 'вгд')
        self.assertEqual(StringMock('в') + StringMock('гд'), 'вгд')

    def test_multiply(self):
        self.assertEqual(StringMock('a') * 3, 'aaa')
        self.assertEqual(3 * StringMock('a'), 'aaa')

        # test unicode
        self.assertEqual(StringMock('в') * 3, 'ввв')
        self.assertEqual(3 * StringMock('в'), 'ввв')

    def test_subindex(self):
        self.assertEqual(StringMock('abc')[0], 'a')
        self.assertEqual(StringMock('abc')[2], 'c')
        self.assertEqual(StringMock('abc')[1:], 'bc')
        self.assertEqual(StringMock('abc')[:-1], 'ab')
        with self.assertRaises(IndexError):
            StringMock('abc')[3]

        # test unicode
        self.assertEqual(StringMock('вгд')[0], 'в')
        self.assertEqual(StringMock('вгд')[2], 'д')
        self.assertEqual(StringMock('вгд')[1:], 'гд')
        self.assertEqual(StringMock('вгд')[:-1], 'вг')
        with self.assertRaises(IndexError):
            StringMock('вгд')[3]

    def test_contains(self):
        self.assertIn('a', StringMock('abc'))
        self.assertIn('г', StringMock('вгд'))

    def test_len(self):
        self.assertEqual(len(StringMock('')), 0)
        self.assertEqual(len(StringMock('abc')), 3)
        self.assertEqual(len(StringMock('вгд')), 3)

    def test_iter(self):
        self.assertEqual([x for x in StringMock('')], [])
        self.assertEqual([x for x in StringMock('abc')], ['a', 'b', 'c'])
        self.assertEqual([x for x in StringMock('вгд')], ['в', 'г', 'д'])

        iterator = iter(StringMock('abc'))
        self.assertEqual(iterator.next(), 'a')
        self.assertEqual(iterator.next(), 'b')
        self.assertEqual(iterator.next(), 'c')
        with self.assertRaises(StopIteration):
            iterator.next()

        # test unicode
        iterator = iter(StringMock('вгд'))
        self.assertEqual(iterator.next(), 'в')
        self.assertEqual(iterator.next(), 'г')
        self.assertEqual(iterator.next(), 'д')
        with self.assertRaises(StopIteration):
            iterator.next()

    def test_nonzero(self):
        self.assertTrue(bool(StringMock('abc')))
        self.assertTrue(bool(StringMock('вгд')))
        self.assertFalse(bool(StringMock('')))

    def test_and(self):
        self.assertEqual(StringMock('') and StringMock('abc'), '')
        self.assertEqual(StringMock('abc') and StringMock(''), '')
        self.assertEqual(StringMock('a') and StringMock('bc'), 'bc')

        self.assertEqual('' and StringMock('abc'), '')
        self.assertEqual(StringMock('abc') and '', '')
        self.assertEqual('a' and StringMock('bc'), 'bc')
        self.assertEqual(StringMock('a') and 'bc', 'bc')

        # test unicode
        self.assertEqual(StringMock('') and StringMock('вгд'), '')
        self.assertEqual(StringMock('вгд') and StringMock(''), '')
        self.assertEqual(StringMock('в') and StringMock('гд'), 'гд')

        self.assertEqual('' and StringMock('вгд'), '')
        self.assertEqual(StringMock('вгд') and '', '')
        self.assertEqual('в' and StringMock('гд'), 'гд')
        self.assertEqual(StringMock('в') and 'гд', 'гд')

    def test_or(self):
        self.assertEqual(StringMock('') or StringMock('abc'), 'abc')
        self.assertEqual(StringMock('abc') or StringMock(''), 'abc')
        self.assertEqual(StringMock('a') or StringMock('bc'), 'a')

        self.assertEqual('' or StringMock('abc'), 'abc')
        self.assertEqual(StringMock('abc') or '', 'abc')
        self.assertEqual('a' or StringMock('bc'), 'a')
        self.assertEqual(StringMock('a') or 'bc', 'a')

        # test unicode
        self.assertEqual(StringMock('') or StringMock('вгд'), 'вгд')
        self.assertEqual(StringMock('вгд') or StringMock(''), 'вгд')
        self.assertEqual(StringMock('в') or StringMock('гд'), 'в')

        self.assertEqual('' or StringMock('вгд'), 'вгд')
        self.assertEqual(StringMock('вгд') or '', 'вгд')
        self.assertEqual('в' or StringMock('гд'), 'в')
        self.assertEqual(StringMock('в') or 'гд', 'в')

    def test_attribute_error(self):
        with self.assertRaises(AttributeError):
            StringMock('').gobbledygook()


class TestSomeStringMethods(TestCase):
    def test_capitalize(self):
        self.assertEqual(StringMock('abc').capitalize(), 'Abc')
        self.assertEqual(StringMock('ABC').capitalize(), 'Abc')

        # test unicode
        self.assertEqual(StringMock('вгд').capitalize(), 'Вгд')
        self.assertEqual(StringMock('ВГД').capitalize(), 'Вгд')

    def test_endswith(self):
        self.assertTrue(StringMock('abc').endswith('c'))
        self.assertFalse(StringMock('abc').endswith('b'))

        # test unicode
        self.assertTrue(StringMock('вгд').endswith('д'))
        self.assertFalse(StringMock('вгд').endswith('г'))

    def test_format(self):
        self.assertEqual(StringMock('{0}').format('abc'), 'abc')
        self.assertEqual(StringMock('{0}').format('вгд'), 'вгд')


if __name__ == '__main__':
    main()
