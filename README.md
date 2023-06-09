# Smart Mark Survey

Smart Mark Survey is a short survey featuring wrestling-related questions. It requires the user's input, which is then commented on by the program, usually in a way that mocks the user's choices. The choices are then exported to a txt file that collates the data in a legible format. The concept was inspired by many real-life interactions I've personally come across betweens alleged 'fans' on the Internet (smart mark being a term that refers to fans who think their wrestling knowledge and preferences is/are superior to anyone elses).

## Save User's Input

The first step in my code is to open a text file to save the user's input. The open() function is used to create a file object and the "w" argument indicates that the file is opened for writing.

![filewriteup](markupfiles/filewrite.png)

## User's Details

The script prompts the user to enter their name and age using the input() function. The print() function is used to display a message to the user and the "-" * 80 expression generates a line of 80 hyphens to create a separator. The seperator is also reused in the survery question code. The user's name and age are saved to the text file using the file.write() method.

![userdetails](markupfiles/userdetails.png)

## Quiz Questions

The script asks the user several questions related to wrestling using the input() function. Similar to the previous step, the print() function displays a message to the user with a separator line. The user's answers are saved to the text file using the file.write() method. Below, you can see the code for the first question.

![filewriteup](markupfiles/question1.png)

As you can see, the question's use the input method, ready to receive the user's data. The print function then displays a message that refers to the user's answer, as well as a comment about the answer. Both of these lines of code are seperated visually using the hyphen seperators used on the user details code. The answer is then written to the user_date text file opened at the beginning.

The code is fairly similar throughout the questions though certain methods have been implemented to give the user a more immersive experience. In the code below (used for question six), the print statement after the input functon contains a sentence, displays the user's answer and then uses the str() function which then allows me to include a string. Using this string, I can then create another sentence after displaying the users data, so for example, if your name is Dan and your dream match is Kenny Omega vs Roman Reigns, the output will be "Hmm. Kenny Omega vs Roman Reigns. Not bad indeed.", I have written it like this so the program plays out like a conversation rather than a generic output such as "Your answer was etc.", for example.

![filewriteup](markupfiles/question6.png)

## Close Text File

After all the questions are answered, the text file is closed using the file.close() method. The script then displays a print message to confirm to the user that their answers have been collated.

![filewriteup](markupfiles/closetext.png)

## Testing

- code put through PEP8 Python Validator (https://pep8ci.herokuapp.com/). 'All clear, no errors found'
- tested locally on GitPod Terminal
- tested deployed version on Heroku

![filewriteup](markupfiles/codevalidator.png)

### Bugs

I have been conscious to keep testing my code in the terminal to make sure all code is acting as it should be. A lot of the methods and functions are used multiple times so, when the first couple of questions ran successfully, I knew what to look out for in terms of how text was displaying in the console and correct formatting in the code. Due to this, I didn’t run into many problems.

The only big issue when creating the program was ultimately inexperience. For example, I didn’t understand how display a string, the user’s inputted date with another string so the code wasn’t running properly. However, I went back over the learning resources and used the str() method, which was then used to any further questions needing to mix strings with displaying the user’s input.

## Deployment

The project was deployed using Heroku, which I had learned about in the previous Love Sandwiches project. To do this, I had to go to Heroku, create a new app, set the Python and NodeJS buildbacks and then link my new app to the GitHub repository.

![filewriteup](markupfiles/deployed.png)

# Credits

-All processes/functions/methods learned from Code Institute Full Stack Development: Python module (bar following entry)
-YouTube video "How to Write to a text .txt file in Python! Processing Lists, and Outputting Data!" used to aid with writing user input to another file: 
https://www.youtube.com/watch?v=6jsCbjQB3y0

