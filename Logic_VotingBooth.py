import re


def submit(voter_id, person_chose, radio_answer, id_input, bottom_label):
    if person_chose == 1:
        president = 'Joe Biden'
    elif person_chose == 2:
        president = 'Donald Trump'
    else:
        president = 'no vote'

    try:
        int(voter_id)
        with open('../Final Project/Counted_Votes.txt', 'r+') as read_file:
            for line in read_file:
                if re.search(f'^{str(voter_id)}, ', line):
                    bottom_label.config(text='ALREADY VOTED', font=('Arial', 25), fg='red')
                    # https://www.geeksforgeeks.org/how-to-set-font-for-text-in-tkinter/ link for when I searched up how to change the font and color
                else:
                    read_file.write(f'{voter_id}, {president}\n')
                    radio_answer.set(0)
                    id_input.delete(0, 100)
                    bottom_label.config(text='SUCCESSFUL VOTE', font=('Arial', 25), fg='green')
    except (FileNotFoundError, IOError):
        with open('../Final Project/Counted_Votes.txt', 'w') as write_file:
            write_file.write(f'{voter_id}, {president}\n')
            radio_answer.set(0)
            id_input.delete(0, 100)
            bottom_label.config(text='SUCCESSFUL VOTE', font=('Arial', 25), fg='green')
    except ValueError:
        bottom_label.config(text='ID MUST BE AN INTEGER, NO SPECIAL CHARACTERS', font=('Arial', 20), fg='red')
