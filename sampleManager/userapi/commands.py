from collections import OrderedDict

__author__ = 'arkilic'
from sampleManager.dataapi.commands import save_container, save_request, save_sample, find_container
from sampleManager.dataapi.commands import find_request, find_sample


def create_container(container_id, container_name, owner_group, contained_container_id=None):
    pass


def add_sample(container_id, sample_id, sample_name, owner_group):
    pass


def create_request(sample_id, request_dict, request_id):
    pass


def change_sample_container():
    pass


def toggle_sample():
    pass


def toggle_request_status():
    pass
Aa

def _isinstance():
    pass


container_keys = OrderedDict()

container_keys['container_id'] = {'description': "The unique identifier for a container",
                                  'type': int,
                                  'validate_fun': _isinstance}


container_keys['container_name'] = {'description': "The unique name for a container",
                                    'type': str,
                                    'validate_fun': _isinstance}

container_keys['owner_group'] = {'description': 'Specifies the group container owner',
                                 'type': int,
                                 'validate_fun': _isinstance}

container_keys['contained_container_id'] = {'description': 'Reference to containers encapsulated within ',
                                            'type': int,
                                            'validate_fun': _isinstance}

sample_keys = OrderedDict()

sample_keys['sample_id'] = {'description': 'The unique identifier for a sample',
                            'type': int,
                            'validate_fun': _isinstance}

sample_keys['container_id'] = {'description': "The unique identifier for a container",
                               'type': int,
                               'validate_fun': _isinstance}

sample_keys['sample_name'] = {'description': "The unique name of the sample",
                              'type': str,
                              'validate_fun': _isinstance}

sample_keys['owner_group'] = {'description': 'Specifies the group container owner',
                              'type': int,
                              'validate_fun': _isinstance}

request_keys = OrderedDict()

request_keys['sample_id'] = {'description': 'The unique identifier for a sample',
                            'type': int,
                            'validate_fun': _isinstance}

request_keys['request_id'] = {'description': "The unique identifier for a request",
                              'type': int,
                              'validate_fun': _isinstance}

request_keys['request_dict'] = {'description': "Name-value container containing steps/tasks for the given request",
                                'type': dict,
                                'validate_fun': _isinstance}
