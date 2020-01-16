from z3 import* 


flag = [BitVec("flag{:02x}".format(i),8) for i in range(0x27)]

s = Solver()

s.add(flag[0]) == ord("T")
s.add(flag[1]) == ord("W")
s.add(flag[2]) == ord("C")
s.add(flag[3]) == ord("T")
s.add(flag[4]) == ord("F")
s.add(flag[5]) == ord("{")
s.add(flag[0x26]) == ord("}")
s.add(flag[0x25]) == ord("5")
s.add(flag[0x07]) == ord("f")
s.add(flag[0x0B]) == ord("8")
s.add(flag[0x0C]) == ord("7")
s.add(flag[0x17]) == ord("2")
s.add(flag[0x1F]) == ord("4")






