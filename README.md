# Smart Mark Survey

Smart Mark Survey is a short survey featuring wrestling-related questions. It requires the user's input, which is then commented on by the program, usually in a way that mocks the user's choices. The choices are then exported to a txt file that collates the data in a legible format. The concept was inspired by many real-life interactions I've personally come across betweens alleged 'fans' on the Internet.

## Save User's Input

The first step in my code is to open a text file to save the user's input. The open() function is used to create a file object and the "w" argument indicates that the file is opened for writing.

## User's Details

The script prompts the user to enter their name and age using the input() function. The print() function is used to display a message to the user and the "-" * 80 expression generates a line of 80 hyphens to create a separator. The seperator is also reused in the survery question code. The user's name and age are saved to the text file using the file.write() method.

## Quiz Questions

The script asks the user several questions related to wrestling using the input() function. Similar to the previous step, the print() function displays a message to the user with a separator line. The user's answers are saved to the text file using the file.write() method. Below, you can see the code for the first question.

As you can see, the question's use the input method, ready to receive the user's data. The print function then displays a message that refers to the user's answer, as well as a comment about the answer. Both of these lines of code are seperated visually using the hyphen seperators used on the user details code. The answer is then written to the user_date text file opened at the beginning.

The code is fairly similar throughout the questions though certain methods have been implemented to give the user a more immersive experience. In the code below (used for question six), the print statement after the input functon contains a sentence, displays the user's answer and then uses the str() function which then allows me to include a string. Using this string, I can then create another sentence after displaying the users data, so for example, if your name is Dan and your dream match is Kenny Omega vs Roman Reigns, the output will be "Hmm. Kenny Omega vs Roman Reigns. Not bad indeed.", I have written it like this so the program plays out like a conversation rather than a generic output such as "Your answer was etc.", for example.

## Close Text File

After all the questions are answered, the text file is closed using the file.close() method. The script then displays a print message to confirm to the user that their answers have been collated.

## Testing

- code put through PEP8 Python Validator. 'All clear, no errors found'
- tested locally on GitPod Terminal
- tested deployed version on Heroku