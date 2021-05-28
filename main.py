

import sys
from antlr4 import *
from krlLexer import krlLexer
from krlParser import krlParser
from krlListener import krlListener
from krlVisitor import krlVisitor
import pyparsing as pp

parseLetters = pp.Keyword("A-Z")
number  = pp.Combine(pp.Word(pp.nums)+pp.Optional(".")+pp.Optional(pp.Word(pp.nums)))            # simple unsigned number
variable = pp.Char(pp.alphas)          # single letter variable, such as x, z, m, etc.
arithOp  = pp.oneOf("+ - * /")      # arithmetic operators
lbrace, rbrace = pp.Suppress('{'), pp.Suppress('}')
lbracket, rbracket = pp.Suppress('['), pp.Suppress(']')

varAssignment = variable("variable") + "=" + number("value")
equation = variable + "=" + number + arithOp + number    # will match "x=2+2", etc.

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
                if str(items).find("FOR") != -1:
                    print(items)


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