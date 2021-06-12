import re


"""

Tasks

- Print Welcome Message
  - write function for this


- read_template function
  - input is path to template
  - output is a string of everything in the file


- parse_template function
  - input will be a string > from read_template function
  - output will be an array with two parts
    - stripped string
    - a tuple with the values taken out


- Create a function to ask user the inputs from parse_template

- Once input is received, use merge function

- merge function  
  - Two inputs:
    - the template string
    - the users Input in a tuple
  - Output will be a combined string

- After madlib response is completed >> print response back in command line

- Write the text back into a file


"""


def print_welcome_message():
    print(
        """
Welcome to this madlib Game. A series of questions will be asked. 
We will be collecting a series of words in order to complete a sentence. 

      """
    )


def read_template(location_of_file):
    try:
        with open(location_of_file, "r") as file:
            content = file.read()
            return content
    except FileNotFoundError as fnf_error:
        print("An error was encountered when grabbing a file")
        print(fnf_error)


def parse_template(string):
    """
    - input will be a string > from read_template function
    - output will be an array with two parts
      - stripped string
      - a tuple with the values taken out
    """

    # try to use regex to get everything inside {}
    pattern = r"\{([\w\s]+)\}"
    words_list = re.findall(pattern, string)
    words_list = tuple(words_list)

    # then substitute everything inside {} with empty ''
    replace = r"\{([\w\s]+)\}"
    new_string = re.sub(replace, "{}", string)

    return (new_string, words_list)


def merge(string, user_input):
    """
    - Two inputs:
      - the template string
      - the users Input in a tuple
    - Output will be a combined string
    """
    pass


if __name__ == "__main__":

    print(read_template("assets/template_madlib.txt"))
