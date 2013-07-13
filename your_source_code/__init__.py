from mininet.cli import CLI
from mininet.net import Mininet
from mininet.topo import SingleSwitchTopo

from utils import do_something

def main():
    do_something()
    sstopo = SingleSwitchTopo(4)
    mn = Mininet(topo = sstopo)
    mn.start()
    mn.pingAll()
    mn.stop()

if __name__ == "__main__":
    main()
