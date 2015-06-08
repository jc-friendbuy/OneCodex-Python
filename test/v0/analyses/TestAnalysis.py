"""
This is a test file for the src/v0/analyses/Analysis class.
"""

from __future__ import print_function
from os import path, stat
from hashlib import md5
import unittest
from v0.analyses.Analysis import Analysis


class TestAnalysis(unittest.TestCase):

    def _get_dummy_analysis_instance(self):
        return Analysis(u"3186542a03c74205", None, None, None, None, None, None, None)

    def test_get_table(self):
        analysis = self._get_dummy_analysis_instance()
        table_results = analysis.get_table()
        self.assertIsInstance(table_results, list)
        self.assertEqual(len(table_results), 125)

    def test_save_raw_data_to_path(self):
        destination_path = u"/Users/jc/Desktop/ocanalysis.tsv.gz"
        analysis = self._get_dummy_analysis_instance()
        analysis.download_and_save_raw_data_to_path(destination_path)
        self.assertTrue(path.isfile(destination_path))
        file_stat_info = stat(destination_path)
        self.assertTrue(file_stat_info.st_size, 93735)
        self.assertTrue(file_stat_info.st_birthtime, 1432661815)
        md5_digest = md5(open(destination_path, u"rb").read()).hexdigest()
        self.assertTrue(md5_digest, u"ef636300ebf69d82720f335842efd2ba")
