# advanced-port-scanner
 advanced python port scanner

# usage: main.py [target] {options}.
     {target} Specify the target (this parameter is mandatory)

     [-h] [--help]      To ask for more detailed help.
     [-i] [--intensive] For all ports scan (1, 65535).
     [-o] [--output]    To save the output to a file.
     [-s] [--timeout]   Define time to connection.
     [-w] [--wordlist]  Use a wordlist of ports in the scan.
     [-t] [--threads]   Define threads to intensive scan (maximum = 4)


# positional arguments:
  target            Specify the target to scan (this parameter is mandatory).

optional arguments:
  -h, --help        show this help message and exit
  -i, --intensive   Use option to intensive scan.
  -o , --output     Save the scan output, output plus file name to save the output.
  -s , --timeout    Choose connection timeout (use floating numbers).
  -w , --wordlist   use a wordlist of ports in the scan, specify the name of the wordlist located in the wordlists
                    folder.
  -t , --threads    Define threads to intensive scan (maximum = 4) | use a int number.
