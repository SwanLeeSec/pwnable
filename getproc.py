# for get Windows Function Address

import sys
from ctypes import *
import ctypes

def usage():
	print  "\n # Get Function Address from hyunmini, fixed by pathFindar # \n"
	print "Usage : %s [dll] [proc]" % sys.argv[0]
	sys.exit()
if len(sys.argv) < 2:
	usage()
target_dll = sys.argv[1]
target_function = sys.argv[2]
dll = windll.LoadLibrary(target_dll)
function = dll.GetProcAddress(dll._handle, target_function)
print "[##] Find Address %s(%s) : 0x%08x" % \
	(target_dll,target_function,fuction)
