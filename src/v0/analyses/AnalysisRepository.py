"""
This module handles Analysis fetching.  It provides functions to fetch ID and status for all the
analyses defined in the system, all of the data for a single analysis (by ID) and to refresh a given
Analysis.
"""

from v0.analyses.Analysis import Analysis
from v0.analyses.AnalysisDataAdapter import AnalysisDataAdapter
from v0.common.OneCodexAPIURLBuilder import OneCodexAPIURLBuilder
from v0.common.OneCodexRequest import OneCodexRequest

_url_builder = OneCodexAPIURLBuilder(u"analyses")


def get_all():
    """
    Get a list of all Analyses defined in the One Codex system.
    :return: A list of dictionary objects, each of which holds the id and status of every
    analysis defined in the system.
    """
    url = _url_builder.get_resource_url()
    request = OneCodexRequest.get(url)
    return request.json()


def get(analysis_id):
    """
    Get the data for an Analysis and return an object populated with that data.
    :param analysis_id: The id of the Analysis to be fetched.
    :return: An Analysis instance with the data corresponding to the id that was given.
    """
    data = _get_analysis_data(analysis_id)
    return _construct_analysis_from_id_and_data(analysis_id, data)


def refresh(analysis):
    """
    Refresh the data for an Analysis from the One Codex system.
    :param analysis: The Analysis object which is to be refreshed.
    :return: None.
    """
    data = _get_analysis_data(analysis.id)
    data_adapter = AnalysisDataAdapter(data)
    analysis.status = data_adapter.status
    analysis.number_reads = data_adapter.number_reads
    analysis.proportion_mapped = data_adapter.proportion_mapped
    analysis.reference_id = data_adapter.reference_id
    analysis.reference_name = data_adapter.reference_name
    analysis.sample_id = data_adapter.sample_id
    analysis.sample_filename = data_adapter.sample_filename


def _get_analysis_data(analysis_id):
    """
    Retrieve the data for a given Analysis ID from the One Codex system.
    :param analysis_id: The ID of the Analysis which is to be queried.
    :return: A data dictionary with the data from One Codex.
    """
    url = _url_builder.get_resource_url(id=analysis_id)
    request = OneCodexRequest.get(url)
    return request.json()


def _construct_analysis_from_id_and_data(id, data):
    """
    Construct an Analysis instance with the given id and from the data dictionary given.
    :param id: The id of the Analysis instance.
    :param data: The data dictionary with the data for the instance.
    :return: An instance of Analysis with the given ID and data.
    """
    data_adapter = AnalysisDataAdapter(data)
    status = data_adapter.status
    number_reads = data_adapter.number_reads
    proportion_mapped = data_adapter.proportion_mapped
    reference_id = data_adapter.reference_id
    reference_name = data_adapter.reference_name
    sample_id = data_adapter.sample_id
    sample_filename = data_adapter.sample_filename
    return Analysis(id, status, number_reads, proportion_mapped, reference_id, reference_name,
                    sample_id, sample_filename)
