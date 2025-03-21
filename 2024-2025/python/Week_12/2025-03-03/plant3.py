def main():
   Q1 =  input("Please enter your favorite movie: ")
   Q2 = input("Please enter the star of your favorite movie: ")
   Q3 = input("Where did the star of your favorite movie live?: ")
   Q4 =  int(input("How many times did you watch your favorite movie?: "))

   print(f"Your favorite movie is {Q1}, starring {Q2}.")
   print(f"{Q2} lives in {Q3}.")
   print(f"The next time you watch the movie {Q1}, you will have watched it {Q4 + 1} times. ")


if __name__ == '__main__':
    main()