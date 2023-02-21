import datetime as dt
from zoneinfo import ZoneInfo

import pytest

from py_kaos_utils.datetime import DT


class TestBaseDatetimeWrapper:
    @pytest.fixture
    def raw_dt(self):
        return dt.datetime(2022, 1, 1, 12, 30, 0)

    @pytest.fixture
    def raw_tz_str(self):
        return 'US/Pacific'

    @pytest.fixture
    def raw_tz_zoneinfo(self):
        return ZoneInfo('US/Pacific')

    def test_tz_is_set__raw_tz_empty(self, raw_dt):
        dtw = DT(raw_dt)
        assert dtw.tz is None

    def test_tz_is_set__raw_tz_None(self, raw_dt):
        dtw = DT(raw_dt, None)
        assert dtw.tz is None

    def test_tz_is_set__raw_tz_str(self, raw_dt, raw_tz_str):
        dtw = DT(raw_dt, raw_tz_str)
        assert dtw.tz is ZoneInfo('US/Pacific')

    def test_tz_is_set__raw_tz_zoneinfo(self, raw_dt, raw_tz_zoneinfo):
        dtw = DT(raw_dt, raw_tz_zoneinfo)
        assert dtw.tz is ZoneInfo('US/Pacific')

    def test_dt__raw_tz_empty(self, raw_dt):
        dtw = DT(raw_dt)
        assert dtw.dt == dt.datetime(2022, 1, 1, 12, 30, 0)

    def test_dt__raw_tz_set(self, raw_dt, raw_tz_str):
        dtw = DT(raw_dt, raw_tz_str)
        assert dtw.dt == dt.datetime(2022, 1, 1, 12, 30, tzinfo=ZoneInfo('US/Pacific'))
