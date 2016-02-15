import sys

import requests
from requests import exceptions

from hmhapi.constants import *

import logging
logger = logging.getLogger(__name__)


class Requestor(object):
    info_uri = None
    role_id = None
    response = None
    require_roster = None
    facet = None
    include = None
    pagination_range = None
    current_params = dict()

    def __init__(self, access_token, api_key, info_uri, role_id=None, require_roster=False, **kwargs):
        self._validate_input(access_token, api_key, info_uri, role_id, require_roster, **kwargs)

        self.info_uri = info_uri
        self._set_access_token(access_token)
        self._set_api_key(api_key)
        self.role_id = role_id
        self.require_roster = require_roster
        self._set_params(kwargs)

    @staticmethod
    def _validate_input(access_token, api_key, info_uri, role_id, require_roster, **kwargs):
        assert isinstance(access_token, (str, unicode)), access_token
        assert isinstance(api_key, (str, unicode)), api_key
        assert isinstance(info_uri, (str, unicode)), info_uri
        if role_id:
            assert isinstance(role_id, (str, unicode)), role_id
        assert isinstance(require_roster, bool), require_roster
        assert isinstance(kwargs, dict), kwargs

    def _set_params(self, params):
        if "facet" in params:
            assert isinstance(params.get("facet"), list)
            self.facet = params.get("facet")
            self.current_params["facet"] = ",".join(self.facet)

        if "include" in params:
            assert isinstance(params.get("include"), list)
            self.include = params.get("include")
            self.current_params["include"] = ",".join(self.include)

        if "pagination_range" in params:
            assert isinstance(params.get("pagination_range"), tuple)
            self.pagination_range = params.get("pagination_range")
            self.current_params["page[page]"] = self.pagination_range[0]
            self.current_params["page[page_size]"] = self.pagination_range[1]

    def _set_access_token(self, access_token):
        assert isinstance(access_token, (str, unicode)), access_token
        self.access_token = access_token

    def _set_api_key(self, api_key):
        assert isinstance(api_key, (str, unicode)), api_key
        self.api_key = api_key

    def _construct_request_url(self):
        if self.role_id:
            if self.require_roster:
                current_url = BASE_URL + self.info_uri + "/" + self.role_id + "/" + ROSTERS_NAME
            else:
                current_url = BASE_URL + self.info_uri + "/" + self.role_id
        else:
            current_url = BASE_URL + self.info_uri
        return current_url

    def send_request(self):
        headers = {
            "Vnd-HMH-Api-Key": self.api_key,
            "Authorization": self.access_token,
            "Accept": "application/json",
            "Content-Type": "application/json"
        }
        current_url = self._construct_request_url()
        print self.current_params
        logger.debug("Current request URl is %s" % current_url)
        logger.debug("Current GET params are %s" % self.current_params)

        try:
            if len(self.current_params):
                r = requests.get(url=current_url, headers=headers, params=self.current_params)
            else:
                r = requests.get(url=current_url, headers=headers)
            r.raise_for_status()
            print r.url
            logger.debug("Current request URl is %s" % r.url)
            self.response = r
        except exceptions.RequestException as e:
            print e
            sys.exit(-1)

    def get_response(self):
        return self.response.json()
