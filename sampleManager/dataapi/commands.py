__author__ = 'arkilic'

from sampleManager.database.collection_definition import Container, Request, Sample
from sampleManager.session.databaseInit import db


def save_container(container_id, container_name, owner_group, collection_ref_id=list()):
    """
    :param container_id: Unique identifier for a given container
    :type container_id: unspecified

    :param container_name: Name for a given container
    :type container_name:str

    :param owner_group: Identifier for given owner
    :type owner_group: int

    :param

    :return: Container instance unique identifier
    :rtype: bson.ObjectId
    """
    container_obj = Container(container_id=container_id, container_name=container_name, owner_group=owner_group,
                              collection_ref_id=collection_ref_id)
    try:
        container_obj.save(wtimeout=100, write_concern={'w': 1})
    except:
        raise


def save_sample(sample_id, container_id, sample_name, collection_id, owner_group):
    """
    :param sample_id: Unique identifier specific to a sample set by ABBIX collection script
    :type sample_id: int

    :param container_id: foreignkey pointing to container a sample belongs to
    :type container_id: bson.ObjectId

    :param collection_id: ???
    :type collection_id: ???

    :param sample_name: Text descriptor for sample
    :type sample_name: str

    :param owner_group: Denotes the group a specific owner belongs
    :type owner_group: int


    :return: None
    :rtype: None
    """
    sample_obj = Sample(sample_id=sample_id, container_id=container_id, sample_name=sample_name,
                        collection_id=collection_id, owner_group=owner_group)
    try:
        sample_obj.save(wtimeout=100, write_concern={'w': 1})
    except:
        raise


def save_request(sample_id, request_dict):
    """
    :param sample_id: foreignkey pointing at a specific sample's _id field
    :type sample_id: bson.ObjectId

    :param request_dict: custom field to be filled by ABBOX collection environment
    :type request_dict: dict

    :return: None
    :rtype: None
    """
    request_obj = Request(sample_id, request_dict)
    try:
        request_obj.save(wtimeout=100, write_concern={'w': 1})
    except:
        raise


def find_container(container_query_dict):
    """
    Submits a query to container collection and returns documents that match search criteria as a pymongo.cursor object
    :param container_query_dict: Dictionary for determining
    :return:
    """
    try:
        container_cursor = db['container'].find(container_query_dict)
    except:
        raise
    return container_cursor


def __decode_container_cursor(container_cursor):
    containers = list()
    for temp_dict in container_cursor:
        pass


def find_request():
    pass


def __decode_request_cursor(request_cursor):
    pass


def find_sample():
    pass


def __decode_sample_cursor(sample_cursor):
    pass


def __get_container_id(container_query_dict=dict()):
    pass


def __get_sample_id(sample_query_dict=dict()):
    pass