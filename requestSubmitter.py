"""
Client to submit new render request to server
"""

import logging

from util import client


logging.basicConfig(level=logging.INFO)
LOGGER = logging.getLogger(__name__)


def send(d):
    """
    Send/Submit a new render request

    :param d: dict. a render request serialized as dictionary
    """
    rrequest = client.add_request(d)
    if rrequest:
        LOGGER.info('request %s sent to server', rrequest.uid)


if __name__ == '__main__':
    test_job_a = {
        'name': 'street_seq01',
        'owner': 'TEST_SUBMITTER_01',
        'umap_path': '/Game/Fire_VDB/Map/Fire_part_02',
        'useq_path': '/Game/NewLevelSequence.NewLevelSequence',
        'uconfig_path': '/Game/Pending_MoviePipelinePrimaryConfig.Pending_MoviePipelinePrimaryConfig'
    }

    test_job_b = {
       'name': 'street_seq02',
        'owner': 'TEST_SUBMITTER_02',
        'umap_path': '/Game/Fire_VDB/Map/Fire_part_02',
        'useq_path': '/Game/NewLevelSequence.NewLevelSequence',
        'uconfig_path': '/Game/Pending_MoviePipelinePrimaryConfig.Pending_MoviePipelinePrimaryConfig'
    }

    for job in [test_job_a, test_job_b]:
        send(job)
