from bokeh.plotting import figure, output_file, show
import random

x1=[]
y1=[]
x2=[]
y2=[]

def montecarlo(sample):
    est_area = 0
	
    for i in range(sample):
        x = random.random()
        y = random.random()
        z = (x**2 + y**2)**0.5
		
        if z <= 1:
            est_area += 1
            x1.append(x)
            y1.append(y)
        else:
            x2.append(x)
            y2.append(y)
			
    return est_area/sample

print("Approximated pi:", montecarlo(10000)*4)
output_file("arc.html")

p = figure(plot_width=750, plot_height=750)
p.circle(x1, y1, size=3, color="blue")
p.circle(x2, y2, size=3, color="orange")

show(p)
