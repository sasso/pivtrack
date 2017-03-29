# -*- coding: utf-8 -*-

import os

PIVOTAL_TRACKER_API_KEY = os.getenv('PIVOTAL_TRACKER_API_KEY', '')

PIVOTAL_TRACKER_API_KEY_HEADER = 'X-TrackerToken'
PIVOTAL_TRACKER_API_BASE_URL = 'https://www.pivotaltracker.com/services/v5'
PIVOTAL_TRACKER_PROJECTS_ENPOINT = PIVOTAL_TRACKER_API_BASE_URL + '/projects'
PIVOTAL_TRACKER_EPICS_ENDPOINT = PIVOTAL_TRACKER_API_BASE_URL + '/projects/{project_id}/epics'
PIVOTAL_TRACKER_EPIC_ENDPOINT = PIVOTAL_TRACKER_API_BASE_URL + '/projects/{project_id}/epics/{epic_id}'

