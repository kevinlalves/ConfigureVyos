import sys
import netmiko
import re


class VyosFunctionality(object):

    def __init__(self, host, user, port):
        vyos_router = {
            'device_type': 'vyos',
            'host': host,
            'username': user,
            'key_file': 'sut/id_rsa',
            'port': port
        }
        self.ssh_connection = netmiko.ConnectHandler(**vyos_router)
    
    def vyos_ping(self, destination_host):
        return self.ssh_connection.send_command(f'ping {destination_host}', re.compile('icmp_seq=10', max_loops=60))


def vyos_ping(host, user, port, destination_host):
    return VyosFunctionality(host, user, port).vyos_ping(destination_host)

if __name__ == '__main__':
    actions = {'ping': vyos_ping}
    action = sys.argv[1]
    args = sys.argv[2:]
    print(actions[action](*args))