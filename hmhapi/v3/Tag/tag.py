import sys

import requests
from requests import exceptions

from hmhapi.constants import *


class Requestor(object):
    base_url = None
    info_uri = None
    role_id = None
    response = None

    def __init__(self, access_token, api_key, base_url, info_uri, require_roster=False, role_id=None):
        self.base_url = base_url
        self.info_uri = info_uri
        self._set_access_token(access_token)
        self._set_api_key(api_key)
        self.role_id = role_id
        self.require_roster = require_roster

    def _set_access_token(self, access_token):
        assert isinstance(access_token, (str, unicode)), access_token
        self.access_token = access_token

    def _set_api_key(self, api_key):
        assert isinstance(api_key, (str, unicode)), api_key
        self.api_key = api_key

    def set_request(self):
        headers = {
            "Vnd-HMH-Api-Key": self.api_key,
            "Authorization": self.access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        if self.role_id:
            if self.require_roster:
                current_url = self.base_url + self.info_uri + "/" + self.role_id + "/" + ROSTERS_NAME
            else:
                current_url = self.base_url + self.info_uri + "/" + self.role_id
        else:
            current_url = self.base_url + self.info_uri
        try:
            r = requests.get(url=current_url, headers=headers)
            r.raise_for_status()
            self.response = r
        except exceptions.RequestException as e:
            print e
            sys.exit(-1)

    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response.json()


class Document(object):
    response = None

    def __init__(self):
        self.access_token = None
        self.api_key = None

    def set_access_token(self, access_token):
        assert isinstance(access_token, (str, unicode)), access_token
        self.access_token = access_token

    def set_api_key(self, api_key):
        assert isinstance(api_key, (str, unicode)), api_key
        self.api_key = api_key

    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response

    def get_all(self):
        print "Requesting all", self.__class__.__name__, "type roles"
        req = Requestor(access_token=self.access_token, api_key=self.api_key, base_url=BASE_URL,
                        info_uri=V3_DOCUMENT_INFO)
        req.set_request()
        self.set_response(req.get_response())

    def get_by_id(self, role_id=None, get_rosters=False):
        if get_rosters:
            print "Requesting rosters for", self.__class__.__name__, "role having refID", role_id
        else:
            print "Requesting", self.__class__.__name__, "role having refID", role_id
        req = Requestor(access_token=self.access_token, api_key=self.api_key, base_url=BASE_URL,
                        info_uri=V3_DOCUMENT_INFO, role_id=role_id, require_roster=get_rosters)
        req.set_request()
        self.set_response(req.get_response())
