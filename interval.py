from goody import type_as_str
from math import sqrt

class Interval:
    # Helper Methods
    def _includes0(self):
        return self.min <= 0 <= self.max
   
    @staticmethod
    def _order2(a,b):
        return min(a,b),max(a,b)

    
    @staticmethod
    def _order4(a,b,c,d):
        return min(a,b,c,d),max(a,b,c,d)

     
    @staticmethod
    def _validate_arguments(l,r):
        return type(l) in [int,float,Interval] and type(r) in [int,float,Interval]
        
        
    def __init__(self, mini, maxi):
        self.mini = mini
        if maxi == None:
            self.maxi = mini
        else:
            self.maxi = maxi
        
    @staticmethod
    def min_max(mini, maxi = None):
        assert type(mini) == int or type(mini) == float
        if maxi != None:
            assert type(maxi) == int or type(maxi) == float
            assert mini <= maxi
        else:
            return Interval(mini, mini)            
        return Interval(mini, maxi)
    
    @staticmethod
    def mid_err(mid, error = 0):
        assert type(mid) == int or type(mid) == float
        assert type(error) == int or type(error) == float
        assert error >= 0
        return Interval((mid - error), (mid + error))
    
    
    def best(self, test = None):
        mini = self.mini
        maxi = self.maxi
        avg = (mini + maxi)/2
        return avg
    
    def error(self, test = None):
        return (self.maxi - self.mini)/2
    
    def relative_error(self, test = None):
        error = (self.maxi - self.mini)/2
        best = (self.mini + self.maxi)/2
        return 100 * abs(error/best)
    
    def __repr__(self):
        return 'Interval(' + str(self.mini) + ',' + str(self.maxi) + ')'
    
    def __str__(self):
        return str(self.best(self)) + '(+/-' + str(self.error(self)) + ')'
    
    def __bool__(self):
        if self.error(self) != 0:
            return True
        else:
            return False
        
    def __pos__(self):
        return Interval((self.mini),(self.maxi))   
    
    def __neg__(self):
        x = (-1*(self.maxi))
        y = (-1 * self.mini)
        return Interval(x, y)
        
    def __add__(self, right):
        if type(right) is int or type(right) is float:
            x = self.mini + right
            y = self.maxi + right
        elif type(self) is int or type(self) is float:
            x = self + right.mini
            y = self + right.maxi 
        elif type(self) is str or type(right) is str:
            raise TypeError
        else:
            x = self.mini + right.mini
            y = self.maxi + right.maxi
        return Interval(x,y)
    
    def __radd__(self, left):
        if type(left) is int or type(left) is float:
            x = self.mini + left
            y = self.maxi + left
        elif type(self) is int or type(self) is float:
            x = self + left.mini
            y = self + left.maxi 
        elif type(self) is str or type(left) is str:
            raise TypeError
        else:
            x = self.mini + left.mini
            y = self.maxi + left.maxi
        return Interval(x,y)

    def __sub__(self, right):
        if type(right) is int or type(right) is float:
            x = self.mini - right
            y = self.maxi - right
        elif type(self) is int or type(self) is float:
            x = self - right.mini
            y = self - right.maxi 
        elif type(self) is str or type(right) is str:
            raise TypeError
        else:
            x = self.mini - right.maxi
            y = self.maxi - right.mini
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)
    
    def __rsub__(self, left):
        if type(left) is int or type(left) is float:
            x = left - self.mini
            y = left - self.maxi
        elif type(self) is int or type(self) is float:
            x = left.mini - self
            y = left.maxi - self 
        elif type(self) is str or type(left) is str:
            raise TypeError
        else:
            x = left.mini - self.maxi
            y = left.maxi - self.mini 
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)

    def __mul__(self, right):
        if type(right) is int or type(right) is float:
            x = self.mini * right
            y = self.maxi * right
        elif type(self) is int or type(self) is float:
            x = self * right.mini
            y = self * right.maxi 
        elif type(self) is str or type(right) is str:
            raise TypeError
        else:
            a = self.mini * right.mini
            b = self.maxi * right.maxi
            c = self.mini * right.maxi
            d = self.maxi * right.mini
            prodlist = [a, b, c, d]
            x = min(prodlist)
            y = max(prodlist)
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)
        
    def __rmul__(self, left):
        if type(left) is int or type(left) is float:
            x = self.mini * left
            y = self.maxi * left
        elif type(self) is int or type(self) is float:
            x = self * left.mini
            y = self * left.maxi 
        elif type(self) is str or type(left) is str:
            raise TypeError
        else:
            a = self.mini * left.mini
            b = self.maxi * left.maxi
            c = self.mini * left.maxi
            d = self.maxi * left.mini
            prodlist = [a, b, c, d]
            x = min(prodlist)
            y = max(prodlist)
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)
    
    def __truediv__(self, right): 
        
        if type(right) is int or type(right) is float:
            x = self.mini / right
            y = self.maxi / right
        elif type(self) is int or type(self) is float:
            x = self / right.mini
            y = self / right.maxi 
        elif type(self) is str or type(right) is str:
            raise TypeError
        else:
            if right.mini < 0 and right.maxi > 0:
                raise ZeroDivisionError
            a = self.mini / right.mini
            b = self.maxi / right.maxi
            c = self.mini / right.maxi
            d = self.maxi / right.mini
            prodlist = [a, b, c, d]
            x = min(prodlist)
            y = max(prodlist)
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)  
        
    def __rtruediv__(self, left):         
        if type(left) is int or type(left) is float:
            if self.mini < 0 and self.maxi > 0:
                raise ZeroDivisionError
            x = left / self.mini
            y = left / self.maxi
        elif type(self) is int or type(self) is float:
            if self.mini < 0 and self.maxi > 0:
                raise ZeroDivisionError
            x = left.mini / self
            y = left.maxi / self 
        elif type(self) is str or type(left) is str:
            raise TypeError
        else:
            if self.mini < 0 and self.maxi > 0:
                raise ZeroDivisionError
            a = left.mini / self.mini
            b = left.maxi / self.maxi
            c = left.maxi / self.mini
            d = left.mini / self.maxi
            prodlist = [a, b, c, d]
            x = min(prodlist)
            y = max(prodlist)
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)   

    
    def __pow__(self,right):
        if  type(right) is not int:
            raise TypeError
        elif right == 0:
            return Interval(1.0,1.0)
        elif right > 0:
            x = (self.mini)**(right)
            y = (self.maxi)**(right)
            if x <= y:
                return Interval(x,y)
            elif y <= x:
                return Interval(y,x)
        elif right < 0:
            x = (1/(self.mini))**(abs(right))
            y = (1/(self.maxi))**(abs(right))
            if x <= y:
                return Interval(x,y)
            elif y <= x:
                return Interval(y,x)
    
    
    def __eq__(self, right):
        if type(self) == Interval and type(right) == Interval:
            if self.mini == right.mini and self.maxi == right.maxi:
                return True
            return False
        elif type(self) == Interval and type(right) != Interval:
            if self.mini == right and self.maxi == right:
                return True
            return False
        elif type(right) == Interval and type(self) != Interval:
            if right.mini == self and right.maxi == self:
                return True
            return False
        
    def __gt__(self, right):
        assert self != right
        assert Interval.compare_mode != None
        assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'
        if (type(self) == Interval and (type(right) != int and type(right) != float and type(right)!= Interval)):
            return NotImplemented
        if Interval.compare_mode == 'liberal':
            if type(self) == Interval and type(right) == Interval:
                if self.best(self) > right.best(right):
                    return True
            else:
                if self.best() > right:
                    return True
            return False
            
        elif Interval.compare_mode == 'conservative': 
            if type(self) == Interval and type(right) == Interval:
                if self.mini > right.maxi:
                    return True
            elif self.maxi > right:
                return True
            return False
        
    def __ge__(self, right):
        assert self != right
        assert Interval.compare_mode != None
        assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'
        if (type(self) == Interval and (type(right) != int and type(right) != float and type(right)!= Interval)):
            return NotImplemented
        if Interval.compare_mode == 'liberal':
            if type(self) == Interval and type(right) == Interval:
                if self.best(self) >= right.best(right):
                    return True
            else:
                if self.best() >= right:
                    return True
            return False
            
        elif Interval.compare_mode == 'conservative': 
            if type(self) == Interval and type(right) == Interval:
                if self.mini >= right.maxi:
                    return True
            elif self.maxi >= right:
                return True
            return False
        
    def __lt__(self, left):
        assert self != left
        assert Interval.compare_mode != None
        assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'
        if (type(self) == Interval and (type(left) != int and type(left) != float and type(left)!= Interval)):
            return NotImplemented
        if Interval.compare_mode == 'liberal':
            if type(self) == Interval and type(left) == Interval:
                if self.best(self) < left.best(left):
                    return True
            else:
                if self.best() < left:
                    return True
            return False
            
        elif Interval.compare_mode == 'conservative': 
            if type(self) == Interval and type(left) == Interval:
                if self.maxi < left.mini:
                    return True
            elif self.maxi < left:
                return True
            return False
            
    def __le__(self, left):
        assert self != left
        assert Interval.compare_mode != None
        assert Interval.compare_mode == 'liberal' or Interval.compare_mode == 'conservative'
        if (type(self) == Interval and (type(left) != int and type(left) != float and type(left)!= Interval)):
            return NotImplemented
        if Interval.compare_mode == 'liberal':
            if type(self) == Interval and type(left) == Interval:
                if self.best(self) <= left.best(left):
                    return True
            else:
                if self.best() <= left:
                    return True
            return False
            
        elif Interval.compare_mode == 'conservative': 
            if type(self) == Interval and type(left) == Interval:
                if self.maxi <= left.mini:
                    return True
            elif self.maxi <= left:
                return True
            return False
        
    def __abs__(self): 
        if self.mini < 0 and self.maxi >= 0:
            return Interval(0.0, self.maxi)
        else:   
            x = abs(self.mini)
            y = abs(self.maxi)
        if x <= y:
            return Interval(x,y)
        if y <= x:
            return Interval(y,x)   
        
    def sqrt(self): 
        if self.mini < 0 or self.maxi < 0:
            raise ValueError
        else:
            x = (self.mini)**(0.5)
            y = (self.maxi)**(0.5)
            return Interval(x, y)   
    
    def __setattr__(self, name, value):
        assert name not in self.__dict__
        assert type(value) in {int, float}
        assert name in {'mini', 'maxi'}
        self.__dict__[name] = value
        return None


    
if __name__ == '__main__':
    '''
    g = Interval.mid_err(9.8,.05)
    print(repr(g))
    g = Interval.min_max(9.75,9.85)
    print(repr(g))
    d = Interval.mid_err(100,1)
    t = (d/(2*g)).sqrt()
    print(t,repr(t),t.relative_error())    
'''
    import driver    
    driver.default_file_name = 'bscp22F21.txt'
#     driver.default_show_exception=True
#     driver.default_show_exception_message=True
#     driver.default_show_traceback=True
    driver.driver()
