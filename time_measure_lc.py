import subprocess
import sys
import os
import shutil
import time

files = os.listdir('./source')

for file in files:
	try:
		subprocess.run('./lzma_comp < source/' + file + " >lzma_/comp_" + file, shell=True)
	except subprocess.CalledProcessError as e:
		print()