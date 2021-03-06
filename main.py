import sys
from automata import Automata
from dfa import DFA
from nfda import NFA

def main():
    while True:
        try:
            
            print("-----Menu-----\n")
            print("1. Define NFDA")
            print("2. Define DFA")
            print("3. Convert NFDA to DFA")
            print("4. Run automata")
            print("0. Exit")
            return int(input("Input yout option: "))
        except Exception as e:
            print("Error: ",e)
            print("¡Try again!")


if __name__ == '__main__':
    option = 1;
    nfa = NFA()
    nfda = NFA()
    dfa = DFA()
    while option != 0:
        option = main()
        if option == 1:
            nfda = NFA()
            nfda.fillInformationDFA()
        elif option == 2:
            dfa.fillInformationDFA()
        elif option == 3:
            dfa.convert_from_nfa(nfda)
            dfa.printInformationAutomata()
        elif option == 4:
            dfa.run_automata()
        else:
            continue

# Examples input quintuple

# input states 
#     a b c v
# input alphabet
#     0 1 2
# input state final
#     a b c
# input state start
#     v
# input matriz transition
#     a with 0: a b
#     a with 1: v
#     a with 2: 
#   b with 0: b a
#     ... etc

