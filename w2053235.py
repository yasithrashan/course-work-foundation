# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code soluƟon.
# Student ID: .........w_2053235 / 20222033....................
# Date: .......12/14/2023......................

#import graphics module
from graphics import *

#Create a Window
win=GraphWin("Histogram",600,500)
win.setBackground("#ecf3ec")

# Set the width and height of each bar
bar_width = 100
bar_height_scale = 40

# assign value for the x 
x = 75

# create a dictionary to progress_count
result_count={"Progress" : 0, "Trailer" : 0, "Retriever" : 0, "Exclude" : 0}

# create a list
result_list=[]

# define progression outcome function
def progression_outcome(pass_credits, fail_credits):
    if pass_credits == 120:
        outcome="Progress"
        
    elif pass_credits == 100:
        outcome=("Progress (module trailer)")
        
    elif fail_credits < 80:
        outcome=("Module retriever")
        
    else:
        outcome=("Exclude")

     # Return the output 'outcome'   
    return outcome

while True:
    try:
        # check credits out of range or not
        credits=[0,20,40,60,80,100,120]
        
        pass_credits=int(input("\nEnter your total PASS credits: "))
        if pass_credits not in credits:
            print("Out of range")
            continue
            

        defer_credits=int(input("Enter your total DEFER credits: "))
        if defer_credits not in credits:
            print("Out of range")
            continue
            

        fail_credits=int(input("Enter your FAIL credits: "))
        if fail_credits not in credits:
            print("Out of range")
            continue
            
            

        total_credits=pass_credits+defer_credits+fail_credits
        if total_credits !=120:
            print("Total is incorrect")
            continue
            

        # Print the outcome
        result= progression_outcome(pass_credits,fail_credits)
        print(result)
        

        # Outcome add to dictionary 'result_count


        print(result_count)
        if result=="Progress":
            result_count["Progress"] += 1 
            
        elif result=="Progress (module trailer)":
            result_count["Trailer"] += 1
    
        elif result=="Module retriever":
            result_count["Retriever"] += 1

        elif result=="Exclude":
            result_count["Exclude"] += 1
        print(result_count)


        # Append outcome to the list 'data_list'
        print(result_list)
        result_list.append((progression_outcome(pass_credits,fail_credits),pass_credits, defer_credits, fail_credits))
        print(result_list)

        # get the option to stop the process or continue
        print("\nWould you like to enter another set of data?")
        option=input("Enter 'y' for yes of 'q' for quit and view the results: ")
        if option == 'q':
            break
        
    except ValueError :
        print("Integer required")

color_map={"Progress":"#97fb97",
            "Trailer":"#95c682",
            "Exclude":"#d8b4b4",
            "Retriever":"#a2bd6e"
           }

# draw bars in historam according to the dictionary
for key, value in result_count.items():
    # calculate the height of the bar based on the value
    bar_height = value * bar_height_scale
    bar_color = color_map.get(key,"pink")
    
    #draw bars in the historam
    bar = Rectangle(Point(x, 400), Point(x + bar_width, 400 - bar_height))
    bar.setFill(bar_color)
    bar.draw(win)

     # draw aline
    line=Line(Point(50,400), Point(550,400))
    line.draw(win)
    
    # add label for each bar
    label = Text(Point(x + bar_width // 2, 420), key)
    label.setStyle("bold")
    label.setTextColor("#7e8aa0")
    label.draw(win)

    count_label = Text(Point(x + bar_width // 2, 400 - bar_height - 10), str(value))
    count_label.setStyle("bold")
    count_label.setTextColor("#7e8aa0")
    count_label.draw(win)

    # Update x for the next bar
    x += bar_width + 15

# Text for displaying "Histogram Result" at the top middle
title_text = Text(Point(150, 20), "Histogram Results")
title_text.setSize(16)
title_text.setStyle("bold")
title_text.setTextColor("#656766")
title_text.draw(win)

# total number of students
total_students = sum(result_count.values())
total_label = Text(Point(125, 450), f"{total_students} outcomes in total.")
total_label.setStyle("bold")
total_label.setTextColor("#7e8aa0")
total_label.draw(win)

# part 2
# Append outcome to the list 'data_list' 
print("\npart 2:")
for data in result_list:
    formatted_output = "{} - {}, {}, {}".format(data[0], data[1], data[2], data[3])
    print(formatted_output)
    
# part 3
# save data into text file
with open ("progression_data.txt","w") as data_file:
    for data in result_list:
        formatted_output = "{} - {}, {}, {}".format(data[0], data[1], data[2], data[3])
        data_file.write(f"{formatted_output}\n")
        
# access and print data from the text file
print("\nPart 3:")
with open ("progression_data.txt", "r") as data_file:
    for line in data_file:
        print(line.strip(), end='\n')

























        
