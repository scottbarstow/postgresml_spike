from unittest import TestCase

import app.core.sample as sample

class TestSample(TestCase):
    def test_do_something(self):
        self.assertEqual(sample.doSomething(), 42)