import goody


def read_voter_preferences(file : open):
    new_dict = {}
    for line in file:
        stripped_line = line.rstrip('\n')
        voter_list = stripped_line.split(';')
        new_dict[voter_list.pop(0)] = voter_list 
    return new_dict 


def dict_as_str(d : {None:None}, key : callable=None, reverse : bool=False) -> str:
    return_string = ''
    for item in sorted(d, key = key, reverse = reverse):
        return_string += '  ' + str(item) + ' -> ' + str(d[item]) + '\n'
    return return_string


def evaluate_ballot(vp : {str:[str]}, cie : {str}) -> {str:int}:
    new_dict = {}
    for val in cie:
        new_dict[val] = 0 
    for x in new_dict.keys():
        for elem in vp.values():
            if elem[0] in new_dict.keys():
                if x == elem[0]:
                    new_dict[x] += 1
            elif elem[0] not in new_dict.keys():
                if x == elem[1]:
                    new_dict[x] += 1
    return new_dict

def remaining_candidates(vd : {str:int}) -> {str}:
    return {k for k,v in vd.items() if v != min(vd.values())}
        
        
def run_election(vp_file : open) -> {str}:
    voter_dict = read_voter_preferences(vp_file)
    print('Preferences Display: voter (str) -> candidate choices decreasing ([str])')
    print(dict_as_str(voter_dict))
    count = 1
    cie = set()
    for i in voter_dict.values():
        for f in i:
            cie.add(f)
    
    for voter in voter_dict.values():
        for candidate in voter:
        
            print('Vote count sorted by candidate on ballot #'+str(count)+': shows only candidates still in election')
            print(dict_as_str(evaluate_ballot(voter_dict, cie)))

            print('Vote count sorted by votes on ballot #'+str(count)+': shows only candidates still in election')
            print(dict_as_str(evaluate_ballot(voter_dict, cie), key = lambda x:(evaluate_ballot(voter_dict, cie))[x], reverse = True))
    

            cie = remaining_candidates(evaluate_ballot(voter_dict, cie))
            count += 1
            if len(cie) == 1 or len(cie) == 0:
                print('Winner singleton set: ' + str(cie))
                return cie       
  
  
    
if __name__ == '__main__':
    # Write script here
    user_input = input('Supply the file name describing all voter preferences: ')
    run_election(open(user_input))
    # For running batch self-tests
    print()
    import driver
    driver.default_file_name = "bsc2.txt"
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()

