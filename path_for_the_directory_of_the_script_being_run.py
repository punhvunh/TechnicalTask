import pathlib


def path_for_the_directory_of_the_script_being_run():
    path = pathlib.Path(__file__).parent.resolve()
    return path
