#

def main():
    #
    #ptx = input("type something: ") #plain text #ignore this

    cipher = None #this is needed here, I don't recommend it tho in most cases


    def example(): #explanation by an example
        print("""
        this is how MEGASC work, let's choose the word "hi" to encrypt,
        and choose "ab" as the passphrase, and "hi" in ASCII is 104 (h) & 105 (i) and 
        combining them as strings will make it 104105 and doing the same thing to our passphrase
        which is "ab" which will be 9798, and now we'll multiply the ASCII Values of the pp (passphrase) with pt (plain text)
        and 104105 * (this is the multiply symbol) 9798 equals to 1020020790, and we'll choose nk (numerical key),
        let's choose 3 as our nk, and choose 8 as our OOM number (OOM: Order of magnitude),
        we will multiply or nk with our OOM number which and that will be 3 * 8 which equals to 24,
        and we'll multiply 24 with that big number, and that will be 1020020790 * 24 and that equals to 24480498960.
        and it's it, Hi is the plain text, 24480498960 is the cypher text, we encrypt "hi" securely.
        the nk and pp act as private keys, just like in normal encryption methods, and OOM can be brute-forced
        but nk and pp can't be brute-forced if they long, even a little bit, a pp of "passo" will be infeasible
        to brute-forced, and just like any normal encryption method but MEGASC made easier for beginners
        """)

    example()

    def process(): #the process of encryption
        cipher

        #keys and the plain text
        ptx = input("Type something: ")  #Plain text
        f_key = input("Type a passphrase (ASCII-only): ")  #First key
        n_key = input("Type numerical key: ").strip()  #Numerical key

        try:
            n_key = float(n_key)  #work on floats or ints
        except ValueError:
            raise TypeError("Numerical key must be a number")

        #Order of Magnitude (OOM) Numbers list
        oom = [1, 2, 4, 8, 16, 32, 64, 96, 128, 256, 512, 1024, 2048, 4096, 
            8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576] #96 should'nt be here but it's here because it look cool to be here

        #OOM input
        omc = input("Choose a OOM number or choose 96: ")
        try:
            omc = int(omc)
        except ValueError:
            raise TypeError("choose 96 or valid OOM number")

        if omc not in oom:
            raise ValueError("Invalid OOM number")

        #ASCII values from the passphrase
        ascii_fkey_product = 1
        for letter in f_key:
            ascii_fkey_product *= ord(letter)

        #ASCII values from the plaintext
        ascii_ptx_product = 1
        for letter in ptx:
            ascii_ptx_product *= ord(letter)

        #cipher text
        cipher = ascii_fkey_product * ascii_ptx_product * n_key * omc

        print(f"\nThe Cipher Text is: {cipher}")
        return cipher


    process()

    strcipher = str(cipher)

    def savf(): #save file
        yes = ["yes", "YES", "Yes", "yEs", "yeS", "y", "Y", "YEs", "YES", "yES", "YeS", "1"]
        no = ["no", "n", "N", "0", "", "nO", "NO", "No"]
        q = input("save the cypher in a textfile, yes or no ? ").strip() #save or no

        if q in yes: #save
            with open("MEGASC_Cypher.txt", "a") as file:
                file.write(strcipher + "\n")
        elif q in no: #don't save
            print("Bye !")
            exit()
        else:
            exit()

    savf() #savf short for save file


if __name__ == "__main__":
    main() #this just for avoiding some problems, if you're beginner in programming you don't need to know it now