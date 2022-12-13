import platform
from collections import namedtuple
import sys
Version = namedtuple("Version", ['major', 'minor',
'patchlevel'])
nt = Version._make(platform.python_version_tuple())

print (nt)
print (nt.major)
print (nt[1])
od = nt._asdict()
print (od.keys())
for k, v in od.items():
 print ("%-10s: %s" % (k, v))