import sys, os


def asking_for_email():
    return input(" Please enter your email: ")


def slicing_email(email):
    return print(" username: ", email.split("@")[0], '\n email sliced successfully!')


def main():
    return slicing_email(asking_for_email())


if __name__ == '__main__':
    main()
