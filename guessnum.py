from random import randint

guesstaken = 0

print("Hello! whats your name?")
myname=input()

number = randint(1,10)
print("Well, " +myname+ ", I am thinking of a number between 1 and 10")

while guesstaken<6:
	print("Take a guess, bitch: ")
	guess = input()
	guess = int(guess)

	guesstaken = guesstaken+1

	if guess>number:
		print("your guess is too high, bitch (dont do drugs)")
		continue

	if guess<number:
		print("your guess is at all time low")
		continue

	if guess==number:
		print("jalwa toh " +myname+ " hai, you guessed the right number. in other words you are completely useless")
		break

	if guess!=number:
		print("you couldnt even do such a simple job. The number i guessed was " +number+ ". You are just takaing up space and oxygen in this world you useless piece of shit.")
		break

			