from z3 import*

#x = Int('x')
#y = Int('y')

#print simplify(x+y + 2*x +3)
#print simplify(x < y + x+2)
#print simplify(And(x+1 >= 3 , x**2 + x**2 + y**2 +2 >=5))

#print x**2 + y**2 >=1 
#set_option(html_mode = False)
#print x**2 + y**2 >=1 
"""
n = x+y >=3 
print "num args : " , n.num_args()
print "children : " , n.children()
print "first child : " , n.arg(0)
print "sec child : " , n.arg(1)
print "operator : " , n.decl()
print "operator name :" , n.decl().name()

s = Solver()
print s 
s.add(x > 10 , y == x+2 )
print s 
print "Solving contraints in solver"
print s.check()
print "Create a new scope"
s.push()
s.add(y <11 )
print s.check()
s.pop()
print s 
print s.check()
"""

x = BitVec('x',16)
y = BitVec('y',16)
print x , y
print x+ 2 
print (x+2 ).sexpr()
print simplify(x+y-1)










