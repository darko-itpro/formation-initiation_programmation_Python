#!/usr/bin/env python

import pytest
from media_manager import media as mm


def test_new_collection_is_data():
    assert mm.create_collection() is not None


def test_new_collection_is_empty():
    assert len(mm.create_collection()) == 0


class TestNewCollection:
    def test_new_collection_is_data(self):
        assert mm.create_collection() is not None


    def test_new_collection_is_empty(self):
        assert len(mm.create_collection()) == 0


@pytest.fixture
def new_collection():
    return mm.create_collection()


def test_can_add_basic_data(new_collection):
    collection = mm.add_movie(new_collection, 'test')
    assert collection is not None
    assert len(collection) == 1


def test_cannot_add_duplicate(new_collection):
    collection = mm.add_movie(new_collection, 'test')

    with pytest.raises(ValueError):
        mm.add_movie(collection, 'test')
