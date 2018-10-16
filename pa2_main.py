if __name__== "__main__":
    wordlist = ["calvin","and","hobbes", "are", "the", "first", "spacemen", "on", "mars"]
    def cap_join(wordlist):
        newstring=" ".join(wordlist)
        newstring= newstring.title()
        return newstring



print(cap_join(wordlist))