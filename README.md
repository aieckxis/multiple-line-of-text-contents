# Write multiple line of text contents into a text file
This Python script creates a file with multiple lines of text in it. As long as the user does not say there are any more lines, it asks them to enter text lines and writes them to the file. The code has error handling to deal with incorrect user input, making sure that the program keeps asking the user for input until a valid one is entered.

## Usage
Using Command Prompt:

1. Open the Start menu and search for "Command Prompt".
2. Click on "Command Prompt" to open the command prompt window.
3. Use the cd command to navigate to the directory containing the script file. For example, if the script file is located in the "Documents" folder, type: cd Documents
4. Type the command python script_name.py to run the script. Replace "script_name.py" with the actual name of the script file.
5. Press Enter to run the script.
6. The script will run and ask the user to input their name and the line and if they will add more lines.

Alternatively, you can also run the script using the Python IDLE environment:

1. Open the Start menu and search for "Python".
2. Click on "Python" to open the Python IDLE environment.
3. Click on "File" at the top of the window and select "Open".
4. Navigate to the directory containing the script file and select it.
5. Click on "Run" at the top of the window and select "Run Module" or press the F5 key.
6. The script will run and ask the user to input their name and the line and if they will add more lines.

## Example
Suppose that the user enter their name as Kate:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234226959-ba0a4a84-e9d4-4286-b941-167bf968f20d.png">

and enter the line shown in the image below:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234227046-a4817a82-1e9e-4caf-9778-49e70b72908d.png">

The program will then ask the user if there are more lines.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234227185-39f27126-6df4-4cd1-98f0-83809283c283.png">

If the user entered the letter 'y', the program will ask the user to enter new line.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234227288-cf1095cb-a6a7-4627-96f6-7e3f6b30f782.png">

but if the user entered the letter 'n', the program will exit the loop and the resulting text file "mylife.txt" contains the following lines of text:

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234227541-0b92b21d-8986-4141-a5f1-73c0e399a50a.png">

## Code Explanation

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234244145-b6f2168e-671c-41a6-bab3-e84d2faab008.png">

This code allows the user to enter multiple lines of text and writes them to a file called "mylife.txt". The line number 5 of code sets the filename as "mylife.txt". The with statement is used to ensure that the file is properly closed after it is opened. This also makes the code more concise. The open() function is called with the file name and the "w" mode parameter, which means that the file is opened in write mode.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234244374-2245045f-b4e4-432c-b197-8f01dd82fec2.png">

The program asked the user to enter their first name to be add in the variable of add_line. A while loop is used to continue asking the user for input until they indicate that there are no more lines to enter. The user is also asked to enter a line of text with the input() function, and the value is stored in the variable line. The write() method is used to add the line of text to the file, followed by a newline character (\n). The user is then prompted to indicate if there are more lines to be entered with the input() function, and the value is stored in the variable add_line.

<img width="500" alt="image" src="https://user-images.githubusercontent.com/129574374/234244882-ae946eec-dae8-4826-8478-bbdc1c26e548.png">

If the user enters "n", the break statement is used to exit the while loop. Or else, if the user enters "y", the continue statement is used to return to the beginning of the loop and prompt the user for another line of text. And if the user enters anything else, an error message is displayed and the loop is repeated until valid input is provided.

## Potential Improvements
- Adding error handling to the code will make it more robust and prevent crashes caused by unexpected user input.
- The program could be improved by adding error handling to handle unexpected input from the user. Additionally, it would be helpful to allow the user to input the name of the file they want to write to, rather than always writing to a file named "mylife.txt".
- The way the program interacts with the user could be improved to make it easier to use. For example, it could provide better instructions or let the user quit at any time.

## Conclusion
In conclusion, the program enables users to enter lines of text and save them to a chosen file. The program's functionality could be improved by adding more advanced features to the relatively simple code, which currently functions as intended. However, the program is a helpful tool for those who want to quickly and easily create and save text files.
