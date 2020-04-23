import argparse
import sys
def main():

    parser = argparse.ArgumentParser(description='Word counter 3000')
    parser.add_argument("nazev_souboru", help='jmeno_souboru_ktery_hledate')
    parser.add_argument("slovo", help='vypise_pocet_slov', action = "store_true")
    parser.add_argument("znak", help='vypise_pocet_znaku', action = "store_true")
    parser.add_argument("radek", help='vypise_pocet_radku', action = "store_true")

    arg = parser.parse_args()

    try:
        soubor = open(arg.textovy_soubor)
        text = soubor.read()
        if arg.znak:
            znak = len(text)
            print(f"\n{text}\nZnaky: {znak}\n")
            file.close()

        elif arg.radek:
            radek = len(text.split("\n"))
            print(f"\n{text}\nŘádky: {radek} \n")
            file.close()

        elif arg.slovo:
            radek = len(text.split("\n"))
            slovo = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nSlova: {slovo} \n")
            file.close()

        elif arg.slovo and arg.znak:
            znak = len(text)
            radek = len(text.split("\n"))
            slovo = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nZnaky: {znak} , Slova: {slovo}\n")
            file.close()

        elif arg.radek and arg.slovo:
            radek = len(text.split("\n"))
            slovo = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nSlova: {slovo} , Rádky: {radek} \n")
            file.close()

        elif arg.radek and arg.znak:
            znak = len(text)
            radek = len(text.split("\n"))
            print(f"\n{text}\nZnaky: {znak} , Rádky: {radek} \n")
            file.close()

        elif arg.slovo and arg.znaky and arg.radek:
            znak = len(text)
            radek = len(text.split("\n"))
            slovo = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nZnaky: {znak} , Slova: {slovo} , Rádky: {radek} \n")
            file.close()

        else:
            znaky = len(text)
            radky = len(text.split("\n"))
            slova = len(text.split(" ")) + (radky - 1)
            print(f"\n{text}\nZnaky: {znak} , Slova: {slovo} , Rádky: {radek} \n")
            file.close()



    except PermissionError:
        print("Něco se stalo (nemas opravneni)")

    except:
        print("Něco se stalo (spatny soubor")


if __name__ == '__main__':
    main()