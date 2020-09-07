from Graph import Graph, Edge
from InfluencerAgent import InfluencerAgent
from InfluencerAdvertisingModel import InfluencerAdvertisingModel

from mesa.visualization.modules import CanvasGrid
from mesa.visualization.modules import ChartModule
from mesa.visualization.ModularVisualization import ModularServer

import random


def agent_portrayal(agent):
    portrayal = {"Shape": "circle",
                 "Color": "red",
                 "Filled": "true",
                 "Layer": 0,
                 "r": 0.5}

    if(agent.hired == True):
        portrayal["Color"] = "blue"
    else:
        if(agent.decision == True):
            portrayal["Color"] = "green"
            portrayal["r"] = 0.2
    return portrayal


def display(graph_type):
    chart1 = ChartModule(
        [{"Label": "No who bought",
        "Color": "Black"}],
        data_collector_name='datacollector'
    )
    chart2 = ChartModule(
        [{"Label": "No bought at every timestep",
        "Color": "Black"}],
        data_collector_name='datacollector'
    )
    if(graph_type=='networkx'):
        grid = CanvasGrid(agent_portrayal, width, height, 500, 500)
        return [grid,chart1,chart2]
    return [chart1,chart2]

def get_node_ids_inRange(filepath, x, y):
    node_ids = []
    with open(filepath) as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip().split(',')
            id = int(line[0])
            outDegree = int(line[1])

            if outDegree >= x and outDegree <=y:
                node_ids.append(id)
    return node_ids

def choose_random_advertisers(node_ids, n):
    return random.sample(node_ids, n)
if __name__ == '__main__':

    width = height = 50
    number_of_nodes = width*height
    graph_type='twitter'
    # graph_type='networkx'

    if(graph_type=='networkx'):
        node_ids = {
            1: [1]
        }
        grid=1
        graph = Graph()
        graph.create_networkx_graph(n=number_of_nodes, k=250)

    if(graph_type=='twitter'):
        # node_ids = [89634510] # outdergree 20
        # node_ids = [115485051] # outdergree 3383
        # node_ids = [115485051, 40981798] # outdergree 3383 and 3216
        # node_ids = [16157855] # outdergree 157
        # node_ids = [14155052] # outdergree 342
        # node_ids = [144040563] # outdergree 628
        # node_ids = [40981798] #outdegree 3216

        node_ids_inRange = get_node_ids_inRange("../data/twitter_id_degree.txt",600,699)
        advertiser_list = choose_random_advertisers(node_ids_inRange, 5)
        print("Advertiser nodes: ", advertiser_list)
        node_ids = {
            # 1:  [115485051]
            # 3: [89634510]
            1: advertiser_list

        }

        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_twitter_combined.txt')

    if(graph_type=='gplus'):

        node_ids = {
            1: [111091089527727420853] #outdegree 17055
        }

        grid=0
        graph = Graph()
        graph.create_twitter_graph(filepath='../data/cleaned_gplus_combined.txt')

    params = {
        "width":width,
        "height":height,
        "Graph": graph,
        "node_ids": node_ids,
        "grid": grid,
        "product_cost": 50
    }

    server = ModularServer(
        InfluencerAdvertisingModel,
        display(graph_type),
        "Influencer Advertising Model",
        params
    )
    server.port = 8521
    server.launch()
