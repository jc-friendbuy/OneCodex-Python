"""
This is a test file for the src/v0/analyses/AnalysisDataAdapter class.
"""
import unittest
from v0.analyses.AnalysisDataAdapter import AnalysisDataAdapter


class TestAnalysisDataAdapter(unittest.TestCase):

    def test_with_all_fields(self):
        data = dict()
        data[u"analysis_status"] = u"Succeeded"
        data[u"n_reads"] = u"20"
        data[u"p_mapped"] = u"0.15"
        data[u"reference_id"] = u"referenceid"
        data[u"reference_name"] = u"Reference name"
        data[u"sample_id"] = u"sampleid"
        data[u"sample_filename"] = u"file.fasta"

        data_adapter = AnalysisDataAdapter(data)
        self.assertEqual(data_adapter.status, u"Succeeded")
        self.assertEqual(data_adapter.number_reads, 20)
        self.assertAlmostEqual(data_adapter.proportion_mapped, 0.15)
        self.assertEqual(data_adapter.reference_id, u"referenceid")
        self.assertEqual(data_adapter.reference_name, u"Reference name")
        self.assertEqual(data_adapter.sample_id, u"sampleid")
        self.assertEqual(data_adapter.sample_filename, u"file.fasta")

    def test_with_some_fields(self):
        data = dict()
        data[u"analysis_status"] = u"Succeeded"
        data[u"reference_id"] = u"referenceid"
        data[u"reference_name"] = u"Reference name"
        data[u"sample_id"] = u"sampleid"
        data[u"sample_filename"] = u"file.fasta"

        data_adapter = AnalysisDataAdapter(data)
        self.assertEqual(data_adapter.status, u"Succeeded")
        self.assertIsNone(data_adapter.number_reads)
        self.assertIsNone(data_adapter.proportion_mapped)
        self.assertEqual(data_adapter.reference_id, u"referenceid")
        self.assertEqual(data_adapter.reference_name, u"Reference name")
        self.assertEqual(data_adapter.sample_id, u"sampleid")
        self.assertEqual(data_adapter.sample_filename, u"file.fasta")

    def test_data_typing(self):
        data = dict()
        data[u"n_reads"] = u"hello"
        data[u"p_mapped"] = u"blah"

        data_adapter = AnalysisDataAdapter(data)
        with self.assertRaisesRegexp(ValueError, "literal"):
            data_adapter.number_reads

        with self.assertRaisesRegexp(ValueError, "convert string to float"):
            data_adapter.proportion_mapped
