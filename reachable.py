import goody
import prompt
from collections import defaultdict


def read_graph(file : open) -> {str:{str}}:
    new_dict = {}
    for line in file:
        if line[0] not in new_dict: 
            new_dict[line[0]] = set(line[2])
        else:   
            new_dict[line[0]].add(line[2])
    return new_dict

        
def graph_as_str(graph : {str:{str}}) -> str:
    return_string = ''
    for item in sorted(graph.keys()):
        return_string += '  ' + str(item) + ' -> ' + str(sorted(graph[item])) + '\n'
    return return_string
        
def reachable(graph : {str:{str}}, start : str, trace : bool = False) -> {str}:
    set1 = set()
    set2 = {start}
    test_list = [start]
        
    if trace == True:
            print('Explored Set:', set1)
            print('Exploring Set:', set2)
            print('The Items in the Exploring and Explored Sets are not Equal -> Repeating Process')
            print('Now Updating The Explored Set to Include Newly Explored Nodes\n')
            
    while set1 != set2:
        set1 = set1|set2
        
        for num in set2:
                if num not in test_list:
                    test_list.append(num)
                    
        for item in test_list:
            if  graph.get(item) != None:
                for y in graph.get(item):                
                    set2.add(y)
        
        if set1 == set2:
            if trace == True:
                print('Explored Set:', set1)
                print('Exploring Set:', set2)
                print('All Nodes Explored - Terminating Process')
                print('----------------------------------------\n')
            return set1
            break
        
        elif trace == True:
            print('Explored Set:', set1)
            print('Exploring Set:', set2)
            print('The Items in the Exploring and Explored Sets are not Equal -> Repeating Process')
            print('Now Updating The Explored Set to Include Newly Explored Nodes\n')
            
            
            


if __name__ == '__main__':
    '''
    user_input = input('Supply the file name describing the graph: ')
    print()
    x = graph_as_str(read_graph(open(user_input)))
    print('Graph Display: source node (str) -> destination nodes sorted ([str])')
    print(x)
    
    def check(y):
        if y == 'done':
            return True
        elif y not in read_graph(open(user_input)).keys():
            print('Entry Error: '+y+';  Illegal: not a source node')
            print('Please enter a legal String')
            print()
            return False
        return True
            
    
    starting_node = str(input('Supply a starting node (or type done): '))
    if starting_node == 'done':
                exit()
    while check(starting_node) == False:
        starting_node = str(input('Supply a starting node (or type done): '))
    
    if starting_node == 'done':
            exit()
    
    while starting_node != 'done':
        tracing_variable = bool(input('Supply algorithm tracing option[True]: '))
        value = reachable(read_graph(open(user_input)), starting_node, tracing_variable)
        print('From the supplied starting node ' + str(starting_node) + ' the set of reachable nodes: ', value)
        print()
        starting_node = str(input('Supply a starting node (or type done): '))
        while check(starting_node) == False:
            starting_node = str(input('Supply a starting node (or type done): '))
            if starting_node == 'done':
                exit()
    '''
                
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc1.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
