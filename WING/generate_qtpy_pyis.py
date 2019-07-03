# Script to generate *.pyi files for Qt.py
# Must run this using the Python that has Qt.py and output is into current directory

# With some help from Stephan Deibel
# of Wingware, I got auto completion of
# Qt.py working in WING IDE using this
# interface file (pointed to in Source
# Analysis) and a collection of PYI files
# generated using a WING utility.

# Questions to iam@nimajneb.com if you're
# using wing and need to get this working.

import sys
import os

try: 
  import Qt
except:
  # customization for local install
  sys.path.append(os.path.normpath(r'Y:\benjamin\Qt.py'))
  sys.path.append(os.path.normpath(r'X:\lib\python27\site-packages'))
  import Qt

WINGHOME = os.path.normpath(r'C:\Program Files (x86)\Wing Pro 7.0')
GEN_PI = r'/src/wingutils/generate_pi.py'.replace('/', '\\')
SCRIPT = os.path.normpath(WINGHOME + GEN_PI)

cmd = '{} "{}"'.format(sys.executable, os.path.normpath(SCRIPT))

for mod in Qt._common_members:
  if mod == 'QtX11Extras':
    continue
  cmdline = '{} Qt.{} {}.pyi'.format(cmd, mod, mod)
  os.system(cmdline)
  
