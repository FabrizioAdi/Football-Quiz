# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high


def run_game():
    choices = []
    correct_choices = 0
    question_number = 1
    
    for key in questions:
        print("********************QUESTION********************")
        print(key)
        for i in answers[question_number-1]:
            print(i)


questions = {
    "Who is the winner of Premier League (England) 2020/21?":"a",
    "What football country does lionel messi represent?":"c",
    "Who broke Gerd Müller's record for the most goals scored in a single Bundesliga season?":"a",

}
answers = [["a. Manchester City", "b. Manchester United", "c. Chelsea London", "d. Leicester City"],
["a. Italy", "b. Uruguay", "c. Argentina", "d. USA"],
["a. Robert Lewandowski (Pol)", "b. Gerd Muller (Ger)", "c. Cristiano Ronaldo (Por)", "d. Thomas Muller (Ger)"]]

# ********************
# ********************

run_game()