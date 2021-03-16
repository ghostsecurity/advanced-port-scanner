# -*- coding: utf-8 -*-

# ~ Author: Nicholas Guirro 
# ~ Chanell: https://www.youtube.com/ghostsecurity
# ~ Instagram: https://www.instagram.com/ghosttsecurity/

# ~ Colors
R = '\033[1;31m'
G = '\033[1;32m'
Y = '\033[1;33m'

print('''
                                     
                             ./+++++/////++o+-                        
                          .+o/.             `/y/            -//:.     
                        -o/                    sy         .h/..-/os+` 
                       o+                      .N        -h`       -h:
                      y:                    :o++.       /s          `m
                     y/               .:`   -y:       .y+           /y
                    +y              .dMMm`    /s:   .oy.           :h 
  .sso+++o:        -d` `hds.       .NMMMM:      .//+:`             `d 
 :y.      :s+`    `h`  `NMMM+     .mMMMMm`                          y.
-y          .++++oo`    /MMMMdo+ :dNNNdo`                           y-
y`                       -shdho.                                  .os 
d .                                                            o+//`  
++y+                                                          s+      
  .h                                                        `oo       
   d                                             -.` `h+++++/.        
   d`                                           .N:/++.               
   +y.`-oh:      :`                              :yo/-.``.:/-         
    ./+:  s/    .hh`                               `:/+//:.+s         
           :o++os`.y                                       d.         
                   o:                                     y/          
                   `h                                   `h/           
                    y-                                 +y.            
                    -y                             ..+s-              
                     h: .                          ss`                
                     `s+/+           .           .so                  
                       `-so          `:.     .:+o/`                   
                          -so++++++//++oooooo/.                       
''')

# ~ Imports
import socket
import time
import sys
from argparse import ArgumentParser

START = 'Scan started at ' + time.strftime('%x %X %z')
END = 'Scan finished at '+ time.strftime('%x %X %z')

# ~ Argparse
parser = ArgumentParser(usage='''main.py [target] {options}.
     {target} Specify the target (this parameter is mandatory)  

     [-h] [--help]      To ask for more detailed help.
     [-i] [--intensive] For all ports scan (1, 65535).
     [-o] [--output]    To save the output to a file.
     [-s] [--timeout]   Define time to connection.
     [-w] [--wordlist]  Use a wordlist of ports in the scan.
     [-t] [--threads]	Define threads to intensive scan (maximum = 4)
	''')
parser.add_argument('target', help='Specify the target to scan (this parameter is mandatory).')
parser.add_argument('-i', '--intensive', action='store_true', dest='intensive',
	help='Use option to intensive scan.')
parser.add_argument('-o', '--output', metavar='', dest='output', 
	help='Save the scan output, output plus file name to save the output.')
parser.add_argument('-s', '--timeout', metavar='', dest='timeout', type=float, default='0.5',
	help='Choose connection timeout (use floating numbers).')
parser.add_argument('-w','--wordlist', metavar='', dest='wordlist',
	help='''use a wordlist of ports in the scan, specify the name of the 
	wordlist located in the wordlists folder.''')
parser.add_argument('-t', '--threads', metavar='', dest='threads', type=int,
	help='Define threads to intensive scan (maximum = 4) | use a int number.')

args = parser.parse_args()

open_p = []

# ~ To save output
def save(args, name, output):
	try:
		print(Y + 'Saving...')	
		file = open(name, 'w')
		file.write(str(output).strip('[]').replace(', ', '\n').replace("'" , ''))
		print(Y + 'Save Sucefull')
	except Exception as error:
		print(R + f'FATAL: {error}')
		sys.exit(1)

# ~ Common Scan
def common(args, target):
	if args.threads:
		print(R +'You cannot use the threads option with this function')
		sys.exit(1)
	if args.wordlist:
		print(R +'You cannot use the wordlist option with this function')
		sys.exit(1)
	if args.intensive == True:
		print(R + 'You cannot use the intensive option with this function')
	global open_p
	ports = [66, 80, 81, 443, 445, 457, 1080, 1100, 1241, 1352, 1433, 1434,	1521, 1944, 2301, 3128,
	3306, 4000, 4001, 4002, 4100, 5000, 5432, 5800,5801, 5802, 6346, 6347, 7001, 7002, 8080, 8888, 
	30821]
	try:
		print(Y + START)
		for port in ports:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(args.timeout)
			code = s.connect_ex((target, port))
			if code == 0:
				print(G + f'[{port}] Open')
				open_p.append(f'{port} - Open')
			else:
				pass
		print(Y + END)
	except Exception as error:
		print(R + f'FATAL: {error}')
		sys.exit(1)
	try:
		if args.output:
			save(args, args.output, open_p)
		else:
			pass 
	except Exception as error:
		print(R + f'FATAL: {error}')
		sys.exit(1)

# ~ Scan with wordlist
def word(args, target):
	if args.threads:
		print(R +'You cannot use the threads option with this function')
		sys.exit(1)
	if args.intensive == True:
		print(R + 'You cannot use the intensive option with this function')

	global START
	global END
	global open_p
	try:	
		w_file = open(f'wordlists/{args.wordlist}')
		r_file = w_file.read().splitlines()
		print(Y + START)
		for port in r_file:
			port = int(port)
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(args.timeout)
			code = s.connect_ex((target, port))
			if code == 0:
				print(G + f'[{port}] Open')
				open_p.append(f'{port} - Open')
			else:
				pass
		print(Y + END)
	except Exception as error:
		print(R + f'FATAL: {error}')

	try:
		if args.output:
			save(args, args.output, open_p)
		else:
			pass 
	except Exception as error:
		print(R + f'FATAL: {error}')

# ~ Scan all ports (1, 65535)
def full(args, target, port_list, threads=4):
	if threads > 4:
		print(R + 'Maximum number of threads allowed is 4')
		sys.exit(1)
	if args.wordlist:
		print(R +'You cannot use the wordlist option with this function')
		sys.exit(1)
	global open_p
	print(Y + START)
	for port in port_list:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		code = s.connect_ex(target, port)
		if code == 0: 
			print(G + f'[{port}] Open')
			open_p.append(f'{port} - Open')	
		else:
			pass
		print(Y + END)

	try:
		if args.output:
			save(args, args.output, open_p)
		else:
			pass 
	
	except Exception as error:
		print(R + f'FATAL: {error}')

# ~ Main funcion to handler functions
def main(args):
	if args.wordlist:
		word(args, args.target)

	elif args.intensive == True:
		full(args, args.target, args.threads )

	else:
		common(args, args.target)

if __name__ == '__main__':
	main(args)

