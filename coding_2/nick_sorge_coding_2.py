'''Turtle Graphics Line Graph Generator'''

# Nick Sorge
# 9/26/2023
# CS 1410

import turtle

def main():
    '''
    Change the first 6 input variables to make a graph!
    Number of data labels must be equivalent to the number of 
    colors and the number of data sets.
    '''
    # Setup for turtle window
    win = turtle.Screen()
    win.bgcolor('black')

    #START INPUT#
    # Input Graph Title
    title = ('Freshman Life Goals\n' +
            '(Percentage of students committed to goal)')
    # Input line Lables
    data_labels = ['well off financially', 'meaningful philosophy in life',
                   'bench maxing', 'thugging it out', 'apocalypse farm bunker']
    # Input line Data Points
    data = [[59, 74, 73, 77, 78], [60, 43, 44, 51, 65], [71, 67, 89, 55, 62],
            [15, 25, 50, 75, 15], [25, 65, 21, 97, 82]]
    # Input the x axis starting value and interval
    x_label = (1978, 10)
    # Input the y axis lower bound and upper bound
    y_bounds = (0, 100)
    # Input possible colors for lines
    colors = ('red', 'green', 'blue', 'orange', 'purple')
    #END INPUT#

    # Turtles
    graph = turtle.Turtle()
    x_turtle = turtle.Turtle()
    y_turtle = turtle.Turtle()
    line = turtle.Turtle()

    # Length of x axis interval
    x_interval = int(600 / (len(data[0]) + 1))
    # Number of x axis labels
    x_count = len(data[0])
    # Number of lines
    lines = len(data_labels)

    # Function calls
    graph_setup(data_labels, colors, title, graph)
    x_tick_marks(x_label, x_interval, x_count, x_turtle)
    y_tick_marks(data, y_bounds, lines, y_turtle)
    draw_lines(data, colors, x_interval, y_bounds, lines, line)
    # Keeps turtle window open after program completes
    turtle.done()

def turtle_setup(input_name):
    ''' 
    Sets up the turtle with all relevant settings.

    Args:
        input_name: name of the turtle
    '''
    input_name.color('white')
    input_name.speed(0)
    #input_name.ht()
    input_name.pu()
    return input_name

def graph_setup(graph_labels, graph_colors, graph_title, graph_turtle):
    '''
    Sets up the graph area, title, and legend.
    
    Args:
        graph_labels: Used to print the legend of line labels
        graph_colors: Used to have the legend display the correct color
        graph_title: Used to print the correct graph title
        graph_turtle: Inputs the turtle to draw graph'''
    # graph_turtle setup
    turtle_setup(graph_turtle)
    # Graph setup
    graph_turtle.goto(-300, 300)
    graph_turtle.pd()
    graph_turtle.seth(270)
    graph_turtle.fd(600)
    graph_turtle.seth(0)
    graph_turtle.fd(600)
    graph_turtle.pu()
    # Prints graph title
    graph_turtle.goto(-300, 320)
    graph_turtle.write(graph_title)
    # Prints graph legend using number of labels to determine how many times to loop
    for i, val in enumerate(graph_labels):
        # Sends turtle to the correct coordinate
        graph_turtle.goto(-290, -320 - (i * 15))
        graph_turtle.pd()
        # Changes color
        graph_turtle.color(graph_colors[i])
        # Draws colored line
        graph_turtle.fd(20)
        graph_turtle.pu()
        graph_turtle.seth(270)
        # Moves 5 pixels down and forward to better space label text
        graph_turtle.fd(5)
        graph_turtle.seth(0)
        graph_turtle.fd(5)
        # Prints label text
        graph_turtle.write(val)

def x_tick_marks(x_tick_label, x_tick_interval, x_tick_line_count, x_tick_turtle):
    '''
    Draws the x axis tick marks
    
    Args:
        x_tick_label: Uses the x_label variable to determine starting value and increment
        x_tick_interval: Determines the length between x ticks
        x_tick_line_count: Used to determine number of x ticks to print
        x_tick_turtle: Inputs the turtle to draw the ticks'''
    # Turtle setup
    turtle_setup(x_tick_turtle)
    x_tick_turtle.goto(-300, -300)
    # Draws x axis ticks using x axis interval and the x axis label start point
    for i in range(x_tick_line_count):
        # Moves forward the length of 1 x interval
        x_tick_turtle.fd(x_tick_interval)
        # Draws upward tick on x axis
        x_tick_turtle.seth(90)
        x_tick_turtle.pd()
        x_tick_turtle.fd(20)
        x_tick_turtle.pu()
        # Prints x axis label using i counter to determine the correct number of incremetns to add
        x_tick_turtle.write(int(x_tick_label[0] + (x_tick_label[1] * i)))
        # Resets position of turtle to be on x axis
        x_tick_turtle.bk(20)
        x_tick_turtle.seth(0)

def y_tick_marks(yt_data, yt_bounds, y_tick_line_count, yt_turtle):
    '''
    Calculates and displays the y axis minimum and maximum tick marks.
    
    Args:
        yt_data: nested list of datapoints
        yt_bounds: upper and lower y axis bound to calculate position of y axis ticks
        y_tick_line_count: used to know how many data sets to iterate over
        yt_turtle: inputs the y_axis turtle to draw the y axis ticks
        '''
    # Sets min and max to something within data range, min first, max second
    min_max = [yt_data[0][0], yt_data[0][0]]
    # Enumerates over the nested data points to determine min and max
    for i in range(y_tick_line_count):
        for j, val in enumerate(yt_data[i]):
            # Determines if current data point is bigger or smaller than the current one
            if val < min_max[0]:
                min_max[0] = yt_data[i][j]
            if val > min_max[1]:
                min_max[1] = yt_data[i][j]
    # Turtle setup
    turtle_setup(yt_turtle)
    yt_turtle.goto(-300, -300)
    # Turtle draws y axis tick marks
    for i in range(2):
        # Calculates y position of y axis ticks based on the difference of the elements in the
        # yt_bounds variable multiplied by the difference of the lower boound and min or max value
        yt_turtle.goto(-300, (600 / (yt_bounds[1] - yt_bounds[0]) * (min_max[i] - yt_bounds[0]) - 300))
        # Positions turtle to print min or max value
        yt_turtle.pd()
        yt_turtle.fd(20)
        # Writes min or max value based on i counter
        yt_turtle.write(min_max[i])
        # Resets turtle to y axis line
        yt_turtle.pu()
        yt_turtle.bk(20)

def draw_lines(line_datapoints, line_colors, x_axis_interval, y_axis_bounds, line_count, line_turtle):
    '''
    Draws the actual lines for the line graph.
    
    Args:
        line_datapoints: nested list of datapoints
        line_colors: list of possible colors
        x_axis_interval: length of x axis interval
        y_axis_bounds: upper and lower y axis bounds
        line_count: number of lines to display
        line_turtle: inputs the line turtle to draw the lines
    '''
    # Turtle setup
    turtle_setup(line_turtle)
    line_turtle.shape('circle')
    line_turtle.shapesize(0.3)
    # Enumerates over the nested data lists and draws a line stamping the data on the graph
    for i in range(line_count):
        # Changes color after each full data list
        line_turtle.color(line_colors[i])
        # Enumerates values in each individual data list
        for j, val in enumerate(line_datapoints[i]):
            # Positions turtle at correct x interval length and calculates y position by
            # dividing the length of the y axis by the difference of y bounds then multiplies
            # that by the difference of the value and the lower y bound
            line_turtle.goto(x_axis_interval * (j + 1) - 300,
                     (600 / (y_axis_bounds[1] - y_axis_bounds[0]) * (val - y_axis_bounds[0]) - 300))
            line_turtle.pd()
            # Stamps a circle and writes value to graph
            line_turtle.stamp()
            line_turtle.write(val)
        line_turtle.pu()

if __name__ == '__main__':
    main()

# Thoughts
#
# I enjoyed this assignment as much as I dislike using turtle graphics. I chose
# not to use any chatterbox functions to get data as it seemed to tedious to
# get information that way. Changing the first 6 variables in main will allow
# the user to change the title, data labels, data, x labels, y bounds, and colors
# of the graph.
