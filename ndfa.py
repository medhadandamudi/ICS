import goody

def read_ndfa(file : open) -> {str:{str:{str}}}:
    outer_dict = {}        
    for line in file:
        stripped_line = line.rstrip('\n')
        split_lines = stripped_line[0:].split(';')
        state = split_lines.pop(0)
        middle_dict = {}
        for i in range(0, len(split_lines), 2):
            inner_set = set()
            for h in range(0, len(split_lines), 2): 
                if split_lines[h] == split_lines[i]:
                    inner_set.add(split_lines[h+1])
            middle_dict[split_lines[i]] = inner_set
        outer_dict[state] = middle_dict   
    return dict(sorted(outer_dict.items()))


def ndfa_as_str(ndfa : {str:{str:{str}}}) -> str:
    return_str = ""
    for n, ts in sorted(ndfa.items()):
        return_str += f"  {n} transitions: {[(t, sorted(e)) for t, e in sorted(ts.items())]}\n"
    return return_str

def process(ndfa : {str:{str:{str}}}, state : str, inputs : [str]) -> [None]:
    return_list = [({state},)]
    for i in inputs:
        return_list.append((i, set()))
        for s in return_list[-2][-1]:
            if i in ndfa[s]:
                return_list[-1][-1].update(ndfa[s][i])
        if len(return_list[-1][-1]) == 0: break
    return_list[0] = state
    return return_list



def interpret(result : [None]) -> str:
    interpret_string = 'Start state = '+ result[0] + '\n'
    result.pop(0)
    inputs = [item[0] for item in result]
    states = [item[1] for item in result]
    for i in range(0,len(inputs)):
        interpret_string += '  Input = '+ str(inputs[i]) +'; new possible states = '+ str(sorted(list(states[i]))) + '\n'  
    interpret_string += 'Stop state(s) = '+ str(sorted(list((states[-1]))))+'\n'
    return interpret_string







if __name__ == '__main__':
    user_input = input('Supply the file name describing a Non-Deterministic Finite Automaton: ')
    print('Non-Deterministic Finite Automaton Display: state (str): list of transitions ([(str,[str])])')
    x = read_ndfa(open(user_input))
    print(ndfa_as_str(x))
    print()
    user_input1 = input('Supply the file name whose lines are a start-state and its inputs: ')
    print()
    print('Trace of NDFA: from its start state')
    for line in open(user_input1):
        stripped_line = line.rstrip('\n')
        newlist = stripped_line.split(';')
        startstate = newlist[0]
        newlist.pop(0)
        list_parameter = newlist
        print(interpret(process( x , startstate, list_parameter))) 
    
    print()
    import driver
    
    driver.default_file_name = "bsc4.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
