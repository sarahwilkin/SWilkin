__author__ = 'Sarah Wilkin'

import os
import re
import igraph
import hashlib

from bs4 import BeautifulSoup


friends = []
os.chdir('/home/sarah/me/html')

global labels
labels = []

l=igraph.Graph()


# method to extract friends url from the html file passed to the function
# returns the urls as a list
def extract_friends(input_file):
    global labels
    temp = []
    friends_file = open(input_file, 'rb')
    soup = BeautifulSoup(friends_file)
    for link in soup.find_all('a', attrs={'href': re.compile("^https://.*friends$")}):
        link = link.get('href')
        # check for duplicates
        if link not in temp:
            temp.append(link)
            labels.append(link)
    for i in temp:
        print i

    return temp
# add first node to graph
def add_friend_to_graph(graph,f):
    for i in f:
        graph.add_vertex(i)
    return graph

#add additional nodes to graph
def add_friends_to_graph(graph, f):
    for url in f:
        if url not in graph.vs:
            graph.add_vertex(url)
    return graph

#add edges to graph
def add_edges_to_graph(graph,friends):
    for i in friends:
        graph.add_edge(friends[0],i)

#build the graph
def create_graph(graph,f, no):
    # add the first node
    if no > 0:
        graph = add_friends_to_graph(graph, f)
    # otherwise add additional nodes
    else:
        graph = add_friend_to_graph(graph,f)
    add_edges_to_graph(graph,f)
    return graph

count = 0

def main(input_file):
	for each_html_file in os.listdir('.'):
		#md5 hash function is applied to each file
		hash_object = hashlib.md5(each_html_file)
		print(hash_object.hexdigest())
		global l
		global count
	   	friend_list = extract_friends(each_html_file)
	    	l = create_graph(l,friend_list, count)
	    	count+=1

	#deletes any nodes with a degree of 0
	for v in l.vs:
	    if v.degree() == 0:
		l.delete_vertices(v)



	#adds the weight of duplicate edges together
	l.simplify()
	delete = []
	
	#delete duplicates in list
	for i in l.vs:
	    if i.degree()==0:
		delete.append(i)

	#delete duplicate labels in list
	for i in delete:
	    if i in labels:
	       labels.remove(i)

	l.delete_vertices(delete)


	
	#prints labels to graph
	label=[]
	for i in l.vs:
	    label.append(i)

	l.vs["label"] = l.vs["name"]
	print l.vs


	#plot the graph
	layout = l.layout("kk")
	igraph.plot(l,layout=layout)

	#export graph file
	l.write_graphml('/home/sarah/me/test.graphml')
