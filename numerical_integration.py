import math

def partition_pts(a,b,n):
    lst = [a + x * (b - a) / n for x in range(n + 1)]
    return lst

def numerical_integration(lower_input, upper_input):
    area_of_rectangles = 0
    single_area_of_rectangle = 0
    #lower_input = 0
    #upper_input = 3.14159
    n_subparts_input = 7
        
    subparts = partition_pts(lower_input, upper_input, n_subparts_input)
    #print(subparts)

    #print("------------------------\n")


    ranges = [10, 100, 100, 1000, 10000, 100000, 1000000]
    cont = 0

    for x in ranges:
        base_rectangle = subparts[cont+1]-subparts[cont]
        height_rectangle = abs(math.sin(x))
        
        #print("BASE RECTANGLE: "+str(base_rectangle))
        #print("HEIGHT RECTANGLE: "+str(height_rectangle))
        
        single_area_of_rectangle = base_rectangle * height_rectangle
        area_of_rectangles += single_area_of_rectangle
        
        #print("Single for value " + str(x) + ": "+str(single_area_of_rectangle))
        #print("Total value: "+str(area_of_rectangles))
        
        #print("------------------------\n")
        single_area_of_rectangle = 0
        cont = cont+1

    #print("Total value: "+str(area_of_rectangles))
    return str(area_of_rectangles)
