#Zad. 2
#Napisz program wyświetlający liczby całkowite z przedziału <100; 50> w porządku malejącym. Wykonaj to na pętli for i while.

arr = [1, 2, 3, 4, 5]
# arr[0:len(arr):2] # = arr[start:stop:end]

#for liczba in range(100, 50, -1):
#    print(liczba)

counter = 100
while counter >= 50:
    print(counter)
    counter -= 1
