import os.path
import subprocess
import sys

class ConfigureLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__), '..', 'sut', 'configure.py')
        self._status = ''
    
    def check_connection(self, host, user, port='22'):
        self._run_command('check', host, user, port)

    def send_configuration(self, host, user, configs, port='22'):
        self._run_command('config', host, user, port, *configs)

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        self._status = subprocess.run(command, universal_newlines=True)
        