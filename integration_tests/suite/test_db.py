# Copyright 2017-2020 The Wazo Authors  (see the AUTHORS file)
# SPDX-License-Identifier: GPL-3.0-or-later

from hamcrest import (
    assert_that,
    empty,
    has_entry,
)
from xivo_test_helpers import until

from .helpers.base import IntegrationTest


class TestDatabase(IntegrationTest):
    asset = 'base'

    def restart_postgres(cls):
        cls.restart_service('postgres', signal='SIGINT')  # fast shutdown
        cls.reset_clients()
        until.true(
            cls.database.is_up, timeout=5, message='Postgres did not come back up'
        )

    def test_query_after_database_restart(self):
        result1 = self.call_logd.cdr.list()

        self.restart_postgres()

        result2 = self.call_logd.cdr.list()

        assert_that(result1, has_entry('items', empty()))
        assert_that(result2, has_entry('items', empty()))
