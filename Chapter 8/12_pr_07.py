def remove_and_split(string,word):
    new= string.replace(word, " ")
    return new.strip()

this = "      my name is disha  "
print(this)
print(this.strip())