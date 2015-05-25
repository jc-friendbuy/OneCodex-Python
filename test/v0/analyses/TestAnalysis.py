"""
This is a test file for the src/v0/analyses/Analysis class.
"""

from __future__ import print_function
import unittest
from v0.analyses.Analysis import Analysis


class TestAnalysis(unittest.TestCase):

    def test_get_resource_url_is_correct(self):
        analysis = Analysis("test_id")
        self.assertEqual(
            analysis._get_resource_url(),
            u"https://beta.onecodex.com/api/v0/analyses/test_id"
        )

    def test_get_action_url_is_correct(self):
        analysis = Analysis("test_id")
        self.assertEqual(
            analysis._get_action_url("table"),
            u"https://beta.onecodex.com/api/v0/analyses/test_id/table"
        )

    def test_get_table_results_is_instance_list(self):
        analysis = Analysis("3186542a03c74205")
        table_results = analysis.get_table()
        self.assertIsInstance(table_results, list)
