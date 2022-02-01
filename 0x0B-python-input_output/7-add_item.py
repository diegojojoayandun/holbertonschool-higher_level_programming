#!/usr/bin/python3
"""module 7-add_item - adds an item"""


from sys import argv
from pathlib import Path


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


list_result = []

file_ok = Path("add_item.json")
if file_ok.is_file():
    str_py = load_from_json_file("add_item.json")
    list_result += str_py

list_argv = argv
del list_argv[0]
list_result += list_argv

save_to_json_file(list_result, "add_item.json")
