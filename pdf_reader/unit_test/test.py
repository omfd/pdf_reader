from unittest import TestCase
import pdf_reader
from pdf_reader.reader_sample import main

class TestJoke(TestCase):
    def test_is_string(self):
        s = pdf_reader.joke()
        self.assertTrue(isinstance(s, basestring))

class TestConsole(TestCase):
    def test_basic(self):
        main()