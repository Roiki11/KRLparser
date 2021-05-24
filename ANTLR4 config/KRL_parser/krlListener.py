# Generated from krl.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .krlParser import krlParser
else:
    from krlParser import krlParser

# This class defines a complete listener for a parse tree produced by krlParser.
class krlListener(ParseTreeListener):

    # Enter a parse tree produced by krlParser#module.
    def enterModule(self, ctx:krlParser.ModuleContext):
        pass

    # Exit a parse tree produced by krlParser#module.
    def exitModule(self, ctx:krlParser.ModuleContext):
        pass


    # Enter a parse tree produced by krlParser#moduleRoutines.
    def enterModuleRoutines(self, ctx:krlParser.ModuleRoutinesContext):
        pass

    # Exit a parse tree produced by krlParser#moduleRoutines.
    def exitModuleRoutines(self, ctx:krlParser.ModuleRoutinesContext):
        pass


    # Enter a parse tree produced by krlParser#mainRoutine.
    def enterMainRoutine(self, ctx:krlParser.MainRoutineContext):
        pass

    # Exit a parse tree produced by krlParser#mainRoutine.
    def exitMainRoutine(self, ctx:krlParser.MainRoutineContext):
        pass


    # Enter a parse tree produced by krlParser#subRoutine.
    def enterSubRoutine(self, ctx:krlParser.SubRoutineContext):
        pass

    # Exit a parse tree produced by krlParser#subRoutine.
    def exitSubRoutine(self, ctx:krlParser.SubRoutineContext):
        pass


    # Enter a parse tree produced by krlParser#procedureDefinition.
    def enterProcedureDefinition(self, ctx:krlParser.ProcedureDefinitionContext):
        pass

    # Exit a parse tree produced by krlParser#procedureDefinition.
    def exitProcedureDefinition(self, ctx:krlParser.ProcedureDefinitionContext):
        pass


    # Enter a parse tree produced by krlParser#procedureName.
    def enterProcedureName(self, ctx:krlParser.ProcedureNameContext):
        pass

    # Exit a parse tree produced by krlParser#procedureName.
    def exitProcedureName(self, ctx:krlParser.ProcedureNameContext):
        pass


    # Enter a parse tree produced by krlParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:krlParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by krlParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:krlParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by krlParser#functionName.
    def enterFunctionName(self, ctx:krlParser.FunctionNameContext):
        pass

    # Exit a parse tree produced by krlParser#functionName.
    def exitFunctionName(self, ctx:krlParser.FunctionNameContext):
        pass


    # Enter a parse tree produced by krlParser#moduleData.
    def enterModuleData(self, ctx:krlParser.ModuleDataContext):
        pass

    # Exit a parse tree produced by krlParser#moduleData.
    def exitModuleData(self, ctx:krlParser.ModuleDataContext):
        pass


    # Enter a parse tree produced by krlParser#moduleName.
    def enterModuleName(self, ctx:krlParser.ModuleNameContext):
        pass

    # Exit a parse tree produced by krlParser#moduleName.
    def exitModuleName(self, ctx:krlParser.ModuleNameContext):
        pass


    # Enter a parse tree produced by krlParser#dataList.
    def enterDataList(self, ctx:krlParser.DataListContext):
        pass

    # Exit a parse tree produced by krlParser#dataList.
    def exitDataList(self, ctx:krlParser.DataListContext):
        pass


    # Enter a parse tree produced by krlParser#arrayInitialisation.
    def enterArrayInitialisation(self, ctx:krlParser.ArrayInitialisationContext):
        pass

    # Exit a parse tree produced by krlParser#arrayInitialisation.
    def exitArrayInitialisation(self, ctx:krlParser.ArrayInitialisationContext):
        pass


    # Enter a parse tree produced by krlParser#typeDeclaration.
    def enterTypeDeclaration(self, ctx:krlParser.TypeDeclarationContext):
        pass

    # Exit a parse tree produced by krlParser#typeDeclaration.
    def exitTypeDeclaration(self, ctx:krlParser.TypeDeclarationContext):
        pass


    # Enter a parse tree produced by krlParser#structureDefinition.
    def enterStructureDefinition(self, ctx:krlParser.StructureDefinitionContext):
        pass

    # Exit a parse tree produced by krlParser#structureDefinition.
    def exitStructureDefinition(self, ctx:krlParser.StructureDefinitionContext):
        pass


    # Enter a parse tree produced by krlParser#enumDefinition.
    def enterEnumDefinition(self, ctx:krlParser.EnumDefinitionContext):
        pass

    # Exit a parse tree produced by krlParser#enumDefinition.
    def exitEnumDefinition(self, ctx:krlParser.EnumDefinitionContext):
        pass


    # Enter a parse tree produced by krlParser#enumValue.
    def enterEnumValue(self, ctx:krlParser.EnumValueContext):
        pass

    # Exit a parse tree produced by krlParser#enumValue.
    def exitEnumValue(self, ctx:krlParser.EnumValueContext):
        pass


    # Enter a parse tree produced by krlParser#variableDeclaration.
    def enterVariableDeclaration(self, ctx:krlParser.VariableDeclarationContext):
        pass

    # Exit a parse tree produced by krlParser#variableDeclaration.
    def exitVariableDeclaration(self, ctx:krlParser.VariableDeclarationContext):
        pass


    # Enter a parse tree produced by krlParser#signalDeclaration.
    def enterSignalDeclaration(self, ctx:krlParser.SignalDeclarationContext):
        pass

    # Exit a parse tree produced by krlParser#signalDeclaration.
    def exitSignalDeclaration(self, ctx:krlParser.SignalDeclarationContext):
        pass


    # Enter a parse tree produced by krlParser#variableDeclarationInDataList.
    def enterVariableDeclarationInDataList(self, ctx:krlParser.VariableDeclarationInDataListContext):
        pass

    # Exit a parse tree produced by krlParser#variableDeclarationInDataList.
    def exitVariableDeclarationInDataList(self, ctx:krlParser.VariableDeclarationInDataListContext):
        pass


    # Enter a parse tree produced by krlParser#variableListRest.
    def enterVariableListRest(self, ctx:krlParser.VariableListRestContext):
        pass

    # Exit a parse tree produced by krlParser#variableListRest.
    def exitVariableListRest(self, ctx:krlParser.VariableListRestContext):
        pass


    # Enter a parse tree produced by krlParser#variableInitialisation.
    def enterVariableInitialisation(self, ctx:krlParser.VariableInitialisationContext):
        pass

    # Exit a parse tree produced by krlParser#variableInitialisation.
    def exitVariableInitialisation(self, ctx:krlParser.VariableInitialisationContext):
        pass


    # Enter a parse tree produced by krlParser#structLiteral.
    def enterStructLiteral(self, ctx:krlParser.StructLiteralContext):
        pass

    # Exit a parse tree produced by krlParser#structLiteral.
    def exitStructLiteral(self, ctx:krlParser.StructLiteralContext):
        pass


    # Enter a parse tree produced by krlParser#structElementList.
    def enterStructElementList(self, ctx:krlParser.StructElementListContext):
        pass

    # Exit a parse tree produced by krlParser#structElementList.
    def exitStructElementList(self, ctx:krlParser.StructElementListContext):
        pass


    # Enter a parse tree produced by krlParser#structElement.
    def enterStructElement(self, ctx:krlParser.StructElementContext):
        pass

    # Exit a parse tree produced by krlParser#structElement.
    def exitStructElement(self, ctx:krlParser.StructElementContext):
        pass


    # Enter a parse tree produced by krlParser#formalParameters.
    def enterFormalParameters(self, ctx:krlParser.FormalParametersContext):
        pass

    # Exit a parse tree produced by krlParser#formalParameters.
    def exitFormalParameters(self, ctx:krlParser.FormalParametersContext):
        pass


    # Enter a parse tree produced by krlParser#parameter.
    def enterParameter(self, ctx:krlParser.ParameterContext):
        pass

    # Exit a parse tree produced by krlParser#parameter.
    def exitParameter(self, ctx:krlParser.ParameterContext):
        pass


    # Enter a parse tree produced by krlParser#routineBody.
    def enterRoutineBody(self, ctx:krlParser.RoutineBodyContext):
        pass

    # Exit a parse tree produced by krlParser#routineBody.
    def exitRoutineBody(self, ctx:krlParser.RoutineBodyContext):
        pass


    # Enter a parse tree produced by krlParser#routineDataSection.
    def enterRoutineDataSection(self, ctx:krlParser.RoutineDataSectionContext):
        pass

    # Exit a parse tree produced by krlParser#routineDataSection.
    def exitRoutineDataSection(self, ctx:krlParser.RoutineDataSectionContext):
        pass


    # Enter a parse tree produced by krlParser#forwardDeclaration.
    def enterForwardDeclaration(self, ctx:krlParser.ForwardDeclarationContext):
        pass

    # Exit a parse tree produced by krlParser#forwardDeclaration.
    def exitForwardDeclaration(self, ctx:krlParser.ForwardDeclarationContext):
        pass


    # Enter a parse tree produced by krlParser#formalParametersWithType.
    def enterFormalParametersWithType(self, ctx:krlParser.FormalParametersWithTypeContext):
        pass

    # Exit a parse tree produced by krlParser#formalParametersWithType.
    def exitFormalParametersWithType(self, ctx:krlParser.FormalParametersWithTypeContext):
        pass


    # Enter a parse tree produced by krlParser#parameterWithType.
    def enterParameterWithType(self, ctx:krlParser.ParameterWithTypeContext):
        pass

    # Exit a parse tree produced by krlParser#parameterWithType.
    def exitParameterWithType(self, ctx:krlParser.ParameterWithTypeContext):
        pass


    # Enter a parse tree produced by krlParser#parameterCallType.
    def enterParameterCallType(self, ctx:krlParser.ParameterCallTypeContext):
        pass

    # Exit a parse tree produced by krlParser#parameterCallType.
    def exitParameterCallType(self, ctx:krlParser.ParameterCallTypeContext):
        pass


    # Enter a parse tree produced by krlParser#importStatement.
    def enterImportStatement(self, ctx:krlParser.ImportStatementContext):
        pass

    # Exit a parse tree produced by krlParser#importStatement.
    def exitImportStatement(self, ctx:krlParser.ImportStatementContext):
        pass


    # Enter a parse tree produced by krlParser#variableName.
    def enterVariableName(self, ctx:krlParser.VariableNameContext):
        pass

    # Exit a parse tree produced by krlParser#variableName.
    def exitVariableName(self, ctx:krlParser.VariableNameContext):
        pass


    # Enter a parse tree produced by krlParser#arrayVariableSuffix.
    def enterArrayVariableSuffix(self, ctx:krlParser.ArrayVariableSuffixContext):
        pass

    # Exit a parse tree produced by krlParser#arrayVariableSuffix.
    def exitArrayVariableSuffix(self, ctx:krlParser.ArrayVariableSuffixContext):
        pass


    # Enter a parse tree produced by krlParser#routineImplementationSection.
    def enterRoutineImplementationSection(self, ctx:krlParser.RoutineImplementationSectionContext):
        pass

    # Exit a parse tree produced by krlParser#routineImplementationSection.
    def exitRoutineImplementationSection(self, ctx:krlParser.RoutineImplementationSectionContext):
        pass


    # Enter a parse tree produced by krlParser#statementList.
    def enterStatementList(self, ctx:krlParser.StatementListContext):
        pass

    # Exit a parse tree produced by krlParser#statementList.
    def exitStatementList(self, ctx:krlParser.StatementListContext):
        pass


    # Enter a parse tree produced by krlParser#statement.
    def enterStatement(self, ctx:krlParser.StatementContext):
        pass

    # Exit a parse tree produced by krlParser#statement.
    def exitStatement(self, ctx:krlParser.StatementContext):
        pass


    # Enter a parse tree produced by krlParser#analogOutputStatement.
    def enterAnalogOutputStatement(self, ctx:krlParser.AnalogOutputStatementContext):
        pass

    # Exit a parse tree produced by krlParser#analogOutputStatement.
    def exitAnalogOutputStatement(self, ctx:krlParser.AnalogOutputStatementContext):
        pass


    # Enter a parse tree produced by krlParser#analogInputStatement.
    def enterAnalogInputStatement(self, ctx:krlParser.AnalogInputStatementContext):
        pass

    # Exit a parse tree produced by krlParser#analogInputStatement.
    def exitAnalogInputStatement(self, ctx:krlParser.AnalogInputStatementContext):
        pass


    # Enter a parse tree produced by krlParser#switchBlockStatementGroups.
    def enterSwitchBlockStatementGroups(self, ctx:krlParser.SwitchBlockStatementGroupsContext):
        pass

    # Exit a parse tree produced by krlParser#switchBlockStatementGroups.
    def exitSwitchBlockStatementGroups(self, ctx:krlParser.SwitchBlockStatementGroupsContext):
        pass


    # Enter a parse tree produced by krlParser#caseLabel.
    def enterCaseLabel(self, ctx:krlParser.CaseLabelContext):
        pass

    # Exit a parse tree produced by krlParser#caseLabel.
    def exitCaseLabel(self, ctx:krlParser.CaseLabelContext):
        pass


    # Enter a parse tree produced by krlParser#defaultLabel.
    def enterDefaultLabel(self, ctx:krlParser.DefaultLabelContext):
        pass

    # Exit a parse tree produced by krlParser#defaultLabel.
    def exitDefaultLabel(self, ctx:krlParser.DefaultLabelContext):
        pass


    # Enter a parse tree produced by krlParser#expressionList.
    def enterExpressionList(self, ctx:krlParser.ExpressionListContext):
        pass

    # Exit a parse tree produced by krlParser#expressionList.
    def exitExpressionList(self, ctx:krlParser.ExpressionListContext):
        pass


    # Enter a parse tree produced by krlParser#assignmentExpression.
    def enterAssignmentExpression(self, ctx:krlParser.AssignmentExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#assignmentExpression.
    def exitAssignmentExpression(self, ctx:krlParser.AssignmentExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#expression.
    def enterExpression(self, ctx:krlParser.ExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#expression.
    def exitExpression(self, ctx:krlParser.ExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#relationalOp.
    def enterRelationalOp(self, ctx:krlParser.RelationalOpContext):
        pass

    # Exit a parse tree produced by krlParser#relationalOp.
    def exitRelationalOp(self, ctx:krlParser.RelationalOpContext):
        pass


    # Enter a parse tree produced by krlParser#conditionalOrExpression.
    def enterConditionalOrExpression(self, ctx:krlParser.ConditionalOrExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#conditionalOrExpression.
    def exitConditionalOrExpression(self, ctx:krlParser.ConditionalOrExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#exclusiveOrExpression.
    def enterExclusiveOrExpression(self, ctx:krlParser.ExclusiveOrExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#exclusiveOrExpression.
    def exitExclusiveOrExpression(self, ctx:krlParser.ExclusiveOrExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#conditionalAndExpression.
    def enterConditionalAndExpression(self, ctx:krlParser.ConditionalAndExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#conditionalAndExpression.
    def exitConditionalAndExpression(self, ctx:krlParser.ConditionalAndExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:krlParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:krlParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:krlParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:krlParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#geometricExpression.
    def enterGeometricExpression(self, ctx:krlParser.GeometricExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#geometricExpression.
    def exitGeometricExpression(self, ctx:krlParser.GeometricExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#unaryNotExpression.
    def enterUnaryNotExpression(self, ctx:krlParser.UnaryNotExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#unaryNotExpression.
    def exitUnaryNotExpression(self, ctx:krlParser.UnaryNotExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#unaryPlusMinuxExpression.
    def enterUnaryPlusMinuxExpression(self, ctx:krlParser.UnaryPlusMinuxExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#unaryPlusMinuxExpression.
    def exitUnaryPlusMinuxExpression(self, ctx:krlParser.UnaryPlusMinuxExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#primary.
    def enterPrimary(self, ctx:krlParser.PrimaryContext):
        pass

    # Exit a parse tree produced by krlParser#primary.
    def exitPrimary(self, ctx:krlParser.PrimaryContext):
        pass


    # Enter a parse tree produced by krlParser#parExpression.
    def enterParExpression(self, ctx:krlParser.ParExpressionContext):
        pass

    # Exit a parse tree produced by krlParser#parExpression.
    def exitParExpression(self, ctx:krlParser.ParExpressionContext):
        pass


    # Enter a parse tree produced by krlParser#type_.
    def enterType_(self, ctx:krlParser.Type_Context):
        pass

    # Exit a parse tree produced by krlParser#type_.
    def exitType_(self, ctx:krlParser.Type_Context):
        pass


    # Enter a parse tree produced by krlParser#typeName.
    def enterTypeName(self, ctx:krlParser.TypeNameContext):
        pass

    # Exit a parse tree produced by krlParser#typeName.
    def exitTypeName(self, ctx:krlParser.TypeNameContext):
        pass


    # Enter a parse tree produced by krlParser#primitiveType.
    def enterPrimitiveType(self, ctx:krlParser.PrimitiveTypeContext):
        pass

    # Exit a parse tree produced by krlParser#primitiveType.
    def exitPrimitiveType(self, ctx:krlParser.PrimitiveTypeContext):
        pass


    # Enter a parse tree produced by krlParser#arguments.
    def enterArguments(self, ctx:krlParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by krlParser#arguments.
    def exitArguments(self, ctx:krlParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by krlParser#literal.
    def enterLiteral(self, ctx:krlParser.LiteralContext):
        pass

    # Exit a parse tree produced by krlParser#literal.
    def exitLiteral(self, ctx:krlParser.LiteralContext):
        pass


    # Enter a parse tree produced by krlParser#enumElement.
    def enterEnumElement(self, ctx:krlParser.EnumElementContext):
        pass

    # Exit a parse tree produced by krlParser#enumElement.
    def exitEnumElement(self, ctx:krlParser.EnumElementContext):
        pass



del krlParser