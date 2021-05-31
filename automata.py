"""
    author: Fabian Hernando Vera Carrillo
"""

import pandas as pd

class Automata:
    def __init__(self):
        self.states = []
        self.alphabet = []
        self.stateFinal = []
        self.stateStart = None
        self.transitionTable = {}

    def fillInformationDFA(self):
        self.states = input("Enter list of states separated by spaces: ").split()
        self.alphabet = input("Enter input alphabet separated by spaces: ").split()
        self.stateStart = input("Input the state initial: ")
        self.stateFinal = input("Input state final or the state separated by spaces: ").split()
        self.fillTransitionTable();
        self.printInformationAutomata()

    def fillTransitionTable(self):
        print("fill transitionTable")
        print("if the transition with symbol is none then enter")
        print("else input the state separated by spaces")
        self.transitionTable = {state: {alphabet: -1 for alphabet in self.alphabet} for state in self.states}
        for state in self.states:
            for symbol in self.alphabet:
                reaching_state =  input(f'{state} with {symbol}:').split()  #Enter all the end states
                self.transitionTable[state][symbol] = reaching_state
    
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
        print(pd.DataFrame(self.transitionTable))

    def run_automata(self):
        print("Alphabet\n",self.alphabet)
        inputData = input("Input your sequence without spaces: ")
        print(inputData)
        currentState = self.stateStart
        for i in inputData:
            if(self.alphabet.__contains__(i)):
                if(self.states.__contains__(self.transitionTable[currentState][i])):
                    currentState = self.transitionTable[currentState][i]
        print('ACCEPTED' if(self.stateFinal.__contains__(currentState)) else 'REJECT')


