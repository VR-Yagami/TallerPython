#Ciclo while
if __name__ == '__main__':
     num=int(input("proporciona un numero: "))
     fact=1
     i=2
     while i<num:
         fact=fact * i
         i = i+1
         print(f"el factorial de {num} es{fact}")