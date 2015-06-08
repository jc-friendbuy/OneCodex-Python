"""
This is a test file for the src/v0/analyses/AnalysisRepository module.
"""
import unittest
from v0.analyses import AnalysisRepository
from v0.analyses.Analysis import Analysis


class TestAnalysisRepository(unittest.TestCase):

    def test_get_all(self):
        analyses = AnalysisRepository.get_all()
        self.assertEqual(len(analyses), 2)

    def test_get(self):
        analysis1 = AnalysisRepository.get(u"3186542a03c74205")
        self.assertEqual(analysis1.status, u"Success")
        self.assertEqual(analysis1.reference_id, u"45c03dc045904304")
        self.assertEqual(analysis1.reference_name, u"RefSeq Complete Genomes")
        self.assertEqual(analysis1.sample_filename, u"sample.fasta")
        self.assertEqual(analysis1.sample_id, u"4fa667531d3c47b6")
        
        analysis2 = AnalysisRepository.get(u"60727ded77604f27")
        self.assertEqual(analysis2.status, u"Success")
        self.assertEqual(analysis2.reference_id, u"a4919c2784bc4c92")
        self.assertEqual(analysis2.reference_name, u"One Codex Database")
        self.assertEqual(analysis2.sample_filename, u"sample.fasta")
        self.assertEqual(analysis2.sample_id, u"4fa667531d3c47b6")

    def test_refresh(self):
        analysis = Analysis(u"3186542a03c74205", None, None, None, None, None, None, None)
        AnalysisRepository.refresh(analysis)
        self.assertEqual(analysis.status, u"Success")
        self.assertEqual(analysis.reference_id, u"45c03dc045904304")
        self.assertEqual(analysis.reference_name, u"RefSeq Complete Genomes")
        self.assertEqual(analysis.sample_filename, u"sample.fasta")
        self.assertEqual(analysis.sample_id, u"4fa667531d3c47b6")
