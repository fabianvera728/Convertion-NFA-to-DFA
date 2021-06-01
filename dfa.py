from automata import Automata

class DFA(Automata):
    
    def __init__(self):
        Automata.__init__(self)
        self.vacio = tuple(["Ø"])
        self.newstates = []
            
    def convert_from_nfa(self, nfa): 
        # the following five code lines define quituple for the DFA
        dfa = {}
        self.alphabet = nfa.alphabet
        self.stateStart = nfa.stateStart
        self.newstates = [[nfa.stateStart]]
        self.states = [tuple([nfa.stateStart])]
        # next we will iterate while the long of the newstates is greater than zero
        while len(self.newstates) != 0:
            bandera = self.newstates[0]
            nstate = tuple([x for x in self.newstates[0]])
            dfa[nstate] = {}
            i = 0
            for symbol in nfa.alphabet:
                temp = []           #creating a temporay list
                for j in nstate:
                    var2 = nfa.transitionTable[tuple([j])][symbol]
                    for k in var2:
                        if( k not in temp and var2 != [] ):
                            temp.append(k)
                    if j in nfa.stateFinal and nstate not in self.stateFinal:
                        self.stateFinal.append(nstate)
                s = tuple(sorted(temp))
                if(s != ()):
                    dfa[nstate][symbol] = s
                    # verify that the state not exist
                    if not self.states.__contains__(s):
                        self.newstates.insert(i,s) #then append it to the new_states_list
                        self.states.append(s)#as well as to the keys_list which contains all the states
                        i += 1
                elif s == ():
                    if(not self.states.__contains__(self.vacio)):
                        self.states.append(self.vacio)
                        dfa[self.vacio] = {x: self.vacio for x in self.alphabet} 
                    dfa[nstate][symbol] = self.vacio
            # Remove of newstates the state visited
            self.newstates.remove(bandera)
            # if the flag is true then the nstate is a final state therefore we add this nstate 
        self.transitionTable = dfa
    
