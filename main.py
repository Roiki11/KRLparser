

import sys
from antlr4 import *
from krlLexer import krlLexer
from krlParser import krlParser
from krlListener import krlListener
from krlVisitor import krlVisitor


class myListener(krlListener):

    def __init__(self):
        self.mainProgram = {}
        self.subPrograms = {}
        self.vars = {}

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
        #print(ctx.getText())
        print(ctx.getChildCount())



    def enterSubRoutine(self, ctx:krlParser.SubRoutineContext):
        print(ctx.getText())

    def enterProcedureDefinition(self, ctx:krlParser.ProcedureDefinitionContext):
        n = ctx.getChildCount()
        y = ctx.getChild(1).getText() #procedure name
        self.mainProgram["name"] = y
        #for x in range(0, n):
         #   y=ctx.getChild(x).getText()
          #  print(y)
        print(self.mainProgram)

    def enterVariableDeclaration(self, ctx:krlParser.VariableDeclarationContext):
        n=ctx.getChildCount()
        print(ctx.DECL())
        print(ctx.type_().getText())
        name = str(ctx.variableName().getText())
        if name is not 0:
            self.vars[name] = 0
            print(self.vars)

    def enterVariableListRest(self, ctx:krlParser.VariableListRestContext):
        print(ctx.getChildCount())
        for x in range(0, ctx.getChildCount()):
            print(ctx.getChild(x))
            y= str(ctx.getText()).strip(",")
            ysp= y.split(",")
            for x in ysp:
                if x is ",":
                    break
                else:
                    self.vars[x] = 0
                    print(self.vars)


class myVisitor(krlVisitor):
    def visitMainRoutine(self, ctx:krlParser.MainRoutineContext):
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
    visitor = myVisitor()
    visitor.visit(tree)




if __name__ == '__main__':
    main()