import sys
import unittest
try:
    from unittest import mock
except ImportError:
    from mock import mock
from mongomock import MongoClient
sys.modules['helga.plugins'] = mock.Mock() # hack to avoid py3 errors in test
from helga.db import db
from helga_{{ cookiecutter.plugin_package }}.helga_{{ cookiecutter.plugin_package }} import logic


class Test{{ cookiecutter.plugin_package }}(unittest.TestCase):
    def setUp(self):
        self.db_patch = mock.patch(
            'pymongo.MongoClient',
            new_callable=lambda: MongoClient
        )
        self.db_patch.start()
        self.addCleanup(self.db_patch.stop)

    def tearDown(self):
        db.{{ cookiecutter.plugin_package }}.drop()

    def test_{{ cookiecutter.plugin_package }}(self):
        self.assertEqual('Hello World!', logic(None))


if __name__ == '__main__':
    unittest.main()
