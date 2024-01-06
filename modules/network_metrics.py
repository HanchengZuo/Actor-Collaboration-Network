import networkx as nx
import random
from pyspark.sql.functions import col, explode, year as year_func
from graphframes import GraphFrame
import pandas as pd
import os

def calculate_single_node_clustering(nx_graph, node):
    return node, nx.clustering(nx_graph, node)

def approximate_betweenness(nx_graph, k):
    return nx.betweenness_centrality(nx_graph, k=k, normalized=True)

def calculate_single_node_closeness(nx_graph, node):
    return node, nx.closeness_centrality(nx_graph, node)
