from __future__ import (absolute_import)

# imports needed for testing
import bson
import pytest
from nose.tools import assert_equal

# add source dir to path.  Shouldn't tox take care of this for me?
import sys
sys.path.append('./src/samplemanager')

import metadatastore.commands as mdsc
from metadatastore.api import Document
from samplemanager import commands as smc


def _type_tester(**kwargs):
    smt = smc._insert_type(**kwargs)
    q_ret = smc.find_types(_id=smt.id)[0]
    assert(bson.ObjectId(q_ret.id) == q_ret.id)

    doc = Document.from_mongo(smt)
    SMType.objects.get(id=smt.id)

    if kwargs is None:
        kwargs = dict()
#    assert_equal(kwargs, smt.)
    return smt

def test_type_insert():
    for kwargs in [{'owner': 'cowan',
                    'name': 'tsamp1',
                    'type_of': 'sample',
                    'is_class': False}]:
        tmp = _type_tester(**kwargs)
        yield tmp


if __name__ == '__main__':
    pytest.main()