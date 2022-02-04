import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable = False,  defaults =  {}):
    def show_listing(s):
        for ln_number, text_of_ln in enumerate(s.split('\n'),1):       
            print(f' {ln_number: >3} {text_of_ln.rstrip()}')

    fields = []
    regex = re.compile('^[A-z][(A-z)(1-9)_]*?$')
    regex2 = re.compile('^[a-z].*$')
    if re.match(regex, str(type_name)) == None or type_name in keyword.kwlist:
        raise SyntaxError
    
    if type(field_names) not in [list, str]:
        raise SyntaxError
    
    if type(field_names) is str:
        if ' ,' in field_names:
            fields = field_names.split(',')
            for item in fields:
                if item in keyword.kwlist or not item.islower() or re.match(regex2, str(item)) == None:
                    raise SyntaxError
        else:
            fields = field_names.replace(',', '').split(' ')
            for item in fields:
                fields[:] = [var for var in fields if var]
                if item in keyword.kwlist or not item.islower() or re.match(regex2, str(item)) == None:
                    raise SyntaxError
        for item in fields:
            if item is  None or item == '':
                fields.pop(item)
                    
    if type(field_names) is list:
        for item in field_names:
            if item in keyword.kwlist or re.match(regex, str(item)) == None:
                raise SyntaxError
            else:
                fields.append(item)
        
    

    class_definition = f"""class {type_name}:
    _fields = {fields}
    _mutable = {mutable}
        
    def __init__(self,"""
    init_str = ''
    for i in fields:
        init_str = init_str + f'{i},'
    class_definition = class_definition + f"""{init_str[:-1]}):"""
    
    for i in fields:
        class_definition = class_definition + f"""
        self.{i} = {i }"""
        
    class_definition = class_definition + f"""
    def __repr__(self):
        return f"{type_name}({{','.join(str(k)+\'=\'+repr(v) for k,v in self.__dict__.items())}})"
    """
    for i in fields:
        class_definition = class_definition + f"""
        
    def get_{i}(self):
        return self.{i}"""
    class_definition = class_definition + f"""
    
    def __getitem__(self, index):
        if type(index) is int:
            return self.__dict__[self._fields[index]]
        elif index in self._fields:
            return self.__dict__[index]
        else: raise IndexError()"""
    
    class_definition = class_definition + f"""

    def __eq__(self, right):
        return repr(self) == repr(right)
        """
    class_definition = class_definition + f"""
    
    def _asdict(self):
        return self.__dict__
    """
    
    class_definition = class_definition + f"""
    
    def _make(iterable):
        return {type_name}(*iterable)
        
    """
    
    
    class_definition = class_definition + f"""
    
    def _replace(self,**kargs):
        if self._mutable == True:
            for k, v in kargs.items():
                if k not in self._fields:
                    raise TypeError
                elif k in self._fields:
                    self.__dict__[k] = v              
        elif self._mutable == False:
            newobject = eval(str(repr(self)))
            for k, v in kargs.items():
                if k not in newobject._fields:
                    raise TypeError
                elif k in newobject._fields:
                    newobject.__dict__[k] = v
            return newobject 
    """
    
    
        
    # Debugging aid: uncomment show_listing below so it always displays source code
    show_listing(class_definition)
    
    # Execute class_definition's str from name_space; followed by binding the
    #   attribute source_code to the class_definition; after the try/except bloc
    #   return this created class object; if any syntax errors occur, show the
    #   listing of the class and trace the error, in the except clause
    
    name_space = dict( __name__ = f'pnamedtuple_{type_name}' )                
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):                    
        show_listing(class_definition)
        traceback.print_exc()
    return name_space[type_name]


    
if __name__ == '__main__':
    # Test simple pnamedtuple below in script: Point=pnamedtuple('Point','x,y')
    Triple1 = pnamedtuple('Triple1', 'a b c')
    #driver tests
    import driver  
    driver.default_file_name = 'bscp3F21.txt'
#     driver.default_show_exception_message = True
#     driver.default_show_traceback = True
    driver.driver()
