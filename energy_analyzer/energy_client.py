import time
from enum import Enum
from typing import Dict, List, Union

from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

Timeseries = List[Dict[str, Union[int, datetime]]]


class MeasureType(Enum):
    SCHEDULING = 1
    SAT_RESET = 2
    LED_RETROFIT = 3
    AHU_VFD = 4


def round_to_last_15m(dt) -> datetime:
    return dt - (dt - datetime.min) % timedelta(minutes=15)


class EnergyClient:
    @staticmethod
    def get_building_expected_energy_usage(
        start: datetime, end: datetime, _building_name: str
    ) -> Timeseries:
        """
        This API call will return a list of dicts that represents timeseries data at 15 minute intervals.

        The start and end dates determine the range of the result.

        Ex. result:
        [
            {
                'timestamp': 2021-09-16 22:00:00,
                'value': 1000
            },
            ...
            {
                'timestamp': 2021-010-16 22:00:00,
                'value': 1000
            },
        ]
        """
        current_time = round_to_last_15m(start)
        results = []

        while current_time < end:
            results.append(
                {
                    "timestamp": current_time,
                    # This value is hard-coded in this example,
                    # but represents an energy prediction that would normally vary over time.
                    "value": 1000,
                }
            )

            current_time += relativedelta(minutes=15)

        # Not used for the at-home challenge
        # time.sleep(3)

        return results

    @staticmethod
    def get_measure_expected_energy_savings(
        measure_type: MeasureType, _measure_name: str
    ) -> Timeseries:
        """
        This API call will return a list of dicts that represents timeseries data at 15 minute intervals.

        The result represents the expected savings over an average year. The year will be set to `2010`, but
        that year should be ignored: this data represents an arbitrary year, not a specific year.

        Ex. result:
        [
            {
                'timestamp': 2010-01-01 00:00:00,
                'value': 200
            },
            ...
            {
                'timestamp': 2010-12-21 23:45:00,
                'value': 200
            },
        ]
        """
        # These values are hard-coded in this example, but represent an energy
        # savings prediction that would normally vary over time.
        # Your solution should account for situations where these values are not static.
        _SAVINGS_BY_MEASURE = {
            MeasureType.SCHEDULING: 100,
            MeasureType.SAT_RESET: 200,
            MeasureType.LED_RETROFIT: 300,
            MeasureType.AHU_VFD: 400,
        }

        current_time = datetime(year=2010, month=1, day=1)
        end = current_time + relativedelta(years=1)
        results = []

        while current_time < end:
            results.append(
                {"timestamp": current_time, "value": _SAVINGS_BY_MEASURE[measure_type]}
            )

            current_time += relativedelta(minutes=15)

        # Not used for the at-home challenge
        # time.sleep(3)

        return results
