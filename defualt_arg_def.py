# default args in function, python.org tutorial 4.7.1

def ask_ok(prompt, retries=4, reminder='Please try again'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in('n', 'no'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)

#using default arguments
ask_ok('are you okay?')
# specifying arguments
ask_ok('are you okay?', 6, 'try again')