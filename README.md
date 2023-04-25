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
