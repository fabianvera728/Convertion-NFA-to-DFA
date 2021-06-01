"""
    author: Fabian Hernando Vera Carrillo
"""

from pandas import DataFrame

class Automata:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.stateFinal = []
        self.stateStart = None
        self.transitionTable = {}

    def fillInformationDFA(self):
        self.states = [tuple([x]) for x in input("Enter list of states separated by spaces: ").split()]
        self.alphabet = input("Enter input alphabet separated by spaces: ").split()
        self.stateStart = input("Input the state initial: ")
        self.stateFinal = tuple(input("Input state final or the state separated by spaces: ").split())
        self.fillTransitionTable();
        self.printInformationAutomata()

    def fillTransitionTable(self):
        print("fill transitionTable example: q0 q1, example: enter")
        for state in self.states:
            self.transitionTable[state] = {symbol: tuple(input(f'{state} with {symbol}: ').split()) for symbol in self.alphabet}
    
    def printInformationAutomata(self): 
        print("----Quintuple----")
        print("\nStates")
        print(self.states)
        print("\nAlphabet")
        print(self.alphabet)
        print("\nState initial")
        print(self.stateStart)
        print("\nState final")
        print(self.stateFinal) 
        print("\nTransition table")
        [print(key,":",value) for key,value in self.transitionTable.items()]

    def run_automata(self):
        print("Alphabet\n",self.alphabet)
        inputData = input("Input your sequence without spaces: ")
        print(inputData)
        currentState = tuple([self.stateStart])
        for i in inputData:
            if(self.alphabet.__contains__(i)):
                if(self.states.__contains__(self.transitionTable[currentState][i])):
                    currentState = self.transitionTable[currentState][i]
        print('ACCEPTED' if(self.stateFinal.__contains__(currentState)) else 'REJECT')


