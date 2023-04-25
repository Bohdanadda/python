import numpy as np

my_array = np.arange(10,40,2)

print(my_array)

print("Rozmiar tablicy:",my_array.shape)

my_array.resize((5,3))
print("Nowy rozmiar:",my_array.shape)

my_array += 3
print("tablica po dodaniu 3 do każdego elementu:\n",my_array)

my_array = my_array.repeat(2)
print("tablica po wielkratnieniu każdego elemetu :\n",my_array)

print("liczba podzielna przes 6:",my_array[my_array % 6 == 0])

def change(A,I):
    B = np.copy(A)
    B[I] = 0
    return B

A = np.array([1,2,3,4,5])
I = [0,2,4]
print("Tablica A:",A)
print("Tablica I:",I)
print("tablicz po zastopieniu elementów na indeksach I wartosci 0 :\n",change(A,I))