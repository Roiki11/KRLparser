

import sys
from antlr4 import *
from krlLexer import krlLexer
from krlParser import krlParser
from krlListener import krlListener
from krlVisitor import krlVisitor
import pyparsing as pp

constants = pp.oneOf(["VEL_AXIS","ACC","ACC_AXIS", "ACC_ETAX", "APO", "BASE", "CIRC_TYPE", "ECO_LEVEL",
                      "GEAR_JERK", "IPO_MODE", "JERK", "LOAD", "ORI_TYPE", "ROTSYS", "SPL_ORI_JOINT_SYS_AUTO",
                      "SYNC_ID", "SYNC_LIST", "TOOL", "VEL", "VEL_ETAX", "CIRC_MODE"])

command = pp.oneOf(["CONTINUE","EXIT","GOTO", "HALT", "IF", "LOOP", "REPEAT", "WAIT", "SWITCH", "WHILE", "RETURN", "BRAKE",
                    "INTERRUPT", "PTP", "PTP_REL", "LIN","LIN_REL", "CIRC", "CIRC_REL", "TRIGGER", "FOR", "ANOUT", "ANIN"])

parseLetters = pp.Keyword("A-Z")
number  = pp.Combine(pp.Word(pp.nums)+pp.Optional(".")+pp.Optional(pp.Word(pp.nums)))            # simple unsigned number
variable = pp.Char(pp.alphas)          # single letter variable, such as x, z, m, etc.
arithOp  = pp.oneOf("+ - * /")      # arithmetic operators
lbrace, rbrace = pp.Suppress('{'), pp.Suppress('}')
lbracket, rbracket = pp.Suppress('['), pp.Suppress(']')

varAssignment = variable("variable") + "=" + number("value")
equation = variable + "=" + number + arithOp + number    # will match "x=2+2", etc.

forStatement = command + varAssignment + "TO" + number
constAssignment = pp.Suppress("$") + constants("sysvar") + lbracket + variable + rbracket + pp.Suppress("=") + number("value")

class myListener(krlListener):

    def __init__(self):
        self.mainProgram = {}
        self.subPrograms = {}
        self.vars = {}
        self.subRoutine = False





    def makeProgram(self, *programs):
        mainProgram = {}
        mainProgram.update(self.mainProgram)
        for program in programs:
            mainProgram.update(program)
        return mainProgram

    def enterModule(self, ctx: krlParser.ModuleContext):
        print(ctx.getChildCount())


    def enterModuleRoutines(self, ctx:krlParser.ModuleRoutinesContext):
        pass

    def enterMainRoutine(self, ctx:krlParser.MainRoutineContext):
        pass



    def enterSubRoutine(self, ctx:krlParser.SubRoutineContext):
        self.subRoutine = True

    def exitSubRoutine(self, ctx:krlParser.SubRoutineContext):
        self.subRoutine = False

    def enterProcedureDefinition(self, ctx:krlParser.ProcedureDefinitionContext):
        n = ctx.getChildCount()
        y = ctx.getChild(1).getText() #procedure name
        if self.subRoutine is False:
            self.mainProgram["mainName"] = y
        else:
            subprog = {"subName": y}
            self.subPrograms.update(subprog)


    def enterVariableDeclaration(self, ctx:krlParser.VariableDeclarationContext):
        n=ctx.getChildCount()
        #print(ctx.DECL())
        #print(ctx.type_().getText())
        name = str(ctx.variableName().getText())
        if name != 0:
            self.vars[name] = 0
            #print(self.vars)

    def enterVariableListRest(self, ctx:krlParser.VariableListRestContext):
        for x in range(0, ctx.getChildCount()):
            #print(ctx.getChild(x))
            y= str(ctx.getText()).strip(",")
            ysp= y.split(",")
            for x in ysp:
                if x == ",":
                    break
                else:
                    self.vars[x] = 0

                    
    def enterFormalParameters(self, ctx:krlParser.FormalParametersContext):

        pass

    def enterRoutineDataSection(self, ctx:krlParser.RoutineDataSectionContext):
        #print(ctx.getText())

        pass

    def enterRoutineImplementationSection(self, ctx:krlParser.RoutineImplementationSectionContext):
        print(ctx.getChildCount())
        y = ctx.statementList().getChildCount()
        lines = []
        forLoop = []
        ifLoop = []

        for x in range(0, y):
            z = str(ctx.statementList().getChild(x).getText())
            a = z.split()
            lines.append(a)
            #print(lines)

        for items in lines:
            if len(items) == 1:
                try:
                    a = items[0]
                    g = varAssignment.parseString(a)
                    if g.variable in self.vars:
                        self.vars[g.variable] = g.value

                except (pp.ParseException) as error:
                    pass
            else:
                for x in items:
                    if x.find("FOR",0,3) != -1:
                        f = forStatement.parseString(x)
                        print(f)
                    elif x.find("$", 0, 1) != -1:
                        s = x.strip("$")
                        print(s)
                        a = constAssignment.parseString(x)
                        self.vars[a.sysvar] = a.value
                        print(self.vars)
                else:
                    pass
                    


    def enterStatement(self, ctx:krlParser.StatementContext):
        pass



def main():
    input_stream = FileStream("ANTLR4 config/Examples/example1.txt")
    lexer = krlLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = krlParser(stream)
    tree = parser.module()
    print(tree.toStringTree(recog=parser))
    printer = myListener()
    walker = ParseTreeWalker()
    walker.walk(printer, tree)
    




if __name__ == '__main__':
    main()