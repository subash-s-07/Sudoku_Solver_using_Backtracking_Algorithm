def passgrid():
     f = open("Solution.txt")
     grid = []
     dum = []
     for i in range(9):
          a = f.readline()
          for j in range(9):
               dum.append(int(a[j]))
          grid.append(dum)
          dum = []
     print(grid)
     return grid
          
passgrid()
