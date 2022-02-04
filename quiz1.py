from collections import defaultdict  # Use or ignore

def function_cycler(*fs : callable) -> callable:
    if len(fs) == 0:
        raise TypeError
    def cycler(x):
        f = fs[cycler.times_called % len(fs)]
        cycler.times_called += 1
        return f(x) 
    cycler.times_called = 0
    return cycler
    

def jobs(db1 : {str:{str:int}}, min_skill_level : int) -> {str}:
    return{k for s in db1.values() for k, v in s.items() if v >= min_skill_level} 

def rank(db1 : {str:{str:int}}) -> [str]:
    return sorted(db1, key = lambda x: (sum(db1[x].values())/-len(db1[x]), x))

def popular(db1 : {str:{str:int}}) -> [str]:
    popular_dict = {}
    for s in db1.values():
        for skill in s.keys():
            if skill  in popular_dict:
                popular_dict[skill] += 1
            elif skill not in popular_dict:
                popular_dict[skill] = 1
    return sorted(popular_dict, key = lambda x: (-popular_dict[x], x))

def who(db1 : {str:{(str,int)}}, job : str, min_skill_level : int) -> [(str,int)]:
    return sorted(((k, v[job]) for k, v in db1.items() if job in v and v[job] >= min_skill_level), key=(lambda t: (-t[1], t[0])))

def by_job(db1 : {str:{str:int}}) -> {str:{str:int}}:
    res = defaultdict(dict)
    for name, jobs in db1.items():
        for job, skill_lvl in jobs.items():
            res[job][name] = skill_lvl
    return res

def by_skill(db1 : {str:{str:int}}) -> [int,[str,[str]]]:
    db = defaultdict(lambda: defaultdict(list))
    for n, d in db1.items():
        for j, s in d.items():
            db[s][j].append(n)
    return [(s, [(j, sorted(n)) for j, n in sorted(d.items(), key=(lambda x: x[0]))]) for s, d in sorted(db.items(), key=(lambda x: -x[0]))]

if __name__ == '__main__':
    from goody import irange
    
    print('\nTesting function_cycler')
    try:
        cycler0 = function_cycler()
        print("Incorrect: Did not raise required exception for no-argument function call")
    except TypeError:
        print("Correct: rasised required exception for no-argument function call")
    
    cycler1 = function_cycler( (lambda x : x), (lambda x : x**2))
    print('Cycler 1:',[cycler1(x) for x in irange(1,10)],'... times called: ',cycler1.times_called)
    cycler2 = function_cycler( (lambda x : x+1), (lambda x : 2*x), (lambda x : x**2))
    print('Cycler 2:',[cycler2(x) for x in irange(1,10)],'... times called: ',cycler2.times_called)
 
    print('Cycler 1 again:',[cycler1(x) for x in irange(10,15)],'... times called: ',cycler1.times_called)
    print('Cycler 2 again:',[cycler2(x) for x in irange(10,20)],'... times called: ',cycler2.times_called)
    
    
    # Note: the keys in this dicts are not specified in alphabetical order
    db1 = {
          'Diane':   {'Laundry': 2,   'Cleaning': 4, 'Gardening': 3},
          'Betty':   {'Gardening': 2, 'Tutoring': 1, 'Cleaning': 3},
          'Charles': {'Plumbing': 2,  'Cleaning': 5},
          'Adam':    {'Cleaning': 4,  'Tutoring': 2, 'Baking': 1}
          }

    db2 = {
           'Adam': {'Laundry': 2, 'Driving': 2, 'Tutoring': 2, 'Reading': 1, 'Gardening': 1},
           'Emil': {'Errands': 4, 'Driving': 1, 'Baking': 3},
           'Chad': {'Repairing': 2, 'Reading': 2, 'Errands': 4, 'Baking': 2},
           'Ivan': {'Gardening': 5, 'Errands': 5, 'Reading': 4, 'Cleaning': 3},
           'Gene': {'Driving': 1, 'Laundry': 1, 'Baking': 2, 'Gardening': 2, 'Repairing': 2, 'Errands': 5},
           'Dana': {'Driving': 2}, 
           'Hope': {'Driving': 5, 'Reading': 3, 'Errands': 2, 'Shopping': 2, 'Gardening': 1, 'Laundry': 2},
           'Bree': {'Baking': 2, 'Errands': 5},
           'Faye': {'Tutoring': 2, 'Reading': 5, 'Repairing': 5, 'Baking': 4}
           }

    print('\nTesting jobs')
    print('jobs(db1,0):',jobs(db1,0))
    print('jobs(db1,3):',jobs(db1,3))
    print('jobs(db2,0):',jobs(db2,0))
    print('jobs(db2,5):',jobs(db2,5))


    print('\nTesting rank')
    print ('rank(db1):',rank(db1))
    print ('rank(db2):',rank(db2))


    print('\nTesting popular')
    print ('popular(db1):',popular(db1))
    print ('popular(db2):',popular(db2))


    print('\nTesting who')
    print("who(db1,'Cleaning',4):", who(db1,'Cleaning',4))
    print("who(db1,'Gardening',0):", who(db1,'Gardening',0))
    print("who(db1,'Tutoring',3):", who(db1,'Tutoring',3))
    print("who(db1,'Gambling',0):", who(db1,'Gambling',0))
    print("who(db2,'Baking',0):", who(db2,'Baking',0))
    print("who(db2,'Cleaning',1):", who(db2,'Cleaning',1))
    print("who(db2,'Driving',2):", who(db2,'Driving',2))
    print("who(db2,'Errands',3):", who(db2,'Errands',3))
    print("who(db2,'Gardening',4):", who(db2,'Gardening',4))
    print("who(db2,'Laundry',5):", who(db2,'Laundry',5))

    print('\nTesting by_job')
    print ('by_job(db1):',by_job(db1))
    print ('by_job(db2):',by_job(db2))


    print('\nTesting by_skill')
    print ('by_skill(db1):',by_skill(db1))
    print ('by_skill(db2):',by_skill(db2))



    print('\ndriver testing with batch_self_check:')
    import driver
    driver.default_file_name = 'bscq1F21.txt'
#     driver.default_show_traceback = True
#     driver.default_show_exception = True
#     driver.default_show_exception_message = True
    driver.driver()
