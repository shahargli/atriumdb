from abc import ABC, abstractmethod
from typing import List, Dict, Tuple


class SQLHandler(ABC):
    @abstractmethod
    def create_schema(self):
        # Creates Tables if they dont exist.
        pass

    @abstractmethod
    def interval_exists(self, measure_id, device_id, start_time_nano):
        pass

    @abstractmethod
    def select_all_devices(self):
        pass

    @abstractmethod
    def select_all_measures(self):
        pass

    @abstractmethod
    def insert_measure(self, measure_tag: str, freq_nhz: int, units: str = None, measure_name: str = None):
        # Insert measure if it doesn't exist, return id.
        pass

    @abstractmethod
    def select_measure(self, measure_id: int = None, measure_tag: str = None, freq_nhz: int = None, units: str = None):
        # Select a measure either by its id, or by a tag, freq, units triplet.
        pass

    @abstractmethod
    def insert_device(self, device_tag: str, device_name: str = None):
        # Insert device if it doesn't exist, return id.
        pass

    @abstractmethod
    def select_device(self, device_id: int = None, device_tag: str = None):
        # Select a measure either by its id, or by its unique tag.
        pass

    @abstractmethod
    def insert_tsc_file_data(self, file_path: str, block_data: List[Dict], interval_data: List[Dict]):
        # Insert a file path to file index.
        # Insert block_index rows with foreign key file_id.
        # Insert interval_index rows.
        pass

    @abstractmethod
    def update_tsc_file_data(self, file_data: Dict[str, Tuple[List[Dict], List[Dict]]], block_ids_to_delete: List[int],
                             file_ids_to_delete: List[int]):
        pass

    @abstractmethod
    def select_file(self, file_id: int = None, file_path: str = None):
        # Select a file path either by its id, or by its path.
        pass

    @abstractmethod
    def select_files(self, file_id_list: List[int]):
        # Selects all files from list of ids.
        pass

    @abstractmethod
    def select_blocks_from_file(self, file_id: int):
        # Selects all blocks from file_id
        pass

    @abstractmethod
    def select_block(self, block_id: int = None, measure_id: int = None, device_id: int = None, file_id: int = None,
                     start_byte: int = None, num_bytes: int = None, start_time_n: int = None, end_time_n: int = None,
                     num_values: int = None):
        # select a block either by its id or by all other params.
        pass

    @abstractmethod
    def select_interval(self, interval_id: int = None, measure_id: int = None, device_id: int = None,
                        start_time_n: int = None, end_time_n: int = None):
        # Select an interval either by its id, or by all other params.
        pass

    @abstractmethod
    def insert_setting(self, setting_name: str, setting_value: str):
        # Inserts a setting into the database.
        pass

    @abstractmethod
    def select_setting(self, setting_name: str):
        # Selects a setting from the database.
        pass

    @abstractmethod
    def insert_patient(self, mrn: str, gender: str = None, dob: str = None, first_name: str = None,
                       middle_name: str = None, last_name: str = None, first_seen: int = None, last_updated: int = None,
                       source_id: int = 1):
        # Insert patient if it doesn't exist, return id.
        pass

    @abstractmethod
    def insert_encounter(self, patient_id: int, bed_id: int, start_time: int, end_time: int = None, source_id: int = 1,
                         visit_number: int = None, last_updated: int = None):
        # Insert encounter if it doesn't exist, return id.
        pass

    @abstractmethod
    def insert_device_encounter(self, device_id: int, encounter_id: int, start_time: int, end_time: int = None,
                                source_id: int = 1):
        # Insert device_encounter if it doesn't exist, return id.
        pass

    @abstractmethod
    def select_all_settings(self):
        # Select all settings from settings table.
        pass

    @abstractmethod
    def insert_source(self, s_name: str, description: str = None):
        # Insert source if it doesn't exist, return id.
        pass

    @abstractmethod
    def insert_institution(self, i_name: str):
        # Insert institution if it doesn't exist, return id.
        pass

    @abstractmethod
    def insert_unit(self, institution_id: int, u_name: str, u_type: str):
        # Insert unit if it doesn't exist, return id.
        pass

    @abstractmethod
    def insert_bed(self, unit_id: int, b_name: str):
        # Insert bed if it doesn't exist, return id.
        pass

    @abstractmethod
    def select_blocks(self, measure_id, start_time_n=None, end_time_n=None, device_id=None, patient_id=None):
        # Get all matching blocks.
        pass

    @abstractmethod
    def select_intervals(self, measure_id, start_time_n=None, end_time_n=None, device_id=None, patient_id=None):
        # Get all matching intervals.
        pass
