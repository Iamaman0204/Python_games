import time
import turtle
import pandas as pd

Font=["Arial", 9, "bold"]
Font_new=["Arial", 40, "bold"]

screen = turtle.Screen()
screen.title("My US Game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")

df = pd.read_csv('50_states.csv')
print(df.columns)

jimmy = turtle.Turtle()
jimmy.penup()
guessed_list =[]

while True:
    answer_string = screen.textinput(title="Guess the State", prompt="Enter the state name of USA")
    # if (df['state'].eq(answer_string)).any():
    df_new=df[df['state'].str.lower() == answer_string.lower()].reset_index()
    if len(df_new)==1:
        if not answer_string in guessed_list:
            guessed_list.append(answer_string.lower())
            print(guessed_list)

        jimmy.goto(df_new.iloc[0, 2], df_new.iloc[0,3])
        jimmy.write(df_new.iloc[0, 1], move=True, align='center', font=Font)
    elif answer_string==None or answer_string.lower() == "quit":
        break
    if len(guessed_list) == 2:
        john = turtle.Turtle()
        john.penup()
        john.hideturtle()
        john.goto(0, 250)
        john.write("YOU WON BITCH", move=True, align='center', font=Font_new)
        screen.ontimer(john.clear, 5000)
        time.sleep(5)
        john.goto(0, 250)
        john.write("PLAY AGAIN", move=True, align='center', font=Font_new)
        screen.ontimer(john.clear, 5000)
        time.sleep(5)
        john.goto(0, 250)
        john.write("BYE", move=True, align='center', font=Font_new)
        screen.ontimer(john.clear, 5000)
        time.sleep(5)
        break

screen.exitonclick()
