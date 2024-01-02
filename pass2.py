def passgrid1():
     f = open("sudgridpass.txt")
     grid = []
     dum = []
     for i in range(9):
          a = f.readline()
          for j in range(9):
               dum.append(int(a[j]))
          grid.append(dum)
          dum = []
     print(len(grid))
     return grid
          
passgrid1()
