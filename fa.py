import goody


def read_fa(file : open) -> {str:{str:str}}:
    new_dict = {}
    inner_dict = {}
    for line in file:
        split_lines = line[0:-1].split(';')
        for i in range(1, len(split_lines), 2):
            inner_dict[split_lines[i]] = split_lines[i+1]
            new_dict[split_lines[0]] = dict(sorted(inner_dict.items(), reverse = True))
    new_dict = dict(sorted(new_dict.items(), reverse = True))
    return new_dict
    

def fa_as_str(fa : {str:{str:str}}) -> str:
    return_str = ''
    for key in dict(sorted(fa.items())):
        return_str = return_str +'  '+ str(key) + ' transitions: ' + str(sorted(list(fa[key].items()))) +'\n'
    return return_str

    
def process(fa : {str:{str:str}}, state : str, inputs : [str]) -> [None]:
    new_list = [(None, state)]
    for i in inputs:
        if i not in fa[new_list[-1][1]]:
            new_list.append(('x', None))
            break
        new_list.append((i, fa[new_list[-1][1]][i]))
    new_list[0] = state
    return new_list

def interpret(fa_result : [None]) -> str:
    interpret_string = 'Start state = '+ fa_result[0] + '\n'
    fa_result.pop(0)
    inputs = [item[0] for item in fa_result]
    states = [item[1] for item in fa_result]
    for i in range(0,len(inputs)):
        if str(inputs[i]) == 'x':
            interpret_string += '  Input = ' + str(inputs[i]) + '; illegal input: simulation terminated\n' 
        else:
            interpret_string += '  Input = '+ str(inputs[i]) +'; new state = '+ str(states[i]) + '\n'  
    interpret_string += 'Stop state = '+ str(states[-1])+'\n'
    return interpret_string




if __name__ == '__main__':
    user_input = input('Supply the file name describing the Finite Automaton: ')
    print('Finite Automaton Display: state (str): list of transitions ([(str,str)])')
    x = read_fa(open(user_input))
    print(fa_as_str(x))
    print()
    user_input1 = input('Supply the file name whose lines are a start-state and its inputs: ')
    print()
    print('Trace of FA: from its start state')
    for line in open(user_input1):
        stripped_line = line.rstrip('\n')
        newlist = stripped_line.split(';')
        startstate = newlist[0]
        newlist.pop(0)
        list_parameter = newlist
        print(interpret(process( x , startstate, list_parameter))) 
    
    print()
    import driver
    
    driver.default_file_name = "bsc3.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
