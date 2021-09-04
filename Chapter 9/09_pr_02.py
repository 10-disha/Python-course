def game():
    return 45

score = game()
with open("hiscore.txt") as f:
    hiscore = int(f.read())

if hiscore<score:
    with open("hiscore.txt","w") as f:
        f.write(str(score))        