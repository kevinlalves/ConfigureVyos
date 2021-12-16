import netmiko
import re


class ConfigureVyos(object):

    def __init__(self, host, user, port=22):
        vyos_router = {
            'device_type': 'vyos',
            'host': host,
            'username': user,
            'key_file': 'sut/id_rsa',
            'port': port,
        }
        self.net_connect = netmiko.ConnectHandler(**vyos_router)

    def send_configuration(self, config_file):
        output = self.net_connect.send_config_from_file(config_file)
        return output


if __name__ == '__main__':
    device_file = open('device.txt', 'r')
    config_file = 'config.txt'
    line = device_file.readline()
    while line != '':
        line = re.split(' ', line)
        if(line[-1] == '\n'):
            del line[-1]
        print(f'Output from {line[0]}\n')
        args = line[1:]
        print(ConfigureVyos(*args).send_configuration(config_file))
        print('\n\n')
        line = device_file.readline()

    