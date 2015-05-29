"""
This is a test file for the src/v0/analyses/Analysis class.
"""

from __future__ import print_function
from os import path, stat
from hashlib import md5
import unittest
from v0.analyses.Analysis import Analysis


class TestAnalysis(unittest.TestCase):

    def test_get_table(self):
        analysis = Analysis("3186542a03c74205")
        table_results = analysis.get_table()
        self.assertIsInstance(table_results, list)
        # TODO: add more tests

    def test_save_raw_data_to_path(self):
        destination_path = "/Users/jc/Desktop/ocanalysis.tsv.gz"
        analysis = Analysis("3186542a03c74205")
        analysis.download_and_save_raw_data_to_path(destination_path)
        self.assertTrue(path.isfile(destination_path))
        file_stat_info = stat(destination_path)
        self.assertTrue(file_stat_info.st_size, 93735)
        self.assertTrue(file_stat_info.st_birthtime, 1432661815)
        md5_digest = md5(open(destination_path, "rb").read()).hexdigest()
        self.assertTrue(md5_digest, "ef636300ebf69d82720f335842efd2ba")

    # ADD MORE TESTS FOR GET TABLE