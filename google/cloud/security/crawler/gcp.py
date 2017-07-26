# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

""" Crawler implementation. """


class ApiClient(object):
    def fetch_organization(self, orgid):
        raise NotImplementedError()

    def _iter_projects(self, orgid):
        raise NotImplementedError()

    def _iter_folders(self, orgid):
        raise NotImplementedError()

    def _iter_buckets(self, projectid):
        raise NotImplementedError()

    def _iter_projects_by_folder(self, folderid):
        raise NotImplementedError()

    def _iter_folders_by_folder(self, folderid):
        raise NotImplementedError()


class TestApiClient(ApiClient):

    def fetch_organization(self, orgid):
        data = {
                'fuubar': {
                        'id': 'fuubar',
                    }
            }
        return data[orgid]

    def _iter_projects(self, orgid):
        data = {
                'fuubar': [
                        {
                            'id': 'project-1',
                            },
                        {
                            'id': 'project-2',
                            },
                    ]
            }
        return self._iter_generic(orgid, data)

    def _iter_folders(self, orgid):
        data = {
                'fuubar': [
                        {
                            'id': 'folder-1',
                            },
                        {
                            'id': 'folder-2',
                            },
                    ]
            }
        return self._iter_generic(orgid, data)

    def _iter_buckets(self, projectid):
        data = {
            }
        return self._iter_generic(projectid, data)

    def _iter_objects(self, bucketid):
        data = {
            }
        return self._iter_generic(bucketid, data)

    def _iter_projects_by_folder(self, folderid):
        data = {
                'folder-1': [
                        {
                            'id': 'folder-1/project-1',
                            },
                    ]
            }
        return self._iter_generic(folderid, data)

    def _iter_folders_by_folder(self, folderid):
        data = {
            }
        return self._iter_generic(folderid, data)

    def _iter_generic(self, key, data):
        try:
            for item in data[key]:
                yield item
        except KeyError:
            for item in []:
                yield item