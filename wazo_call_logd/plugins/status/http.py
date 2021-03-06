# Copyright 2018-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from wazo_call_logd.auth import required_acl
from wazo_call_logd.http import AuthResource


class StatusResource(AuthResource):
    def __init__(self, status_aggregator):
        self.status_aggregator = status_aggregator

    @required_acl('call-logd.status.read')
    def get(self):
        return self.status_aggregator.status(), 200
