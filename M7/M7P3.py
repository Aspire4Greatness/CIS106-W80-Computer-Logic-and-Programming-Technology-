again = input("do you want to get average?")
again = again.lower()
responses = 0

while again == 'yes':
    name = input("name? ")
    score1 = float(input("test score 1? "))
    score2 = float(input("test score 2? "))
    average = (score1+score2)/2 
    print(f"name: {name}")
    print(f"average: {average}")
    again = input("do you want to repeat?")
    responses = responses + 1 
    pass
print(f"Number of responses: {responses}")