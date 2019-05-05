"""
CCN.py Version 1.3 - WORKING

Script Description :   This script runs a simulation of a packet switched
                       network running a flood routing algorithm to
                       deliver packets.

Language:              Python (3.5.x)
Libraries:             matplotlib (Please refer to readme for installation)
Module:                Computer and Communication Networks (21483)
Tutor:                 Dr John Easton
Due Date:              25.04.19
Version:               1.3 (Minor fix to graphs)
Author:                Shannon Farrell (1555082)
Comment Style:         PEP-8 Compliant
Debugger:              pdb
Simulation time:       41 seconds 
"""

import matplotlib.pyplot as plt                                                   
from collections import Counter                                                                 
import pdb


#class declarations
class node:

    """A node in mesh network structure

    Class attributes:
        name               Char human readable name of node (A-Z)
        duplicate_packets  List containing number of duplicate packets
                           for each time step
        node_congestion    List containing number of active packets
                           for each time step
        queue              List of packet objects, buffer for pending packets
        neighbours         Array of char containing neighbour node names
        w                  Array of binary signals for neighbour connections
    """

    
    def __init__(self, name, duplicate_packets,node_congestion ,queue, neighbours,w):
        self.name = name
        self.duplicate_packets = duplicate_packets
        self.node_congestion = node_congestion
        self.queue = queue
        self.neighbours = neighbours
        self.w = w
        

class packet:

    """A node in mesh network structure

    Class attributes:
        data               String containing packet data
        hopcount           Int containing time to live for packet 
        source             Char name of packet's sender 
        failure            TODO : not implemented in version 1.3
    """
    
    def __init__(self, data, hopcount, source,failure):
        self.data = data
        self.hopcount = hopcount 
        self.source = source
        self.failure = failure
        

#Functions used by script
def congestion_control(ctype):
    
    """
    Sets the type of control for the flooding algorithm
    based on users choice, returns time to live for packet
    """

    if ctype == 1 : #read user input, assign hop count on this
        hop_count = 10
        
    if ctype ==2 :
        hop_count = 15 #subnet length
        
    return hop_count



def display_simulation_graphs(time,selection) :

    """
    Prints node congestion and duplication activity
    for all time steps in the simulation
    User may set selection as 1 to see in detail activity
    for each node, else 0 to see average accross all nodes
    """

    range_max = time        #maximum list range
    ave_congestion  = 0     #sum of average congestion at node
    ave_duplicate = 0       #sum of average duplication at node
    total_congestion = []   #list of total congestion in network per time step
    total_duplicte = []     #list of total duplicates in network per time step
    
    time_interval = list(range(1,range_max))   #time steps 1-no.iterations
    time_interval2 = list(range(0,range_max))  #adjusted time step for individual nodes
    n = len(network)    

    
    #1. work out the total accross all nodes number of active packets per time interval 

    for i in range(time-1) : 

        for j in range(len(network)):
            
            ave_congestion = ave_congestion + \
                             network[j].node_congestion[i] # get the recorded congestion for that time period
        
        total_congestion.append(ave_congestion/n)   #append mean congestion to array for time i
        ave_congestion = 0                          #clear the figure for next time step


    #2. now we have the total congestion accross all nodes, compute duplucate packets
    
    for i in range(time-1) :

        for j in range(len(network)):
            
            ave_duplicate = ave_duplicate + \
                            network[j].duplicate_packets[i] # get the recorded duplicates for that time period
        
        total_duplicte.append(ave_duplicate/n) #append mean duplication to array for time i
        ave_duplicate = 0                      #clear the figure for next time step

    
    
    #Plot figure for average network congestion
    
    plt.figure('Fig 1. Average congestion per time sample')
    plt.title('Fig 1. Average congestion per time sample')
    plt.xlabel('Time (t)')
    plt.ylabel('No. of live packets')
    plt.plot(time_interval,total_congestion)
    plt.legend(['Average accross all nodes'])


    #Plot figure for average duplicate packets in network

    plt.figure('Fig 2. Average no. of duplicate packets per time sample')
    plt.title('Fig 2. Average no. of duplicate packets per time sample')
    plt.xlabel('Time (t)')
    plt.ylabel('No. of duplicate packets')
    plt.plot(time_interval,total_duplicte, color='m')
    plt.legend(['Average accross all nodes'])

    #Plot average congestion view for all nodes

    plt.figure('Fig 3. Average Congestion for all nodes')
    plt.title('Fig 3. Average Congestion for all nodes')
    plt.xlabel('Time (t)')
    plt.ylabel('No. of live packets')
    
    for i in range(len(network)):
        plt.plot(time_interval2,network[i].node_congestion)
    
    plt.legend(['Node A', 'Node B', 'Node C', 'Node D',\
                'Node E', 'Node F', 'Node G', 'Node H', \
                'Node I', 'Node J', 'Node K', 'Node L', \
                'Node M', 'Node N', 'Node O'])

    if(selection) : #if user wants to print INDIVIDUAL NODES
        
        #plot congestion figures for each node
        for i in range(len(network)):
            
            name = network[i].name
            plt.figure('Node ' + name + 'Congestion for each node per time sample')
            plt.title('Node ' + name + 'Congestion for each node per time sample')
            plt.xlabel('Time (t)')
            plt.ylabel('No. of live packets')
            plt.legend(['Node ' + name])
            plt.plot(time_interval2,network[i].node_congestion)

       # no of duplicates for each node

        for i in range(len(network)):
            
            name = network[i].name
            plt.figure('Node ' + name + 'duplicate packets for each node per time sample')
            plt.title('Node ' + name + 'duplicate packets for each node per time sample')
            plt.xlabel('Time (t)')
            plt.ylabel('No. of duplicate packets')
            plt.legend(['Node ' + name])
            plt.plot(time_interval2,network[i].duplicate_packets)
            
  
    plt.show() #display figures on screen


def create_neighbours():
    
    """Creates neighbour connections for each node in the network"""
    
    #for every node in the network assign left and right neighbours
    
    network[0].neighbours = ['B','C']
    network[1].neighbours = ['A','D','E']
    network[2].neighbours = ['A','F','G']
    network[3].neighbours = ['B','H']
    network[4].neighbours = ['B','F','J']
    network[5].neighbours = ['C','E','K']

    network[6].neighbours = ['C','K']
    network[7].neighbours = ['D','I']
    network[8].neighbours = ['H','J','O']
    network[9].neighbours = ['I','E']
    network[10].neighbours = ['F','G','L']
    network[11].neighbours = ['K','M','N']

    network[12].neighbours = ['L','N']
    network[13].neighbours = ['O','L','M']
    network[14].neighbours = ['I','N']

    
    #initialise data flags for each neighbour as 0 (able to write)
    for i in range(len(network)) :
        
        for j in range(len(network[i].neighbours)) :
            network[i].w.append(0)
     
            

def initialise(starting_node, packets) :

    """
    Initilaises the system by queuing all packets
    on starting nodes buffer
    """

    for i in range(len(packets)) :                  #for every packet user wants to simulate
        packets[i].source = starting_node.name      #set the source as starting node
        starting_node.queue.append(packets[i])      #push this onto starting nodes queue
   
 
  


def simulation(time) :

    """
    Iterative function which runs packet transmission simulation 
    for each node in network. Checks their empty signal from funcion
    and clears all read/write flags per time step
    """
  
    node_free_signals = [0 for x in range(15)]  # create list to hold status of buffer
    node_free_signals[0] = 1                    # assign starting node as 1 to start the process
    

    while(node_free_signals.count(1) != 0):   #while all of the buffers have packets to send
 
        time +=1
        print("Time count : ", time)

        for i in range(len(network)):                           #for each node in the network
            node_free_signals[i] = check_and_send(network[i])   #simulate packet transmission
           

        #on each iteration clear the write flags
        #this is to enable the neighbour to send packet on next iteration, preventing loop

        for j in range(len(network)): 
              network[j].w.clear()                       #clear all elements from list
              
              for k in range (len(network[j].neighbours)) :
                  network[j].w.append(0)                 #reset as 0

    return time



def decrement_hop(activenode,neighbourindex):

    """
    Appends the packet into the neighbours buffer
    with new time to live
    """

    #place in neighbours buffer, packet with decremented hopcount
    network[neighbourindex].queue.append(packet(activenode.queue[0].data \
                                                ,activenode.queue[0].hopcount - 1,\
                                                activenode.name, 0))



def get_packets(activenode):

    """
    Counts the amount of duplicate packets and live
    packets per time step, appends this to list for graph plotting
    """

    
    packets = []                #list to hold packets currently in queue
    k = 0                       #key iterator in dictionary
    v = 0                       #value iterator in dictionary
    duplicates = 0;             #number of duplicates
    
    activepackets = len(activenode.queue)   

    
    for i in range(len(activenode.queue)):      #populate packet list
        packets.append(activenode.queue[i].data)

    duplicate_count = Counter(packets)  #count the number of occurence of each packet in list

    
    for k, v in duplicate_count.items(): #iterate through dictionary created by counter()
        v = v - 1                        #no of duplicates is no. of occ - 1
        
        if(v > 0):                       #if duplicates exist
            duplicates = duplicates + 1  #add 1 to number of duplicates


    activenode.duplicate_packets.append(duplicates)     #append this to duplicates for time t
    activenode.node_congestion.append(activepackets)    #append no of packets for time t
   

   

def check_and_send(activenode) :

    """
    Main function in simulation, called by 'Simulation' method. Goes through
    each of the active node's neighbours, checks if it isn't packet's source
    checks data lines to see if it is free to write, performs packet checks
    and sends. Returns if buffer is empty or not to 'Simulation'
    """

    queue_empty_flag = 1   #set default flag as a full buffer
    neighbourindex = 0     #index in network of neighbour of node activenode
    clr_to_send = 0        #flag checking if data line is available
    x = 0                  #my location in the neighbouring nodes neighbour list
    
    get_packets(activenode) #1. get the amount of duplicate and active packets
    
    print("\n********************** \nrunning simulation with node ", \
          activenode.name, " \n********************** \n ")
   

    if(activenode.queue) :      #2. if there are packets to send
        
        if(activenode.queue[0].hopcount > 0) :   #if packet in queue has hopcount of 1 or more
        
            for n in range (len(activenode.neighbours)) :   #for each neighbour node has
                
                
                if(activenode.neighbours[n] != activenode.queue[0].source) : #if neighbour isnt pckt source

                    #look for the index of the neighbour in the network
                    neighbourindex = [x.name for x in network].index(activenode.neighbours[n])

                    #look for my position in the neighbouring node's neighbour list
                    x = network[neighbourindex].neighbours.index(activenode.name)
                    
                    #check they arent writing to me (0)
                    clear_to_send = network[neighbourindex].w[x]

                    if(clear_to_send == 0) :                        #if their write line to me is 0

                        decrement_hop(activenode,neighbourindex)    #append into their queue
                        
                        network[neighbourindex].w[x] = 1 #raise self write and that write
                        activenode.w[n] = 1 
          
                        
                        print("sucessfully writtten packet : ",\
                              activenode.queue[0].data, "   from node ",\
                              activenode.name ,"to node " \
                              ,network[neighbourindex].name)


                        if(n ==len(activenode.neighbours) - 1):   #if current neighbour is last one in list
                            activenode.queue.pop(0)               #remove it from my queue

                            if not activenode.queue :             #if there are no items left now
                                queue_empty_flag = 0              #return empty flag as high


                else :  #if this neighbour is the source of the packet
                    
                    if(n ==len(activenode.neighbours) - 1):  #if it is last neighbour in list
                            activenode.queue.pop(0)          #remove from my queue

                            if not activenode.queue :        #if there are no packets left now 
                                queue_empty_flag = 0         #return empty flag as high

        else: #if hop count is 0
            activenode.queue.pop(0)                 #remove it from queue
            print("Discarding packet, time to live finished")
   
    else : #if buffer is empty
        queue_empty_flag = 0    #return empty flag as high
        

    return queue_empty_flag




# Main Program and all class instantiations

    """
    Main program, sets initial user parameters, runs utility functions
    to initialise packets, initialise network nodes,
    runs simulation function and graph functions
    """


time = 0        #initial time 
no_nodes = 15   #TODO : make this dynamic, number of nodes in network
method = 1      #control method type leave as 1 for hop count = 10
show_graphs = 0 #control flag for type of graphs, 0 for overview, 1 for detailed graphs
network = []    #list of all nodes in the network


# 2. Create network nodes and create arrangement

for i in range(ord('A'),ord('O')+1) :               #create 15 network nodes named A-O
    network.append(node(chr(i),[],[],[],[],[]))     #add this new node into list

hop_count = congestion_control(method)              #set hop count as user defined control method
create_neighbours()                                 # set up the neighbours 


#3. create the data to be sent and packets.

tokenword = ['floodrouting','Simulation'] #packets to be sent through network, adding more increase simulation time
packets = []                              #initial list of packets

for i in range(len(tokenword)) :
    packets.append(packet(tokenword[i],hop_count, '',0))  
    
 

# 3. inject packet into network and simulate it

initialise(network[0], packets)          # pop node onto buffer A
time = simulation(time)                 # simulate the network functionality



print("\n \n \n \n \n \nTime taken to complete simulation = ", time)  
print("Plotting simulation graphs")

display_simulation_graphs(time,show_graphs)  #draw graphs 

