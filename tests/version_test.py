import unittest
from HyperAPI.utils.version import Version


class VersionTestCase(unittest.TestCase):

    def test_version(self):
        v_naught = Version(0)
        v_null = Version(None)
        v_dev = Version('dev')
        v_major = Version('1')
        v_minor = Version('1.1')
        v_patch = Version('1.1.1')
        v_int = Version(1)
        v_float = Version(1.1)
        v_version = Version(Version('1.1.1'))

        self.assertTrue(v_dev.is_dev)
        self.assertTrue(v_null.is_dev)

        self.assertFalse(v_naught.is_dev)
        self.assertFalse(v_major.is_dev)
        self.assertFalse(v_minor.is_dev)
        self.assertFalse(v_patch.is_dev)
        self.assertFalse(v_int.is_dev)
        self.assertFalse(v_float.is_dev)
        self.assertFalse(v_version.is_dev)

        self.assertTrue(v_naught < v_null)
        self.assertFalse(v_naught >= v_null)

        self.assertTrue(v_naught < v_dev)
        self.assertFalse(v_naught >= v_dev)

        self.assertTrue(v_major < v_dev)
        self.assertFalse(v_major >= v_dev)

        self.assertTrue(v_major < v_minor)
        self.assertFalse(v_major >= v_minor)

        self.assertTrue(v_minor < v_patch)
        self.assertFalse(v_minor >= v_patch)

        self.assertTrue(v_major == v_int)
        self.assertFalse(v_major != v_int)

        self.assertTrue(v_minor == v_float)
        self.assertFalse(v_minor != v_float)

        self.assertTrue(v_patch == v_version)
        self.assertTrue(v_dev != v_version)
