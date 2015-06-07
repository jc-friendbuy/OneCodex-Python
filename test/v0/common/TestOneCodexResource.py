"""
This is a test file for the src/v0/common/OneCodexResource class.
"""

import unittest
from v0.common.OneCodexAPIURLBuilder import OneCodexAPIURLBuilder


class TestOneCodexResource(unittest.TestCase):

    def tearDown(self):
        OneCodexAPIURLBuilder._resource_name = None

    def test_no_resource_name_raises_assertion_error(self):
        with self.assertRaises(AssertionError) as raise_cm:
            resource = OneCodexAPIURLBuilder()
        self.assertEqual(raise_cm.exception.message, "Missing resource definition")

    def test_get_resource_url(self):
        OneCodexAPIURLBuilder._resource_name = u"test"
        resource = OneCodexAPIURLBuilder()
        self.assertEqual(
            resource.get_resource_url(),
            u"https://beta.onecodex.com/api/v0/test"
        )
        self.assertEqual(
            resource.get_resource_url(id=u"test_id"),
            u"https://beta.onecodex.com/api/v0/test/test_id"
        )
        self.assertEqual(
            resource.get_resource_url(action=u"test_action"),
            u"https://beta.onecodex.com/api/v0/test/test_action"
        )
        self.assertEqual(
            resource.get_resource_url(id=u"test_id", action=u"test_action"),
            u"https://beta.onecodex.com/api/v0/test/test_id/test_action"
        )
