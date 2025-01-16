def main() :
    print("We want to know if you like programming!")
    print()
    greeting(input("What is your name?"))

def greeting(name):
    print("What is the college you're attending{}?".format(name))
    answer = input()
    print("What high school did you attend{}?".format(name))
    answer = input()
    print("What institusion is more fun{}?".format(name))
    answer = input()
if __name__ == "__main__":
    main()
