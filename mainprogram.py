#for standalone program
import requests
import os
import allfunction
import subprocess
import sys

current_version = open("version", "r").read()
print(current_version)

file_name = sys.argv[1]
updated_code_url = "https://raw.githubusercontent.com/agentswagt/Remote-Command-Executer---onHeart/master/sample/sample_code.py"

updated_source_code = allfunction.sdp(updated_code_url)
os.system("rm {}".format(file_name))

allfunction.file_saver("{}".format(file_name), updated_source_code)
