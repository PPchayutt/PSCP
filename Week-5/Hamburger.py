"""Hamburger"""
top = int(input())
bottom = int(input())
meat = (top+bottom)*2
meat2 = "*" * meat
topbread = "|" * top
bottombread = "|" * bottom
print(topbread+meat2+bottombread)
