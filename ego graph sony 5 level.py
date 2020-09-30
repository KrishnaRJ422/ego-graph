 -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 21:59:18 2020

@author: krish
"""

import networkx as nx


nodes=[('sony', {'count': 5}),
       ('microsoft', {'count': 2}),
       ('samsung', {'count': 1}),
       ('lg oled', {'count': 1}),
       ('canon', {'count': 1}),
       ('bose headphones', {'count': 1}),
       ('apple', {'count': 3}),
       ('google', {'count': 1}),
       ('code', {'count': 1}),
       ('amazon', {'count': 1}),
       ('iphone', {'count': 2}),
       ('lg tv', {'count': 1}),
       ('sony tv', {'count': 1}),       
       ('samsung qled', {'count': 1}),
       ('sony oled', {'count': 1}),
       ('nanocell', {'count': 1}),
       ('uhd', {'count': 1}),
       ('nikon', {'count': 1}),
       ('hp printer', {'count': 1}),
       ('epson printer', {'count': 1}),
       ('cannon', {'count': 1}),
       ('beats', {'count': 1}),
       ('airpods', {'count': 1}),
       ('jbl', {'count': 1}),
       ('quietcontrol 30', {'count': 1})
       
       
       
       ]

edges=[('microsoft', 'sony', {'weight': 5, 'distance': 1}),
       ('samsung', 'sony', {'weight': 4, 'distance': 2}),
       ('lg oled', 'sony', {'weight': 3, 'distance': 3}),
       ('canon', 'sony', {'weight': 2, 'distance': 4}),
       ('bose headphones', 'sony', {'weight': 1, 'distance': 5}),
       ('sony', 'microsoft', {'weight': 5, 'distance': 1}),
       ('apple', 'microsoft', {'weight': 4, 'distance': 2}),
       ('google', 'microsoft', {'weight': 3, 'distance': 3}),
       ('code', 'microsoft', {'weight': 2, 'distance': 4}),
       ('amazon', 'microsoft', {'weight': 1, 'distance': 5}),
       ('sony', 'samsung', {'weight': 5, 'distance': 1}),
       ('iphone', 'samsung', {'weight': 4, 'distance': 2}),
       ('lg tv', 'samsung', {'weight': 3, 'distance': 3}),
       ('apple', 'samsung', {'weight': 2, 'distance': 4}),
       ('sony tv', 'samsung', {'weight': 1, 'distance': 5}),
       ('sony', 'lg oled', {'weight': 5, 'distance': 1}),
       ('samsung qled', 'lg oled', {'weight': 4, 'distance': 2}),
       ('sony oled', 'lg oled', {'weight': 4, 'distance': 3}),
       ('nanocell', 'lg oled', {'weight': 4, 'distance': 4}),
       ('uhd', 'lg oled', {'weight': 1, 'distance': 5}),
       ('sony', 'canon', {'weight': 5, 'distance': 1}),
       ('nikon', 'canon', {'weight': 4, 'distance': 2}),
       ('cannon', 'canon', {'weight': 3, 'distance': 3}),
       ('hp printer', 'canon', {'weight': 4, 'distance': 4}),
       ('epson printers', 'canon', {'weight': 1, 'distance': 5}),
       ('sony', 'bose headphones', {'weight': 5, 'distance': 1}),
       ('beats', 'bose headphones', {'weight': 4, 'distance': 2}),
       ('airpods', 'bose headphones', {'weight': 3, 'distance': 3}),
       ('jbl', 'bose headphones', {'weight': 4, 'distance': 4}),
       ('quietcontrol 30', 'bose headphones', {'weight': 1, 'distance': 5})
       
       ]

G=nx.Graph()
G.add_nodes_from(nodes)
G.add_edges_from(edges)

EG = nx.ego_graph(G, 'sony', distance = 'distance', radius = 25)

EG
#single plot
#nx.draw(EG,with_labels=True,node_size=1000,node_color='r')

EG.number_of_nodes()

EG.number_of_edges()

import matplotlib.pyplot as plt

plt.figure(figsize=(25,15))
pos = nx.spring_layout(EG,scale=10)
#nx.draw(EG, pos, node_color="skyblue", font_size=15,node_size=2800, with_labels=True,nodelist=['sony'])

# Draw ego as large and red
#options = {"node_size": 300, "node_color": "r"}
nx.draw_networkx_nodes(EG, pos,font_size=6, nodelist=['sony'], node_color='green',node_size=15000)

nx.draw_networkx_nodes(EG, pos,font_size=6, nodelist=['samsung','microsoft','canon','lg oled','bose headphones'], node_color='yellow',node_size=10000)
nx.draw_networkx_nodes(EG, pos,font_size=6,nodelist=['amazon','sony tv','apple','code','iphone','lg tv','google','samsung qled','sony oled','nanocell','uhd','epson printers','hp printer','cannon','nikon','jbl','airpods','beats','quietcontrol 30'], node_color='skyblue',node_size=8000)

nx.draw_networkx_edges(EG, pos, edgelist=edges, edge_color='red',linewidths=5, arrows=True,with_label=True)
nx.draw_networkx_labels(EG,pos,font_size=22,font_family='arial',font_weight='bold')
#plt.show()
plt.savefig('ego_graph_sony5.png')
