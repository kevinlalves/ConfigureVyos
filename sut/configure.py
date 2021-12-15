import netmiko
import sys

class ConfigureVyos(object):

    def __init__(self, host, user, port):
        vyos_router = {
            'device_type': 'vyos',
            'host': host,
            'username': user,
            'key_file': 'id_rsa',
            'port': port,
        }
        self.net_connect = netmiko.ConnectHandler(**vyos_router)

    def check_connection(self):
        return self.net_connect.send_command('hostname')

    def send_configuration(self, configs):
        output = self.net_connect.send_config_set(configs, exit_config_mode=False)
        self.net_connect.commit()
        self.net_connect.exit_config_mode()
        return output


def check_connection(host, user, port):
    return ConfigureVyos(host, user, port).check_connection()


def send_configuration(host, user, port, *configs):
    return ConfigureVyos(host, user, port).send_configuration(configs)

if __name__ == '__main__':
    actions = {'check': check_connection, 'config': send_configuration}
    action = sys.argv[1]
    args = sys.argv[2:]
    actions[action](*args)
    