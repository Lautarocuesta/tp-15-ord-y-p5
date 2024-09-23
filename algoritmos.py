import py5
import random

# Lista a ordenar 
array = [1,4,2,3]
sorting_generator = None
delay = 30  
is_sorting = False

def setup():
    global array
    py5.size(800, 600)
    array = [py5.random(50, 550) for _ in range(50)]  # Lista aleatoria
    py5.frame_rate(60)

def draw():
    py5.background(220)
    draw_array(array)
    
    global is_sorting
    if is_sorting and sorting_generator:
        try:
            next(sorting_generator)
        except StopIteration:
            is_sorting = False

def draw_array(arr, idx1=None, idx2=None, swapped=False):
    py5.stroke(0)
    bar_width = py5.width / len(arr)
    for i in range(len(arr)):
        if i == idx1 or i == idx2:
            py5.fill(255, 0, 0)  # Rojo para comparación
        else:
            py5.fill(0, 255, 0) if swapped else py5.fill(255)  # Verde para intercambio
        py5.rect(i * bar_width, py5.height - arr[i], bar_width, arr[i])

def key_pressed():
    global sorting_generator, is_sorting, array
    if py5.key == 'b':
        sorting_generator = bubble_sort(array, draw_array, delay)
        is_sorting = True
    elif py5.key == 'q':
        sorting_generator = quick_sort(array, 0, len(array)-1, draw_array, delay)
        is_sorting = True
    elif py5.key == 'r':
        array = [py5.random(50, 550) for _ in range(50)]  # Reiniciar lista
        is_sorting = False

# Algoritmos de ordenamiento implementados
def bubble_sort(arr, draw_array, delay):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            draw_array(arr, j, j+1)  # Dibujar comparación
            py5.delay(delay)
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                draw_array(arr, j, j+1, swapped=True)  # Dibujar intercambio
                py5.delay(delay)
            yield

def quick_sort(arr, low, high, draw_array, delay):
    if low < high:
        pi = partition(arr, low, high, draw_array, delay)
        yield from quick_sort(arr, low, pi-1, draw_array, delay)
        yield from quick_sort(arr, pi+1, high, draw_array, delay)

def partition(arr, low, high, draw_array, delay):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        draw_array(arr, j, high)  # Dibujar comparación con el pivote
        py5.delay(delay)
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
            draw_array(arr, i, j, swapped=True)
            py5.delay(delay)
        yield
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

py5.run_sketch()
