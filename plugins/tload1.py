from __future__ import absolute_import
from utils.util import parametrized


class Article(object):

    @parametrized('api')
    def test_route(self, param):
        print param
        print self

    def test_isolation(self):
        pass
