import datetime as dt
import zoneinfo
from typing import Optional


class DatetimeWrapperInterface:
    def _format(self, fmt: str):
        raise NotImplementedError

    def format(self):
        raise NotImplementedError


class BaseDatetimeWrapper(DatetimeWrapperInterface):
    def __init__(self, raw_datetime, timezone_str=None):
        self.raw_datetime: dt.datetime = raw_datetime
        self.timezone_str: Optional[str] = timezone_str

    @property
    def zoneinfo(self):
        return self.timezone_str and zoneinfo.ZoneInfo(self.timezone_str)

    @property
    def datetime(self):
        return self.raw_datetime.astimezone(self.zoneinfo) if self.zoneinfo else self.raw_datetime

    def _format(self, fmt: str):
        return self.datetime.strftime(fmt)


class STRFFormatsMixin(DatetimeWrapperInterface):
    local = '%c'
    main = '%b %d, %Y - %I:%M %p %Z'
    f1 = '%Y-%m-%d %I:%M %p %Z'

    def format(self):
        return self.format_main()

    def format_local(self):
        return self._format(self.local)

    def format_main(self):
        return self._format(self.main)

    def format_f1(self):
        return self._format(self.f1)


class DatetimeWrapper(
    BaseDatetimeWrapper,
    STRFFormatsMixin,
):
    raw_datetime: dt.datetime | str

    @property
    def parse(self):
        from dateutil import parser
        return parser.parse

    def __init__(self, raw_datetime, timezone_str=None):
        if not isinstance(raw_datetime, dt.date):
            self.raw_datetime = self.parse(raw_datetime)
        super().__init__(raw_datetime, timezone_str)


DT = DatetimeWrapper

__all__ = (
    'BaseDatetimeWrapper',
    'STRFFormatsMixin',
    'DatetimeWrapper',
    'DT',
)
