import os
import sys
script_dir = os.path.dirname(__file__)
mymodule_dir = os.path.join(script_dir, '..', 'controllers')
sys.path.append(mymodule_dir)