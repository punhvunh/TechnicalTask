import json
import os

from path_for_the_directory_of_the_script_being_run import path_for_the_directory_of_the_script_being_run


class Utilities:

    @staticmethod
    def assert_value(input_value, output_value, exception_text):
        assert input_value == output_value, f'{exception_text}'
        print("Assert pass: success")

    @staticmethod
    def gets_data_from_json_file(filename):
        file_path = os.path.join(path_for_the_directory_of_the_script_being_run(), 'files', 'json_files', filename)
        with open(file_path, encoding='utf-8') as f:
            return json.load(f)
