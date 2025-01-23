def main() :
    print("Hello, Carolina's program wants to get to know you!")
    print()

    print("What is your name?")
    name = input()
    print()

    print("{}, What is the college you're attending?".format(name))
    college = input()
    print()

    print("{}, What high school did you attend?".format(name))
    high_school = input()
    print()

    print("{}, Were you involved in any extracurricular activities while attending {}?".format(name,high_school))
    activity = input()
    if activity.lower() == "no":
        involve = "didn't"
        print()
        print("That's a bit of a bummmer, hope your're delving into more activities during your time at {}.".format(college))
    else:
        involve = "did"
        print()
        print("That's awesome {}, which activities?".format(name))
        the_activities = input()
        print()
        print("Very cool! Hope you're able to continue with {} either in and outside of {}.".format(the_activities.lower(),college))

    print()
    print("Which institution is more fun, {}?".format(name))
    answer = input()
    if answer == college:
        fun = high_school
    else:
        fun = college
    print()

    print("It was nice speaking with you, {}.".format(name))
    print()

    print("I've learned that you are attending {} and the high school you attended was {}.".format(college, high_school))
    print()
    print("Also, you {} get involved in extracurricular activities while in {}.".format(involve, high_school))
    print()
    print("Lastly, you believe {} is more fun than {}.".format(answer,fun))
    print()

    print("This experience was lovely getting to know you!")
    print("Thank you for your time!!")

if __name__ == "__main__":
    main()
