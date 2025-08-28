import random
n = random.randint(1,500)
count = 0
while True:
    # print(n)
    guess = int(input("Guess yout number between 1-500:"))
    if guess == n:
        count =count+1
        print("you won! in",count,"tries")
        break
    elif guess < n:
        print("Oops go a little higher ")
        count =count+1
    elif guess > n:
        print("Oops go a little lower ")
        count =count+1

