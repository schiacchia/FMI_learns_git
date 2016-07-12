def countDNA():
    with open('rosalind_dna.txt') as f:
        s = f.read()
        a = 0
        c = 0
        g = 0
        t = 0
        for letter in s:
            if letter == "A":
                a += 1
            elif letter == "G":
                g += 1
            elif letter == "C":
                c += 1
            elif letter == "T":
                t += 1
            else:
                print "invalid DNA string"
    f.close()
    print a, c, g, t

countDNA()
