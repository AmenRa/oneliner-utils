__all__ = [
    "join_path",
    #
    "read",
    "read_csv",
    "read_gzip",
    "read_gzip_list",
    "read_json",
    "read_jsonl",
    "read_list",
    "read_numpy",
    "read_pickle",
    #
    "load",
    "load_csv",
    "load_gzip",
    "load_gzip_list",
    "load_json",
    "load_jsonl",
    "load_list",
    "load_numpy",
    "load_pickle",
    #
    "write",
    "write_csv",
    "write_json",
    "write_jsonl",
    "write_list",
    "write_numpy",
    "write_pickle",
    #
    "save",
    "save_csv",
    "save_json",
    "save_jsonl",
    "save_list",
    "save_numpy",
    "save_pickle",
]

from .csv_handler import read_csv, write_csv
from .gzip_handler import read_gzip, read_gzip_list
from .json_handler import read_json, write_json
from .jsonl_handler import read_jsonl, write_jsonl
from .list_handler import read_list, write_list
from .numpy_handler import read_numpy, write_numpy
from .path_handler import join_path
from .pickle_handler import read_pickle, write_pickle
from .string_handler import read, write

# Aliases ======================================================================
# Read / Load ------------------------------------------------------------------
load = read
load_csv = read_csv
load_gzip = read_gzip
load_gzip_list = read_gzip_list
load_json = read_json
load_jsonl = read_jsonl
load_list = read_list
load_numpy = read_numpy
load_pickle = read_pickle
# Write / Save -----------------------------------------------------------------
save = write
save_csv = write_csv
save_json = write_json
save_jsonl = write_jsonl
save_list = write_list
save_numpy = write_numpy
save_pickle = write_pickle
