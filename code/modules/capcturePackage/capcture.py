from scapy.all import *

# pcap = sniff(offline = "xx.pcap")
# dpkt = sniff(iface="wlp7s0", count=100)
# dpkt = sniff(count=100)
# str_dpkt = str(dpkt)
# print(str_dpkt)
import pcap
import dpkt


def captData():
    pc = pcap.pcap('wlan0')
    pc.setfilter('tcp port 80')
    for ptime, pdata in pc:
        anlyCap(pdata);


def anlyCap(pdata):
    p = dpkt.ethernet.Ethernet(pdata)
    if p.data.__class__.__name__ == 'IP':
        ip = '%d.%d.%d.%d' % tuple(map(ord, list(p.data.dst)))
        if p.data.data.__class__.__name__ == 'TCP':
            if p.data.data.dport == 80:
                print(p.data.data.data)


captData()
