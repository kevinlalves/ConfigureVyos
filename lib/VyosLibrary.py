import os.path
import subprocess
import sys

NUM_PACKETS = '10'

class VyosLibrary(object):

    def __init__(self):
        self._sut_path = os.path.join(os.path.dirname(__file__), '..', 'sut', 'vyos.py')
        self._status = ''
    
    def host_vyos_ping(self, host):
        self._run_internal_command('ping', '-c', NUM_PACKETS, host)

    def vyos_ping(self, host, user, destination_host, port='22'):
        self._run_command('ping', host, user, port, destination_host)

    def _run_command(self, command, *args):
        command = [sys.executable, self._sut_path, command] + list(args)
        self._status = subprocess.run(command, universal_newlines=True, timeout=10)
        return self._status.stdout

    def _run_internal_command(self, command, *args):
        command = [command] + list(args)
        self._status = subprocess.run(command, universal_newlines=True)
        return self._status.stdout
        