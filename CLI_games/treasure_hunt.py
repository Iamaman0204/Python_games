import time

start = """............................................



          ______ _______ ______ ______ _______ 
         / __  //__  __// __  // __  //__  __/
        / / /_/   / /  / /_/ // /_/ /   / /  
        _\ \     / /  / __  //   __/   / / 
      / /_/ /   / /  / / / // /\ \    / /  
     /_____/   /_/  /_/ /_//_/  \_\  /_/  
            PRESS ENTER TO CONTINUE!
    

............................................"""
good_ending = """               _________
              |MMMMMMMMM|                _
  ________    |MMMMMMMMM|              _|l|_
 |!!!!!!!_|___|MMMMMMMMM|             |lllll|
 |!!!!!!|=========|MMMMM|             |lllll|_______
 |!!!!!!|=========|MMMMM|            _|lllll|HHHHHHH|
 |!!!!!!|=========|MMMMM|   ________|lllllllll|HHHHH|
 |!!!!!!|=========|MMMMM|  |unununun|lllllllll|HHHHH|______
 |!!!!!!|=========|MMMMM|  |nunununu|lllllllll|HH|:::::::::|
 |!!!!!!|=========|MMM__|..|un__unun|lllllllll|HH|:::::::::|
 |!!!!!!|=======_=|M_( ')' );' .)unu|lllllllll|HH|:::::::::|
 |!!!_!!|======( )|(. ` ,) (_ ', )un|lllllllll|HH|:::::::::| ~~~
 |!!(.)!|===__(`.')_(_ ')_,)(. _)unu|lllllllll|HH|:__::::::|~~  ~~
 |!(.`')|==( .)' .)MMM|M|| |un|nunun|lllllllll|``|( ,)_::::| ~~~~ ~
  -(: _)|=(`. ')_)|---|- '  ``|`````|lll____ll|  (_; `'):::|~~~  ~~~
     |  |==(_'_)|=|    ______        ''/\   \\'   |(_'_)::::|\~~~~__|)__
     |   ''''|''o/`.-``~~~~~ ``-.     /--\___\    ``|`````` /____\____/
 jrei        |  h ( `; ~~~ ~~  ~ )    |M_|#_#|      ' --   __________|~
       --   *      '-.._~~__~..-'   --           -* -     /  ~~~~ ~~~~~~
 *   -   -      --           ----         ---         _.-'~~~~~     ~ ~~
__--_________............-------------'''''''''''''''` ~~~~~    ~~~ ~~~~
~~    ~~~~~~~~     ~~~~~~~   ~~~~~~~~~   ~~~~~~~~~~      ~~~~~~~     ~~~
~~~~~~~~~  ~~~~  ~~~~~ ~~~~~~~~~ ~ ~      ~~~~~~ ~~~~~~     ~~~~    ~~~~
~~~~~~~~     ~~~~~~~~~~~~~~~        ~~~~~~~~~~~~ ~~~~~~  ~~~ ~~~~~~  ~~~
             You found the treasure near river bank!
                       Congratulation!!!
 """
right_answer = """             _(_)_                          wWWWw   _
   @@@@       (_)@(_)   vVVVv     _     @@@@  (___) _(_)_
  @@()@@ wWWWw  (_)\    (___)   _(_)_  @@()@@   Y  (_)@(_)
   @@@@  (___)     `|/    Y    (_)@(_)  @@@@   \|/   (_)\\
    /      Y       \|    \|/    /(_)    \|      |/      |
 \ |     \ |/       | / \ | /  \|/       |/    \|      \|/
jgs|//   \\\\|///  \\\\\|//\\\\\|/// \|///  \\\\\|//  \\\\|//  \\\\\|//
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                You Pass This Round 
                   {} Rounds Left
"""
lose = """                  .------.
                   ||'||||'|
                  ,|| -.._ |
                  \|`.-. .-.
                   | `-'A'-'
                   | ( --.`|
                  _|`.`___,'__   ____ 
              _,-'_| _   _/   /';    `.
           ,-/ / '     /     ; ;       )
          / (__()     /     (__()\     |
         |  (__()    |   __(__() : `--  \\
         \ _'__()`------'  (__() \       :
         ;  |\/|           |\/;\  \      |
         ;  '__'           |__| `. ;.__, (
         :   \ /           ;\;|   /  \    ,--.
         `._ \__\          ;__|  ;   |   /`.,-`.
         /   |\/|          |\;|  |   :   \`/`.__\ 
        ;    |__|___ __ ___|__;__|    \   `\`/`._`.
       ,     |\;|   _\/_   |\/|\/|     \  _|`,`.`.,--.
       ;    ;|__|___\/\/___|__|__|      `( ,/ /.`/`.,-`.
           ; |   ,   | |   `.    |       \`.;//;`\`/ ,. \\
              YOU LOSE       `-  |        `::_;   `\ `' /
            TRY AGAIN !!!                                """

prompt = "You have to find the correct path of this game!\nLet the game begin :)------>>>>>>>>>>>>>>>"
question_1 = "Which city is capital of india?\na)Mumbai\nb)Delhi\nc)Patna\nd)Kolkata"
answer_1 = "b"
question_2 = "What is the name of the famous temple located in Old Delhi?\na)Lotus Temple\nb)Jama Masjid\nc)Hanuman Mandir\nd)ISKCON temple"
answer_2 = "c"
question_3 = "Which bridge is located near Hanuman Mandir?\na)Yudhister Setu\nb)Geeta Colony bridge\nc)Signature Bridge\nd)Old Iron Bridge"
answer_3 = "d"


def printer(x):
    for i in x.split("\n"):
        print(i)
        time.sleep(0.1)


printer(start)
input()

question = [question_1, question_2, question_3]
answer = [answer_1, answer_2, answer_3]

i = 0
for i in range(len(question)):
    printer(question[i])
    ans = input("What is your option(a,b,c or d) :")
    if answer[i] == ans.lower():
        printer(right_answer.format(len(question) - i - 1))
        input("Press Enter to continue.........>")
    else:
        printer(lose)
        break
if i == len(question):
    printer(good_ending)
