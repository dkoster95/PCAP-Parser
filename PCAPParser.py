from scapy.all import *
import argparse
import os
import sys

def configure_parameters():
    parser = argparse.ArgumentParser(description='PCAP Parser and filter')
    parser.add_argument('--pcap', metavar='<pcap file path>',
                        help='pcap file path to parse', required=True)
    parser.add_argument('--host', metavar='<host host string>',
                        help='host to filter', required=True)
    return parser.parse_args()

def is_path_correct(file_path):
    if not os.path.isfile(file_name):
        print('"{}" does not exist'.format(file_name), file=sys.stderr)
    return os.path.isfile(file_name)

def parse_pcap(file_path, host):
    print('Parsing and filtering.. {0}'.format(file_path))
    print('Running tshark command......')
    print("Format parsed in: HOST   IP_Source   IP_DESTINATION  REQUEST_METHOD  REQUEST_FULL_URI    DATA")
    print("-------------------*-------------------*-------------------*-------------------*-------------------*-------------------*")
    os.system("tshark  -r {0} -Y 'http.host contains {1}' -T fields -e http.host -e ip.src -e ip.dst -e http.request.method -e http.request.full_uri -e data.data".format(file_path,host))
if __name__ == '__main__':
    args = configure_parameters()
    file_name = args.pcap
    host = args.host
    if not is_path_correct(file_name):
        print("-------------------*-------------------*-------------------*-------------------*-------------------*-------------------*")
        sys.exit(-1)

    parse_pcap(file_name,host)
    print("-------------------*-------------------*-------------------*-------------------*-------------------*-------------------*")
    sys.exit(0)
