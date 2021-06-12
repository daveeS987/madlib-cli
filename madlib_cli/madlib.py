import re


def print_welcome_message():
    print(
        """
*******  Welcome to The MadLib Game!! *******  
A series of questions will be asked. 

Please answer all questions

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

    pattern = r"\{([\w\s]+)\}"
    words_list = re.findall(pattern, string)
    words_tuple = tuple(words_list)

    replace = r"\{([\w\s]+)\}"
    new_string = re.sub(replace, "{}", string)

    return (new_string, words_tuple)


def merge(string, user_input):
    """
    - Two inputs:
      - the template string
      - a tuple with user input
    - Output will be a combined string
    """
    merged_string = string.format(*user_input)
    return merged_string


def ask_user_questions(words_tuple):
    """
    - input is a tuple of keywords
    - output is a tuple of user answers
    """

    answers = []

    for words in words_tuple:
        response = input(f"Please enter a {words} >> ")
        answers.append(response)

    answer_tuple = tuple(answers)
    return answer_tuple


def main():
    print_welcome_message()
    raw_template = read_template("assets/dark_and_stormy_night_template.txt")
    stripped_string, key_words = parse_template(raw_template)
    user_response = ask_user_questions(key_words)
    user_input_merged = merge(stripped_string, user_response)

    print(user_input_merged)
    with open("assets/users_custom_file.txt", "w") as new_file:
        new_file.write(user_input_merged)


if __name__ == "__main__":

    main()
