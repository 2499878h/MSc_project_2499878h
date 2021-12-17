# -*- coding: utf-8 -*-
import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
from keras.models import load_model
import preprocess
import numpy as np

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


def re_preprocess_data(data):
    def re_deal_protocol_types(keyword):
        tmp = keyword[1]
        if tmp in protocol_list:
            return protocol_list.index(tmp)

    def re_deal_service_types(keyword):
        tmp = keyword[2]
        if tmp in service_list:
            return service_list.index(tmp)

    def re_deal_connect_status(keyword):
        tmp = keyword[3]
        if tmp in connect_status_list:
            return connect_status_list.index(tmp)

    data_list = data
    row = data
    data_list[1] = re_deal_protocol_types(row)
    data_list[2] = re_deal_service_types(row)
    data_list[3] = re_deal_connect_status(row)
    return data_list


def format_input():
    # row = np.array(input().split(","))
    row = np.array(sys.argv[1].split(","))
    row = re_preprocess_data(row)
    row = list(map(float, row))
    # print(row)
    # One dimensional list
    return row


def write_text_clean(strings: str, filepath: str) -> None:
    # The path of strings is PCAP.
    # The path of filepath is TEXT's path.

    ftxt = open(filepath, 'w')
    ftxt.write(strings + '\n')
    ftxt.close()
    return None


def write_text(strings: str, filepath: str) -> None:
    # The path of strings is PCAP.
    # The path of filepath is TEXT's path.

    ftxt = open(filepath, 'a')
    ftxt.write(strings + '\n')
    ftxt.close()
    return None


if __name__ == '__main__':
    # For example
    # python run.py 0,udp,private,SF,105,146,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,0.0,0.0,0.0,0.0,1.0,0.0,0.0,255,254,1.0,0.01,0.0,0.0,0.0,0.0,0.0,0.0
    model = load_model('./script/model.h5')
    # print('Model is restoring...')
    temp_list = []

    # Format input and convert to two dimensional list
    temp_list.append(format_input())

    # test
    # row = [[0.0, 1.0, 9.0, 9.0, 45.0, 110.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0, 9.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.44, 255.0, 246.0, 0.96, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]

    temp_list = np.array(temp_list)

    #predict = model.predict(row)
    # print(predict)
    temp_list = (model.predict(temp_list)).astype(float).ravel()

    # Show the probability of behavior analysis and prediction

    write_text_clean("###\nThe analysis results of behavior detection model are as follows:", "./script/test.txt")

    for i in range(23):
        write_text("{}:{:.3f}%".format(label_list[i][:-1], temp_list[i] * 100),
                   "./script/test.txt")

    # Display final forecast results
    index = np.argmax(temp_list)
    write_text("###\nThe analysis results of the behavior detection model is:{}".format(label_list[index]), "./script/test.txt")

    # print('Result is done...')
