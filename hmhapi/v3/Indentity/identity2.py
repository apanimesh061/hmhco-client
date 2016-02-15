from hmhapi.v3.ApiRequest.Requestor import Requestor

import logging
logger = logging.getLogger(__name__)


class Role(object):
    response = None
    access_token = None
    api_key = None

    def __init__(self):
        self.access_token = None
        self.api_key = None

    def set_access_token(self, access_token):
        self.access_token = access_token

    def set_api_key(self, api_key):
        self.api_key = api_key

    def set_response(self, response):
        self.response = response

    def get_response(self):
        return self.response

    def _get_all(self, role_uri):
        req = Requestor(
            access_token=self.access_token,
            api_key=self.api_key,
            info_uri=role_uri
        )
        req.send_request()
        self.set_response(req.get_response())

    def _get_role(self, role_uri, role_id, require_rosters=False, facet=None, include=None, pagination_range=None):
        current_params = dict()
        if facet:
            current_params["facet"] = facet
        if include:
            current_params["include"] = include
        if pagination_range:
            current_params["pagination_range"] = pagination_range

        req = Requestor(
            access_token=self.access_token,
            api_key=self.api_key,
            info_uri=role_uri,
            role_id=role_id,
            require_roster=require_rosters,
            **current_params
        )
        req.send_request()
        self.set_response(req.get_response())
