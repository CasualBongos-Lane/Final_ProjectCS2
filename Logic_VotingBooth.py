import re


def submit(voter_id: str, person_chose: int, radio_answer, id_input, bottom_label):
    """
    This Function Creates a File and stores Votes

    :param voter_id: This is the Voter ID which is an Integer that gets written to the file
    :param person_chose: This is the Choice of president; Joe Biden, Donald Trump, Or no vote if no radio button selected
    :param radio_answer: This resets the Radio Button after a Successful Vote
    :param id_input: This param is needed since it Clears the Entry box after a successful vote
    :param bottom_label: This Changes the Bottom Label depending on whether the vote is successful or not
    :return: This function does not return anything as the voter_id/person_chose are put into a file rather than being returned to the user
    """

    if person_chose == 1:
        president = 'Joe Biden'
    elif person_chose == 2:
        president = 'Donald Trump'
    else:
        president = 'no vote'
    #This if statement at the top determines who the person voted for so the correct name can be filed

    try:
        new_value = int(voter_id.strip())#Raises the ValueError Exception in case of special characters
        with open('Counted_Votes.txt', 'r') as read_file:
            for line in read_file:
                line.strip()
                if re.search(f'^{str(new_value)}, ', line):
                    bottom_label.config(text='ALREADY VOTED', font=('Arial', 25), fg='red')
                    # https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/ link for when I searched up how to change the font and color
                    return
                    #The point of returning nothing here is that the program interprets the function as being complete
                    #and it skips the rest of the code

        with open('Counted_Votes.txt', 'a') as write_file: #If someone has not voted this will append their vote to the text file
            write_file.write(f'{new_value}, {president}\n')
            radio_answer.set(0)
            id_input.delete(0, 100)
            bottom_label.config(text='SUCCESSFUL VOTE', font=('Arial', 25), fg='green')

    except FileNotFoundError: #If the file is not within the program folder it will create one and store the vote
        new_value = int(voter_id.strip())
        with open('Counted_Votes.txt', 'w') as write_file:
            write_file.write(f'{new_value}, {president}\n')
            radio_answer.set(0)
            id_input.delete(0, 100)
            bottom_label.config(text='SUCCESSFUL VOTE', font=('Arial', 25), fg='green')

    except ValueError: #Catches any Special Characters like *&^%(including spaces) or letters like A,a,b,d,y,C, etc.
        bottom_label.config(text='ID MUST BE AN INTEGER, NO SPECIAL CHARACTERS', font=('Arial', 20), fg='red')
