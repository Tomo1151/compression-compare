import subprocess
import sys
import os
import shutil
import time

files = os.listdir('./source')

for file in files:
	try:
		subprocess.run('./zlibc d zlib_/comp_' + file + " zlib_/decomp_" + file, shell=True)
	except subprocess.CalledProcessError as e:
		print()