#for windows mininet installation - 
#need to install and set paths of modules wget and 7-zip
#wget -
#http://downloads.sourceforge.net/gnuwin32/wget-1.11.4-1-setup.exe
#unzip -
#http://www.7-zip.org/a/7z1602-x64.exe

import subprocess
import os

#Global Variables
features = ['odl-mdsal-clustering', 'odl-dlux-core', 'odl-dlux-node', 'odl-dlux-yangui', 'odl-dlux-yangvisualizer', 'odl-l2switch-switch']

#Functions
def install_odl():
	os.system('sudo apt-get install default-jdk')
	os.system('sudo apt-get install default-jre')
	os.system('wget https://nexus.opendaylight.org/content/groups/public/org/opendaylight/integration/distribution-karaf/0.3.4-Lithium-SR4/distribution-karaf-0.3.4-Lithium-SR4.zip')
	os.system('distribution-karaf-0.3.4-Lithium-SR4.zip')
	cmd = './distribution-karaf-0.3.4-Lithium-SR4/bin/karaf'
	p = subprocess.Popen(['sudo', '-S'] + cmd.split(), stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, universal_newlines=True)
	args = 'feature:install'
	for s in features:
		args = args + ' ' + s
	args = args + '\n'
	p.stdin.write(args)
	print('ODL has been installed')
	os.system('./distribution-karaf-0.3.4-Lithium-SR4/bin/karaf')
		
def install_mininet():
	f = 'D:\ODL\mininet.bat'
	p = subprocess.Popen(f, shell = True, stdout = subprocess.PIPE)
	print('Mininet has been set up')
	
def vpn_feature_install():
	cmd = './distribution-karaf-0.3.4-Lithium-SR4/bin/karaf'
	p = subprocess.Popen(['sudo', 'S'] + cmd.split(), stdout = subprocess.PIPE, stdin = subprocess.PIPE, stderr = subprocess.PIPE, shell = True, universal_newlines=True)
	for s in features_vpn:
		args = args + ' ' + s
	args = args + '\n'
	args = args + 'bundle:install'
	for s in bundles:
		args = args + ' ' + s
	args = args + '\n'
	p.stdin.write(args)
