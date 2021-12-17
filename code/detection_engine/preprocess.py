# -*- coding: utf-8 -*-
from tensorflow.keras.utils import to_categorical

# List to be converted
protocol_list = ['tcp', 'udp', 'icmp']
service_list = ['aol', 'auth', 'bgp', 'courier', 'csnet_ns', 'ctf', 'daytime', 'discard', 'domain', 'domain_u',
                        'echo', 'eco_i', 'ecr_i', 'efs', 'exec', 'finger', 'ftp', 'ftp_data', 'gopher', 'harvest',
                        'hostnames',
                        'http', 'http_2784', 'http_443', 'http_8001', 'imap4', 'IRC', 'iso_tsap', 'klogin', 'kshell',
                        'ldap',
                        'link', 'login', 'mtp', 'name', 'netbios_dgm', 'netbios_ns', 'netbios_ssn', 'netstat', 'nnsp',
                        'nntp',
                        'ntp_u', 'other', 'pm_dump', 'pop_2', 'pop_3', 'printer', 'private', 'red_i', 'remote_job',
                        'rje',
                        'shell',
                        'smtp', 'sql_net', 'ssh', 'sunrpc', 'supdup', 'systat', 'telnet', 'tftp_u', 'tim_i', 'time',
                        'urh_i', 'urp_i',
                        'uucp', 'uucp_path', 'vmnet', 'whois', 'X11', 'Z39_50']
connect_status_list = ['OTH', 'REJ', 'RSTO', 'RSTOS0', 'RSTR', 'S0', 'S1', 'S2', 'S3', 'SF', 'SH']
label_list = ['normal.', 'buffer_overflow.', 'loadmodule.', 'perl.', 'neptune.', 'smurf.',
                      'guess_passwd.', 'pod.', 'teardrop.', 'portsweep.', 'ipsweep.', 'land.', 'ftp_write.',
                      'back.', 'imap.', 'satan.', 'phf.', 'nmap.', 'multihop.', 'warezmaster.', 'warezclient.',
                      'spy.', 'rootkit.']


# Data preprocessing function
def preprocess_data(data):
    # Convert the three protocol types in the source file line to numbers
    def deal_protocol_types(keyword):
        tmp = bytes.decode(keyword[1])
        if tmp in protocol_list:
            return protocol_list.index(tmp)

    # Convert 70 network service types in the source file line to numbers
    def deal_service_types(keyword):
        tmp = bytes.decode(keyword[2])
        if tmp in service_list:
            return service_list.index(tmp)

    # Convert the 11 network connection states in the source file line to numbers
    def deal_connect_status(keyword):
        tmp = bytes.decode(keyword[3])
        if tmp in connect_status_list:
            return connect_status_list.index(tmp)

    # Data cleaning
    data_list = data
    for i in range(data.shape[0]):
        row = data[i]
        # Convert the three protocol types in the source file line to digital ID
        data_list[i][1] = deal_protocol_types(row)
        # Convert 70 network service types in the source file line to digital identification
        data_list[i][2] = deal_service_types(row)
        # Convert 11 network connection states in the source file line to digital identification
        data_list[i][3] = deal_connect_status(row)
    return data_list


def preprocess_data_target(target_data):
    # Define the function to convert the attack types in the source file line into digital identification
    # (there are 22 attack types in the training set, while the remaining 17 types only appear in the test set)
    def handleLabel(label):
        tmp = bytes.decode(label)
        if tmp in label_list:
            return label_list.index(tmp)

    target_data_list = target_data
    for i in range(target_data.shape[0]):
        row = target_data[i]
        # Convert 23 attack types in the source file line to digital identification
        target_data_list[i] = handleLabel(row)
    return to_categorical(target_data_list)


if __name__ == '__main__':
    pass