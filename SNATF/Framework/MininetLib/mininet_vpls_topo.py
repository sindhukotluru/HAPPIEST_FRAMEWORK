from mininet.node import Host, RemoteController
from mininet.topo import Topo
class VLANHost( Host ):
 def config( self, vlan=100, **params ):
 	 """Configure VLANHost according to (optional) parameters:
	 vlan: VLAN ID for default interface"""
	 r = super( Host, self ).config( **params )
	 intf = self.defaultIntf()
	# remove IP from default, "physical" interface
	 self.cmd( 'ifconfig %s inet 0' % intf )
	# create VLAN interface
	 self.cmd( 'vconfig add %s %d' % ( intf, vlan ) )
	# assign the host's IP to the VLAN interface
	 self.cmd( 'ifconfig %s.%d inet %s' % ( intf, vlan, params['ip'] ) )
	# update the intf name and host's intf map
	 newName = '%s.%d' % ( intf, vlan )
	# update the (Mininet) interface to refer to VLAN interface name
	 intf.name = newName
	# add VLAN interface to host's name to intf map
	 self.nameToIntf[ newName ] = intf
	 return r
class MyTopo( Topo ):
 "Simple topology example."
 def __init__( self ):
 	"Create custom topo."
 	# Initialize topology
 	Topo.__init__( self )
 	# Add hosts and switches
	host1=self.addHost( 'h1', cls=VLANHost, vlan=100)
 	host2=self.addHost( 'h2', cls=VLANHost, vlan=200)
 	host3=self.addHost( 'h3', cls=VLANHost, vlan=300)
	host4=self.addHost( 'h4', cls=VLANHost, vlan=400)
#	host5=self.addHost( 'h5', cls=VLANHost, vlan=200)
#	host6=self.addHost( 'h6', cls=VLANHost, vlan=300)
	s1 = self.addSwitch( 's1' )
	s2 = self.addSwitch( 's2' )
	s3 = self.addSwitch( 's3' )
	s4 = self.addSwitch( 's4' )
	self.addLink(s1,host1)
	self.addLink(s1,s2)
	self.addLink(s2,host2)
	self.addLink(s2,s3)
	self.addLink(s3,host3)
	self.addLink(s3,s4)
	self.addLink(s4,host4)
	self.addLink(s4,s1)
topos = { 'mytopo': ( lambda: MyTopo() ) }
