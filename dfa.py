from automata import Automata

class DFA(Automata):
    
    def __init__(self):
        Automata.__init__(self)
        self.vacio = "x"
        self.newstates = []
            
    def convert_from_nfa(self, nfa): 
        # the following five code lines define quituple for the DFA
        dfa = {}
        self.alphabet = nfa.alphabet
        self.stateStart = nfa.stateStart
        self.newstates.append(nfa.stateStart)
        self.states = list(nfa.stateStart)
        # next we will iterate while the long of the newstates is greater than zero
        while len(self.newstates) != 0:
            dfa[self.newstates[0]] = {}
            i = 0
            flag = False
            nstate = self.newstates[0]
            for symbol in nfa.alphabet:
                temp = []           #creating a temporay list
                for j in nstate:
                    for k in nfa.transitionTable[j][symbol]:
                        # if( not (k in temp) and  not temp.__contains__(k) and nfa.transitionTable[j][symbol] != "" ):
                        if( k not in temp and nfa.transitionTable[j][symbol] != "" ):
                            temp.extend(k)
                    if nfa.stateFinal.__contains__(j) and not self.stateFinal.__contains__(nstate):
                        flag = True
                s = "".join(sorted(temp)) 
                if(s != ''):
                    dfa[nstate][symbol] = s
                    # verify that the state not exist
                    if not self.states.__contains__(s):
                        self.newstates.insert(i,s) #then append it to the new_states_list
                        self.states.append(s)  #as well as to the keys_list which contains all the states
                        i += 1
                if s == '':
                    if(not self.states.__contains__(self.vacio)):
                        self.states.append(self.vacio)
                        dfa[self.vacio] = {x: self.vacio for x in self.alphabet} 
                    dfa[nstate][symbol] = self.vacio
            # Remove of newstates the state visited
            self.newstates.remove(nstate)
            # if the flag is true then the nstate is a final state therefore we add this nstate 
            if flag:
                self.stateFinal.append(nstate)
        self.transitionTable = dfa
    
