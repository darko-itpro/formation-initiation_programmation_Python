#!/usr/bin/env python 

import unittest as ut
from media_manager import media_manager as mm


class TestCreateCollection(ut.TestCase):
    def test_new_collection_is_data(self):
        self.assertIsNotNone(mm.create_collection())

    def test_new_collection_is_empty(self):
        self.assertEqual(0, len(mm.create_collection()))


class TestAddMedia(ut.TestCase):
    def setUp(self):
        self.collection = mm.create_collection()

    def test_can_add_basic_data(self):
        collection = mm.add_movie(self.collection, 'test')
        self.assertIsNotNone(collection)
        self.assertEqual(1, len(collection))

    def test_cannot_add_duplicate(self):
        collection = mm.add_movie(self.collection, 'test')
        with self.assertRaises(ValueError):
            mm.add_movie(collection, 'test')
