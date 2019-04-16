nodes = (1,2,3,4,5,6,7,8,9)
edges = [(1,4),(7,1),(4,7),(9,7), (9,3), (3,6), (6,9),(8,6),(8,5),(5,2),(2,8)]

def reverse_graph(edges):
  rev = [(e[1],e[0]) for e in edges]
  return rev


def call_1st_loop(nodes, edges):
  edges = reverse_graph(edges)
  order = dfs_loop(nodes,edges)
  return order
  
def call_2nd_loop(order, edges):
  explored = set()
  curr_s = None
  lead_comp = {}
  for ft in range(len(nodes), 0, -1):
    i = order[ft]
    if i not in explored:
      curr_s = i
      explored = dfs_lead(edges, curr_s, i, explored, lead_comp)
  return lead_comp



def dfs_loop(nodes,edges):
  ft_node = {}
  finish_t = 0
  explored = set()
  curr_s = None
  for i in range(len(nodes), 0, -1):
    if i not in explored:
      curr_s = i
      finish_t, explored = dfs(nodes,edges, finish_t, curr_s, i, explored, ft_node)
    
  return ft_node
  
  
def dfs(nodes,edges, finish_t, curr_s, node_i, explored,ft_node):
  explored.add(node_i)
  leader = curr_s
  el_edges = [e for e in edges if e[0] == node_i]
  for edge in el_edges:
    v = edge[1]
    if v not in explored:
      finish_t, explored = dfs(nodes,edges, finish_t,leader, v, explored, ft_node)
  finish_t = finish_t + 1
  #print("finish time of node %s is %s" % (node_i,finish_t))
  ft_node[finish_t] = node_i
  #print("leader of %s node is %s" % (node_i, leader))
  return finish_t, explored

def dfs_lead(edges, curr_s, node_i,explored,lead_comp):
  explored.add(node_i)
  leader = curr_s
  el_edges = [e for e in edges if e[0] == node_i]
  for edge in el_edges:
    v = edge[1]
    if v not in explored:
      explored = dfs_lead(edges, leader, v, explored, lead_comp)
  if leader not in lead_comp:
    lead_comp.setdefault(leader,[]) 
  lead_comp[leader].append(node_i)
  return explored
  
  
order = call_1st_loop(nodes, edges)
print(call_2nd_loop(order, edges))
  
  

