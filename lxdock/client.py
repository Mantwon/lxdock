#!/usr/bin/python3
import ast
import asyncio
import pylxd
import pyslp
import random

from pyslp.slptool import SLPClient


def get_slp_hosts():
    loop = asyncio.get_event_loop()
    slp_client = SLPClient(ip_addrs=['0.0.0.0'])
    url_entries = loop.run_until_complete(
        slp_client.findsrvs(service_type="lxd_host")
    )
    host_list = url_entries
    return host_list

def get_client(host_list=get_slp_hosts()):
    """ Returns a PyLXD client to be used to orchestrate containers. """
    endpoint = '{}'.format(random.choice(host_list))
    client = pylxd.Client(endpoint=endpoint,verify=False)
    return client
