# -*- coding: utf-8 -*-
import pandas as pd
# import csv


def write_csv(dataDir, targetDir):
    # Flag
    col_names = ["duration", "protocol_type", "service", "flag", "src_bytes", "dst_bytes", "land", "wrong_fragment",
                 "urgent", "hot", "num_failed_logins", "logged_in", "num_compromised", "root_shell", "su_attempted",
                 "num_root", "num_file_creations", "num_shells", "num_access_files", "num_outbound_cmds",
                 "is_host_login", "is_guest_login", "count", "srv_count", "serror_rate", "srv_serror_rate",
                 "rerror_rate", "srv_rerror_rate", "same_srv_rate", "diff_srv_rate", "srv_diff_host_rate",
                 "dst_host_count", "dst_host_srv_count", "dst_host_same_srv_rate", "dst_host_diff_srv_rate",
                 "dst_host_same_src_port_rate", "dst_host_srv_diff_host_rate", "dst_host_serror_rate",
                 "dst_host_srv_serror_rate", "dst_host_rerror_rate", "dst_host_srv_rerror_rate", "label"]
    # test
    # print(len(col_names))

    # test
    # data = csv.reader(open("fileName.csv"))
    # for row in data:
    #     print(row)

    # Get data
    data = pd.read_table(dataDir, header=None, sep=',', names=col_names)
    # test
    # data = pd.read_table(sourceDir, names=col_names)
    # print(data.head(1))

    # test
    # print(data)
    # data_new = data.drop([""], axis=1)

    # Create csv
    data.to_csv(targetDir, index=0)
    # data.to_csv(targetDir)


if __name__ == '__main__':
    write_csv('../data/kddcup.testdata.unlabeled_10_percent', '../data_deal/kddcup_testdata_unlabeled_10_percent.csv')
    print("kddcup_testdata_unlabeled_10_percent.csv is created.")
    write_csv('../data/kddcup.data.corrected', '../data_deal/kddcup_data.csv')
    print("kddcup_data.csv is created.")