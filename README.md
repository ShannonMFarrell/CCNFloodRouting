# CCNFloodRouting
Simulating flood routing in Python
Author : Shannon Farrell
Version : 1.3
Python  : 3.5.x
Libraries :  Matplotlib

Dependencies :
This file requires Python 3.X to run
This file uses an external library 'matplotlib' to plot simulation graphs
on Windows 10 this may be installed through the administrator command line, if you have PIP package manager installed, 
this can be installed by using the command : " python -m pip install matplotlib ". For detailed instructions or for other 
operating systems or package managers, please visit : https://matplotlib.org/faq/installing_faq.html


Instructions to run this file :
Please download this file to your computer, unzip and double click to run. Ensure you have the dependencies installed above.
For best results right click the unzipped file and click "Edit with IDLE". This allows you to debug the file and set
breakpoints using Pythons pdb debugging tool to view indepth line-by-line code manipulation.

Within the file in the main program a variable called "show_graphs" has been set to 0. This allows you to view average congestion
figures and average duplication figures, as well as a 15 figure plot of congestion for individual nodes. This can be switched to 1 #
to view duplication and congestion figures for EACH NODE INDIVIDUALLY. It is reccomended that you close high-intensity applications
when running this variable as 1, as 33 graphs in matplotlib will appear. Graphs can also be viewed as part of this zip file as
individual PNG files. If this variable is left as 1, a warning in python will appear. This can be ignored.

The total simulation time is 41 seconds tested on a Windows 10 OS PC with 1TB Hard drive, 8GB RAM, AMD A10 Processor.
The simulation time may vary on other devices, please note that this has been thoroughly tested and will not enter an
infinite loop, simulation time will increase if you adjust the number of packets being sent.


Thank you






