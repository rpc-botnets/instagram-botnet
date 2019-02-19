from .methods import methods
from functools import reduce
from .nodes import node_classes
from .support import dotdict



class MalformedScript(Exception):
    pass


def assert_good_script(script):
    for action in script['actions']:
    
        if not 'name' in action:
            raise MalformedScript('missing `name` in some action')
            
        name = action['name']
        
        if not 'from' in action:
            raise MalformedScript(f'missing `from` in action {name}')
        
        if not 'edges' in action:
            raise MalformedScript(f' missing `edges` in action {name}')
        
        if not 'nodes' in action:
            raise MalformedScript(f' missing `nodes` in action {name}')
        
        get_name = lambda e: list(e.keys())[0] if isinstance(e, dict) else e
        
        for edge in (get_name(edge) for edge in action['edges']):
            if not edge in methods:
                raise MalformedScript(f'unknown edge {edge} in action {name}')
            
        check, problem = check_edges(action['edges'], action['from'])
        
        if not check:
            raise MalformedScript(f'wrong edges chaining in action {name}, {problem}')




def check_edges(edges, from_type,):
    
    meth = {**methods, 'starting_point': dotdict(returns=node_classes[from_type])}
    
    reducer = lambda edges, last: edges + [last] \
        if edges[-1] is not None \
        and  isinstance(meth[edges[-1]].returns, meth[last].accepts) \
        else edges + [None]
        
    get_name = lambda e: list(e.keys())[0] if isinstance(e, dict) else e
        
    names = [get_name(edge) for edge in edges]
        
    checks = reduce(reducer, names, ['starting_point'])
    
    if None in checks:
        index = checks.index(None)
        errored_edge = names[index]
        right_type = methods[errored_edge].accepts
        wrong_type = methods[names[index - 1]].returns if index > 0 else from_type
        problem = f'`{errored_edge}` must receive nodes of type `{str(right_type)}`, not `{str(wrong_type)}`'
        return False, problem
        
    else:
        return True, ''


