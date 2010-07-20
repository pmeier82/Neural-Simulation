# -*- coding: utf-8 -*-
################################################################################
##
##  Copyright 2010 Philipp Meier <pmeier82@googlemail.com>
##
##  Licensed under the EUPL, Version 1.1 or – as soon they will be approved by
##  the European Commission - subsequent versions of the EUPL (the "Licence");
##  You may not use this work except in compliance with the Licence.
##  You may obtain a copy of the Licence at:
##
##  http://ec.europa.eu/idabc/eupl
##
##  Unless required by applicable law or agreed to in writing, software
##  distributed under the Licence is distributed on an "AS IS" basis,
##  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
##  See the Licence for the specific language governing permissions and
##  limitations under the Licence.
##
################################################################################
#
# sim - data_io/client.py
#
# Philipp Meier - <pmeier82 at googlemail dot com>
# 2010-07-19
#

"""client stub for the simulator protocoll"""
__docformat__ = 'restructuredtext'


##---IMPORTS

# builtins
from select import select
from socket import socket, AF_INET, SOCK_STREAM
from threading import Event, Thread
from time import sleep
from Queue import Queue
# own packages
from package import SimPkg, recv_pkg, send_pkg


##---PACKAGE DISTRO

__all__ = ['SimIOClientNotifier', 'SimIOConnection']


##---CLASSES

class SimIOClientNotifier(object):

    def notify(self):
        """to be implemented in a subclass"""
        pass


class SimIOConnection(Thread):
    """connection thread for the sim client stub"""

    def __init__(self, addr, q_recv, q_send, interest=[], poll=0.001):
        """
        :Parameters:
            addr : tuple
                Socket connection address and port tuple.
            q_recv : Queue
                The queue for received items.
            q_send : Queue
                The queue for items to send.
            interest : list
                list of objects implementing the SimNotifier interface
                Default=[]
            poll : float
                select intervall
                Default=0.001
        """

        # super
        super(SimIOConnection, self).__init__(name='SimIOConnection')
        self.daemon = True

        # inits
        self.addr_ini = addr
        self.poll = float(poll)
        self.q_recv = q_recv or Queue()
        self.q_send = q_send or Queue()
        self._interest = list(interest)
        self._online = False
        self._is_shutdown = Event()
        self._is_shutdown.set()

    def run(self):
        """thread context"""

        # setup the socket
        sock = socket(AF_INET, SOCK_STREAM)
        sock.connect(self.addr_ini)
        self._online = True
        self._is_shutdown.clear()
        self.q_send.put(SimPkg(tid=SimPkg.T_CON))

        # doomsday loop
        while self._online:
            # select
            r, w, e = select([sock], [], [sock], self.poll)
            # error
            if len(e) > 0:
                break
            # receive
            if len(r) > 0:
                pkg = recv_pkg(sock)
                if pkg is None:
                    break
                self.q_recv.put(pkg)
            # send
            while not self.q_send.empty():
                item = self.q_send.get()
                send_pkg(sock, item)
                self.q_send.task_done()
        self._is_shutdown.set()

    def stop(self):
        """stop the thread"""

        self._online = False
        self._is_shutdown.wait()

    ## notification interface

    def register_interest(self, interest):
        """register an object implementiong the SimClientNotifier interaface"""

        assert isinstance(interest, SimClientNotifier)




##---MAIN

if __name__ == '__main__':

    from Queue import Empty

    print 'initialize'
    q_r, q_s = Queue(), Queue()
    client = SimIOConnection(('localhost', 31337), q_r, q_s)
    client.start()

    print 'started client, going to listen:'
    again = True
    while again:
        try:
            item = q_r.get(True, 1000)
            if item is not None:
                print item
            print '.'
        except Empty:
            continue
        except:
            again = False
    print 'Done.'
