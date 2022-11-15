__all__ = [
    "create_path",
    "join_path",
    #
    "read",
    "read_csv",
    "read_gzip",
    "read_gzip_list",
    "read_gzip_json_list",
    "read_json",
    "read_jsonl",
    "read_list",
    "read_lz4",
    "read_numpy",
    "read_pickle",
    #
    "load",
    "load_csv",
    "load_gzip",
    "load_gzip_list",
    "load_gzip_json_list",
    "load_json",
    "load_jsonl",
    "load_list",
    "write_lz4",
    "load_numpy",
    "load_pickle",
    #
    "write",
    "write_csv",
    "write_gzip",
    "write_gzip_list",
    "write_gzip_json_list",
    "write_json",
    "write_jsonl",
    "write_list",
    "write_lz4",
    "write_numpy",
    "write_pickle",
    #
    "save",
    "save_csv",
    "save_gzip",
    "save_gzip_list",
    "save_gzip_json_list",
    "save_json",
    "save_jsonl",
    "save_list",
    "save_lz4",
    "save_numpy",
    "save_pickle",
]

from .handlers.csv_handler import read_csv, write_csv
from .handlers.gzip_handler import (
    read_gzip,
    read_gzip_json_list,
    read_gzip_list,
    write_gzip,
    write_gzip_json_list,
    write_gzip_list,
)
from .handlers.json_handler import read_json, write_json
from .handlers.jsonl_handler import read_jsonl, write_jsonl
from .handlers.list_handler import read_list, write_list
from .handlers.lz4_handler import read_lz4, write_lz4
from .handlers.numpy_handler import read_numpy, write_numpy
from .handlers.path_handler import create_path, join_path
from .handlers.pickle_handler import read_pickle, write_pickle
from .handlers.string_handler import read, write

# Aliases ======================================================================
# Read / Load ------------------------------------------------------------------
load = read
load_csv = read_csv
load_gzip = read_gzip
load_gzip_list = read_gzip_list
load_gzip_json_list = read_gzip_json_list
load_json = read_json
load_jsonl = read_jsonl
load_list = read_list
load_lz4 = read_lz4
load_numpy = read_numpy
load_pickle = read_pickle
# Write / Save -----------------------------------------------------------------
save = write
save_csv = write_csv
save_gzip = write_gzip
save_gzip_list = write_gzip_list
save_gzip_json_list = write_gzip_json_list
save_json = write_json
save_jsonl = write_jsonl
save_list = write_list
save_lz4 = write_lz4
save_numpy = write_numpy
save_pickle = write_pickle
