import os
import sys

def main(rep):

    for filename in os.listdir(rep):
        if filename[-3:] != 'zip':
            i = 0
            while filename[i] != '_':
                i += 1
            nom = filename[:i]

            dst = "{}/{}.py".format(rep, nom)
            src = "{}/{}".format(rep, filename)

            os.rename(src, dst)

if __name__ == '__main__':

    if len(sys.argv) == 1:
        print("il manque le nom du répertoire")
        exit()

    rep = sys.argv[1]
    main(rep)
