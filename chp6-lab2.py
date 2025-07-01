import matplotlib.pyplot as plt

def main():

    #Lays the foundation for the graphs apperance
    plt.grid(True)
    plt.axis('square')

    #Limiting factors for the graph
    plt.xlim(xmin=-20, xmax=20)
    plt.ylim(ymin=-20, ymax=20)

    #Inputs for the m and b values for y=m*x+b
    print('This program with graph a line when given the slope and intercept.\n Please enter the values for m and b given the form y = mx + b')
    m = float(input('m: '))
    b = float(input('b: '))

    #Creates points for the x and y values on the graph by using y=m*x+b 
    x_coords = [x for x in range(-20, 21)]
    y_coords = [m * x + b for x in x_coords]

    #Plots the points given onto the graph in memory
    plt.plot(x_coords, y_coords)

    #Shows graph
    plt.show()
   
    
main()
