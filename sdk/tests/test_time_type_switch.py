import numpy as np

from atriumdb import AtriumSDK
from tests.testing_framework import _test_for_both

DB_NAME = 'time_type_switch'


def test_time_type_switch():
    _test_for_both(DB_NAME, _test_time_type_switch)


def _test_time_type_switch(db_type, dataset_location, connection_params):
    sdk = AtriumSDK.create_dataset(
        dataset_location=dataset_location, database_type=db_type, connection_params=connection_params)

    # Create Raw Data
    start_time_s = 1234567890
    start_time_nano = start_time_s * (10 ** 9)

    freq_hz = 500
    freq_nhz = freq_hz * (10 ** 9)

    period_ns = (10 ** 18) // freq_nhz

    num_values = 1_000_000

    gap_data = [10_000, 24_000_000, 12_000, 138_000_000, 54_403, 34_560_000_000, 104_903, 56_530_000_000]
    gap_data = np.array(gap_data, dtype=np.int64)
    timestamp_arr = np.arange(start_time_nano, start_time_nano + (num_values * period_ns), period_ns, dtype=np.int64)

    # Add the gaps
    for i in range(gap_data.size // 2):
        index = gap_data[(i * 2)]
        gap = gap_data[(i * 2) + 1]

        timestamp_arr[index:] += gap

    # Create values
    values = (1000 * np.sin(timestamp_arr)).astype(np.int64)

    end_time_nano = int(timestamp_arr[-1]) + period_ns

    measure_id = sdk.insert_measure(measure_tag="sig1", freq=freq_nhz, units="mV")
    device_id = sdk.insert_device(device_tag="dev1")

    sdk.write_data_easy(measure_id, device_id, gap_data, values, freq=freq_nhz)

    # Check time type 2
    _, r_times, r_values = sdk.get_data(
        measure_id, start_time_nano, end_time_nano, device_id=device_id, time_type=2, analog=False)

    assert np.array_equal(r_times, gap_data)
    assert np.array_equal(r_values, values)

    # Check time type 1
    _, r_times, r_values = sdk.get_data(
        measure_id, start_time_nano, end_time_nano, device_id=device_id, time_type=1, analog=False)

    assert np.array_equal(r_times, timestamp_arr)
    assert np.array_equal(r_values, values)

