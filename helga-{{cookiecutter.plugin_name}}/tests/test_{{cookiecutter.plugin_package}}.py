import unittest


class Test{{ cookiecutter.plugin_package }}(unittest.TestCase):
    def test_{{ cookiecutter.plugin_package }}(self):
        self.assertTrue(False)


if __name__ == '__main__':
    unittest.main()
