import copy
import math
import sys
from typing import overload

sys.path.insert(0, "../ChironCore/")

import cfg.ChironCFG as cfgK
import cfg.cfgBuilder as cfgB
from lattice import  *
import ChironAST.ChironAST as ChironAST
import abstractInterpretation as AI

'''
    Class for interval domain
'''

X=[0,0]
Y=[0,0]
dir = ['r','l','t','d']
var_range=[-1000,1000]

class IntervalDomain(Lattice):

    '''Initialize abstract value'''
    def __init__(self, data):
        pass

    '''To display abstract values'''
    def __str__(self):
        pass

    '''To check whether abstract value is bot or not'''
    def isBot(self):
        pass

    '''To check whether abstract value is Top or not'''
    def isTop(self):
        pass

    '''Implement the meet operator'''
    def meet(self, other):
        pass

    '''Implement the join operator'''
    def join(self, other):
        pass

    '''partial order with the other abstract value'''
    def __le__(self, other):
        pass

    '''equality check with other abstract value'''
    def __eq__(self, other):
        pass

    '''
        Add here required abstract transformers
    '''
    pass

class IntervalTransferFunction(TransferFunction):
    def __init__(self):
        pass

    def transferFunction(self, currBBIN, currBB):
        '''
            Transfer function for basic block 'currBB'
            args: In val for currBB, currBB
            Returns newly calculated values in a form of list

            This is the transfer function you write for Abstract Interpretation.
        '''
        #implement your transfer function here
        current_out = copy.deepcopy(currBBIN)
        # if(currBB.__str__() != 'END'):
        #     if(type(currBB.instrlist[0][0]) == ChironAST.MoveCommand):
                # pass
        # if(currBB.__str__() == 'END'):
        #     # print("END : ",current_out)
        #     outVal = [{'OUT' : current_out['IN']}]
        #     return outVal
        # outVal = []
        # outVal = [{'OUT' : current_out['IN']}]
        # return outVal

        outVal = []
        return outVal

class ForwardAnalysis():
    def __init__(self):
        self.transferFunctionInstance = IntervalTransferFunction()
        self.type = "IntervalTF"

    '''
        This function is to initialize in of the basic block currBB
        Returns a dictinary {varName -> abstractValues}
        isStartNode is a flag for stating whether currBB is start basic block or not
    '''
    def initialize(self, currBB, isStartNode):
        val = {}
        #Your additional initialisation code if any
        if(isStartNode):
            val = { 'IN' : {'X' : {'left' : X[0] , 'right' : X[1]} , 'Y' : {'left' : Y[0] , 'right' : Y[1]} , 'D' : dir[0] , 'is_bot' : False}}
        #Your additional initialisation code if any
        return val


    #just a dummy equallity check function for dictionary
    def isEqual(self, dA, dB):
        for i in dA.keys():
            if i not in dB.keys():
                return False
            if dA[i] != dB[i]:
                return False
        return True

    '''
        Define the meet operation
        Returns a dictinary {varName -> abstractValues}
    '''
    def meet(self, predList):
        assert isinstance(predList, list)
        meetVal = {}
        for i in predList:
            print(i)
        print("----------------hello--------------------")
        meetVal = {}
        for pred in predList:
            meetVal['IN'] = pred['OUT']
        # return meetVal
        return meetVal

def analyzeUsingAI(irHandler):
    '''
        get the cfg outof IR
        each basic block consists of single statement
    '''
    # call worklist and get the in/out values of each basic block
    abstractInterpreter = AI.AbstractInterpreter(irHandler)
    bbIn, bbOut = abstractInterpreter.worklistAlgorithm(irHandler.cfg)
    print( "bbin : ",bbIn )
    print("bb out : " , bbOut)
    #implement your analysis according to the questions on each basic blocks
    pass
