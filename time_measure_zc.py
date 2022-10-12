import subprocess
import sys
import os
import shutil
import time

files = os.listdir('./source')

for file in files:
	try:
		subprocess.run('./zlibc c source/' + file + " zlib_/comp_" + file, shell=True)
	except subprocess.CalledProcessError as e:
		print()