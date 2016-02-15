from hmhapi.constants import *
from identity2 import *

import logging
logger = logging.getLogger(__name__)


class Student(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(Student, self)._get_all(role_uri=V3_STUDENT_INFO)

    def get_role(self, role_id=None, require_rosters=False, facet=None, include=None, pagination_range=None):
        if require_rosters:
            logger.debug("Requesting rosters for", self.__class__.__name__, "role having refID %s" % role_id)
        else:
            logger.debug("Requesting", self.__class__.__name__, "role having refID %s" % role_id)
        super(Student, self)._get_role(
            role_uri=V3_STUDENT_INFO,
            role_id=role_id,
            require_rosters=require_rosters,
            facet=facet,
            include=include,
            pagination_range=pagination_range
        )


class Me(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(Me, self)._get_all(role_uri=V3_ME_INFO)


class Staff(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(Staff, self)._get_all(role_uri=V3_STAFF_INFO)

    def get_role(self, role_id=None, require_rosters=False, facet=None, include=None, pagination_range=None):
        if require_rosters:
            logger.debug("Requesting rosters for", self.__class__.__name__, "role having refID %s" % role_id)
        else:
            logger.debug("Requesting", self.__class__.__name__, "role having refID %s" % role_id)
        super(Staff, self)._get_role(
            role_uri=V3_STUDENT_INFO,
            role_id=role_id,
            require_rosters=require_rosters,
            facet=facet,
            include=include,
            pagination_range=pagination_range
        )


class Roster(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(Roster, self)._get_all(role_uri=V3_STAFF_INFO)

    def get_role(self, role_id=None, require_rosters=False, facet=None, include=None, pagination_range=None):
        if require_rosters:
            logger.debug("Requesting rosters for", self.__class__.__name__, "role having refID %s" % role_id)
        else:
            logger.debug("Requesting", self.__class__.__name__, "role having refID %s" % role_id)
        super(Roster, self)._get_role(
            role_uri=V3_STUDENT_INFO,
            role_id=role_id,
            require_rosters=require_rosters,
            facet=facet,
            include=include,
            pagination_range=pagination_range
        )


class Section(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(Section, self)._get_all(role_uri=V3_STAFF_INFO)


class School(Role):
    def get_all(self):
        logger.debug("Requesting all", self.__class__.__name__, "type roles")
        super(School, self)._get_all(role_uri=V3_STAFF_INFO)
