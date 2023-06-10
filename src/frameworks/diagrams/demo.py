# Employee Hierarchy
from diagrams import Diagram, Node, Edge

with Diagram(filename='employee_hierarchy', outformat="pdf", direction='LR', node_attr={'fontsize': '12', 'color': 'gold'},
             edge_attr={'labeldistance': '0.7'}, graph_attr={'bgcolor': 'skyblue'}):
    # Node 1 : Boss
    boss = Node("Boss")

    # Node 2 : Senior Engineer
    senior_engineer = Node("Senior Engineer")

    # Node 3: Junior Engineer
    junior_engineer = Node("Junior Engineer")

    # Edge 1
    edge_one = Edge(label='just today', color='red', style='dashed')

    # Edge 2
    edge_two = Edge(label='not forever', color='green', style='dotted')

    boss >> edge_one >> senior_engineer >> edge_two >> junior_engineer
