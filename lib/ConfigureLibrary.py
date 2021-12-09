import os.path
import subprocess
import sys

class ConfigureLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__), '..', 'sut', 'configure.py')
        self._status = ''
    
    def access_vyos(self, user, address):
        self._run_command('access', user, address)

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(*args)
        process = subprocess.Popen(command, universal_newlines=True, stdout=subprocess.PIPE,
                                    stderr=subprocess.STDOUT)
        self._status = process.communicate()[0].strip()