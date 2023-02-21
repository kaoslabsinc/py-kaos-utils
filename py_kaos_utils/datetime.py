import datetime as dt
import zoneinfo
from typing import Optional
from zoneinfo import ZoneInfo


class BaseDatetimeWrapper:
    def __init__(self,
                 raw_dt: dt.datetime,
                 raw_tz: Optional[str | ZoneInfo] = None):
        self._tz: Optional[ZoneInfo]
        self._dt: dt.datetime = raw_dt
        self.tz = raw_tz

    @property
    def tz(self) -> Optional[ZoneInfo]:
        return self._tz

    @tz.setter
    def tz(self, value: str | ZoneInfo | None):
        if value is None:
            self._tz = None
        elif isinstance(value, ZoneInfo):
            self._tz = value
        else:
            self._tz = zoneinfo.ZoneInfo(value)

    @property
    def dt(self):
        return self._dt.astimezone(self.tz) if self.tz else self._dt


class DatetimeWrapper(BaseDatetimeWrapper):
    raw_datetime: dt.datetime | str

    @property
    def parse(self):
        from dateutil import parser
        return parser.parse

    def __init__(self,
                 raw_dt: str | dt.datetime,
                 raw_tz: Optional[str | ZoneInfo] = None):
        if not isinstance(raw_dt, dt.date):
            raw_dt = self.parse(raw_dt)
        super().__init__(raw_dt, raw_tz)

    def strf(self, fmt: str = '%b %d, %Y - %I:%M %p %Z'):
        return self.dt.strftime(fmt)


DT = DatetimeWrapper

__all__ = (
    'BaseDatetimeWrapper',
    'DatetimeWrapper',
    'DT',
)
