"""
Python bindings for slang, the SystemVerilog compiler library
"""
from __future__ import annotations
import os
import pybind11_stubgen.typing_ext
import typing
__all__ = ['ASTContext', 'ASTFlags', 'AbortAssertionExpr', 'AcceptOnPropertyExprSyntax', 'ActionBlockSyntax', 'AnonymousProgramSymbol', 'AnonymousProgramSyntax', 'AnsiPortListSyntax', 'AnsiUdpPortListSyntax', 'ArbitrarySymbolExpression', 'ArgumentDirection', 'ArgumentListSyntax', 'ArgumentSyntax', 'ArrayOrRandomizeMethodExpressionSyntax', 'AssertionExpr', 'AssertionExprKind', 'AssertionInstanceExpression', 'AssertionItemPortListSyntax', 'AssertionItemPortSyntax', 'AssertionKind', 'AssertionPortSymbol', 'AssignmentExpression', 'AssignmentPatternExpressionBase', 'AssignmentPatternExpressionSyntax', 'AssignmentPatternItemSyntax', 'AssignmentPatternSyntax', 'AssociativeArrayType', 'AttributeInstanceSyntax', 'AttributeSpecSyntax', 'AttributeSymbol', 'BadExpressionSyntax', 'Bag', 'BeginKeywordsDirectiveSyntax', 'BinSelectWithFilterExpr', 'BinSelectWithFilterExprSyntax', 'BinaryAssertionExpr', 'BinaryAssertionOperator', 'BinaryBinsSelectExpr', 'BinaryBinsSelectExprSyntax', 'BinaryBlockEventExpressionSyntax', 'BinaryConditionalDirectiveExpressionSyntax', 'BinaryEventExpressionSyntax', 'BinaryExpression', 'BinaryExpressionSyntax', 'BinaryOperator', 'BinaryPropertyExprSyntax', 'BinarySequenceExprSyntax', 'BindDirectiveSyntax', 'BindTargetListSyntax', 'BinsSelectConditionExprSyntax', 'BinsSelectExpr', 'BinsSelectExprKind', 'BinsSelectExpressionSyntax', 'BinsSelectionSyntax', 'BitSelectSyntax', 'BlockCoverageEventSyntax', 'BlockEventExpressionSyntax', 'BlockEventListControl', 'BlockStatement', 'BlockStatementSyntax', 'BreakStatement', 'BufferID', 'BumpAllocator', 'CHandleType', 'CallExpression', 'CaseAssertionExpr', 'CaseGenerateSyntax', 'CaseItemSyntax', 'CasePropertyExprSyntax', 'CaseStatement', 'CaseStatementCondition', 'CaseStatementSyntax', 'CastExpressionSyntax', 'CellConfigRuleSyntax', 'ChargeStrengthSyntax', 'CheckerDataDeclarationSyntax', 'CheckerDeclarationSyntax', 'CheckerInstanceBodySymbol', 'CheckerInstanceStatementSyntax', 'CheckerInstanceSymbol', 'CheckerInstantiationSyntax', 'CheckerSymbol', 'ClassDeclarationSyntax', 'ClassMethodDeclarationSyntax', 'ClassMethodPrototypeSyntax', 'ClassNameSyntax', 'ClassPropertyDeclarationSyntax', 'ClassPropertySymbol', 'ClassSpecifierSyntax', 'ClassType', 'ClockVarSymbol', 'ClockingAssertionExpr', 'ClockingBlockSymbol', 'ClockingDeclarationSyntax', 'ClockingDirectionSyntax', 'ClockingEventExpression', 'ClockingItemSyntax', 'ClockingPropertyExprSyntax', 'ClockingSequenceExprSyntax', 'ClockingSkew', 'ClockingSkewSyntax', 'ColonExpressionClauseSyntax', 'CommandLineOptions', 'Compilation', 'CompilationFlags', 'CompilationOptions', 'CompilationUnitSymbol', 'CompilationUnitSyntax', 'ConcatenationExpression', 'ConcatenationExpressionSyntax', 'ConcurrentAssertionMemberSyntax', 'ConcurrentAssertionStatement', 'ConcurrentAssertionStatementSyntax', 'ConditionBinsSelectExpr', 'ConditionalAssertionExpr', 'ConditionalBranchDirectiveSyntax', 'ConditionalConstraint', 'ConditionalConstraintSyntax', 'ConditionalDirectiveExpressionSyntax', 'ConditionalExpression', 'ConditionalExpressionSyntax', 'ConditionalPathDeclarationSyntax', 'ConditionalPatternSyntax', 'ConditionalPredicateSyntax', 'ConditionalPropertyExprSyntax', 'ConditionalStatement', 'ConditionalStatementSyntax', 'ConfigBlockSymbol', 'ConfigCellIdentifierSyntax', 'ConfigDeclarationSyntax', 'ConfigInstanceIdentifierSyntax', 'ConfigLiblistSyntax', 'ConfigRuleClauseSyntax', 'ConfigRuleSyntax', 'ConfigUseClauseSyntax', 'ConstantPattern', 'ConstantRange', 'ConstantValue', 'Constraint', 'ConstraintBlockSymbol', 'ConstraintBlockSyntax', 'ConstraintDeclarationSyntax', 'ConstraintItemSyntax', 'ConstraintKind', 'ConstraintList', 'ConstraintPrototypeSyntax', 'ContinueStatement', 'ContinuousAssignSymbol', 'ContinuousAssignSyntax', 'ConversionExpression', 'ConversionKind', 'CopyClassExpression', 'CopyClassExpressionSyntax', 'CoverCrossBodySymbol', 'CoverCrossSymbol', 'CoverCrossSyntax', 'CoverageBinInitializerSyntax', 'CoverageBinSymbol', 'CoverageBinsArraySizeSyntax', 'CoverageBinsSyntax', 'CoverageIffClauseSyntax', 'CoverageOptionSetter', 'CoverageOptionSyntax', 'CovergroupBodySymbol', 'CovergroupDeclarationSyntax', 'CovergroupType', 'CoverpointSymbol', 'CoverpointSyntax', 'CrossIdBinsSelectExpr', 'CycleDelayControl', 'DPIExportSyntax', 'DPIImportSyntax', 'DPIOpenArrayType', 'DataDeclarationSyntax', 'DataTypeExpression', 'DataTypeSyntax', 'DeclaratorSyntax', 'DeclaredType', 'DefParamAssignmentSyntax', 'DefParamSymbol', 'DefParamSyntax', 'DefaultCaseItemSyntax', 'DefaultClockingReferenceSyntax', 'DefaultConfigRuleSyntax', 'DefaultCoverageBinInitializerSyntax', 'DefaultDisableDeclarationSyntax', 'DefaultExtendsClauseArgSyntax', 'DefaultFunctionPortSyntax', 'DefaultNetTypeDirectiveSyntax', 'DefaultPropertyCaseItemSyntax', 'DefaultRsCaseItemSyntax', 'DefaultSkewItemSyntax', 'DeferredAssertionSyntax', 'DefineDirectiveSyntax', 'DefinitionKind', 'DefinitionSymbol', 'Delay3Control', 'Delay3Syntax', 'DelayControl', 'DelaySyntax', 'DelayedSequenceElementSyntax', 'DelayedSequenceExprSyntax', 'DiagCode', 'DiagGroup', 'DiagSubsystem', 'Diagnostic', 'DiagnosticClient', 'DiagnosticEngine', 'DiagnosticSeverity', 'Diagnostics', 'Diags', 'DimensionKind', 'DimensionSpecifierSyntax', 'DirectiveSyntax', 'DisableConstraintSyntax', 'DisableForkStatement', 'DisableForkStatementSyntax', 'DisableIffAssertionExpr', 'DisableIffSyntax', 'DisableSoftConstraint', 'DisableStatement', 'DisableStatementSyntax', 'DistConstraintListSyntax', 'DistExpression', 'DistItemSyntax', 'DistWeightSyntax', 'DividerClauseSyntax', 'DoWhileLoopStatement', 'DoWhileStatementSyntax', 'DotMemberClauseSyntax', 'DriveStrengthSyntax', 'Driver', 'DriverKind', 'DynamicArrayType', 'EdgeControlSpecifierSyntax', 'EdgeDescriptorSyntax', 'EdgeKind', 'EdgeSensitivePathSuffixSyntax', 'ElabSystemTaskKind', 'ElabSystemTaskSymbol', 'ElabSystemTaskSyntax', 'ElementSelectExpression', 'ElementSelectExpressionSyntax', 'ElementSelectSyntax', 'ElseClauseSyntax', 'ElseConstraintClauseSyntax', 'ElsePropertyClauseSyntax', 'EmptyArgumentExpression', 'EmptyArgumentSyntax', 'EmptyIdentifierNameSyntax', 'EmptyMemberSymbol', 'EmptyMemberSyntax', 'EmptyNonAnsiPortSyntax', 'EmptyPortConnectionSyntax', 'EmptyQueueExpressionSyntax', 'EmptyStatement', 'EmptyStatementSyntax', 'EmptyTimingCheckArgSyntax', 'EnumType', 'EnumTypeSyntax', 'EnumValueSymbol', 'EqualsAssertionArgClauseSyntax', 'EqualsTypeClauseSyntax', 'EqualsValueClauseSyntax', 'ErrorType', 'EvalContext', 'EvalFlags', 'EvaluatedDimension', 'EventControlSyntax', 'EventControlWithExpressionSyntax', 'EventExpressionSyntax', 'EventListControl', 'EventTriggerStatement', 'EventTriggerStatementSyntax', 'EventType', 'ExplicitAnsiPortSyntax', 'ExplicitImportSymbol', 'ExplicitNonAnsiPortSyntax', 'Expression', 'ExpressionConstraint', 'ExpressionConstraintSyntax', 'ExpressionCoverageBinInitializerSyntax', 'ExpressionKind', 'ExpressionOrDistSyntax', 'ExpressionPatternSyntax', 'ExpressionStatement', 'ExpressionStatementSyntax', 'ExpressionSyntax', 'ExpressionTimingCheckArgSyntax', 'ExtendsClauseSyntax', 'ExternInterfaceMethodSyntax', 'ExternModuleDeclSyntax', 'ExternUdpDeclSyntax', 'FieldSymbol', 'FilePathSpecSyntax', 'FirstMatchAssertionExpr', 'FirstMatchSequenceExprSyntax', 'FixedSizeUnpackedArrayType', 'FloatingType', 'ForLoopStatement', 'ForLoopStatementSyntax', 'ForVariableDeclarationSyntax', 'ForeachConstraint', 'ForeachLoopListSyntax', 'ForeachLoopStatement', 'ForeachLoopStatementSyntax', 'ForeverLoopStatement', 'ForeverStatementSyntax', 'FormalArgumentSymbol', 'ForwardTypeRestriction', 'ForwardTypeRestrictionSyntax', 'ForwardTypedefDeclarationSyntax', 'ForwardingTypedefSymbol', 'FunctionDeclarationSyntax', 'FunctionPortBaseSyntax', 'FunctionPortListSyntax', 'FunctionPortSyntax', 'FunctionPrototypeSyntax', 'GenerateBlockArraySymbol', 'GenerateBlockSymbol', 'GenerateBlockSyntax', 'GenerateRegionSyntax', 'GenericClassDefSymbol', 'GenvarDeclarationSyntax', 'GenvarSymbol', 'HierarchicalInstanceSyntax', 'HierarchicalValueExpression', 'HierarchyInstantiationSyntax', 'IdWithExprCoverageBinInitializerSyntax', 'IdentifierNameSyntax', 'IdentifierSelectNameSyntax', 'IfGenerateSyntax', 'IfNonePathDeclarationSyntax', 'IffEventClauseSyntax', 'ImmediateAssertionMemberSyntax', 'ImmediateAssertionStatement', 'ImmediateAssertionStatementSyntax', 'ImplementsClauseSyntax', 'ImplicationConstraint', 'ImplicationConstraintSyntax', 'ImplicitAnsiPortSyntax', 'ImplicitEventControl', 'ImplicitEventControlSyntax', 'ImplicitNonAnsiPortSyntax', 'ImplicitTypeSyntax', 'IncludeDirectiveSyntax', 'InsideExpression', 'InsideExpressionSyntax', 'InstanceArraySymbol', 'InstanceBodySymbol', 'InstanceConfigRuleSyntax', 'InstanceNameSyntax', 'InstanceSymbol', 'InstanceSymbolBase', 'IntegerLiteral', 'IntegerTypeSyntax', 'IntegerVectorExpressionSyntax', 'IntegralFlags', 'IntegralType', 'InterfacePortHeaderSyntax', 'InterfacePortSymbol', 'IntersectClauseSyntax', 'InvalidAssertionExpr', 'InvalidBinsSelectExpr', 'InvalidConstraint', 'InvalidExpression', 'InvalidPattern', 'InvalidStatement', 'InvalidTimingControl', 'InvocationExpressionSyntax', 'IteratorSymbol', 'JumpStatementSyntax', 'KeywordNameSyntax', 'KeywordTypeSyntax', 'LValue', 'LValueReferenceExpression', 'LanguageVersion', 'LetDeclSymbol', 'LetDeclarationSyntax', 'LexerOptions', 'LibraryDeclarationSyntax', 'LibraryIncDirClauseSyntax', 'LibraryIncludeStatementSyntax', 'LibraryMapSyntax', 'LineDirectiveSyntax', 'LiteralBase', 'LiteralExpressionSyntax', 'LocalAssertionVarSymbol', 'LocalVariableDeclarationSyntax', 'Lookup', 'LookupFlags', 'LookupLocation', 'LookupResult', 'LookupResultFlags', 'LoopConstraintSyntax', 'LoopGenerateSyntax', 'LoopStatementSyntax', 'MacroActualArgumentListSyntax', 'MacroActualArgumentSyntax', 'MacroArgumentDefaultSyntax', 'MacroFormalArgumentListSyntax', 'MacroFormalArgumentSyntax', 'MacroUsageSyntax', 'MatchesClauseSyntax', 'MemberAccessExpression', 'MemberAccessExpressionSyntax', 'MemberSyntax', 'MethodFlags', 'MethodPrototypeSymbol', 'MinTypMax', 'MinTypMaxExpression', 'MinTypMaxExpressionSyntax', 'ModportClockingPortSyntax', 'ModportClockingSymbol', 'ModportDeclarationSyntax', 'ModportExplicitPortSyntax', 'ModportItemSyntax', 'ModportNamedPortSyntax', 'ModportPortSymbol', 'ModportPortSyntax', 'ModportSimplePortListSyntax', 'ModportSubroutinePortListSyntax', 'ModportSubroutinePortSyntax', 'ModportSymbol', 'ModuleDeclarationSyntax', 'ModuleHeaderSyntax', 'MultiPortSymbol', 'MultipleConcatenationExpressionSyntax', 'NameSyntax', 'NameValuePragmaExpressionSyntax', 'NamedArgumentSyntax', 'NamedBlockClauseSyntax', 'NamedConditionalDirectiveExpressionSyntax', 'NamedLabelSyntax', 'NamedParamAssignmentSyntax', 'NamedPortConnectionSyntax', 'NamedStructurePatternMemberSyntax', 'NamedTypeSyntax', 'NamedValueExpression', 'NetAliasSymbol', 'NetAliasSyntax', 'NetDeclarationSyntax', 'NetPortHeaderSyntax', 'NetStrengthSyntax', 'NetSymbol', 'NetType', 'NetTypeDeclarationSyntax', 'NewArrayExpression', 'NewArrayExpressionSyntax', 'NewClassExpression', 'NewClassExpressionSyntax', 'NewCovergroupExpression', 'NonAnsiPortListSyntax', 'NonAnsiPortSyntax', 'NonAnsiUdpPortListSyntax', 'NonConstantFunction', 'Null', 'NullLiteral', 'NullType', 'NumberPragmaExpressionSyntax', 'OneStepDelayControl', 'OneStepDelaySyntax', 'OrderedArgumentSyntax', 'OrderedParamAssignmentSyntax', 'OrderedPortConnectionSyntax', 'OrderedStructurePatternMemberSyntax', 'PackageExportAllDeclarationSyntax', 'PackageExportDeclarationSyntax', 'PackageImportDeclarationSyntax', 'PackageImportItemSyntax', 'PackageSymbol', 'PackedArrayType', 'PackedStructType', 'PackedUnionType', 'ParamAssignmentSyntax', 'ParameterDeclarationBaseSyntax', 'ParameterDeclarationStatementSyntax', 'ParameterDeclarationSyntax', 'ParameterPortListSyntax', 'ParameterSymbol', 'ParameterSymbolBase', 'ParameterValueAssignmentSyntax', 'ParenExpressionListSyntax', 'ParenPragmaExpressionSyntax', 'ParenthesizedBinsSelectExprSyntax', 'ParenthesizedConditionalDirectiveExpressionSyntax', 'ParenthesizedEventExpressionSyntax', 'ParenthesizedExpressionSyntax', 'ParenthesizedPatternSyntax', 'ParenthesizedPropertyExprSyntax', 'ParenthesizedSequenceExprSyntax', 'ParserOptions', 'PathDeclarationSyntax', 'PathDescriptionSyntax', 'PathSuffixSyntax', 'Pattern', 'PatternCaseItemSyntax', 'PatternCaseStatement', 'PatternKind', 'PatternSyntax', 'PatternVarSymbol', 'PortConcatenationSyntax', 'PortConnection', 'PortConnectionSyntax', 'PortDeclarationSyntax', 'PortExpressionSyntax', 'PortHeaderSyntax', 'PortListSyntax', 'PortReferenceSyntax', 'PortSymbol', 'PostfixUnaryExpressionSyntax', 'PragmaDirectiveSyntax', 'PragmaExpressionSyntax', 'PredefinedIntegerType', 'PrefixUnaryExpressionSyntax', 'PreprocessorOptions', 'PrimaryBlockEventExpressionSyntax', 'PrimaryExpressionSyntax', 'PrimitiveInstanceSymbol', 'PrimitiveInstantiationSyntax', 'PrimitivePortDirection', 'PrimitivePortSymbol', 'PrimitiveSymbol', 'ProceduralAssignStatement', 'ProceduralAssignStatementSyntax', 'ProceduralBlockKind', 'ProceduralBlockSymbol', 'ProceduralBlockSyntax', 'ProceduralCheckerStatement', 'ProceduralDeassignStatement', 'ProceduralDeassignStatementSyntax', 'ProductionSyntax', 'PropertyCaseItemSyntax', 'PropertyDeclarationSyntax', 'PropertyExprSyntax', 'PropertySpecSyntax', 'PropertySymbol', 'PropertyType', 'PullStrengthSyntax', 'PulseStyleDeclarationSyntax', 'PulseStyleKind', 'PulseStyleSymbol', 'QueueDimensionSpecifierSyntax', 'QueueType', 'RandCaseItemSyntax', 'RandCaseStatement', 'RandCaseStatementSyntax', 'RandJoinClauseSyntax', 'RandMode', 'RandSeqProductionSymbol', 'RandSequenceStatement', 'RandSequenceStatementSyntax', 'RangeCoverageBinInitializerSyntax', 'RangeDimensionSpecifierSyntax', 'RangeListSyntax', 'RangeSelectExpression', 'RangeSelectSyntax', 'RangeSelectionKind', 'RealLiteral', 'RepeatLoopStatement', 'RepeatedEventControl', 'RepeatedEventControlSyntax', 'ReplicatedAssignmentPatternExpression', 'ReplicatedAssignmentPatternSyntax', 'ReplicationExpression', 'ReportedDiagnostic', 'ReturnStatement', 'ReturnStatementSyntax', 'RootSymbol', 'RsCaseItemSyntax', 'RsCaseSyntax', 'RsCodeBlockSyntax', 'RsElseClauseSyntax', 'RsIfElseSyntax', 'RsProdItemSyntax', 'RsProdSyntax', 'RsRepeatSyntax', 'RsRuleSyntax', 'RsWeightClauseSyntax', 'SVInt', 'ScalarType', 'Scope', 'ScopedNameSyntax', 'ScriptSession', 'SelectorSyntax', 'SequenceConcatExpr', 'SequenceDeclarationSyntax', 'SequenceExprSyntax', 'SequenceMatchListSyntax', 'SequenceRange', 'SequenceRepetition', 'SequenceRepetitionSyntax', 'SequenceSymbol', 'SequenceType', 'SequenceWithMatchExpr', 'SetExprBinsSelectExpr', 'SignalEventControl', 'SignalEventExpressionSyntax', 'SignedCastExpressionSyntax', 'SimpleAssertionExpr', 'SimpleAssignmentPatternExpression', 'SimpleAssignmentPatternSyntax', 'SimpleBinsSelectExprSyntax', 'SimpleDirectiveSyntax', 'SimplePathSuffixSyntax', 'SimplePragmaExpressionSyntax', 'SimplePropertyExprSyntax', 'SimpleSequenceExprSyntax', 'SimpleSystemSubroutine', 'SolveBeforeConstraint', 'SolveBeforeConstraintSyntax', 'SourceBuffer', 'SourceLibrary', 'SourceLoader', 'SourceLocation', 'SourceManager', 'SourceOptions', 'SourceRange', 'SpecifyBlockSymbol', 'SpecifyBlockSyntax', 'SpecparamDeclarationSyntax', 'SpecparamDeclaratorSyntax', 'SpecparamSymbol', 'StandardCaseItemSyntax', 'StandardPropertyCaseItemSyntax', 'StandardRsCaseItemSyntax', 'Statement', 'StatementBlockKind', 'StatementBlockSymbol', 'StatementKind', 'StatementList', 'StatementSyntax', 'StreamExpressionSyntax', 'StreamExpressionWithRangeSyntax', 'StreamingConcatenationExpression', 'StreamingConcatenationExpressionSyntax', 'StringLiteral', 'StringType', 'StrongWeakAssertionExpr', 'StrongWeakPropertyExprSyntax', 'StructUnionMemberSyntax', 'StructUnionTypeSyntax', 'StructurePattern', 'StructurePatternMemberSyntax', 'StructurePatternSyntax', 'StructuredAssignmentPatternExpression', 'StructuredAssignmentPatternSyntax', 'SubroutineKind', 'SubroutineSymbol', 'SuperNewDefaultedArgsExpressionSyntax', 'Symbol', 'SymbolKind', 'SyntaxKind', 'SyntaxNode', 'SyntaxPrinter', 'SyntaxTree', 'SystemNameSyntax', 'SystemSubroutine', 'SystemTimingCheckKind', 'SystemTimingCheckSymbol', 'SystemTimingCheckSyntax', 'TaggedPattern', 'TaggedPatternSyntax', 'TaggedUnionExpression', 'TaggedUnionExpressionSyntax', 'TempVarSymbol', 'TextDiagnosticClient', 'TimeLiteral', 'TimeScale', 'TimeScaleDirectiveSyntax', 'TimeScaleMagnitude', 'TimeScaleValue', 'TimeUnit', 'TimeUnitsDeclarationSyntax', 'TimedStatement', 'TimingCheckArgSyntax', 'TimingCheckEventArgSyntax', 'TimingCheckEventConditionSyntax', 'TimingControl', 'TimingControlExpressionSyntax', 'TimingControlKind', 'TimingControlStatementSyntax', 'TimingControlSyntax', 'TimingPathSymbol', 'Token', 'TokenKind', 'TransListCoverageBinInitializerSyntax', 'TransRangeSyntax', 'TransRepeatRangeSyntax', 'TransSetSyntax', 'TransparentMemberSymbol', 'Trivia', 'TriviaKind', 'Type', 'TypeAliasType', 'TypeAssignmentSyntax', 'TypeParameterDeclarationSyntax', 'TypeParameterSymbol', 'TypePrinter', 'TypePrintingOptions', 'TypeRefType', 'TypeReferenceExpression', 'TypeReferenceSyntax', 'TypedefDeclarationSyntax', 'UdpBodySyntax', 'UdpDeclarationSyntax', 'UdpEdgeFieldSyntax', 'UdpEntrySyntax', 'UdpFieldBaseSyntax', 'UdpInitialStmtSyntax', 'UdpInputPortDeclSyntax', 'UdpOutputPortDeclSyntax', 'UdpPortDeclSyntax', 'UdpPortListSyntax', 'UdpSimpleFieldSyntax', 'UnaryAssertionExpr', 'UnaryAssertionOperator', 'UnaryBinsSelectExpr', 'UnaryBinsSelectExprSyntax', 'UnaryConditionalDirectiveExpressionSyntax', 'UnaryExpression', 'UnaryOperator', 'UnaryPropertyExprSyntax', 'UnarySelectPropertyExprSyntax', 'UnbasedUnsizedIntegerLiteral', 'Unbounded', 'UnboundedLiteral', 'UnboundedType', 'UnconditionalBranchDirectiveSyntax', 'UnconnectedDrive', 'UnconnectedDriveDirectiveSyntax', 'UndefDirectiveSyntax', 'UninstantiatedDefSymbol', 'UniquePriorityCheck', 'UniquenessConstraint', 'UniquenessConstraintSyntax', 'UnpackedStructType', 'UnpackedUnionType', 'UntypedType', 'UserDefinedNetDeclarationSyntax', 'ValueDriver', 'ValueExpressionBase', 'ValueRangeExpression', 'ValueRangeExpressionSyntax', 'ValueRangeKind', 'ValueSymbol', 'VariableDeclStatement', 'VariableDimensionSyntax', 'VariableFlags', 'VariableLifetime', 'VariablePattern', 'VariablePatternSyntax', 'VariablePortHeaderSyntax', 'VariableSymbol', 'VersionInfo', 'VirtualInterfaceType', 'VirtualInterfaceTypeSyntax', 'Visibility', 'VisitAction', 'VoidCastedCallStatementSyntax', 'VoidType', 'WaitForkStatement', 'WaitForkStatementSyntax', 'WaitOrderStatement', 'WaitOrderStatementSyntax', 'WaitStatement', 'WaitStatementSyntax', 'WhileLoopStatement', 'WildcardDimensionSpecifierSyntax', 'WildcardImportSymbol', 'WildcardPattern', 'WildcardPatternSyntax', 'WildcardPortConnectionSyntax', 'WildcardPortListSyntax', 'WildcardUdpPortListSyntax', 'WithClauseSyntax', 'WithFunctionClauseSyntax', 'WithFunctionSampleSyntax', 'clog2', 'literalBaseFromChar', 'logic_t']
class ASTContext:
    def __init__(self, scope: Scope, lookupLocation: LookupLocation, flags: ASTFlags) -> None:
        ...
    def addAssertionBacktrace(self, diag: Diagnostic) -> None:
        ...
    @typing.overload
    def addDiag(self, code: DiagCode, location: SourceLocation) -> Diagnostic:
        ...
    @typing.overload
    def addDiag(self, code: DiagCode, sourceRange: SourceRange) -> Diagnostic:
        ...
    def eval(self, expr: Expression, extraFlags: EvalFlags) -> ConstantValue:
        ...
    def evalDimension(self, syntax: VariableDimensionSyntax, requireRange: bool, isPacked: bool) -> EvaluatedDimension:
        ...
    @typing.overload
    def evalInteger(self, syntax: ExpressionSyntax, extraFlags: ASTFlags) -> int | None:
        ...
    @typing.overload
    def evalInteger(self, expr: Expression, extraFlags: EvalFlags) -> int | None:
        ...
    @typing.overload
    def evalPackedDimension(self, syntax: VariableDimensionSyntax) -> EvaluatedDimension:
        ...
    @typing.overload
    def evalPackedDimension(self, syntax: ElementSelectSyntax) -> EvaluatedDimension:
        ...
    def evalUnpackedDimension(self, syntax: VariableDimensionSyntax) -> EvaluatedDimension:
        ...
    def getRandMode(self, symbol: Symbol) -> RandMode:
        ...
    def requireBooleanConvertible(self, expr: Expression) -> bool:
        ...
    def requireGtZero(self, value: int | None, range: SourceRange) -> bool:
        ...
    @typing.overload
    def requireIntegral(self, expr: Expression) -> bool:
        ...
    @typing.overload
    def requireIntegral(self, cv: ConstantValue, range: SourceRange) -> bool:
        ...
    def requireNoUnknowns(self, value: SVInt, range: SourceRange) -> bool:
        ...
    @typing.overload
    def requirePositive(self, value: SVInt, range: SourceRange) -> bool:
        ...
    @typing.overload
    def requirePositive(self, value: int | None, range: SourceRange) -> bool:
        ...
    @typing.overload
    def requireSimpleExpr(self, expr: PropertyExprSyntax) -> ExpressionSyntax:
        ...
    @typing.overload
    def requireSimpleExpr(self, expr: PropertyExprSyntax, code: DiagCode) -> ExpressionSyntax:
        ...
    @typing.overload
    def requireValidBitWidth(self, width: int, range: SourceRange) -> bool:
        ...
    @typing.overload
    def requireValidBitWidth(self, value: SVInt, range: SourceRange) -> int | None:
        ...
    def resetFlags(self, addedFlags: ASTFlags) -> ASTContext:
        ...
    def tryEval(self, expr: Expression) -> ConstantValue:
        ...
    @property
    def flags(self) -> ASTFlags:
        ...
    @property
    def getCompilation(self) -> Compilation:
        ...
    @property
    def getContainingSubroutine(self) -> SubroutineSymbol:
        ...
    @property
    def getDriverKind(self) -> DriverKind:
        ...
    @property
    def getInstance(self) -> InstanceSymbolBase:
        ...
    @property
    def getLocation(self) -> 'LookupLocation':
        ...
    @property
    def getProceduralBlock(self) -> ProceduralBlockSymbol:
        ...
    @property
    def inAlwaysCombLatch(self) -> bool:
        ...
    @property
    def inUnevaluatedBranch(self) -> bool:
        ...
    @property
    def lookupIndex(self) -> SymbolIndex:
        ...
    @property
    def scope(self) -> 'Scope':
        ...
class ASTFlags:
    AllowClockingBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowClockingBlock: 524288>
    AllowCoverageSampleFormal: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowCoverageSampleFormal: 134217728>
    AllowCoverpoint: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowCoverpoint: 268435456>
    AllowDataType: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowDataType: 4>
    AllowInterconnect: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowInterconnect: 8589934592>
    AllowNetType: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowNetType: 536870912>
    AllowTypeReferences: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowTypeReferences: 131072>
    AllowUnboundedLiteral: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowUnboundedLiteral: 2048>
    AllowUnboundedLiteralArithmetic: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AllowUnboundedLiteralArithmetic: 4096>
    AssertionDefaultArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionDefaultArg: 274877906944>
    AssertionDelayOrRepetition: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionDelayOrRepetition: 2097152>
    AssertionExpr: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionExpr: 262144>
    AssertionInstanceArgCheck: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssertionInstanceArgCheck: 1048576>
    AssignmentAllowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssignmentAllowed: 32>
    AssignmentDisallowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.AssignmentDisallowed: 64>
    ConcurrentAssertActionBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ConcurrentAssertActionBlock: 67108864>
    ConfigParam: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ConfigParam: 2199023255552>
    DPIArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.DPIArg: 137438953472>
    EnumInitializer: typing.ClassVar[ASTFlags]  # value = <ASTFlags.EnumInitializer: 8>
    EventExpression: typing.ClassVar[ASTFlags]  # value = <ASTFlags.EventExpression: 65536>
    Final: typing.ClassVar[ASTFlags]  # value = <ASTFlags.Final: 16384>
    ForkJoinAnyNone: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ForkJoinAnyNone: 8796093022208>
    Function: typing.ClassVar[ASTFlags]  # value = <ASTFlags.Function: 8192>
    InsideConcatenation: typing.ClassVar[ASTFlags]  # value = <ASTFlags.InsideConcatenation: 1>
    LAndRValue: typing.ClassVar[ASTFlags]  # value = <ASTFlags.LAndRValue: 549755813888>
    LValue: typing.ClassVar[ASTFlags]  # value = <ASTFlags.LValue: 4194304>
    NoAttributes: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NoAttributes: 16>
    NoReference: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NoReference: 1099511627776>
    NonBlockingTimingControl: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NonBlockingTimingControl: 32768>
    NonProcedural: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NonProcedural: 128>
    None_: typing.ClassVar[ASTFlags]  # value = <ASTFlags.None: 0>
    NotADriver: typing.ClassVar[ASTFlags]  # value = <ASTFlags.NotADriver: 17179869184>
    OutputArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.OutputArg: 1073741824>
    ProceduralAssign: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ProceduralAssign: 2147483648>
    ProceduralForceRelease: typing.ClassVar[ASTFlags]  # value = <ASTFlags.ProceduralForceRelease: 4294967296>
    PropertyNegation: typing.ClassVar[ASTFlags]  # value = <ASTFlags.PropertyNegation: 8388608>
    PropertyTimeAdvance: typing.ClassVar[ASTFlags]  # value = <ASTFlags.PropertyTimeAdvance: 16777216>
    RecursivePropertyArg: typing.ClassVar[ASTFlags]  # value = <ASTFlags.RecursivePropertyArg: 33554432>
    SpecifyBlock: typing.ClassVar[ASTFlags]  # value = <ASTFlags.SpecifyBlock: 68719476736>
    StaticInitializer: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StaticInitializer: 256>
    StreamingAllowed: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StreamingAllowed: 512>
    StreamingWithRange: typing.ClassVar[ASTFlags]  # value = <ASTFlags.StreamingWithRange: 34359738368>
    TopLevelStatement: typing.ClassVar[ASTFlags]  # value = <ASTFlags.TopLevelStatement: 1024>
    TypeOperator: typing.ClassVar[ASTFlags]  # value = <ASTFlags.TypeOperator: 4398046511104>
    UnevaluatedBranch: typing.ClassVar[ASTFlags]  # value = <ASTFlags.UnevaluatedBranch: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AbortAssertionExpr(AssertionExpr):
    class Action:
        Accept: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Accept: 0>
        Reject: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Reject: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Accept: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Accept: 0>
    Reject: typing.ClassVar[AbortAssertionExpr.Action]  # value = <Action.Reject: 1>
    @property
    def action(self) -> AbortAssertionExpr.Action:
        ...
    @property
    def condition(self) -> Expression:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def isSync(self) -> bool:
        ...
class AcceptOnPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    expr: PropertyExprSyntax
    keyword: Token
    openParen: Token
class ActionBlockSyntax(SyntaxNode):
    elseClause: ElseClauseSyntax
    statement: StatementSyntax
class AnonymousProgramSymbol(Symbol, Scope):
    pass
class AnonymousProgramSyntax(MemberSyntax):
    endkeyword: Token
    keyword: Token
    members: SyntaxList[MemberSyntax]
    semi: Token
class AnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[MemberSyntax]
class AnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[UdpPortDeclSyntax]
    semi: Token
class ArbitrarySymbolExpression(Expression):
    @property
    def symbol(self) -> Symbol:
        ...
class ArgumentDirection:
    In: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.In: 0>
    InOut: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.InOut: 2>
    Out: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.Out: 1>
    Ref: typing.ClassVar[ArgumentDirection]  # value = <ArgumentDirection.Ref: 3>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ArgumentListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    parameters: SeparatedSyntaxList[ArgumentSyntax]
class ArgumentSyntax(SyntaxNode):
    pass
class ArrayOrRandomizeMethodExpressionSyntax(ExpressionSyntax):
    args: ParenExpressionListSyntax
    constraints: ConstraintBlockSyntax
    method: ExpressionSyntax
    with_: Token
class AssertionExpr:
    def __repr__(self) -> str:
        ...
    @property
    def admitsEmpty(self) -> bool:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> AssertionExprKind:
        ...
    @property
    def syntax(self) -> SyntaxNode:
        ...
class AssertionExprKind:
    Abort: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Abort: 9>
    Binary: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Binary: 5>
    Case: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Case: 11>
    Clocking: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Clocking: 7>
    Conditional: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Conditional: 10>
    DisableIff: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.DisableIff: 12>
    FirstMatch: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.FirstMatch: 6>
    Invalid: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Invalid: 0>
    SequenceConcat: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.SequenceConcat: 2>
    SequenceWithMatch: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.SequenceWithMatch: 3>
    Simple: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Simple: 1>
    StrongWeak: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.StrongWeak: 8>
    Unary: typing.ClassVar[AssertionExprKind]  # value = <AssertionExprKind.Unary: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AssertionInstanceExpression(Expression):
    @property
    def arguments(self) -> span[tuple[Symbol, Expression | AssertionExpr | TimingControl]]:
        ...
    @property
    def body(self) -> AssertionExpr:
        ...
    @property
    def isRecursiveProperty(self) -> bool:
        ...
    @property
    def localVars(self) -> span[Symbol]:
        ...
    @property
    def symbol(self) -> Symbol:
        ...
class AssertionItemPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[AssertionItemPortSyntax]
class AssertionItemPortSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
    defaultValue: EqualsAssertionArgClauseSyntax
    dimensions: SyntaxList[VariableDimensionSyntax]
    direction: Token
    local: Token
    name: Token
    type: DataTypeSyntax
class AssertionKind:
    Assert: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Assert: 0>
    Assume: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Assume: 1>
    CoverProperty: typing.ClassVar[AssertionKind]  # value = <AssertionKind.CoverProperty: 2>
    CoverSequence: typing.ClassVar[AssertionKind]  # value = <AssertionKind.CoverSequence: 3>
    Expect: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Expect: 5>
    Restrict: typing.ClassVar[AssertionKind]  # value = <AssertionKind.Restrict: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class AssertionPortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection | None:
        ...
    @property
    def isLocalVar(self) -> bool:
        ...
    @property
    def type(self) -> Type:
        ...
class AssignmentExpression(Expression):
    @property
    def isCompound(self) -> bool:
        ...
    @property
    def isLValueArg(self) -> bool:
        ...
    @property
    def isNonBlocking(self) -> bool:
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def op(self) -> BinaryOperator | None:
        ...
    @property
    def right(self) -> Expression:
        ...
    @property
    def timingControl(self) -> TimingControl:
        ...
class AssignmentPatternExpressionBase(Expression):
    @property
    def elements(self) -> span[Expression]:
        ...
class AssignmentPatternExpressionSyntax(PrimaryExpressionSyntax):
    pattern: AssignmentPatternSyntax
    type: DataTypeSyntax
class AssignmentPatternItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    key: ExpressionSyntax
class AssignmentPatternSyntax(SyntaxNode):
    pass
class AssociativeArrayType(Type):
    @property
    def elementType(self) -> Type:
        ...
    @property
    def indexType(self) -> Type:
        ...
class AttributeInstanceSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    specs: SeparatedSyntaxList[AttributeSpecSyntax]
class AttributeSpecSyntax(SyntaxNode):
    name: Token
    value: EqualsValueClauseSyntax
class AttributeSymbol(Symbol):
    @property
    def value(self) -> ConstantValue:
        ...
class BadExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
class Bag:
    compilationOptions: CompilationOptions
    lexerOptions: LexerOptions
    parserOptions: ParserOptions
    preprocessorOptions: PreprocessorOptions
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, list: list) -> None:
        ...
class BeginKeywordsDirectiveSyntax(DirectiveSyntax):
    versionSpecifier: Token
class BinSelectWithFilterExpr(BinsSelectExpr):
    @property
    def expr(self) -> BinsSelectExpr:
        ...
    @property
    def filter(self) -> Expression:
        ...
    @property
    def matchesExpr(self) -> Expression:
        ...
class BinSelectWithFilterExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    filter: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
    openParen: Token
    with_: Token
class BinaryAssertionExpr(AssertionExpr):
    @property
    def left(self) -> AssertionExpr:
        ...
    @property
    def op(self) -> BinaryAssertionOperator:
        ...
    @property
    def right(self) -> AssertionExpr:
        ...
class BinaryAssertionOperator:
    And: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.And: 0>
    Iff: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Iff: 5>
    Implies: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Implies: 10>
    Intersect: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Intersect: 2>
    NonOverlappedFollowedBy: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.NonOverlappedFollowedBy: 14>
    NonOverlappedImplication: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.NonOverlappedImplication: 12>
    Or: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Or: 1>
    OverlappedFollowedBy: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.OverlappedFollowedBy: 13>
    OverlappedImplication: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.OverlappedImplication: 11>
    SUntil: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.SUntil: 7>
    SUntilWith: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.SUntilWith: 9>
    Throughout: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Throughout: 3>
    Until: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Until: 6>
    UntilWith: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.UntilWith: 8>
    Within: typing.ClassVar[BinaryAssertionOperator]  # value = <BinaryAssertionOperator.Within: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinaryBinsSelectExpr(BinsSelectExpr):
    class Op:
        And: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.And: 0>
        Or: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.Or: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    And: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.And: 0>
    Or: typing.ClassVar[BinaryBinsSelectExpr.Op]  # value = <Op.Or: 1>
    @property
    def left(self) -> BinsSelectExpr:
        ...
    @property
    def op(self) -> BinaryBinsSelectExpr.Op:
        ...
    @property
    def right(self) -> BinsSelectExpr:
        ...
class BinaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    left: BinsSelectExpressionSyntax
    op: Token
    right: BinsSelectExpressionSyntax
class BinaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    left: BlockEventExpressionSyntax
    orKeyword: Token
    right: BlockEventExpressionSyntax
class BinaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    left: ConditionalDirectiveExpressionSyntax
    op: Token
    right: ConditionalDirectiveExpressionSyntax
class BinaryEventExpressionSyntax(EventExpressionSyntax):
    left: EventExpressionSyntax
    operatorToken: Token
    right: EventExpressionSyntax
class BinaryExpression(Expression):
    @property
    def left(self) -> Expression:
        ...
    @property
    def op(self) -> BinaryOperator:
        ...
    @property
    def right(self) -> Expression:
        ...
class BinaryExpressionSyntax(ExpressionSyntax):
    attributes: SyntaxList[AttributeInstanceSyntax]
    left: ExpressionSyntax
    operatorToken: Token
    right: ExpressionSyntax
class BinaryOperator:
    Add: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Add: 0>
    ArithmeticShiftLeft: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.ArithmeticShiftLeft: 25>
    ArithmeticShiftRight: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.ArithmeticShiftRight: 26>
    BinaryAnd: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryAnd: 5>
    BinaryOr: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryOr: 6>
    BinaryXnor: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryXnor: 8>
    BinaryXor: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.BinaryXor: 7>
    CaseEquality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.CaseEquality: 11>
    CaseInequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.CaseInequality: 12>
    Divide: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Divide: 3>
    Equality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Equality: 9>
    GreaterThan: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.GreaterThan: 14>
    GreaterThanEqual: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.GreaterThanEqual: 13>
    Inequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Inequality: 10>
    LessThan: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LessThan: 16>
    LessThanEqual: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LessThanEqual: 15>
    LogicalAnd: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalAnd: 19>
    LogicalEquivalence: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalEquivalence: 22>
    LogicalImplication: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalImplication: 21>
    LogicalOr: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalOr: 20>
    LogicalShiftLeft: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalShiftLeft: 23>
    LogicalShiftRight: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.LogicalShiftRight: 24>
    Mod: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Mod: 4>
    Multiply: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Multiply: 2>
    Power: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Power: 27>
    Subtract: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.Subtract: 1>
    WildcardEquality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.WildcardEquality: 17>
    WildcardInequality: typing.ClassVar[BinaryOperator]  # value = <BinaryOperator.WildcardInequality: 18>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinaryPropertyExprSyntax(PropertyExprSyntax):
    left: PropertyExprSyntax
    op: Token
    right: PropertyExprSyntax
class BinarySequenceExprSyntax(SequenceExprSyntax):
    left: SequenceExprSyntax
    op: Token
    right: SequenceExprSyntax
class BindDirectiveSyntax(MemberSyntax):
    bind: Token
    instantiation: MemberSyntax
    target: NameSyntax
    targetInstances: BindTargetListSyntax
class BindTargetListSyntax(SyntaxNode):
    colon: Token
    targets: SeparatedSyntaxList[NameSyntax]
class BinsSelectConditionExprSyntax(BinsSelectExpressionSyntax):
    binsof: Token
    closeParen: Token
    intersects: IntersectClauseSyntax
    name: NameSyntax
    openParen: Token
class BinsSelectExpr:
    def __repr__(self) -> str:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> BinsSelectExprKind:
        ...
    @property
    def syntax(self) -> SyntaxNode:
        ...
class BinsSelectExprKind:
    Binary: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Binary: 3>
    Condition: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Condition: 1>
    CrossId: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.CrossId: 6>
    Invalid: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Invalid: 0>
    SetExpr: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.SetExpr: 4>
    Unary: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.Unary: 2>
    WithFilter: typing.ClassVar[BinsSelectExprKind]  # value = <BinsSelectExprKind.WithFilter: 5>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class BinsSelectExpressionSyntax(SyntaxNode):
    pass
class BinsSelectionSyntax(MemberSyntax):
    equals: Token
    expr: BinsSelectExpressionSyntax
    iff: CoverageIffClauseSyntax
    keyword: Token
    name: Token
    semi: Token
class BitSelectSyntax(SelectorSyntax):
    expr: ExpressionSyntax
class BlockCoverageEventSyntax(SyntaxNode):
    atat: Token
    closeParen: Token
    expr: BlockEventExpressionSyntax
    openParen: Token
class BlockEventExpressionSyntax(SyntaxNode):
    pass
class BlockEventListControl(TimingControl):
    class Event:
        @property
        def isBegin(self) -> bool:
            ...
        @property
        def target(self) -> Symbol:
            ...
    @property
    def events(self) -> span[BlockEventListControl::Event]:
        ...
class BlockStatement(Statement):
    @property
    def blockKind(self) -> StatementBlockKind:
        ...
    @property
    def blockSymbol(self) -> StatementBlockSymbol:
        ...
    @property
    def body(self) -> Statement:
        ...
class BlockStatementSyntax(StatementSyntax):
    begin: Token
    blockName: NamedBlockClauseSyntax
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: SyntaxList[SyntaxNode]
class BreakStatement(Statement):
    pass
class BufferID:
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: BufferID) -> bool:
        ...
    def __ge__(self, arg0: BufferID) -> bool:
        ...
    def __gt__(self, arg0: BufferID) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    def __init__(self) -> None:
        ...
    def __le__(self, arg0: BufferID) -> bool:
        ...
    def __lt__(self, arg0: BufferID) -> bool:
        ...
    def __ne__(self, arg0: BufferID) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def id(self) -> int:
        ...
    @property
    def placeholder() -> BufferID:
        ...
class BumpAllocator:
    def __init__(self) -> None:
        ...
class CHandleType(Type):
    pass
class CallExpression(Expression):
    class IteratorCallInfo:
        @property
        def iterExpr(self) -> Expression:
            ...
        @property
        def iterVar(self) -> ValueSymbol:
            ...
    class RandomizeCallInfo:
        @property
        def constraintRestrictions(self) -> span[str]:
            ...
        @property
        def inlineConstraints(self) -> Constraint:
            ...
    class SystemCallInfo:
        @property
        def extraInfo(self) -> None | CallExpression.IteratorCallInfo | CallExpression.RandomizeCallInfo:
            ...
        @property
        def scope(self) -> 'Scope':
            ...
        @property
        def subroutine(self) -> SystemSubroutine:
            ...
    @property
    def arguments(self) -> span[Expression]:
        ...
    @property
    def isSystemCall(self) -> bool:
        ...
    @property
    def subroutine(self) -> SubroutineSymbol | CallExpression.SystemCallInfo:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def subroutineName(self) -> str:
        ...
    @property
    def thisClass(self) -> Expression:
        ...
class CaseAssertionExpr(AssertionExpr):
    class ItemGroup:
        @property
        def body(self) -> AssertionExpr:
            ...
        @property
        def expressions(self) -> span[Expression]:
            ...
    @property
    def defaultCase(self) -> AssertionExpr:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def items(self) -> span[CaseAssertionExpr::ItemGroup]:
        ...
class CaseGenerateSyntax(MemberSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    endCase: Token
    items: SyntaxList[CaseItemSyntax]
    keyword: Token
    openParen: Token
class CaseItemSyntax(SyntaxNode):
    pass
class CasePropertyExprSyntax(PropertyExprSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: SyntaxList[PropertyCaseItemSyntax]
    openParen: Token
class CaseStatement(Statement):
    class ItemGroup:
        @property
        def expressions(self) -> span[Expression]:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def condition(self) -> CaseStatementCondition:
        ...
    @property
    def defaultCase(self) -> Statement:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def items(self) -> span[CaseStatement::ItemGroup]:
        ...
class CaseStatementCondition:
    Inside: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.Inside: 3>
    Normal: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.Normal: 0>
    WildcardJustZ: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.WildcardJustZ: 2>
    WildcardXOrZ: typing.ClassVar[CaseStatementCondition]  # value = <CaseStatementCondition.WildcardXOrZ: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CaseStatementSyntax(StatementSyntax):
    caseKeyword: Token
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: SyntaxList[CaseItemSyntax]
    matchesOrInside: Token
    openParen: Token
    uniqueOrPriority: Token
class CastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    left: ExpressionSyntax
    right: ParenthesizedExpressionSyntax
class CellConfigRuleSyntax(ConfigRuleSyntax):
    cell: Token
    name: ConfigCellIdentifierSyntax
    ruleClause: ConfigRuleClauseSyntax
    semi: Token
class ChargeStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token
class CheckerDataDeclarationSyntax(MemberSyntax):
    data: DataDeclarationSyntax
    rand: Token
class CheckerDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    members: SyntaxList[MemberSyntax]
    name: Token
    portList: AssertionItemPortListSyntax
    semi: Token
class CheckerInstanceBodySymbol(Symbol, Scope):
    @property
    def checker(self) -> CheckerSymbol:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
    @property
    def parentInstance(self) -> CheckerInstanceSymbol:
        ...
class CheckerInstanceStatementSyntax(StatementSyntax):
    instance: CheckerInstantiationSyntax
class CheckerInstanceSymbol(InstanceSymbolBase):
    class Connection:
        @property
        def actual(self) -> Expression | AssertionExpr | TimingControl:
            ...
        @property
        def attributes(self) -> span[AttributeSymbol]:
            ...
        @property
        def formal(self) -> Symbol:
            ...
        @property
        def outputInitialExpr(self) -> Expression:
            ...
    @property
    def body(self) -> CheckerInstanceBodySymbol:
        ...
    @property
    def portConnections(self) -> span[CheckerInstanceSymbol::Connection]:
        ...
class CheckerInstantiationSyntax(MemberSyntax):
    instances: SeparatedSyntaxList[HierarchicalInstanceSyntax]
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: NameSyntax
class CheckerSymbol(Symbol, Scope):
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class ClassDeclarationSyntax(MemberSyntax):
    classKeyword: Token
    endBlockName: NamedBlockClauseSyntax
    endClass: Token
    extendsClause: ExtendsClauseSyntax
    finalSpecifier: ClassSpecifierSyntax
    implementsClause: ImplementsClauseSyntax
    items: SyntaxList[MemberSyntax]
    name: Token
    parameters: ParameterPortListSyntax
    semi: Token
    virtualOrInterface: Token
class ClassMethodDeclarationSyntax(MemberSyntax):
    declaration: FunctionDeclarationSyntax
    qualifiers: TokenList
class ClassMethodPrototypeSyntax(MemberSyntax):
    prototype: FunctionPrototypeSyntax
    qualifiers: TokenList
    semi: Token
class ClassNameSyntax(NameSyntax):
    identifier: Token
    parameters: ParameterValueAssignmentSyntax
class ClassPropertyDeclarationSyntax(MemberSyntax):
    declaration: MemberSyntax
    qualifiers: TokenList
class ClassPropertySymbol(VariableSymbol):
    @property
    def randMode(self) -> RandMode:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class ClassSpecifierSyntax(SyntaxNode):
    colon: Token
    keyword: Token
class ClassType(Type, Scope):
    @property
    def baseClass(self) -> Type:
        ...
    @property
    def baseConstructorCall(self) -> Expression:
        ...
    @property
    def constructor(self) -> SubroutineSymbol:
        ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def genericClass(self) -> GenericClassDefSymbol:
        ...
    @property
    def implementedInterfaces(self) -> span[Type]:
        ...
    @property
    def isAbstract(self) -> bool:
        ...
    @property
    def isFinal(self) -> bool:
        ...
    @property
    def isInterface(self) -> bool:
        ...
class ClockVarSymbol(VariableSymbol):
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def inputSkew(self) -> ClockingSkew:
        ...
    @property
    def outputSkew(self) -> ClockingSkew:
        ...
class ClockingAssertionExpr(AssertionExpr):
    @property
    def clocking(self) -> TimingControl:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
class ClockingBlockSymbol(Symbol, Scope):
    @property
    def defaultInputSkew(self) -> ClockingSkew:
        ...
    @property
    def defaultOutputSkew(self) -> ClockingSkew:
        ...
    @property
    def event(self) -> TimingControl:
        ...
class ClockingDeclarationSyntax(MemberSyntax):
    at: Token
    blockName: Token
    clocking: Token
    endBlockName: NamedBlockClauseSyntax
    endClocking: Token
    event: EventExpressionSyntax
    globalOrDefault: Token
    items: SyntaxList[MemberSyntax]
    semi: Token
class ClockingDirectionSyntax(SyntaxNode):
    input: Token
    inputSkew: ClockingSkewSyntax
    output: Token
    outputSkew: ClockingSkewSyntax
class ClockingEventExpression(Expression):
    @property
    def timingControl(self) -> TimingControl:
        ...
class ClockingItemSyntax(MemberSyntax):
    decls: SeparatedSyntaxList[AttributeSpecSyntax]
    direction: ClockingDirectionSyntax
    semi: Token
class ClockingPropertyExprSyntax(PropertyExprSyntax):
    event: TimingControlSyntax
    expr: PropertyExprSyntax
class ClockingSequenceExprSyntax(SequenceExprSyntax):
    event: TimingControlSyntax
    expr: SequenceExprSyntax
class ClockingSkew:
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def edge(self) -> EdgeKind:
        ...
    @property
    def hasValue(self) -> bool:
        ...
class ClockingSkewSyntax(SyntaxNode):
    delay: TimingControlSyntax
    edge: Token
class ColonExpressionClauseSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
class CommandLineOptions:
    expandEnvVars: bool
    ignoreDuplicates: bool
    ignoreProgramName: bool
    supportsComments: bool
    def __init__(self) -> None:
        ...
class Compilation:
    class DefinitionLookupResult:
        configRoot: ConfigBlockSymbol
        configRule: ConfigRule
        definition: Symbol
        def __init__(self) -> None:
            ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, options: Bag) -> None:
        ...
    def addDiagnostics(self, diagnostics: Diagnostics) -> None:
        ...
    def addSyntaxTree(self, tree: SyntaxTree) -> None:
        ...
    def addSystemMethod(self, typeKind: SymbolKind, method: SystemSubroutine) -> None:
        ...
    def addSystemSubroutine(self, subroutine: SystemSubroutine) -> None:
        ...
    def createScriptScope(self) -> CompilationUnitSymbol:
        ...
    def getAllDiagnostics(self) -> Diagnostics:
        ...
    @typing.overload
    def getAttributes(self, symbol: Symbol) -> span[AttributeSymbol]:
        ...
    @typing.overload
    def getAttributes(self, stmt: Statement) -> span[AttributeSymbol]:
        ...
    @typing.overload
    def getAttributes(self, expr: Expression) -> span[AttributeSymbol]:
        ...
    @typing.overload
    def getAttributes(self, conn: PortConnection) -> span[AttributeSymbol]:
        ...
    def getCompilationUnit(self, syntax: CompilationUnitSyntax) -> CompilationUnitSymbol:
        ...
    def getCompilationUnits(self) -> span[CompilationUnitSymbol]:
        ...
    def getDefinitions(self) -> list[Symbol]:
        ...
    def getGateType(self, name: str) -> PrimitiveSymbol:
        ...
    def getNetType(self, kind: TokenKind) -> NetType:
        ...
    def getPackage(self, name: str) -> PackageSymbol:
        ...
    def getPackages(self) -> list[PackageSymbol]:
        ...
    def getParseDiagnostics(self) -> Diagnostics:
        ...
    def getRoot(self) -> RootSymbol:
        ...
    def getSemanticDiagnostics(self) -> Diagnostics:
        ...
    def getSourceLibrary(self, name: str) -> SourceLibrary:
        ...
    def getStdPackage(self) -> PackageSymbol:
        ...
    def getSyntaxTrees(self) -> span[SyntaxTree]:
        ...
    def getSystemMethod(self, typeKind: SymbolKind, name: str) -> SystemSubroutine:
        ...
    def getSystemSubroutine(self, name: str) -> SystemSubroutine:
        ...
    def getType(self, kind: SyntaxKind) -> Type:
        ...
    def parseName(self, name: str) -> NameSyntax:
        ...
    def tryGetDefinition(self, name: str, scope: 'Scope') -> Compilation.DefinitionLookupResult:
        ...
    def tryParseName(self, name: str, diags: Diagnostics) -> NameSyntax:
        ...
    @property
    def bitType(self) -> Type:
        ...
    @property
    def byteType(self) -> Type:
        ...
    @property
    def defaultLibrary(self) -> SourceLibrary:
        ...
    @property
    def defaultTimeScale(self) -> TimeScale | None:
        ...
    @property
    def errorType(self) -> Type:
        ...
    @property
    def intType(self) -> Type:
        ...
    @property
    def integerType(self) -> Type:
        ...
    @property
    def isFinalized(self) -> bool:
        ...
    @property
    def logicType(self) -> Type:
        ...
    @property
    def nullType(self) -> Type:
        ...
    @property
    def options(self) -> CompilationOptions:
        ...
    @property
    def realType(self) -> Type:
        ...
    @property
    def shortRealType(self) -> Type:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
    @property
    def stringType(self) -> Type:
        ...
    @property
    def typeRefType(self) -> Type:
        ...
    @property
    def unboundedType(self) -> Type:
        ...
    @property
    def unsignedIntType(self) -> Type:
        ...
    @property
    def voidType(self) -> Type:
        ...
    @property
    def wireNetType(self) -> NetType:
        ...
class CompilationFlags:
    AllowBareValParamAssignment: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowBareValParamAssignment: 2048>
    AllowDupInitialDrivers: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowDupInitialDrivers: 8>
    AllowHierarchicalConst: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowHierarchicalConst: 1>
    AllowMultiDrivenLocals: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowMultiDrivenLocals: 8192>
    AllowRecursiveImplicitCall: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowRecursiveImplicitCall: 1024>
    AllowSelfDeterminedStreamConcat: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowSelfDeterminedStreamConcat: 4096>
    AllowTopLevelIfacePorts: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowTopLevelIfacePorts: 16>
    AllowUseBeforeDeclare: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.AllowUseBeforeDeclare: 4>
    IgnoreUnknownModules: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.IgnoreUnknownModules: 256>
    LintMode: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.LintMode: 64>
    None_: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.None: 0>
    RelaxEnumConversions: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.RelaxEnumConversions: 2>
    RelaxStringConversions: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.RelaxStringConversions: 512>
    StrictDriverChecking: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.StrictDriverChecking: 32>
    SuppressUnused: typing.ClassVar[CompilationFlags]  # value = <CompilationFlags.SuppressUnused: 128>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CompilationOptions:
    defaultLiblist: list[str]
    defaultTimeScale: TimeScale | None
    errorLimit: int
    flags: CompilationFlags
    languageVersion: LanguageVersion
    maxConstexprBacktrace: int
    maxConstexprDepth: int
    maxConstexprSteps: int
    maxDefParamSteps: int
    maxGenerateSteps: int
    maxInstanceArray: int
    maxInstanceDepth: int
    minTypMax: MinTypMax
    paramOverrides: list[str]
    topModules: set[str]
    typoCorrectionLimit: int
    def __init__(self) -> None:
        ...
class CompilationUnitSymbol(Symbol, Scope):
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class CompilationUnitSyntax(SyntaxNode):
    endOfFile: Token
    members: SyntaxList[MemberSyntax]
class ConcatenationExpression(Expression):
    @property
    def operands(self) -> span[Expression]:
        ...
class ConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: SeparatedSyntaxList[ExpressionSyntax]
    openBrace: Token
class ConcurrentAssertionMemberSyntax(MemberSyntax):
    statement: ConcurrentAssertionStatementSyntax
class ConcurrentAssertionStatement(Statement):
    @property
    def assertionKind(self) -> AssertionKind:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
    @property
    def propertySpec(self) -> AssertionExpr:
        ...
class ConcurrentAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    keyword: Token
    openParen: Token
    propertyOrSequence: Token
    propertySpec: PropertySpecSyntax
class ConditionBinsSelectExpr(BinsSelectExpr):
    @property
    def intersects(self) -> span[Expression]:
        ...
    @property
    def target(self) -> Symbol:
        ...
class ConditionalAssertionExpr(AssertionExpr):
    @property
    def condition(self) -> Expression:
        ...
    @property
    def elseExpr(self) -> AssertionExpr:
        ...
    @property
    def ifExpr(self) -> AssertionExpr:
        ...
class ConditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: TokenList
    expr: ConditionalDirectiveExpressionSyntax
class ConditionalConstraint(Constraint):
    @property
    def elseBody(self) -> Constraint:
        ...
    @property
    def ifBody(self) -> Constraint:
        ...
    @property
    def predicate(self) -> Expression:
        ...
class ConditionalConstraintSyntax(ConstraintItemSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    constraints: ConstraintItemSyntax
    elseClause: ElseConstraintClauseSyntax
    ifKeyword: Token
    openParen: Token
class ConditionalDirectiveExpressionSyntax(SyntaxNode):
    pass
class ConditionalExpression(Expression):
    class Condition:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @property
    def conditions(self) -> span[ConditionalExpression::Condition]:
        ...
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
class ConditionalExpressionSyntax(ExpressionSyntax):
    attributes: SyntaxList[AttributeInstanceSyntax]
    colon: Token
    left: ExpressionSyntax
    predicate: ConditionalPredicateSyntax
    question: Token
    right: ExpressionSyntax
class ConditionalPathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    keyword: Token
    openParen: Token
    path: PathDeclarationSyntax
    predicate: ExpressionSyntax
class ConditionalPatternSyntax(SyntaxNode):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
class ConditionalPredicateSyntax(SyntaxNode):
    conditions: SeparatedSyntaxList[ConditionalPatternSyntax]
class ConditionalPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElsePropertyClauseSyntax
    expr: PropertyExprSyntax
    ifKeyword: Token
    openParen: Token
class ConditionalStatement(Statement):
    class Condition:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def conditions(self) -> span[ConditionalStatement::Condition]:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
class ConditionalStatementSyntax(StatementSyntax):
    closeParen: Token
    elseClause: ElseClauseSyntax
    ifKeyword: Token
    openParen: Token
    predicate: ConditionalPredicateSyntax
    statement: StatementSyntax
    uniqueOrPriority: Token
class ConfigBlockSymbol(Symbol, Scope):
    pass
class ConfigCellIdentifierSyntax(SyntaxNode):
    cell: Token
    dot: Token
    library: Token
class ConfigDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    config: Token
    design: Token
    endconfig: Token
    localparams: SyntaxList[ParameterDeclarationStatementSyntax]
    name: Token
    rules: SyntaxList[ConfigRuleSyntax]
    semi1: Token
    semi2: Token
    topCells: SyntaxList[ConfigCellIdentifierSyntax]
class ConfigInstanceIdentifierSyntax(SyntaxNode):
    dot: Token
    name: Token
class ConfigLiblistSyntax(ConfigRuleClauseSyntax):
    liblist: Token
    libraries: TokenList
class ConfigRuleClauseSyntax(SyntaxNode):
    pass
class ConfigRuleSyntax(SyntaxNode):
    pass
class ConfigUseClauseSyntax(ConfigRuleClauseSyntax):
    colon: Token
    config: Token
    name: ConfigCellIdentifierSyntax
    paramAssignments: ParameterValueAssignmentSyntax
    use: Token
class ConstantPattern(Pattern):
    @property
    def expr(self) -> Expression:
        ...
class ConstantRange:
    __hash__: typing.ClassVar[None] = None
    left: int
    right: int
    def __eq__(self, arg0: ConstantRange) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, left: int, right: int) -> None:
        ...
    def __ne__(self, arg0: ConstantRange) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def containsPoint(self, arg0: int) -> bool:
        ...
    def getIndexedRange(self: int, arg0: int, arg1: bool, arg2: bool) -> ConstantRange | None:
        ...
    def overlaps(self, arg0: ConstantRange) -> bool:
        ...
    def reverse(self) -> ConstantRange:
        ...
    def subrange(self, arg0: ConstantRange) -> ConstantRange:
        ...
    def translateIndex(self, arg0: int) -> int:
        ...
    @property
    def isLittleEndian(self) -> bool:
        ...
    @property
    def lower(self) -> int:
        ...
    @property
    def upper(self) -> int:
        ...
    @property
    def width(self) -> int:
        ...
class ConstantValue:
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: ConstantValue) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, integer: SVInt) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    @typing.overload
    def __init__(self, value: float) -> None:
        ...
    def __ne__(self, arg0: ConstantValue) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def bitstreamWidth(self) -> int:
        ...
    def convertToByteArray(self, size: int, isSigned: bool) -> ConstantValue:
        ...
    def convertToByteQueue(self, isSigned: bool) -> ConstantValue:
        ...
    @typing.overload
    def convertToInt(self) -> ConstantValue:
        ...
    @typing.overload
    def convertToInt(self, width: int, isSigned: bool, isFourState: bool) -> ConstantValue:
        ...
    def convertToReal(self) -> ConstantValue:
        ...
    def convertToShortReal(self) -> ConstantValue:
        ...
    def convertToStr(self) -> ConstantValue:
        ...
    def empty(self) -> bool:
        ...
    def getSlice(self, upper: int, lower: int, defaultValue: ConstantValue) -> ConstantValue:
        ...
    def hasUnknown(self) -> bool:
        ...
    def isContainer(self) -> bool:
        ...
    def isFalse(self) -> bool:
        ...
    def isTrue(self) -> bool:
        ...
    def size(self) -> int:
        ...
    @property
    def value(self) -> typing.Any:
        ...
class Constraint:
    def __repr__(self) -> str:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> ConstraintKind:
        ...
    @property
    def syntax(self) -> ConstraintItemSyntax:
        ...
class ConstraintBlockSymbol(Symbol, Scope):
    @property
    def constraints(self) -> Constraint:
        ...
    @property
    def isExplicitExtern(self) -> bool:
        ...
    @property
    def isExtern(self) -> bool:
        ...
    @property
    def isPure(self) -> bool:
        ...
    @property
    def isStatic(self) -> bool:
        ...
    @property
    def thisVar(self) -> VariableSymbol:
        ...
class ConstraintBlockSyntax(ConstraintItemSyntax):
    closeBrace: Token
    items: SyntaxList[ConstraintItemSyntax]
    openBrace: Token
class ConstraintDeclarationSyntax(MemberSyntax):
    block: ConstraintBlockSyntax
    keyword: Token
    name: NameSyntax
    qualifiers: TokenList
class ConstraintItemSyntax(SyntaxNode):
    pass
class ConstraintKind:
    Conditional: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Conditional: 4>
    DisableSoft: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.DisableSoft: 6>
    Expression: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Expression: 2>
    Foreach: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Foreach: 8>
    Implication: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Implication: 3>
    Invalid: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Invalid: 0>
    List: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.List: 1>
    SolveBefore: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.SolveBefore: 7>
    Uniqueness: typing.ClassVar[ConstraintKind]  # value = <ConstraintKind.Uniqueness: 5>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ConstraintList(Constraint):
    @property
    def list(self) -> span[Constraint]:
        ...
class ConstraintPrototypeSyntax(MemberSyntax):
    keyword: Token
    name: NameSyntax
    qualifiers: TokenList
    semi: Token
class ContinueStatement(Statement):
    pass
class ContinuousAssignSymbol(Symbol):
    @property
    def assignment(self) -> Expression:
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[DriveStrength | None, DriveStrength | None]:
        ...
class ContinuousAssignSyntax(MemberSyntax):
    assign: Token
    assignments: SeparatedSyntaxList[ExpressionSyntax]
    delay: TimingControlSyntax
    semi: Token
    strength: DriveStrengthSyntax
class ConversionExpression(Expression):
    @property
    def conversionKind(self) -> ConversionKind:
        ...
    @property
    def isImplicit(self) -> bool:
        ...
    @property
    def operand(self) -> Expression:
        ...
class ConversionKind:
    BitstreamCast: typing.ClassVar[ConversionKind]  # value = <ConversionKind.BitstreamCast: 4>
    Explicit: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Explicit: 3>
    Implicit: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Implicit: 0>
    Propagated: typing.ClassVar[ConversionKind]  # value = <ConversionKind.Propagated: 1>
    StreamingConcat: typing.ClassVar[ConversionKind]  # value = <ConversionKind.StreamingConcat: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class CopyClassExpression(Expression):
    @property
    def sourceExpr(self) -> Expression:
        ...
class CopyClassExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    scopedNew: NameSyntax
class CoverCrossBodySymbol(Symbol, Scope):
    @property
    def crossQueueType(self) -> Type:
        ...
class CoverCrossSymbol(Symbol, Scope):
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
    @property
    def targets(self) -> span[CoverpointSymbol]:
        ...
class CoverCrossSyntax(MemberSyntax):
    closeBrace: Token
    cross: Token
    emptySemi: Token
    iff: CoverageIffClauseSyntax
    items: SeparatedSyntaxList[IdentifierNameSyntax]
    label: NamedLabelSyntax
    members: SyntaxList[MemberSyntax]
    openBrace: Token
class CoverageBinInitializerSyntax(SyntaxNode):
    pass
class CoverageBinSymbol(Symbol):
    class BinKind:
        Bins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.Bins: 0>
        IgnoreBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IgnoreBins: 2>
        IllegalBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IllegalBins: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class TransRangeList:
        class RepeatKind:
            Consecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Consecutive: 1>
            GoTo: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.GoTo: 3>
            Nonconsecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Nonconsecutive: 2>
            None_: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.None: 0>
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __init__(self, value: int) -> None:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def __doc__(self) -> str:
                ...
            @property
            def __members__(self) -> dict:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        Consecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Consecutive: 1>
        GoTo: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.GoTo: 3>
        Nonconsecutive: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.Nonconsecutive: 2>
        None_: typing.ClassVar[CoverageBinSymbol.TransRangeList.RepeatKind]  # value = <RepeatKind.None: 0>
        @property
        def items(self) -> span[Expression]:
            ...
        @property
        def repeatFrom(self) -> Expression:
            ...
        @property
        def repeatKind(self) -> CoverageBinSymbol.TransRangeList.RepeatKind:
            ...
        @property
        def repeatTo(self) -> Expression:
            ...
    Bins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.Bins: 0>
    IgnoreBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IgnoreBins: 2>
    IllegalBins: typing.ClassVar[CoverageBinSymbol.BinKind]  # value = <BinKind.IllegalBins: 1>
    @property
    def binsKind(self) -> CoverageBinSymbol.BinKind:
        ...
    @property
    def crossSelectExpr(self) -> BinsSelectExpr:
        ...
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def isArray(self) -> bool:
        ...
    @property
    def isDefault(self) -> bool:
        ...
    @property
    def isDefaultSequence(self) -> bool:
        ...
    @property
    def isWildcard(self) -> bool:
        ...
    @property
    def numberOfBinsExpr(self) -> Expression:
        ...
    @property
    def setCoverageExpr(self) -> Expression:
        ...
    @property
    def values(self) -> span[Expression]:
        ...
    @property
    def withExpr(self) -> Expression:
        ...
class CoverageBinsArraySizeSyntax(SyntaxNode):
    closeBracket: Token
    expr: ExpressionSyntax
    openBracket: Token
class CoverageBinsSyntax(MemberSyntax):
    equals: Token
    iff: CoverageIffClauseSyntax
    initializer: CoverageBinInitializerSyntax
    keyword: Token
    name: Token
    semi: Token
    size: CoverageBinsArraySizeSyntax
    wildcard: Token
class CoverageIffClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token
class CoverageOptionSetter:
    @property
    def expression(self) -> Expression:
        ...
    @property
    def isTypeOption(self) -> bool:
        ...
    @property
    def name(self) -> str:
        ...
class CoverageOptionSyntax(MemberSyntax):
    expr: ExpressionSyntax
    semi: Token
class CovergroupBodySymbol(Symbol, Scope):
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
class CovergroupDeclarationSyntax(MemberSyntax):
    covergroup: Token
    endBlockName: NamedBlockClauseSyntax
    endgroup: Token
    event: SyntaxNode
    members: SyntaxList[MemberSyntax]
    name: Token
    portList: FunctionPortListSyntax
    semi: Token
class CovergroupType(Type, Scope):
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def body(self) -> CovergroupBodySymbol:
        ...
    @property
    def coverageEvent(self) -> TimingControl:
        ...
    @property
    def sampleArguments(self) -> span[FormalArgumentSymbol]:
        ...
class CoverpointSymbol(Symbol, Scope):
    @property
    def coverageExpr(self) -> Expression:
        ...
    @property
    def iffExpr(self) -> Expression:
        ...
    @property
    def options(self) -> span[CoverageOptionSetter]:
        ...
    @property
    def type(self) -> Type:
        ...
class CoverpointSyntax(MemberSyntax):
    closeBrace: Token
    coverpoint: Token
    emptySemi: Token
    expr: ExpressionSyntax
    iff: CoverageIffClauseSyntax
    label: NamedLabelSyntax
    members: SyntaxList[MemberSyntax]
    openBrace: Token
    type: DataTypeSyntax
class CrossIdBinsSelectExpr(BinsSelectExpr):
    pass
class CycleDelayControl(TimingControl):
    @property
    def expr(self) -> Expression:
        ...
class DPIExportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    functionOrTask: Token
    keyword: Token
    name: Token
    semi: Token
    specString: Token
class DPIImportSyntax(MemberSyntax):
    c_identifier: Token
    equals: Token
    keyword: Token
    method: FunctionPrototypeSyntax
    property: Token
    semi: Token
    specString: Token
class DPIOpenArrayType(Type):
    @property
    def elementType(self) -> Type:
        ...
    @property
    def isPacked(self) -> bool:
        ...
class DataDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    modifiers: TokenList
    semi: Token
    type: DataTypeSyntax
class DataTypeExpression(Expression):
    pass
class DataTypeSyntax(ExpressionSyntax):
    pass
class DeclaratorSyntax(SyntaxNode):
    dimensions: SyntaxList[VariableDimensionSyntax]
    initializer: EqualsValueClauseSyntax
    name: Token
class DeclaredType:
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def initializerLocation(self) -> SourceLocation:
        ...
    @property
    def initializerSyntax(self) -> ExpressionSyntax:
        ...
    @property
    def isEvaluating(self) -> bool:
        ...
    @property
    def type(self) -> Type:
        ...
    @property
    def typeSyntax(self) -> DataTypeSyntax:
        ...
class DefParamAssignmentSyntax(SyntaxNode):
    name: NameSyntax
    setter: EqualsValueClauseSyntax
class DefParamSymbol(Symbol):
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def target(self) -> Symbol:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class DefParamSyntax(MemberSyntax):
    assignments: SeparatedSyntaxList[DefParamAssignmentSyntax]
    defparam: Token
    semi: Token
class DefaultCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    defaultKeyword: Token
class DefaultClockingReferenceSyntax(MemberSyntax):
    clocking: Token
    defaultKeyword: Token
    name: Token
    semi: Token
class DefaultConfigRuleSyntax(ConfigRuleSyntax):
    defaultKeyword: Token
    liblist: ConfigLiblistSyntax
    semi: Token
class DefaultCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    defaultKeyword: Token
    sequenceKeyword: Token
class DefaultDisableDeclarationSyntax(MemberSyntax):
    defaultKeyword: Token
    disableKeyword: Token
    expr: ExpressionSyntax
    iffKeyword: Token
    semi: Token
class DefaultExtendsClauseArgSyntax(SyntaxNode):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token
class DefaultFunctionPortSyntax(FunctionPortBaseSyntax):
    keyword: Token
class DefaultNetTypeDirectiveSyntax(DirectiveSyntax):
    netType: Token
class DefaultPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    expr: PropertyExprSyntax
    semi: Token
class DefaultRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    defaultKeyword: Token
    item: RsProdItemSyntax
    semi: Token
class DefaultSkewItemSyntax(MemberSyntax):
    direction: ClockingDirectionSyntax
    keyword: Token
    semi: Token
class DeferredAssertionSyntax(SyntaxNode):
    finalKeyword: Token
    hash: Token
    zero: Token
class DefineDirectiveSyntax(DirectiveSyntax):
    body: TokenList
    formalArguments: MacroFormalArgumentListSyntax
    name: Token
class DefinitionKind:
    Interface: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Interface: 1>
    Module: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Module: 0>
    Program: typing.ClassVar[DefinitionKind]  # value = <DefinitionKind.Program: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DefinitionSymbol(Symbol):
    def __repr__(self) -> str:
        ...
    def getArticleKindString(self) -> str:
        ...
    def getKindString(self) -> str:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def defaultNetType(self) -> NetType:
        ...
    @property
    def definitionKind(self) -> DefinitionKind:
        ...
    @property
    def isInstantiated(self) -> bool:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
    @property
    def unconnectedDrive(self) -> UnconnectedDrive:
        ...
class Delay3Control(TimingControl):
    @property
    def expr1(self) -> Expression:
        ...
    @property
    def expr2(self) -> Expression:
        ...
    @property
    def expr3(self) -> Expression:
        ...
class Delay3Syntax(TimingControlSyntax):
    closeParen: Token
    comma1: Token
    comma2: Token
    delay1: ExpressionSyntax
    delay2: ExpressionSyntax
    delay3: ExpressionSyntax
    hash: Token
    openParen: Token
class DelayControl(TimingControl):
    @property
    def expr(self) -> Expression:
        ...
class DelaySyntax(TimingControlSyntax):
    delayValue: ExpressionSyntax
    hash: Token
class DelayedSequenceElementSyntax(SyntaxNode):
    closeBracket: Token
    delayVal: ExpressionSyntax
    doubleHash: Token
    expr: SequenceExprSyntax
    op: Token
    openBracket: Token
    range: SelectorSyntax
class DelayedSequenceExprSyntax(SequenceExprSyntax):
    elements: SyntaxList[DelayedSequenceElementSyntax]
    first: SequenceExprSyntax
class DiagCode:
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: DiagCode) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, subsystem: DiagSubsystem, code: int) -> None:
        ...
    def __ne__(self, arg0: DiagCode) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def getCode(self) -> int:
        ...
    def getSubsystem(self) -> DiagSubsystem:
        ...
class DiagGroup:
    def __init__(self, name: str, diags: list[DiagCode]) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def getDiags(self) -> span[DiagCode]:
        ...
    def getName(self) -> str:
        ...
class DiagSubsystem:
    Compilation: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Compilation: 13>
    ConstEval: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.ConstEval: 12>
    Declarations: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Declarations: 6>
    Expressions: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Expressions: 7>
    General: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.General: 1>
    Invalid: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Invalid: 0>
    Lexer: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Lexer: 2>
    Lookup: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Lookup: 10>
    Meta: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Meta: 14>
    Netlist: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Netlist: 16>
    Numeric: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Numeric: 3>
    Parser: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Parser: 5>
    Preprocessor: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Preprocessor: 4>
    Statements: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Statements: 8>
    SysFuncs: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.SysFuncs: 11>
    Tidy: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Tidy: 15>
    Types: typing.ClassVar[DiagSubsystem]  # value = <DiagSubsystem.Types: 9>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Diagnostic:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: Diagnostic) -> bool:
        ...
    def __init__(self, code: DiagCode, location: SourceLocation) -> None:
        ...
    def __ne__(self, arg0: Diagnostic) -> bool:
        ...
    def isError(self) -> bool:
        ...
    @property
    def args(self) -> list[str | int | int | str | ConstantValue | tuple[int, ...]]:
        ...
    @property
    def code(self) -> DiagCode:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def ranges(self) -> list[SourceRange]:
        ...
    @property
    def symbol(self) -> Symbol:
        ...
class DiagnosticClient:
    def report(self, diagnostic: ReportedDiagnostic) -> None:
        ...
    def setEngine(self, engine: DiagnosticEngine) -> None:
        ...
class DiagnosticEngine:
    @staticmethod
    def reportAll(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __init__(self, sourceManager: SourceManager) -> None:
        ...
    def addClient(self, client: DiagnosticClient) -> None:
        ...
    def clearClients(self) -> None:
        ...
    def clearCounts(self) -> None:
        ...
    @typing.overload
    def clearMappings(self) -> None:
        ...
    @typing.overload
    def clearMappings(self, severity: DiagnosticSeverity) -> None:
        ...
    def findDiagGroup(self, name: str) -> DiagGroup:
        ...
    def findFromOptionName(self, optionName: str) -> span[DiagCode]:
        ...
    def formatMessage(self, diag: Diagnostic) -> str:
        ...
    def getMessage(self, code: DiagCode) -> str:
        ...
    def getOptionName(self, code: DiagCode) -> str:
        ...
    def getSeverity(self, code: DiagCode, location: SourceLocation) -> DiagnosticSeverity:
        ...
    def issue(self, diagnostic: Diagnostic) -> None:
        ...
    def setDefaultWarnings(self) -> None:
        ...
    def setErrorLimit(self, limit: int) -> None:
        ...
    def setErrorsAsFatal(self, set: bool) -> None:
        ...
    def setFatalsAsErrors(self, set: bool) -> None:
        ...
    def setIgnoreAllNotes(self, set: bool) -> None:
        ...
    def setIgnoreAllWarnings(self, set: bool) -> None:
        ...
    @typing.overload
    def setMappingsFromPragmas(self) -> Diagnostics:
        ...
    @typing.overload
    def setMappingsFromPragmas(self, buffer: BufferID) -> Diagnostics:
        ...
    def setMessage(self, code: DiagCode, message: str) -> None:
        ...
    @typing.overload
    def setSeverity(self, code: DiagCode, severity: DiagnosticSeverity) -> None:
        ...
    @typing.overload
    def setSeverity(self, group: DiagGroup, severity: DiagnosticSeverity) -> None:
        ...
    def setWarningOptions(self, options: span[str]) -> Diagnostics:
        ...
    def setWarningsAsErrors(self, set: bool) -> None:
        ...
    @property
    def numErrors(self) -> int:
        ...
    @property
    def numWarnings(self) -> int:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
class DiagnosticSeverity:
    Error: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Error: 3>
    Fatal: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Fatal: 4>
    Ignored: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Ignored: 0>
    Note: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Note: 1>
    Warning: typing.ClassVar[DiagnosticSeverity]  # value = <DiagnosticSeverity.Warning: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Diagnostics:
    def __getitem__(self, arg0: int) -> Diagnostic:
        ...
    def __init__(self) -> None:
        ...
    def __iter__(self) -> typing.Iterator[Diagnostic]:
        ...
    def __len__(self) -> int:
        ...
    @typing.overload
    def add(self, code: DiagCode, location: SourceLocation) -> Diagnostic:
        ...
    @typing.overload
    def add(self, code: DiagCode, range: SourceRange) -> Diagnostic:
        ...
    @typing.overload
    def add(self, source: Symbol, code: DiagCode, location: SourceLocation) -> Diagnostic:
        ...
    @typing.overload
    def add(self, source: Symbol, code: DiagCode, range: SourceRange) -> Diagnostic:
        ...
    def sort(self, sourceManager: SourceManager) -> None:
        ...
class Diags:
    @property
    def AlwaysFFEventControl(self) -> DiagCode:
        ...
    @property
    def AlwaysInChecker(self) -> DiagCode:
        ...
    @property
    def AmbiguousWildcardImport(self) -> DiagCode:
        ...
    @property
    def AnsiIfacePortDefault(self) -> DiagCode:
        ...
    @property
    def ArgCannotBeEmpty(self) -> DiagCode:
        ...
    @property
    def ArgDoesNotExist(self) -> DiagCode:
        ...
    @property
    def ArrayDimTooLarge(self) -> DiagCode:
        ...
    @property
    def ArrayLocatorWithClause(self) -> DiagCode:
        ...
    @property
    def ArrayMethodComparable(self) -> DiagCode:
        ...
    @property
    def ArrayMethodIntegral(self) -> DiagCode:
        ...
    @property
    def AssertionArgNeedsRegExpr(self) -> DiagCode:
        ...
    @property
    def AssertionArgTypeMismatch(self) -> DiagCode:
        ...
    @property
    def AssertionArgTypeSequence(self) -> DiagCode:
        ...
    @property
    def AssertionDelayFormalType(self) -> DiagCode:
        ...
    @property
    def AssertionExprType(self) -> DiagCode:
        ...
    @property
    def AssertionFuncArg(self) -> DiagCode:
        ...
    @property
    def AssertionOutputLocalVar(self) -> DiagCode:
        ...
    @property
    def AssertionPortDirNoLocal(self) -> DiagCode:
        ...
    @property
    def AssertionPortOutputDefault(self) -> DiagCode:
        ...
    @property
    def AssertionPortPropOutput(self) -> DiagCode:
        ...
    @property
    def AssertionPortRef(self) -> DiagCode:
        ...
    @property
    def AssertionPortTypedLValue(self) -> DiagCode:
        ...
    @property
    def AssignToCHandle(self) -> DiagCode:
        ...
    @property
    def AssignToNet(self) -> DiagCode:
        ...
    @property
    def AssignedToLocalBodyParam(self) -> DiagCode:
        ...
    @property
    def AssignedToLocalPortParam(self) -> DiagCode:
        ...
    @property
    def AssignmentNotAllowed(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternAssociativeType(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternDynamicDefault(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternDynamicType(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternKeyDupDefault(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternKeyDupName(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternKeyDupValue(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternKeyExpr(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternLValueDynamic(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternMissingElements(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternNoContext(self) -> DiagCode:
        ...
    @property
    def AssignmentPatternNoMember(self) -> DiagCode:
        ...
    @property
    def AssignmentRequiresParens(self) -> DiagCode:
        ...
    @property
    def AssignmentToConstVar(self) -> DiagCode:
        ...
    @property
    def AssociativeWildcardNotAllowed(self) -> DiagCode:
        ...
    @property
    def AttributesNotAllowed(self) -> DiagCode:
        ...
    @property
    def AutoFromNonBlockingTiming(self) -> DiagCode:
        ...
    @property
    def AutoFromNonProcedural(self) -> DiagCode:
        ...
    @property
    def AutoFromStaticInit(self) -> DiagCode:
        ...
    @property
    def AutoVarToRefStatic(self) -> DiagCode:
        ...
    @property
    def AutoVarTraced(self) -> DiagCode:
        ...
    @property
    def AutoVariableHierarchical(self) -> DiagCode:
        ...
    @property
    def AutomaticNotAllowed(self) -> DiagCode:
        ...
    @property
    def BadAssignment(self) -> DiagCode:
        ...
    @property
    def BadAssignmentPatternType(self) -> DiagCode:
        ...
    @property
    def BadBinaryDigit(self) -> DiagCode:
        ...
    @property
    def BadBinaryExpression(self) -> DiagCode:
        ...
    @property
    def BadCastType(self) -> DiagCode:
        ...
    @property
    def BadConcatExpression(self) -> DiagCode:
        ...
    @property
    def BadConditionalExpression(self) -> DiagCode:
        ...
    @property
    def BadConversion(self) -> DiagCode:
        ...
    @property
    def BadDecimalDigit(self) -> DiagCode:
        ...
    @property
    def BadDisableSoft(self) -> DiagCode:
        ...
    @property
    def BadFinishNum(self) -> DiagCode:
        ...
    @property
    def BadForceNetType(self) -> DiagCode:
        ...
    @property
    def BadHexDigit(self) -> DiagCode:
        ...
    @property
    def BadIndexExpression(self) -> DiagCode:
        ...
    @property
    def BadInstanceArrayRange(self) -> DiagCode:
        ...
    @property
    def BadIntegerCast(self) -> DiagCode:
        ...
    @property
    def BadOctalDigit(self) -> DiagCode:
        ...
    @property
    def BadProceduralAssign(self) -> DiagCode:
        ...
    @property
    def BadProceduralForce(self) -> DiagCode:
        ...
    @property
    def BadReplicationExpression(self) -> DiagCode:
        ...
    @property
    def BadSetMembershipType(self) -> DiagCode:
        ...
    @property
    def BadSliceType(self) -> DiagCode:
        ...
    @property
    def BadSolveBefore(self) -> DiagCode:
        ...
    @property
    def BadStreamCast(self) -> DiagCode:
        ...
    @property
    def BadStreamContext(self) -> DiagCode:
        ...
    @property
    def BadStreamExprType(self) -> DiagCode:
        ...
    @property
    def BadStreamSize(self) -> DiagCode:
        ...
    @property
    def BadStreamSlice(self) -> DiagCode:
        ...
    @property
    def BadStreamSourceType(self) -> DiagCode:
        ...
    @property
    def BadStreamTargetType(self) -> DiagCode:
        ...
    @property
    def BadStreamWithOrder(self) -> DiagCode:
        ...
    @property
    def BadStreamWithType(self) -> DiagCode:
        ...
    @property
    def BadSystemSubroutineArg(self) -> DiagCode:
        ...
    @property
    def BadTypeParamExpr(self) -> DiagCode:
        ...
    @property
    def BadUnaryExpression(self) -> DiagCode:
        ...
    @property
    def BadValueRange(self) -> DiagCode:
        ...
    @property
    def BaseConstructorDuplicate(self) -> DiagCode:
        ...
    @property
    def BaseConstructorNotCalled(self) -> DiagCode:
        ...
    @property
    def BindDirectiveInvalidName(self) -> DiagCode:
        ...
    @property
    def BindTargetPrimitive(self) -> DiagCode:
        ...
    @property
    def BindTypeParamMismatch(self) -> DiagCode:
        ...
    @property
    def BindTypeParamNotFound(self) -> DiagCode:
        ...
    @property
    def BindUnderBind(self) -> DiagCode:
        ...
    @property
    def BlockingAssignToFreeVar(self) -> DiagCode:
        ...
    @property
    def BlockingInAlwaysFF(self) -> DiagCode:
        ...
    @property
    def BodyForPure(self) -> DiagCode:
        ...
    @property
    def BodyForPureConstraint(self) -> DiagCode:
        ...
    @property
    def BodyParamNoInitializer(self) -> DiagCode:
        ...
    @property
    def CHandleInAssertion(self) -> DiagCode:
        ...
    @property
    def CannotCompareTwoInstances(self) -> DiagCode:
        ...
    @property
    def CannotDeclareType(self) -> DiagCode:
        ...
    @property
    def CannotIndexScalar(self) -> DiagCode:
        ...
    @property
    def CantDeclarePortSigned(self) -> DiagCode:
        ...
    @property
    def CantModifyConst(self) -> DiagCode:
        ...
    @property
    def CaseGenerateDup(self) -> DiagCode:
        ...
    @property
    def CaseGenerateEmpty(self) -> DiagCode:
        ...
    @property
    def CaseGenerateNoBlock(self) -> DiagCode:
        ...
    @property
    def CaseInsideKeyword(self) -> DiagCode:
        ...
    @property
    def CaseStatementEmpty(self) -> DiagCode:
        ...
    @property
    def ChainedMethodParens(self) -> DiagCode:
        ...
    @property
    def ChargeWithTriReg(self) -> DiagCode:
        ...
    @property
    def CheckerArgCannotBeEmpty(self) -> DiagCode:
        ...
    @property
    def CheckerBlockingAssign(self) -> DiagCode:
        ...
    @property
    def CheckerClassBadInstantiation(self) -> DiagCode:
        ...
    @property
    def CheckerFuncArg(self) -> DiagCode:
        ...
    @property
    def CheckerFuncBadInstantiation(self) -> DiagCode:
        ...
    @property
    def CheckerHierarchical(self) -> DiagCode:
        ...
    @property
    def CheckerInCheckerProc(self) -> DiagCode:
        ...
    @property
    def CheckerInForkJoin(self) -> DiagCode:
        ...
    @property
    def CheckerOutputBadType(self) -> DiagCode:
        ...
    @property
    def CheckerParameterAssign(self) -> DiagCode:
        ...
    @property
    def CheckerPortDirectionType(self) -> DiagCode:
        ...
    @property
    def CheckerPortInout(self) -> DiagCode:
        ...
    @property
    def CheckerTimingControl(self) -> DiagCode:
        ...
    @property
    def ClassInheritanceCycle(self) -> DiagCode:
        ...
    @property
    def ClassMemberInAssertion(self) -> DiagCode:
        ...
    @property
    def ClassPrivateMembersBitstream(self) -> DiagCode:
        ...
    @property
    def ClassSpecifierConflict(self) -> DiagCode:
        ...
    @property
    def ClockVarAssignConcat(self) -> DiagCode:
        ...
    @property
    def ClockVarBadTiming(self) -> DiagCode:
        ...
    @property
    def ClockVarOutputRead(self) -> DiagCode:
        ...
    @property
    def ClockVarSyncDrive(self) -> DiagCode:
        ...
    @property
    def ClockVarTargetAssign(self) -> DiagCode:
        ...
    @property
    def ClockingBlockEventEdge(self) -> DiagCode:
        ...
    @property
    def ClockingNameEmpty(self) -> DiagCode:
        ...
    @property
    def CompilationUnitFromPackage(self) -> DiagCode:
        ...
    @property
    def ConcatWithStringInt(self) -> DiagCode:
        ...
    @property
    def ConcurrentAssertActionBlock(self) -> DiagCode:
        ...
    @property
    def ConfigDupTop(self) -> DiagCode:
        ...
    @property
    def ConfigInstanceUnderOtherConfig(self) -> DiagCode:
        ...
    @property
    def ConfigInstanceWrongTop(self) -> DiagCode:
        ...
    @property
    def ConfigMissingName(self) -> DiagCode:
        ...
    @property
    def ConfigOverrideTop(self) -> DiagCode:
        ...
    @property
    def ConfigParamLiteral(self) -> DiagCode:
        ...
    @property
    def ConfigParamsForPrimitive(self) -> DiagCode:
        ...
    @property
    def ConfigParamsIgnored(self) -> DiagCode:
        ...
    @property
    def ConfigParamsOrdered(self) -> DiagCode:
        ...
    @property
    def ConfigSpecificCellLiblist(self) -> DiagCode:
        ...
    @property
    def ConstEvalAssertionFailed(self) -> DiagCode:
        ...
    @property
    def ConstEvalAssociativeElementNotFound(self) -> DiagCode:
        ...
    @property
    def ConstEvalAssociativeIndexInvalid(self) -> DiagCode:
        ...
    @property
    def ConstEvalBitstreamCastSize(self) -> DiagCode:
        ...
    @property
    def ConstEvalCaseItemsNotUnique(self) -> DiagCode:
        ...
    @property
    def ConstEvalCheckers(self) -> DiagCode:
        ...
    @property
    def ConstEvalClassType(self) -> DiagCode:
        ...
    @property
    def ConstEvalCovergroupType(self) -> DiagCode:
        ...
    @property
    def ConstEvalDPINotConstant(self) -> DiagCode:
        ...
    @property
    def ConstEvalDisableTarget(self) -> DiagCode:
        ...
    @property
    def ConstEvalDynamicArrayIndex(self) -> DiagCode:
        ...
    @property
    def ConstEvalDynamicArrayRange(self) -> DiagCode:
        ...
    @property
    def ConstEvalDynamicToFixedSize(self) -> DiagCode:
        ...
    @property
    def ConstEvalEmptyQueue(self) -> DiagCode:
        ...
    @property
    def ConstEvalExceededMaxCallDepth(self) -> DiagCode:
        ...
    @property
    def ConstEvalExceededMaxSteps(self) -> DiagCode:
        ...
    @property
    def ConstEvalFunctionArgDirection(self) -> DiagCode:
        ...
    @property
    def ConstEvalFunctionIdentifiersMustBeLocal(self) -> DiagCode:
        ...
    @property
    def ConstEvalFunctionInsideGenerate(self) -> DiagCode:
        ...
    @property
    def ConstEvalHierarchicalName(self) -> DiagCode:
        ...
    @property
    def ConstEvalIdUsedInCEBeforeDecl(self) -> DiagCode:
        ...
    @property
    def ConstEvalIfItemsNotUnique(self) -> DiagCode:
        ...
    @property
    def ConstEvalMethodNotConstant(self) -> DiagCode:
        ...
    @property
    def ConstEvalNoCaseItemsMatched(self) -> DiagCode:
        ...
    @property
    def ConstEvalNoIfItemsMatched(self) -> DiagCode:
        ...
    @property
    def ConstEvalNonConstVariable(self) -> DiagCode:
        ...
    @property
    def ConstEvalParallelBlockNotConst(self) -> DiagCode:
        ...
    @property
    def ConstEvalParamCycle(self) -> DiagCode:
        ...
    @property
    def ConstEvalProceduralAssign(self) -> DiagCode:
        ...
    @property
    def ConstEvalQueueRange(self) -> DiagCode:
        ...
    @property
    def ConstEvalRandValue(self) -> DiagCode:
        ...
    @property
    def ConstEvalReplicationCountInvalid(self) -> DiagCode:
        ...
    @property
    def ConstEvalStaticSkipped(self) -> DiagCode:
        ...
    @property
    def ConstEvalSubroutineNotConstant(self) -> DiagCode:
        ...
    @property
    def ConstEvalTaggedUnion(self) -> DiagCode:
        ...
    @property
    def ConstEvalTaskNotConstant(self) -> DiagCode:
        ...
    @property
    def ConstEvalTimedStmtNotConst(self) -> DiagCode:
        ...
    @property
    def ConstEvalVoidNotConstant(self) -> DiagCode:
        ...
    @property
    def ConstFunctionPortRequiresRef(self) -> DiagCode:
        ...
    @property
    def ConstPortNotAllowed(self) -> DiagCode:
        ...
    @property
    def ConstSysTaskIgnored(self) -> DiagCode:
        ...
    @property
    def ConstVarNoInitializer(self) -> DiagCode:
        ...
    @property
    def ConstVarToRef(self) -> DiagCode:
        ...
    @property
    def ConstantConversion(self) -> DiagCode:
        ...
    @property
    def ConstraintNotInClass(self) -> DiagCode:
        ...
    @property
    def ConstraintQualOutOfBlock(self) -> DiagCode:
        ...
    @property
    def ConstructorOutsideClass(self) -> DiagCode:
        ...
    @property
    def ConstructorReturnType(self) -> DiagCode:
        ...
    @property
    def CopyClassTarget(self) -> DiagCode:
        ...
    @property
    def CouldNotOpenIncludeFile(self) -> DiagCode:
        ...
    @property
    def CouldNotResolveHierarchicalPath(self) -> DiagCode:
        ...
    @property
    def CoverCrossItems(self) -> DiagCode:
        ...
    @property
    def CoverOptionImmutable(self) -> DiagCode:
        ...
    @property
    def CoverStmtNoFail(self) -> DiagCode:
        ...
    @property
    def CoverageBinDefSeqSize(self) -> DiagCode:
        ...
    @property
    def CoverageBinDefaultIgnore(self) -> DiagCode:
        ...
    @property
    def CoverageBinDefaultWildcard(self) -> DiagCode:
        ...
    @property
    def CoverageBinTargetName(self) -> DiagCode:
        ...
    @property
    def CoverageBinTransSize(self) -> DiagCode:
        ...
    @property
    def CoverageExprVar(self) -> DiagCode:
        ...
    @property
    def CoverageOptionDup(self) -> DiagCode:
        ...
    @property
    def CoverageSampleFormal(self) -> DiagCode:
        ...
    @property
    def CoverageSetType(self) -> DiagCode:
        ...
    @property
    def CovergroupOutArg(self) -> DiagCode:
        ...
    @property
    def CycleDelayNonClock(self) -> DiagCode:
        ...
    @property
    def DPIExportDifferentScope(self) -> DiagCode:
        ...
    @property
    def DPIExportDuplicate(self) -> DiagCode:
        ...
    @property
    def DPIExportDuplicateCId(self) -> DiagCode:
        ...
    @property
    def DPIExportImportedFunc(self) -> DiagCode:
        ...
    @property
    def DPIExportKindMismatch(self) -> DiagCode:
        ...
    @property
    def DPIPureArg(self) -> DiagCode:
        ...
    @property
    def DPIPureReturn(self) -> DiagCode:
        ...
    @property
    def DPIPureTask(self) -> DiagCode:
        ...
    @property
    def DPIRefArg(self) -> DiagCode:
        ...
    @property
    def DPISignatureMismatch(self) -> DiagCode:
        ...
    @property
    def DPISpecDisallowed(self) -> DiagCode:
        ...
    @property
    def DecimalDigitMultipleUnknown(self) -> DiagCode:
        ...
    @property
    def DeclModifierConflict(self) -> DiagCode:
        ...
    @property
    def DeclModifierOrdering(self) -> DiagCode:
        ...
    @property
    def DeclarationsAtStart(self) -> DiagCode:
        ...
    @property
    def DefParamCycle(self) -> DiagCode:
        ...
    @property
    def DefParamLocal(self) -> DiagCode:
        ...
    @property
    def DefParamTarget(self) -> DiagCode:
        ...
    @property
    def DefParamTargetChange(self) -> DiagCode:
        ...
    @property
    def DefaultArgNotAllowed(self) -> DiagCode:
        ...
    @property
    def DefaultSuperArgLocalReference(self) -> DiagCode:
        ...
    @property
    def DeferredAssertAutoRefArg(self) -> DiagCode:
        ...
    @property
    def DeferredAssertNonVoid(self) -> DiagCode:
        ...
    @property
    def DeferredAssertOutArg(self) -> DiagCode:
        ...
    @property
    def DeferredDelayMustBeZero(self) -> DiagCode:
        ...
    @property
    def DefinitionUsedAsType(self) -> DiagCode:
        ...
    @property
    def DefinitionUsedAsValue(self) -> DiagCode:
        ...
    @property
    def DefparamBadHierarchy(self) -> DiagCode:
        ...
    @property
    def Delay3NotAllowed(self) -> DiagCode:
        ...
    @property
    def Delay3OnVar(self) -> DiagCode:
        ...
    @property
    def Delay3UdpNotAllowed(self) -> DiagCode:
        ...
    @property
    def DelayNotNumeric(self) -> DiagCode:
        ...
    @property
    def DelaysNotAllowed(self) -> DiagCode:
        ...
    @property
    def DigitsLeadingUnderscore(self) -> DiagCode:
        ...
    @property
    def DimensionIndexInvalid(self) -> DiagCode:
        ...
    @property
    def DimensionRequiresConstRange(self) -> DiagCode:
        ...
    @property
    def DirectionOnInterfacePort(self) -> DiagCode:
        ...
    @property
    def DirectionWithInterfacePort(self) -> DiagCode:
        ...
    @property
    def DirectiveInsideDesignElement(self) -> DiagCode:
        ...
    @property
    def DisableIffLocalVar(self) -> DiagCode:
        ...
    @property
    def DisableIffMatched(self) -> DiagCode:
        ...
    @property
    def DisallowedPortDefault(self) -> DiagCode:
        ...
    @property
    def DotIntoInstArray(self) -> DiagCode:
        ...
    @property
    def DotOnType(self) -> DiagCode:
        ...
    @property
    def DriveStrengthHighZ(self) -> DiagCode:
        ...
    @property
    def DriveStrengthInvalid(self) -> DiagCode:
        ...
    @property
    def DriveStrengthNotAllowed(self) -> DiagCode:
        ...
    @property
    def DupConfigRule(self) -> DiagCode:
        ...
    @property
    def DupInterfaceExternMethod(self) -> DiagCode:
        ...
    @property
    def DupTimingPath(self) -> DiagCode:
        ...
    @property
    def DuplicateArgAssignment(self) -> DiagCode:
        ...
    @property
    def DuplicateAttribute(self) -> DiagCode:
        ...
    @property
    def DuplicateClassSpecifier(self) -> DiagCode:
        ...
    @property
    def DuplicateDeclModifier(self) -> DiagCode:
        ...
    @property
    def DuplicateDefinition(self) -> DiagCode:
        ...
    @property
    def DuplicateDefparam(self) -> DiagCode:
        ...
    @property
    def DuplicateImport(self) -> DiagCode:
        ...
    @property
    def DuplicateParamAssignment(self) -> DiagCode:
        ...
    @property
    def DuplicatePortConnection(self) -> DiagCode:
        ...
    @property
    def DuplicateQualifier(self) -> DiagCode:
        ...
    @property
    def DuplicateWildcardPortConnection(self) -> DiagCode:
        ...
    @property
    def DynamicDimensionIndex(self) -> DiagCode:
        ...
    @property
    def DynamicNotProcedural(self) -> DiagCode:
        ...
    @property
    def EdgeDescWrongKeyword(self) -> DiagCode:
        ...
    @property
    def EmbeddedNull(self) -> DiagCode:
        ...
    @property
    def EmptyArgNotAllowed(self) -> DiagCode:
        ...
    @property
    def EmptyAssignmentPattern(self) -> DiagCode:
        ...
    @property
    def EmptyBody(self) -> DiagCode:
        ...
    @property
    def EmptyConcatNotAllowed(self) -> DiagCode:
        ...
    @property
    def EmptyMember(self) -> DiagCode:
        ...
    @property
    def EmptyStatement(self) -> DiagCode:
        ...
    @property
    def EmptyUdpPort(self) -> DiagCode:
        ...
    @property
    def EndNameMismatch(self) -> DiagCode:
        ...
    @property
    def EndNameNotEmpty(self) -> DiagCode:
        ...
    @property
    def EnumIncrementUnknown(self) -> DiagCode:
        ...
    @property
    def EnumRangeLiteral(self) -> DiagCode:
        ...
    @property
    def EnumRangeMultiDimensional(self) -> DiagCode:
        ...
    @property
    def EnumValueDuplicate(self) -> DiagCode:
        ...
    @property
    def EnumValueOutOfRange(self) -> DiagCode:
        ...
    @property
    def EnumValueOverflow(self) -> DiagCode:
        ...
    @property
    def EnumValueSizeMismatch(self) -> DiagCode:
        ...
    @property
    def EnumValueUnknownBits(self) -> DiagCode:
        ...
    @property
    def ErrorTask(self) -> DiagCode:
        ...
    @property
    def EscapedWhitespace(self) -> DiagCode:
        ...
    @property
    def EventExprAssertionArg(self) -> DiagCode:
        ...
    @property
    def EventExpressionConstant(self) -> DiagCode:
        ...
    @property
    def EventExpressionFuncArg(self) -> DiagCode:
        ...
    @property
    def ExceededMaxIncludeDepth(self) -> DiagCode:
        ...
    @property
    def ExpectedAnsiPort(self) -> DiagCode:
        ...
    @property
    def ExpectedArgument(self) -> DiagCode:
        ...
    @property
    def ExpectedAssertionItemPort(self) -> DiagCode:
        ...
    @property
    def ExpectedAssignmentKey(self) -> DiagCode:
        ...
    @property
    def ExpectedAttribute(self) -> DiagCode:
        ...
    @property
    def ExpectedCaseItem(self) -> DiagCode:
        ...
    @property
    def ExpectedClassPropertyName(self) -> DiagCode:
        ...
    @property
    def ExpectedClassSpecifier(self) -> DiagCode:
        ...
    @property
    def ExpectedClockingSkew(self) -> DiagCode:
        ...
    @property
    def ExpectedClosingQuote(self) -> DiagCode:
        ...
    @property
    def ExpectedConditionalPattern(self) -> DiagCode:
        ...
    @property
    def ExpectedConstraintName(self) -> DiagCode:
        ...
    @property
    def ExpectedContinuousAssignment(self) -> DiagCode:
        ...
    @property
    def ExpectedDPISpecString(self) -> DiagCode:
        ...
    @property
    def ExpectedDeclarator(self) -> DiagCode:
        ...
    @property
    def ExpectedDiagPragmaArg(self) -> DiagCode:
        ...
    @property
    def ExpectedDiagPragmaLevel(self) -> DiagCode:
        ...
    @property
    def ExpectedDistItem(self) -> DiagCode:
        ...
    @property
    def ExpectedDriveStrength(self) -> DiagCode:
        ...
    @property
    def ExpectedEdgeDescriptor(self) -> DiagCode:
        ...
    @property
    def ExpectedEnumBase(self) -> DiagCode:
        ...
    @property
    def ExpectedExpression(self) -> DiagCode:
        ...
    @property
    def ExpectedForInitializer(self) -> DiagCode:
        ...
    @property
    def ExpectedFunctionPort(self) -> DiagCode:
        ...
    @property
    def ExpectedFunctionPortList(self) -> DiagCode:
        ...
    @property
    def ExpectedGenvarIterVar(self) -> DiagCode:
        ...
    @property
    def ExpectedHierarchicalInstantiation(self) -> DiagCode:
        ...
    @property
    def ExpectedIdentifier(self) -> DiagCode:
        ...
    @property
    def ExpectedIfOrCase(self) -> DiagCode:
        ...
    @property
    def ExpectedImportExport(self) -> DiagCode:
        ...
    @property
    def ExpectedIncludeFileName(self) -> DiagCode:
        ...
    @property
    def ExpectedIntegerBaseAfterSigned(self) -> DiagCode:
        ...
    @property
    def ExpectedIntegerLiteral(self) -> DiagCode:
        ...
    @property
    def ExpectedInterfaceClassName(self) -> DiagCode:
        ...
    @property
    def ExpectedIterationExpression(self) -> DiagCode:
        ...
    @property
    def ExpectedIteratorName(self) -> DiagCode:
        ...
    @property
    def ExpectedMacroArgs(self) -> DiagCode:
        ...
    @property
    def ExpectedMacroStringifyEnd(self) -> DiagCode:
        ...
    @property
    def ExpectedMember(self) -> DiagCode:
        ...
    @property
    def ExpectedModOrVarName(self) -> DiagCode:
        ...
    @property
    def ExpectedModportPort(self) -> DiagCode:
        ...
    @property
    def ExpectedModuleInstance(self) -> DiagCode:
        ...
    @property
    def ExpectedModuleName(self) -> DiagCode:
        ...
    @property
    def ExpectedNetDelay(self) -> DiagCode:
        ...
    @property
    def ExpectedNetStrength(self) -> DiagCode:
        ...
    @property
    def ExpectedNetType(self) -> DiagCode:
        ...
    @property
    def ExpectedNonAnsiPort(self) -> DiagCode:
        ...
    @property
    def ExpectedPackageImport(self) -> DiagCode:
        ...
    @property
    def ExpectedParameterPort(self) -> DiagCode:
        ...
    @property
    def ExpectedPathOp(self) -> DiagCode:
        ...
    @property
    def ExpectedPattern(self) -> DiagCode:
        ...
    @property
    def ExpectedPortConnection(self) -> DiagCode:
        ...
    @property
    def ExpectedPortList(self) -> DiagCode:
        ...
    @property
    def ExpectedPragmaExpression(self) -> DiagCode:
        ...
    @property
    def ExpectedPragmaName(self) -> DiagCode:
        ...
    @property
    def ExpectedProtectArg(self) -> DiagCode:
        ...
    @property
    def ExpectedProtectKeyword(self) -> DiagCode:
        ...
    @property
    def ExpectedRsRule(self) -> DiagCode:
        ...
    @property
    def ExpectedSampleKeyword(self) -> DiagCode:
        ...
    @property
    def ExpectedScopeOrAssert(self) -> DiagCode:
        ...
    @property
    def ExpectedStatement(self) -> DiagCode:
        ...
    @property
    def ExpectedStreamExpression(self) -> DiagCode:
        ...
    @property
    def ExpectedStringLiteral(self) -> DiagCode:
        ...
    @property
    def ExpectedSubroutineName(self) -> DiagCode:
        ...
    @property
    def ExpectedTimeLiteral(self) -> DiagCode:
        ...
    @property
    def ExpectedToken(self) -> DiagCode:
        ...
    @property
    def ExpectedUdpPort(self) -> DiagCode:
        ...
    @property
    def ExpectedUdpSymbol(self) -> DiagCode:
        ...
    @property
    def ExpectedValueRangeElement(self) -> DiagCode:
        ...
    @property
    def ExpectedVariableAssignment(self) -> DiagCode:
        ...
    @property
    def ExpectedVariableName(self) -> DiagCode:
        ...
    @property
    def ExpectedVectorDigits(self) -> DiagCode:
        ...
    @property
    def ExprMustBeIntegral(self) -> DiagCode:
        ...
    @property
    def ExprNotConstraint(self) -> DiagCode:
        ...
    @property
    def ExprNotStatement(self) -> DiagCode:
        ...
    @property
    def ExpressionNotAssignable(self) -> DiagCode:
        ...
    @property
    def ExpressionNotCallable(self) -> DiagCode:
        ...
    @property
    def ExtendClassFromIface(self) -> DiagCode:
        ...
    @property
    def ExtendFromFinal(self) -> DiagCode:
        ...
    @property
    def ExtendIfaceFromClass(self) -> DiagCode:
        ...
    @property
    def ExternDeclMismatchImpl(self) -> DiagCode:
        ...
    @property
    def ExternDeclMismatchPrev(self) -> DiagCode:
        ...
    @property
    def ExternFuncForkJoin(self) -> DiagCode:
        ...
    @property
    def ExternIfaceArrayMethod(self) -> DiagCode:
        ...
    @property
    def ExternWildcardPortList(self) -> DiagCode:
        ...
    @property
    def ExtraPragmaArgs(self) -> DiagCode:
        ...
    @property
    def ExtraProtectEnd(self) -> DiagCode:
        ...
    @property
    def FatalTask(self) -> DiagCode:
        ...
    @property
    def FinalSpecifierLast(self) -> DiagCode:
        ...
    @property
    def FinalWithPure(self) -> DiagCode:
        ...
    @property
    def FloatBoolConv(self) -> DiagCode:
        ...
    @property
    def ForeachDynamicDimAfterSkipped(self) -> DiagCode:
        ...
    @property
    def ForeachWildcardIndex(self) -> DiagCode:
        ...
    @property
    def ForkJoinAlwaysComb(self) -> DiagCode:
        ...
    @property
    def FormatEmptyArg(self) -> DiagCode:
        ...
    @property
    def FormatMismatchedType(self) -> DiagCode:
        ...
    @property
    def FormatMultibitStrength(self) -> DiagCode:
        ...
    @property
    def FormatNoArgument(self) -> DiagCode:
        ...
    @property
    def FormatRealInt(self) -> DiagCode:
        ...
    @property
    def FormatSpecifierInvalidWidth(self) -> DiagCode:
        ...
    @property
    def FormatSpecifierNotFloat(self) -> DiagCode:
        ...
    @property
    def FormatSpecifierWidthNotAllowed(self) -> DiagCode:
        ...
    @property
    def FormatTooManyArgs(self) -> DiagCode:
        ...
    @property
    def FormatUnspecifiedType(self) -> DiagCode:
        ...
    @property
    def ForwardTypedefDoesNotMatch(self) -> DiagCode:
        ...
    @property
    def ForwardTypedefVisibility(self) -> DiagCode:
        ...
    @property
    def GenericClassScopeResolution(self) -> DiagCode:
        ...
    @property
    def GenvarDuplicate(self) -> DiagCode:
        ...
    @property
    def GenvarUnknownBits(self) -> DiagCode:
        ...
    @property
    def GlobalClockEventExpr(self) -> DiagCode:
        ...
    @property
    def GlobalClockingEmpty(self) -> DiagCode:
        ...
    @property
    def GlobalClockingGenerate(self) -> DiagCode:
        ...
    @property
    def GlobalSampledValueAssertionExpr(self) -> DiagCode:
        ...
    @property
    def GlobalSampledValueNested(self) -> DiagCode:
        ...
    @property
    def HierarchicalFromPackage(self) -> DiagCode:
        ...
    @property
    def IfNoneEdgeSensitive(self) -> DiagCode:
        ...
    @property
    def IfaceExtendIncomplete(self) -> DiagCode:
        ...
    @property
    def IfaceExtendTypeParam(self) -> DiagCode:
        ...
    @property
    def IfaceImportExportTarget(self) -> DiagCode:
        ...
    @property
    def IfaceMethodHidden(self) -> DiagCode:
        ...
    @property
    def IfaceMethodNoImpl(self) -> DiagCode:
        ...
    @property
    def IfaceMethodNotExtern(self) -> DiagCode:
        ...
    @property
    def IfaceMethodNotVirtual(self) -> DiagCode:
        ...
    @property
    def IfaceMethodPure(self) -> DiagCode:
        ...
    @property
    def IfaceNameConflict(self) -> DiagCode:
        ...
    @property
    def IfacePortInExpr(self) -> DiagCode:
        ...
    @property
    def IgnoredMacroPaste(self) -> DiagCode:
        ...
    @property
    def IgnoredSlice(self) -> DiagCode:
        ...
    @property
    def IllegalReferenceToProgramItem(self) -> DiagCode:
        ...
    @property
    def ImplementNonIface(self) -> DiagCode:
        ...
    @property
    def ImplicitConvert(self) -> DiagCode:
        ...
    @property
    def ImplicitNamedPortNotFound(self) -> DiagCode:
        ...
    @property
    def ImplicitNamedPortTypeMismatch(self) -> DiagCode:
        ...
    @property
    def ImplicitNetPortNoDefault(self) -> DiagCode:
        ...
    @property
    def ImplicitNotAllowed(self) -> DiagCode:
        ...
    @property
    def ImportNameCollision(self) -> DiagCode:
        ...
    @property
    def InOutDefaultSkew(self) -> DiagCode:
        ...
    @property
    def InOutPortCannotBeVariable(self) -> DiagCode:
        ...
    @property
    def InOutUWireConn(self) -> DiagCode:
        ...
    @property
    def InOutUWirePort(self) -> DiagCode:
        ...
    @property
    def InOutVarPortConn(self) -> DiagCode:
        ...
    @property
    def IncDecNotAllowed(self) -> DiagCode:
        ...
    @property
    def IndexOOB(self) -> DiagCode:
        ...
    @property
    def IndexValueInvalid(self) -> DiagCode:
        ...
    @property
    def InequivalentUniquenessTypes(self) -> DiagCode:
        ...
    @property
    def InferredValDefArg(self) -> DiagCode:
        ...
    @property
    def InfinitelyRecursiveHierarchy(self) -> DiagCode:
        ...
    @property
    def InfoTask(self) -> DiagCode:
        ...
    @property
    def InheritFromAbstract(self) -> DiagCode:
        ...
    @property
    def InheritFromAbstractConstraint(self) -> DiagCode:
        ...
    @property
    def InitializerRequired(self) -> DiagCode:
        ...
    @property
    def InputPortAssign(self) -> DiagCode:
        ...
    @property
    def InputPortCoercion(self) -> DiagCode:
        ...
    @property
    def InstanceArrayEndianMismatch(self) -> DiagCode:
        ...
    @property
    def InstanceMissingParens(self) -> DiagCode:
        ...
    @property
    def InstanceNameRequired(self) -> DiagCode:
        ...
    @property
    def InstanceWithDelay(self) -> DiagCode:
        ...
    @property
    def InstanceWithStrength(self) -> DiagCode:
        ...
    @property
    def IntBoolConv(self) -> DiagCode:
        ...
    @property
    def InterconnectDelaySyntax(self) -> DiagCode:
        ...
    @property
    def InterconnectInitializer(self) -> DiagCode:
        ...
    @property
    def InterconnectMultiPort(self) -> DiagCode:
        ...
    @property
    def InterconnectPortVar(self) -> DiagCode:
        ...
    @property
    def InterconnectReference(self) -> DiagCode:
        ...
    @property
    def InterconnectTypeSyntax(self) -> DiagCode:
        ...
    @property
    def InterfacePortInvalidExpression(self) -> DiagCode:
        ...
    @property
    def InterfacePortNotConnected(self) -> DiagCode:
        ...
    @property
    def InterfacePortTypeMismatch(self) -> DiagCode:
        ...
    @property
    def InvalidAccessDotColon(self) -> DiagCode:
        ...
    @property
    def InvalidArgumentExpr(self) -> DiagCode:
        ...
    @property
    def InvalidArrayElemType(self) -> DiagCode:
        ...
    @property
    def InvalidArraySize(self) -> DiagCode:
        ...
    @property
    def InvalidAssociativeIndexType(self) -> DiagCode:
        ...
    @property
    def InvalidBindTarget(self) -> DiagCode:
        ...
    @property
    def InvalidBinsMatches(self) -> DiagCode:
        ...
    @property
    def InvalidBinsTarget(self) -> DiagCode:
        ...
    @property
    def InvalidBlockEventTarget(self) -> DiagCode:
        ...
    @property
    def InvalidClassAccess(self) -> DiagCode:
        ...
    @property
    def InvalidClockingSignal(self) -> DiagCode:
        ...
    @property
    def InvalidCommaInPropExpr(self) -> DiagCode:
        ...
    @property
    def InvalidConstraintQualifier(self) -> DiagCode:
        ...
    @property
    def InvalidConstructorAccess(self) -> DiagCode:
        ...
    @property
    def InvalidCoverageOption(self) -> DiagCode:
        ...
    @property
    def InvalidDPIArgType(self) -> DiagCode:
        ...
    @property
    def InvalidDPICIdentifier(self) -> DiagCode:
        ...
    @property
    def InvalidDPIReturnType(self) -> DiagCode:
        ...
    @property
    def InvalidDeferredAssertAction(self) -> DiagCode:
        ...
    @property
    def InvalidDelayValue(self) -> DiagCode:
        ...
    @property
    def InvalidDimensionRange(self) -> DiagCode:
        ...
    @property
    def InvalidDisableTarget(self) -> DiagCode:
        ...
    @property
    def InvalidDistExpression(self) -> DiagCode:
        ...
    @property
    def InvalidEdgeDescriptor(self) -> DiagCode:
        ...
    @property
    def InvalidEncodingByte(self) -> DiagCode:
        ...
    @property
    def InvalidEnumBase(self) -> DiagCode:
        ...
    @property
    def InvalidEventExpression(self) -> DiagCode:
        ...
    @property
    def InvalidExtendsDefault(self) -> DiagCode:
        ...
    @property
    def InvalidForInitializer(self) -> DiagCode:
        ...
    @property
    def InvalidForStepExpression(self) -> DiagCode:
        ...
    @property
    def InvalidGenvarIterExpression(self) -> DiagCode:
        ...
    @property
    def InvalidHexEscapeCode(self) -> DiagCode:
        ...
    @property
    def InvalidHierarchicalIfacePortConn(self) -> DiagCode:
        ...
    @property
    def InvalidInferredTimeScale(self) -> DiagCode:
        ...
    @property
    def InvalidInstanceForParent(self) -> DiagCode:
        ...
    @property
    def InvalidLineDirectiveLevel(self) -> DiagCode:
        ...
    @property
    def InvalidMacroName(self) -> DiagCode:
        ...
    @property
    def InvalidMatchItem(self) -> DiagCode:
        ...
    @property
    def InvalidMemberAccess(self) -> DiagCode:
        ...
    @property
    def InvalidMethodOverride(self) -> DiagCode:
        ...
    @property
    def InvalidMethodQualifier(self) -> DiagCode:
        ...
    @property
    def InvalidModportAccess(self) -> DiagCode:
        ...
    @property
    def InvalidNGateCount(self) -> DiagCode:
        ...
    @property
    def InvalidNetType(self) -> DiagCode:
        ...
    @property
    def InvalidPackageDecl(self) -> DiagCode:
        ...
    @property
    def InvalidParamOverrideOpt(self) -> DiagCode:
        ...
    @property
    def InvalidPortSubType(self) -> DiagCode:
        ...
    @property
    def InvalidPortType(self) -> DiagCode:
        ...
    @property
    def InvalidPragmaNumber(self) -> DiagCode:
        ...
    @property
    def InvalidPragmaViewport(self) -> DiagCode:
        ...
    @property
    def InvalidPrimInstanceForParent(self) -> DiagCode:
        ...
    @property
    def InvalidPrimitivePortConn(self) -> DiagCode:
        ...
    @property
    def InvalidPropertyIndex(self) -> DiagCode:
        ...
    @property
    def InvalidPropertyQualifier(self) -> DiagCode:
        ...
    @property
    def InvalidPropertyRange(self) -> DiagCode:
        ...
    @property
    def InvalidPullStrength(self) -> DiagCode:
        ...
    @property
    def InvalidPulseStyle(self) -> DiagCode:
        ...
    @property
    def InvalidQualifierForConstructor(self) -> DiagCode:
        ...
    @property
    def InvalidQualifierForIfaceMember(self) -> DiagCode:
        ...
    @property
    def InvalidQualifierForMember(self) -> DiagCode:
        ...
    @property
    def InvalidRandType(self) -> DiagCode:
        ...
    @property
    def InvalidRandomizeOverride(self) -> DiagCode:
        ...
    @property
    def InvalidRefArg(self) -> DiagCode:
        ...
    @property
    def InvalidRepeatRange(self) -> DiagCode:
        ...
    @property
    def InvalidScopeIndexExpression(self) -> DiagCode:
        ...
    @property
    def InvalidSignalEventInSeq(self) -> DiagCode:
        ...
    @property
    def InvalidSpecifyDest(self) -> DiagCode:
        ...
    @property
    def InvalidSpecifyPath(self) -> DiagCode:
        ...
    @property
    def InvalidSpecifySource(self) -> DiagCode:
        ...
    @property
    def InvalidSpecifyType(self) -> DiagCode:
        ...
    @property
    def InvalidStmtInChecker(self) -> DiagCode:
        ...
    @property
    def InvalidStringArg(self) -> DiagCode:
        ...
    @property
    def InvalidSuperNew(self) -> DiagCode:
        ...
    @property
    def InvalidSuperNewDefault(self) -> DiagCode:
        ...
    @property
    def InvalidSyntaxInEventExpr(self) -> DiagCode:
        ...
    @property
    def InvalidThisHandle(self) -> DiagCode:
        ...
    @property
    def InvalidTimeScalePrecision(self) -> DiagCode:
        ...
    @property
    def InvalidTimeScaleSpecifier(self) -> DiagCode:
        ...
    @property
    def InvalidTimingCheckNotifierArg(self) -> DiagCode:
        ...
    @property
    def InvalidTopModule(self) -> DiagCode:
        ...
    @property
    def InvalidUTF8Seq(self) -> DiagCode:
        ...
    @property
    def InvalidUnionMember(self) -> DiagCode:
        ...
    @property
    def InvalidUniquenessExpr(self) -> DiagCode:
        ...
    @property
    def InvalidUserDefinedNetType(self) -> DiagCode:
        ...
    @property
    def IteratorArgsWithoutWithClause(self) -> DiagCode:
        ...
    @property
    def LabelAndName(self) -> DiagCode:
        ...
    @property
    def LetHierarchical(self) -> DiagCode:
        ...
    @property
    def LifetimeForPrototype(self) -> DiagCode:
        ...
    @property
    def LiteralSizeIsZero(self) -> DiagCode:
        ...
    @property
    def LiteralSizeTooLarge(self) -> DiagCode:
        ...
    @property
    def LocalFormalVarMultiAssign(self) -> DiagCode:
        ...
    @property
    def LocalMemberAccess(self) -> DiagCode:
        ...
    @property
    def LocalNotAllowed(self) -> DiagCode:
        ...
    @property
    def LocalParamNoInitializer(self) -> DiagCode:
        ...
    @property
    def LocalVarEventExpr(self) -> DiagCode:
        ...
    @property
    def LocalVarMatchItem(self) -> DiagCode:
        ...
    @property
    def LocalVarOutputEmptyMatch(self) -> DiagCode:
        ...
    @property
    def LocalVarTypeRequired(self) -> DiagCode:
        ...
    @property
    def LoopVarShadowsArray(self) -> DiagCode:
        ...
    @property
    def MacroOpsOutsideDefinition(self) -> DiagCode:
        ...
    @property
    def MacroTokensAfterPragmaProtect(self) -> DiagCode:
        ...
    @property
    def MatchItemsAdmitEmpty(self) -> DiagCode:
        ...
    @property
    def MaxGenerateStepsExceeded(self) -> DiagCode:
        ...
    @property
    def MaxInstanceArrayExceeded(self) -> DiagCode:
        ...
    @property
    def MaxInstanceDepthExceeded(self) -> DiagCode:
        ...
    @property
    def MemberDefinitionBeforeClass(self) -> DiagCode:
        ...
    @property
    def MethodArgCountMismatch(self) -> DiagCode:
        ...
    @property
    def MethodArgDefaultMismatch(self) -> DiagCode:
        ...
    @property
    def MethodArgDirectionMismatch(self) -> DiagCode:
        ...
    @property
    def MethodArgNameMismatch(self) -> DiagCode:
        ...
    @property
    def MethodArgNoDefault(self) -> DiagCode:
        ...
    @property
    def MethodArgTypeMismatch(self) -> DiagCode:
        ...
    @property
    def MethodKindMismatch(self) -> DiagCode:
        ...
    @property
    def MethodReturnMismatch(self) -> DiagCode:
        ...
    @property
    def MethodReturnTypeScoped(self) -> DiagCode:
        ...
    @property
    def MethodStaticLifetime(self) -> DiagCode:
        ...
    @property
    def MismatchStaticConstraint(self) -> DiagCode:
        ...
    @property
    def MismatchedEndKeywordsDirective(self) -> DiagCode:
        ...
    @property
    def MismatchedTimeScales(self) -> DiagCode:
        ...
    @property
    def MismatchedUserDefPortConn(self) -> DiagCode:
        ...
    @property
    def MismatchedUserDefPortDir(self) -> DiagCode:
        ...
    @property
    def MisplacedDirectiveChar(self) -> DiagCode:
        ...
    @property
    def MisplacedTrailingSeparator(self) -> DiagCode:
        ...
    @property
    def MissingConstraintBlock(self) -> DiagCode:
        ...
    @property
    def MissingEndIfDirective(self) -> DiagCode:
        ...
    @property
    def MissingExponentDigits(self) -> DiagCode:
        ...
    @property
    def MissingExportImpl(self) -> DiagCode:
        ...
    @property
    def MissingExternImpl(self) -> DiagCode:
        ...
    @property
    def MissingExternModuleImpl(self) -> DiagCode:
        ...
    @property
    def MissingExternWildcardPorts(self) -> DiagCode:
        ...
    @property
    def MissingFormatSpecifier(self) -> DiagCode:
        ...
    @property
    def MissingFractionalDigits(self) -> DiagCode:
        ...
    @property
    def MissingInvocationParens(self) -> DiagCode:
        ...
    @property
    def MissingModportPortDirection(self) -> DiagCode:
        ...
    @property
    def MissingPortIODeclaration(self) -> DiagCode:
        ...
    @property
    def MissingReturnValue(self) -> DiagCode:
        ...
    @property
    def MissingReturnValueProd(self) -> DiagCode:
        ...
    @property
    def MissingTimeScale(self) -> DiagCode:
        ...
    @property
    def MixedVarAssigns(self) -> DiagCode:
        ...
    @property
    def MixingOrderedAndNamedArgs(self) -> DiagCode:
        ...
    @property
    def MixingOrderedAndNamedParams(self) -> DiagCode:
        ...
    @property
    def MixingOrderedAndNamedPorts(self) -> DiagCode:
        ...
    @property
    def MixingSubroutinePortKinds(self) -> DiagCode:
        ...
    @property
    def ModportConnMismatch(self) -> DiagCode:
        ...
    @property
    def MultiBitEdge(self) -> DiagCode:
        ...
    @property
    def MultipleAlwaysAssigns(self) -> DiagCode:
        ...
    @property
    def MultipleContAssigns(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultCases(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultClocking(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultConstructorArg(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultDisable(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultInputSkew(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultOutputSkew(self) -> DiagCode:
        ...
    @property
    def MultipleDefaultRules(self) -> DiagCode:
        ...
    @property
    def MultipleGenerateDefaultCases(self) -> DiagCode:
        ...
    @property
    def MultipleGlobalClocking(self) -> DiagCode:
        ...
    @property
    def MultiplePackedOpenArrays(self) -> DiagCode:
        ...
    @property
    def MultipleParallelTerminals(self) -> DiagCode:
        ...
    @property
    def MultipleTopDupName(self) -> DiagCode:
        ...
    @property
    def MultipleUDNTDrivers(self) -> DiagCode:
        ...
    @property
    def MultipleUWireDrivers(self) -> DiagCode:
        ...
    @property
    def NTResolveArgModify(self) -> DiagCode:
        ...
    @property
    def NTResolveClass(self) -> DiagCode:
        ...
    @property
    def NTResolveReturn(self) -> DiagCode:
        ...
    @property
    def NTResolveSingleArg(self) -> DiagCode:
        ...
    @property
    def NTResolveTask(self) -> DiagCode:
        ...
    @property
    def NTResolveUserDef(self) -> DiagCode:
        ...
    @property
    def NameListWithScopeRandomize(self) -> DiagCode:
        ...
    @property
    def NamedArgNotAllowed(self) -> DiagCode:
        ...
    @property
    def NegativeTimingLimit(self) -> DiagCode:
        ...
    @property
    def NestedBlockComment(self) -> DiagCode:
        ...
    @property
    def NestedConfigMultipleTops(self) -> DiagCode:
        ...
    @property
    def NestedDisableIff(self) -> DiagCode:
        ...
    @property
    def NestedIface(self) -> DiagCode:
        ...
    @property
    def NestedNonStaticClassMethod(self) -> DiagCode:
        ...
    @property
    def NestedNonStaticClassProperty(self) -> DiagCode:
        ...
    @property
    def NestedProtectBegin(self) -> DiagCode:
        ...
    @property
    def NetAliasCommonNetType(self) -> DiagCode:
        ...
    @property
    def NetAliasHierarchical(self) -> DiagCode:
        ...
    @property
    def NetAliasNotANet(self) -> DiagCode:
        ...
    @property
    def NetAliasWidthMismatch(self) -> DiagCode:
        ...
    @property
    def NetInconsistent(self) -> DiagCode:
        ...
    @property
    def NetRangeInconsistent(self) -> DiagCode:
        ...
    @property
    def NewArrayTarget(self) -> DiagCode:
        ...
    @property
    def NewClassTarget(self) -> DiagCode:
        ...
    @property
    def NewInterfaceClass(self) -> DiagCode:
        ...
    @property
    def NewKeywordQualified(self) -> DiagCode:
        ...
    @property
    def NewVirtualClass(self) -> DiagCode:
        ...
    @property
    def NoChangeEdgeRequired(self) -> DiagCode:
        ...
    @property
    def NoCommaInList(self) -> DiagCode:
        ...
    @property
    def NoCommonComparisonType(self) -> DiagCode:
        ...
    @property
    def NoConstraintBody(self) -> DiagCode:
        ...
    @property
    def NoDeclInClass(self) -> DiagCode:
        ...
    @property
    def NoDefaultClocking(self) -> DiagCode:
        ...
    @property
    def NoDefaultSpecialization(self) -> DiagCode:
        ...
    @property
    def NoGlobalClocking(self) -> DiagCode:
        ...
    @property
    def NoImplicitConversion(self) -> DiagCode:
        ...
    @property
    def NoLabelOnSemicolon(self) -> DiagCode:
        ...
    @property
    def NoMemberImplFound(self) -> DiagCode:
        ...
    @property
    def NoTopModules(self) -> DiagCode:
        ...
    @property
    def NonIntegralConstraintExpr(self) -> DiagCode:
        ...
    @property
    def NonIntegralConstraintLiteral(self) -> DiagCode:
        ...
    @property
    def NonIntegralCoverageExpr(self) -> DiagCode:
        ...
    @property
    def NonPrintableChar(self) -> DiagCode:
        ...
    @property
    def NonProceduralFuncArg(self) -> DiagCode:
        ...
    @property
    def NonStandardGenBlock(self) -> DiagCode:
        ...
    @property
    def NonStaticClassMethod(self) -> DiagCode:
        ...
    @property
    def NonStaticClassProperty(self) -> DiagCode:
        ...
    @property
    def NonblockingAssignmentToAuto(self) -> DiagCode:
        ...
    @property
    def NonblockingDynamicAssign(self) -> DiagCode:
        ...
    @property
    def NonblockingInFinal(self) -> DiagCode:
        ...
    @property
    def NonstandardDist(self) -> DiagCode:
        ...
    @property
    def NonstandardEscapeCode(self) -> DiagCode:
        ...
    @property
    def NonstandardForeach(self) -> DiagCode:
        ...
    @property
    def NonstandardSysFunc(self) -> DiagCode:
        ...
    @property
    def NotAChecker(self) -> DiagCode:
        ...
    @property
    def NotAClass(self) -> DiagCode:
        ...
    @property
    def NotAClockingBlock(self) -> DiagCode:
        ...
    @property
    def NotAGenericClass(self) -> DiagCode:
        ...
    @property
    def NotAGenvar(self) -> DiagCode:
        ...
    @property
    def NotAHierarchicalScope(self) -> DiagCode:
        ...
    @property
    def NotAModport(self) -> DiagCode:
        ...
    @property
    def NotAProduction(self) -> DiagCode:
        ...
    @property
    def NotASubroutine(self) -> DiagCode:
        ...
    @property
    def NotAType(self) -> DiagCode:
        ...
    @property
    def NotAValue(self) -> DiagCode:
        ...
    @property
    def NotAllowedInAnonymousProgram(self) -> DiagCode:
        ...
    @property
    def NotAllowedInCU(self) -> DiagCode:
        ...
    @property
    def NotAllowedInChecker(self) -> DiagCode:
        ...
    @property
    def NotAllowedInClass(self) -> DiagCode:
        ...
    @property
    def NotAllowedInClocking(self) -> DiagCode:
        ...
    @property
    def NotAllowedInGenerate(self) -> DiagCode:
        ...
    @property
    def NotAllowedInIfaceClass(self) -> DiagCode:
        ...
    @property
    def NotAllowedInInterface(self) -> DiagCode:
        ...
    @property
    def NotAllowedInModport(self) -> DiagCode:
        ...
    @property
    def NotAllowedInModule(self) -> DiagCode:
        ...
    @property
    def NotAllowedInPackage(self) -> DiagCode:
        ...
    @property
    def NotAllowedInProgram(self) -> DiagCode:
        ...
    @property
    def NotAnArray(self) -> DiagCode:
        ...
    @property
    def NotAnEvent(self) -> DiagCode:
        ...
    @property
    def NotAnInterface(self) -> DiagCode:
        ...
    @property
    def NotAnInterfaceOrPort(self) -> DiagCode:
        ...
    @property
    def NotBooleanConvertible(self) -> DiagCode:
        ...
    @property
    def NotEnoughMacroArgs(self) -> DiagCode:
        ...
    @property
    def NoteAssignedHere(self) -> DiagCode:
        ...
    @property
    def NoteCommonAncestor(self) -> DiagCode:
        ...
    @property
    def NoteComparisonReduces(self) -> DiagCode:
        ...
    @property
    def NoteConfigRule(self) -> DiagCode:
        ...
    @property
    def NoteDeclarationHere(self) -> DiagCode:
        ...
    @property
    def NoteDirectiveHere(self) -> DiagCode:
        ...
    @property
    def NoteDrivenHere(self) -> DiagCode:
        ...
    @property
    def NoteExpandedHere(self) -> DiagCode:
        ...
    @property
    def NoteFromHere2(self) -> DiagCode:
        ...
    @property
    def NoteImportedFrom(self) -> DiagCode:
        ...
    @property
    def NoteInCallTo(self) -> DiagCode:
        ...
    @property
    def NoteOriginalAssign(self) -> DiagCode:
        ...
    @property
    def NotePreviousDefinition(self) -> DiagCode:
        ...
    @property
    def NotePreviousMatch(self) -> DiagCode:
        ...
    @property
    def NotePreviousUsage(self) -> DiagCode:
        ...
    @property
    def NoteReferencedHere(self) -> DiagCode:
        ...
    @property
    def NoteSkippingFrames(self) -> DiagCode:
        ...
    @property
    def NoteToMatchThis(self) -> DiagCode:
        ...
    @property
    def NoteWhileExpanding(self) -> DiagCode:
        ...
    @property
    def NullPortExpression(self) -> DiagCode:
        ...
    @property
    def ObjectTooLarge(self) -> DiagCode:
        ...
    @property
    def OctalEscapeCodeTooBig(self) -> DiagCode:
        ...
    @property
    def OutRefFuncConstraint(self) -> DiagCode:
        ...
    @property
    def OutputPortCoercion(self) -> DiagCode:
        ...
    @property
    def OverridingExtends(self) -> DiagCode:
        ...
    @property
    def OverridingFinal(self) -> DiagCode:
        ...
    @property
    def OverridingInitial(self) -> DiagCode:
        ...
    @property
    def PackageExportSelf(self) -> DiagCode:
        ...
    @property
    def PackageImportSelf(self) -> DiagCode:
        ...
    @property
    def PackageNetInit(self) -> DiagCode:
        ...
    @property
    def PackedArrayNotIntegral(self) -> DiagCode:
        ...
    @property
    def PackedDimsOnPredefinedType(self) -> DiagCode:
        ...
    @property
    def PackedDimsOnUnpacked(self) -> DiagCode:
        ...
    @property
    def PackedDimsRequireFullRange(self) -> DiagCode:
        ...
    @property
    def PackedMemberHasInitializer(self) -> DiagCode:
        ...
    @property
    def PackedMemberNotIntegral(self) -> DiagCode:
        ...
    @property
    def PackedTypeTooLarge(self) -> DiagCode:
        ...
    @property
    def PackedUnionWidthMismatch(self) -> DiagCode:
        ...
    @property
    def ParallelPathWidth(self) -> DiagCode:
        ...
    @property
    def ParamHasNoValue(self) -> DiagCode:
        ...
    @property
    def ParameterDoesNotExist(self) -> DiagCode:
        ...
    @property
    def ParseTreeTooDeep(self) -> DiagCode:
        ...
    @property
    def PastNumTicksInvalid(self) -> DiagCode:
        ...
    @property
    def PathPulseInExpr(self) -> DiagCode:
        ...
    @property
    def PathPulseInvalidPathName(self) -> DiagCode:
        ...
    @property
    def PatternStructTooFew(self) -> DiagCode:
        ...
    @property
    def PatternStructTooMany(self) -> DiagCode:
        ...
    @property
    def PatternStructType(self) -> DiagCode:
        ...
    @property
    def PatternTaggedType(self) -> DiagCode:
        ...
    @property
    def PlaRangeInAscendingOrder(self) -> DiagCode:
        ...
    @property
    def PointlessVoidCast(self) -> DiagCode:
        ...
    @property
    def PortConcatInOut(self) -> DiagCode:
        ...
    @property
    def PortConcatRef(self) -> DiagCode:
        ...
    @property
    def PortConnArrayMismatch(self) -> DiagCode:
        ...
    @property
    def PortConnDimensionsMismatch(self) -> DiagCode:
        ...
    @property
    def PortDeclDimensionsMismatch(self) -> DiagCode:
        ...
    @property
    def PortDeclInANSIModule(self) -> DiagCode:
        ...
    @property
    def PortDoesNotExist(self) -> DiagCode:
        ...
    @property
    def PortTypeNotInterfaceOrData(self) -> DiagCode:
        ...
    @property
    def PortWidthExpand(self) -> DiagCode:
        ...
    @property
    def PortWidthTruncate(self) -> DiagCode:
        ...
    @property
    def PrimitiveAnsiMix(self) -> DiagCode:
        ...
    @property
    def PrimitiveDupInitial(self) -> DiagCode:
        ...
    @property
    def PrimitiveDupOutput(self) -> DiagCode:
        ...
    @property
    def PrimitiveInitVal(self) -> DiagCode:
        ...
    @property
    def PrimitiveInitialInComb(self) -> DiagCode:
        ...
    @property
    def PrimitiveOutputFirst(self) -> DiagCode:
        ...
    @property
    def PrimitivePortCountWrong(self) -> DiagCode:
        ...
    @property
    def PrimitivePortDup(self) -> DiagCode:
        ...
    @property
    def PrimitivePortMissing(self) -> DiagCode:
        ...
    @property
    def PrimitivePortUnknown(self) -> DiagCode:
        ...
    @property
    def PrimitiveRegDup(self) -> DiagCode:
        ...
    @property
    def PrimitiveRegInput(self) -> DiagCode:
        ...
    @property
    def PrimitiveTwoPorts(self) -> DiagCode:
        ...
    @property
    def PrimitiveWrongInitial(self) -> DiagCode:
        ...
    @property
    def PropAbortLocalVar(self) -> DiagCode:
        ...
    @property
    def PropAbortMatched(self) -> DiagCode:
        ...
    @property
    def PropExprInSequence(self) -> DiagCode:
        ...
    @property
    def PropInstanceRepetition(self) -> DiagCode:
        ...
    @property
    def PropertyLhsInvalid(self) -> DiagCode:
        ...
    @property
    def PropertyPortInLet(self) -> DiagCode:
        ...
    @property
    def PropertyPortInSeq(self) -> DiagCode:
        ...
    @property
    def ProtectArgList(self) -> DiagCode:
        ...
    @property
    def ProtectEncodingBytes(self) -> DiagCode:
        ...
    @property
    def ProtectedEnvelope(self) -> DiagCode:
        ...
    @property
    def ProtectedMemberAccess(self) -> DiagCode:
        ...
    @property
    def PullStrengthHighZ(self) -> DiagCode:
        ...
    @property
    def PulseControlPATHPULSE(self) -> DiagCode:
        ...
    @property
    def PulseControlSpecifyParent(self) -> DiagCode:
        ...
    @property
    def PulseControlTwoValues(self) -> DiagCode:
        ...
    @property
    def PureConstraintInAbstract(self) -> DiagCode:
        ...
    @property
    def PureInAbstract(self) -> DiagCode:
        ...
    @property
    def PureRequiresVirtual(self) -> DiagCode:
        ...
    @property
    def QualifierConflict(self) -> DiagCode:
        ...
    @property
    def QualifierNotFirst(self) -> DiagCode:
        ...
    @property
    def QualifiersOnOutOfBlock(self) -> DiagCode:
        ...
    @property
    def QueryOnAssociativeNonIntegral(self) -> DiagCode:
        ...
    @property
    def QueryOnAssociativeWildcard(self) -> DiagCode:
        ...
    @property
    def QueryOnDynamicType(self) -> DiagCode:
        ...
    @property
    def RandCInDist(self) -> DiagCode:
        ...
    @property
    def RandCInSoft(self) -> DiagCode:
        ...
    @property
    def RandCInSolveBefore(self) -> DiagCode:
        ...
    @property
    def RandCInUnique(self) -> DiagCode:
        ...
    @property
    def RandJoinNotEnough(self) -> DiagCode:
        ...
    @property
    def RandJoinNotNumeric(self) -> DiagCode:
        ...
    @property
    def RandJoinProdItem(self) -> DiagCode:
        ...
    @property
    def RandNeededInDist(self) -> DiagCode:
        ...
    @property
    def RandOnPackedMember(self) -> DiagCode:
        ...
    @property
    def RandOnUnionMember(self) -> DiagCode:
        ...
    @property
    def RangeOOB(self) -> DiagCode:
        ...
    @property
    def RangeSelectAssociative(self) -> DiagCode:
        ...
    @property
    def RangeWidthOOB(self) -> DiagCode:
        ...
    @property
    def RangeWidthOverflow(self) -> DiagCode:
        ...
    @property
    def RawProtectEOF(self) -> DiagCode:
        ...
    @property
    def RealLiteralOverflow(self) -> DiagCode:
        ...
    @property
    def RealLiteralUnderflow(self) -> DiagCode:
        ...
    @property
    def RecursiveClassSpecialization(self) -> DiagCode:
        ...
    @property
    def RecursiveDefinition(self) -> DiagCode:
        ...
    @property
    def RecursiveLet(self) -> DiagCode:
        ...
    @property
    def RecursiveMacro(self) -> DiagCode:
        ...
    @property
    def RecursivePropArgExpr(self) -> DiagCode:
        ...
    @property
    def RecursivePropDisableIff(self) -> DiagCode:
        ...
    @property
    def RecursivePropNegation(self) -> DiagCode:
        ...
    @property
    def RecursivePropTimeAdvance(self) -> DiagCode:
        ...
    @property
    def RecursiveSequence(self) -> DiagCode:
        ...
    @property
    def RedefiningMacro(self) -> DiagCode:
        ...
    @property
    def Redefinition(self) -> DiagCode:
        ...
    @property
    def RedefinitionDifferentType(self) -> DiagCode:
        ...
    @property
    def RefArgAutomaticFunc(self) -> DiagCode:
        ...
    @property
    def RefArgForkJoin(self) -> DiagCode:
        ...
    @property
    def RefPortMustBeVariable(self) -> DiagCode:
        ...
    @property
    def RefPortUnconnected(self) -> DiagCode:
        ...
    @property
    def RefPortUnnamedUnconnected(self) -> DiagCode:
        ...
    @property
    def RefTypeMismatch(self) -> DiagCode:
        ...
    @property
    def RegAfterNettype(self) -> DiagCode:
        ...
    @property
    def RepeatControlNotEvent(self) -> DiagCode:
        ...
    @property
    def RepeatNotNumeric(self) -> DiagCode:
        ...
    @property
    def ReplicationZeroOutsideConcat(self) -> DiagCode:
        ...
    @property
    def RestrictStmtNoFail(self) -> DiagCode:
        ...
    @property
    def ReturnInParallel(self) -> DiagCode:
        ...
    @property
    def ReturnNotInSubroutine(self) -> DiagCode:
        ...
    @property
    def ReversedValueRange(self) -> DiagCode:
        ...
    @property
    def SampledValueLocalVar(self) -> DiagCode:
        ...
    @property
    def SampledValueMatched(self) -> DiagCode:
        ...
    @property
    def ScopeIncompleteTypedef(self) -> DiagCode:
        ...
    @property
    def ScopeIndexOutOfRange(self) -> DiagCode:
        ...
    @property
    def ScopeNotIndexable(self) -> DiagCode:
        ...
    @property
    def ScopedClassCopy(self) -> DiagCode:
        ...
    @property
    def SelectAfterRangeSelect(self) -> DiagCode:
        ...
    @property
    def SelectEndianDynamic(self) -> DiagCode:
        ...
    @property
    def SelectEndianMismatch(self) -> DiagCode:
        ...
    @property
    def SelectOfVectoredNet(self) -> DiagCode:
        ...
    @property
    def SeqInstanceRepetition(self) -> DiagCode:
        ...
    @property
    def SeqMethodInputLocalVar(self) -> DiagCode:
        ...
    @property
    def SeqPropAdmitEmpty(self) -> DiagCode:
        ...
    @property
    def SeqRangeMinMax(self) -> DiagCode:
        ...
    @property
    def SequenceMethodLocalVar(self) -> DiagCode:
        ...
    @property
    def SignConversion(self) -> DiagCode:
        ...
    @property
    def SignedIntegerOverflow(self) -> DiagCode:
        ...
    @property
    def SignednessNoEffect(self) -> DiagCode:
        ...
    @property
    def SingleBitVectored(self) -> DiagCode:
        ...
    @property
    def SolveBeforeDisallowed(self) -> DiagCode:
        ...
    @property
    def SpecifiersNotAllowed(self) -> DiagCode:
        ...
    @property
    def SpecifyBlockParam(self) -> DiagCode:
        ...
    @property
    def SpecifyPathBadReference(self) -> DiagCode:
        ...
    @property
    def SpecifyPathConditionExpr(self) -> DiagCode:
        ...
    @property
    def SpecifyPathMultiDim(self) -> DiagCode:
        ...
    @property
    def SpecparamInConstant(self) -> DiagCode:
        ...
    @property
    def SplitDistWeightOp(self) -> DiagCode:
        ...
    @property
    def StatementNotInLoop(self) -> DiagCode:
        ...
    @property
    def StaticAssert(self) -> DiagCode:
        ...
    @property
    def StaticConstNoInitializer(self) -> DiagCode:
        ...
    @property
    def StaticInitializerMustBeExplicit(self) -> DiagCode:
        ...
    @property
    def SubroutineMatchAutoRefArg(self) -> DiagCode:
        ...
    @property
    def SubroutineMatchNonVoid(self) -> DiagCode:
        ...
    @property
    def SubroutineMatchOutArg(self) -> DiagCode:
        ...
    @property
    def SubroutinePortInitializer(self) -> DiagCode:
        ...
    @property
    def SubroutinePrototypeScoped(self) -> DiagCode:
        ...
    @property
    def SuperNoBase(self) -> DiagCode:
        ...
    @property
    def SuperOutsideClass(self) -> DiagCode:
        ...
    @property
    def SysFuncHierarchicalNotAllowed(self) -> DiagCode:
        ...
    @property
    def SysFuncNotConst(self) -> DiagCode:
        ...
    @property
    def TaggedStruct(self) -> DiagCode:
        ...
    @property
    def TaggedUnionMissingInit(self) -> DiagCode:
        ...
    @property
    def TaggedUnionTarget(self) -> DiagCode:
        ...
    @property
    def TaskConstructor(self) -> DiagCode:
        ...
    @property
    def TaskFromFinal(self) -> DiagCode:
        ...
    @property
    def TaskFromFunction(self) -> DiagCode:
        ...
    @property
    def TaskInConstraint(self) -> DiagCode:
        ...
    @property
    def TaskReturnType(self) -> DiagCode:
        ...
    @property
    def ThroughoutLhsInvalid(self) -> DiagCode:
        ...
    @property
    def TimeScaleFirstInScope(self) -> DiagCode:
        ...
    @property
    def TimingCheckEventEdgeRequired(self) -> DiagCode:
        ...
    @property
    def TimingCheckEventNotAllowed(self) -> DiagCode:
        ...
    @property
    def TimingControlNotAllowed(self) -> DiagCode:
        ...
    @property
    def TimingInFuncNotAllowed(self) -> DiagCode:
        ...
    @property
    def TooFewArguments(self) -> DiagCode:
        ...
    @property
    def TooManyActualMacroArgs(self) -> DiagCode:
        ...
    @property
    def TooManyArguments(self) -> DiagCode:
        ...
    @property
    def TooManyEdgeDescriptors(self) -> DiagCode:
        ...
    @property
    def TooManyErrors(self) -> DiagCode:
        ...
    @property
    def TooManyForeachVars(self) -> DiagCode:
        ...
    @property
    def TooManyLexerErrors(self) -> DiagCode:
        ...
    @property
    def TooManyParamAssignments(self) -> DiagCode:
        ...
    @property
    def TooManyPortConnections(self) -> DiagCode:
        ...
    @property
    def TopModuleIfacePort(self) -> DiagCode:
        ...
    @property
    def TopModuleRefPort(self) -> DiagCode:
        ...
    @property
    def TopModuleUnnamedRefPort(self) -> DiagCode:
        ...
    @property
    def TypeHierarchical(self) -> DiagCode:
        ...
    @property
    def TypeIsNotAClass(self) -> DiagCode:
        ...
    @property
    def TypeRefDeclVar(self) -> DiagCode:
        ...
    @property
    def TypeRefHierarchical(self) -> DiagCode:
        ...
    @property
    def TypeRefVoid(self) -> DiagCode:
        ...
    @property
    def TypeRestrictionMismatch(self) -> DiagCode:
        ...
    @property
    def TypoIdentifier(self) -> DiagCode:
        ...
    @property
    def UTF8Char(self) -> DiagCode:
        ...
    @property
    def UdpAllX(self) -> DiagCode:
        ...
    @property
    def UdpCombState(self) -> DiagCode:
        ...
    @property
    def UdpDupDiffOutput(self) -> DiagCode:
        ...
    @property
    def UdpDupTransition(self) -> DiagCode:
        ...
    @property
    def UdpEdgeInComb(self) -> DiagCode:
        ...
    @property
    def UdpInvalidEdgeSymbol(self) -> DiagCode:
        ...
    @property
    def UdpInvalidInputOnly(self) -> DiagCode:
        ...
    @property
    def UdpInvalidMinus(self) -> DiagCode:
        ...
    @property
    def UdpInvalidOutput(self) -> DiagCode:
        ...
    @property
    def UdpInvalidSymbol(self) -> DiagCode:
        ...
    @property
    def UdpInvalidTransition(self) -> DiagCode:
        ...
    @property
    def UdpSequentialState(self) -> DiagCode:
        ...
    @property
    def UdpSingleChar(self) -> DiagCode:
        ...
    @property
    def UdpTransSameChar(self) -> DiagCode:
        ...
    @property
    def UdpTransitionLength(self) -> DiagCode:
        ...
    @property
    def UdpWrongInputCount(self) -> DiagCode:
        ...
    @property
    def UnassignedVariable(self) -> DiagCode:
        ...
    @property
    def UnbalancedMacroArgDims(self) -> DiagCode:
        ...
    @property
    def UnboundedNotAllowed(self) -> DiagCode:
        ...
    @property
    def UnconnectedArg(self) -> DiagCode:
        ...
    @property
    def UnconnectedNamedPort(self) -> DiagCode:
        ...
    @property
    def UnconnectedUnnamedPort(self) -> DiagCode:
        ...
    @property
    def UndeclaredButFoundPackage(self) -> DiagCode:
        ...
    @property
    def UndeclaredIdentifier(self) -> DiagCode:
        ...
    @property
    def UndefineBuiltinDirective(self) -> DiagCode:
        ...
    @property
    def UndrivenNet(self) -> DiagCode:
        ...
    @property
    def UndrivenPort(self) -> DiagCode:
        ...
    @property
    def UnexpectedClockingExpr(self) -> DiagCode:
        ...
    @property
    def UnexpectedConditionalDirective(self) -> DiagCode:
        ...
    @property
    def UnexpectedConstraintBlock(self) -> DiagCode:
        ...
    @property
    def UnexpectedEdgeKeyword(self) -> DiagCode:
        ...
    @property
    def UnexpectedLetPortKeyword(self) -> DiagCode:
        ...
    @property
    def UnexpectedNameToken(self) -> DiagCode:
        ...
    @property
    def UnexpectedPortDecl(self) -> DiagCode:
        ...
    @property
    def UnexpectedQualifiers(self) -> DiagCode:
        ...
    @property
    def UnexpectedSelection(self) -> DiagCode:
        ...
    @property
    def UnexpectedWithClause(self) -> DiagCode:
        ...
    @property
    def UnicodeBOM(self) -> DiagCode:
        ...
    @property
    def UniquePriorityAfterElse(self) -> DiagCode:
        ...
    @property
    def UnknownClassMember(self) -> DiagCode:
        ...
    @property
    def UnknownClassOrPackage(self) -> DiagCode:
        ...
    @property
    def UnknownConstraintLiteral(self) -> DiagCode:
        ...
    @property
    def UnknownCovergroupMember(self) -> DiagCode:
        ...
    @property
    def UnknownDiagPragmaArg(self) -> DiagCode:
        ...
    @property
    def UnknownDirective(self) -> DiagCode:
        ...
    @property
    def UnknownEscapeCode(self) -> DiagCode:
        ...
    @property
    def UnknownFormatSpecifier(self) -> DiagCode:
        ...
    @property
    def UnknownInterface(self) -> DiagCode:
        ...
    @property
    def UnknownLibrary(self) -> DiagCode:
        ...
    @property
    def UnknownMember(self) -> DiagCode:
        ...
    @property
    def UnknownModule(self) -> DiagCode:
        ...
    @property
    def UnknownPackage(self) -> DiagCode:
        ...
    @property
    def UnknownPackageMember(self) -> DiagCode:
        ...
    @property
    def UnknownPragma(self) -> DiagCode:
        ...
    @property
    def UnknownPrimitive(self) -> DiagCode:
        ...
    @property
    def UnknownProtectEncoding(self) -> DiagCode:
        ...
    @property
    def UnknownProtectKeyword(self) -> DiagCode:
        ...
    @property
    def UnknownProtectOption(self) -> DiagCode:
        ...
    @property
    def UnknownSystemMethod(self) -> DiagCode:
        ...
    @property
    def UnknownSystemName(self) -> DiagCode:
        ...
    @property
    def UnknownSystemTimingCheck(self) -> DiagCode:
        ...
    @property
    def UnknownWarningOption(self) -> DiagCode:
        ...
    @property
    def UnpackedArrayParamType(self) -> DiagCode:
        ...
    @property
    def UnpackedConcatAssociative(self) -> DiagCode:
        ...
    @property
    def UnpackedConcatSize(self) -> DiagCode:
        ...
    @property
    def UnpackedSigned(self) -> DiagCode:
        ...
    @property
    def UnrecognizedKeywordVersion(self) -> DiagCode:
        ...
    @property
    def UnresolvedForwardTypedef(self) -> DiagCode:
        ...
    @property
    def UnsizedInConcat(self) -> DiagCode:
        ...
    @property
    def UnterminatedBlockComment(self) -> DiagCode:
        ...
    @property
    def UnusedArgument(self) -> DiagCode:
        ...
    @property
    def UnusedAssertionDecl(self) -> DiagCode:
        ...
    @property
    def UnusedButSetNet(self) -> DiagCode:
        ...
    @property
    def UnusedButSetPort(self) -> DiagCode:
        ...
    @property
    def UnusedButSetVariable(self) -> DiagCode:
        ...
    @property
    def UnusedConfigCell(self) -> DiagCode:
        ...
    @property
    def UnusedConfigInstance(self) -> DiagCode:
        ...
    @property
    def UnusedDefinition(self) -> DiagCode:
        ...
    @property
    def UnusedGenvar(self) -> DiagCode:
        ...
    @property
    def UnusedImplicitNet(self) -> DiagCode:
        ...
    @property
    def UnusedNet(self) -> DiagCode:
        ...
    @property
    def UnusedParameter(self) -> DiagCode:
        ...
    @property
    def UnusedPort(self) -> DiagCode:
        ...
    @property
    def UnusedPortDecl(self) -> DiagCode:
        ...
    @property
    def UnusedResult(self) -> DiagCode:
        ...
    @property
    def UnusedTypeParameter(self) -> DiagCode:
        ...
    @property
    def UnusedTypedef(self) -> DiagCode:
        ...
    @property
    def UnusedVariable(self) -> DiagCode:
        ...
    @property
    def UsedBeforeDeclared(self) -> DiagCode:
        ...
    @property
    def UselessCast(self) -> DiagCode:
        ...
    @property
    def UserDefPartialDriver(self) -> DiagCode:
        ...
    @property
    def UserDefPortMixedConcat(self) -> DiagCode:
        ...
    @property
    def UserDefPortTwoSided(self) -> DiagCode:
        ...
    @property
    def ValueExceedsMaxBitWidth(self) -> DiagCode:
        ...
    @property
    def ValueMustBeIntegral(self) -> DiagCode:
        ...
    @property
    def ValueMustBePositive(self) -> DiagCode:
        ...
    @property
    def ValueMustNotBeUnknown(self) -> DiagCode:
        ...
    @property
    def ValueOutOfRange(self) -> DiagCode:
        ...
    @property
    def ValueRangeUnbounded(self) -> DiagCode:
        ...
    @property
    def VarDeclWithDelay(self) -> DiagCode:
        ...
    @property
    def VarWithInterfacePort(self) -> DiagCode:
        ...
    @property
    def VectorLiteralOverflow(self) -> DiagCode:
        ...
    @property
    def VirtualArgCountMismatch(self) -> DiagCode:
        ...
    @property
    def VirtualArgDirectionMismatch(self) -> DiagCode:
        ...
    @property
    def VirtualArgNameMismatch(self) -> DiagCode:
        ...
    @property
    def VirtualArgNoDerivedDefault(self) -> DiagCode:
        ...
    @property
    def VirtualArgNoParentDefault(self) -> DiagCode:
        ...
    @property
    def VirtualArgTypeMismatch(self) -> DiagCode:
        ...
    @property
    def VirtualIfaceDefparam(self) -> DiagCode:
        ...
    @property
    def VirtualInterfaceIfaceMember(self) -> DiagCode:
        ...
    @property
    def VirtualInterfaceUnionMember(self) -> DiagCode:
        ...
    @property
    def VirtualKindMismatch(self) -> DiagCode:
        ...
    @property
    def VirtualReturnMismatch(self) -> DiagCode:
        ...
    @property
    def VoidAssignment(self) -> DiagCode:
        ...
    @property
    def VoidCastFuncCall(self) -> DiagCode:
        ...
    @property
    def VoidNotAllowed(self) -> DiagCode:
        ...
    @property
    def WarnUnknownLibrary(self) -> DiagCode:
        ...
    @property
    def WarningTask(self) -> DiagCode:
        ...
    @property
    def WidthExpand(self) -> DiagCode:
        ...
    @property
    def WidthTruncate(self) -> DiagCode:
        ...
    @property
    def WildcardPortGenericIface(self) -> DiagCode:
        ...
    @property
    def WireDataType(self) -> DiagCode:
        ...
    @property
    def WithClauseNotAllowed(self) -> DiagCode:
        ...
    @property
    def WriteToInputClockVar(self) -> DiagCode:
        ...
    @property
    def WrongBindTargetDef(self) -> DiagCode:
        ...
    @property
    def WrongLanguageVersion(self) -> DiagCode:
        ...
    @property
    def WrongNumberAssignmentPatterns(self) -> DiagCode:
        ...
    @property
    def WrongSpecifyDelayCount(self) -> DiagCode:
        ...
class DimensionKind:
    AbbreviatedRange: typing.ClassVar[DimensionKind]  # value = <DimensionKind.AbbreviatedRange: 2>
    Associative: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Associative: 4>
    DPIOpenArray: typing.ClassVar[DimensionKind]  # value = <DimensionKind.DPIOpenArray: 6>
    Dynamic: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Dynamic: 3>
    Queue: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Queue: 5>
    Range: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Range: 1>
    Unknown: typing.ClassVar[DimensionKind]  # value = <DimensionKind.Unknown: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DimensionSpecifierSyntax(SyntaxNode):
    pass
class DirectiveSyntax(SyntaxNode):
    directive: Token
class DisableConstraintSyntax(ConstraintItemSyntax):
    disable: Token
    name: NameSyntax
    semi: Token
    soft: Token
class DisableForkStatement(Statement):
    pass
class DisableForkStatementSyntax(StatementSyntax):
    disable: Token
    fork: Token
    semi: Token
class DisableIffAssertionExpr(AssertionExpr):
    @property
    def condition(self) -> Expression:
        ...
    @property
    def expr(self) -> AssertionExpr:
        ...
class DisableIffSyntax(SyntaxNode):
    closeParen: Token
    disable: Token
    expr: ExpressionSyntax
    iff: Token
    openParen: Token
class DisableSoftConstraint(Constraint):
    @property
    def target(self) -> Expression:
        ...
class DisableStatement(Statement):
    @property
    def isHierarchical(self) -> bool:
        ...
    @property
    def target(self) -> Symbol:
        ...
class DisableStatementSyntax(StatementSyntax):
    disable: Token
    name: NameSyntax
    semi: Token
class DistConstraintListSyntax(SyntaxNode):
    closeBrace: Token
    dist: Token
    items: SeparatedSyntaxList[DistItemSyntax]
    openBrace: Token
class DistExpression(Expression):
    class DistItem:
        @property
        def value(self) -> Expression:
            ...
        @property
        def weight(self) -> DistExpression.DistWeight | None:
            ...
    class DistWeight:
        class Kind:
            PerRange: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerRange: 1>
            PerValue: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerValue: 0>
            def __eq__(self, other: typing.Any) -> bool:
                ...
            def __getstate__(self) -> int:
                ...
            def __hash__(self) -> int:
                ...
            def __index__(self) -> int:
                ...
            def __init__(self, value: int) -> None:
                ...
            def __int__(self) -> int:
                ...
            def __ne__(self, other: typing.Any) -> bool:
                ...
            def __repr__(self) -> str:
                ...
            def __setstate__(self, state: int) -> None:
                ...
            def __str__(self) -> str:
                ...
            @property
            def __doc__(self) -> str:
                ...
            @property
            def __members__(self) -> dict:
                ...
            @property
            def name(self) -> str:
                ...
            @property
            def value(self) -> int:
                ...
        PerRange: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerRange: 1>
        PerValue: typing.ClassVar[DistExpression.DistWeight.Kind]  # value = <Kind.PerValue: 0>
        @property
        def expr(self) -> Expression:
            ...
        @property
        def kind(self) -> DistExpression.DistWeight.Kind:
            ...
    @property
    def items(self) -> span[DistExpression::DistItem]:
        ...
    @property
    def left(self) -> Expression:
        ...
class DistItemSyntax(SyntaxNode):
    range: ExpressionSyntax
    weight: DistWeightSyntax
class DistWeightSyntax(SyntaxNode):
    expr: ExpressionSyntax
    extraOp: Token
    op: Token
class DividerClauseSyntax(SyntaxNode):
    divide: Token
    value: Token
class DoWhileLoopStatement(Statement):
    @property
    def body(self) -> Statement:
        ...
    @property
    def cond(self) -> Expression:
        ...
class DoWhileStatementSyntax(StatementSyntax):
    closeParen: Token
    doKeyword: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    statement: StatementSyntax
    whileKeyword: Token
class DotMemberClauseSyntax(SyntaxNode):
    dot: Token
    member: Token
class DriveStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    comma: Token
    openParen: Token
    strength0: Token
    strength1: Token
class Driver:
    languageVersion: LanguageVersion
    def __init__(self) -> None:
        ...
    def addStandardArgs(self) -> None:
        ...
    def createCompilation(self) -> Compilation:
        ...
    def createOptionBag(self) -> Bag:
        ...
    def parseAllSources(self) -> bool:
        ...
    def parseCommandLine(self, arg: str, parseOptions: CommandLineOptions = CommandLineOptions()) -> bool:
        ...
    def processCommandFiles(self, fileName: str, makeRelative: bool, separateUnit: bool) -> bool:
        ...
    def processOptions(self) -> bool:
        ...
    def reportCompilation(self, compilation: Compilation, quiet: bool) -> bool:
        ...
    def reportMacros(self) -> None:
        ...
    def reportParseDiags(self) -> bool:
        ...
    def runPreprocessor(self, includeComments: bool, includeDirectives: bool, obfuscateIds: bool, useFixedObfuscationSeed: bool = False) -> bool:
        ...
    @property
    def diagClient(self) -> TextDiagnosticClient:
        ...
    @property
    def diagEngine(self) -> DiagnosticEngine:
        ...
    @property
    def sourceLoader(self) -> SourceLoader:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
    @property
    def syntaxTrees(self) -> list[SyntaxTree]:
        ...
class DriverKind:
    Continuous: typing.ClassVar[DriverKind]  # value = <DriverKind.Continuous: 1>
    Other: typing.ClassVar[DriverKind]  # value = <DriverKind.Other: 2>
    Procedural: typing.ClassVar[DriverKind]  # value = <DriverKind.Procedural: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class DynamicArrayType(Type):
    @property
    def elementType(self) -> Type:
        ...
class EdgeControlSpecifierSyntax(SyntaxNode):
    closeBracket: Token
    descriptors: SeparatedSyntaxList[EdgeDescriptorSyntax]
    openBracket: Token
class EdgeDescriptorSyntax(SyntaxNode):
    t1: Token
    t2: Token
class EdgeKind:
    BothEdges: typing.ClassVar[EdgeKind]  # value = <EdgeKind.BothEdges: 3>
    NegEdge: typing.ClassVar[EdgeKind]  # value = <EdgeKind.NegEdge: 2>
    None_: typing.ClassVar[EdgeKind]  # value = <EdgeKind.None: 0>
    PosEdge: typing.ClassVar[EdgeKind]  # value = <EdgeKind.PosEdge: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EdgeSensitivePathSuffixSyntax(PathSuffixSyntax):
    closeParen: Token
    colon: Token
    expr: ExpressionSyntax
    openParen: Token
    outputs: SeparatedSyntaxList[NameSyntax]
    polarityOperator: Token
class ElabSystemTaskKind:
    Error: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Error: 1>
    Fatal: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Fatal: 0>
    Info: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Info: 3>
    StaticAssert: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.StaticAssert: 4>
    Warning: typing.ClassVar[ElabSystemTaskKind]  # value = <ElabSystemTaskKind.Warning: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ElabSystemTaskSymbol(Symbol):
    @property
    def assertCondition(self) -> Expression:
        ...
    @property
    def message(self) -> str | None:
        ...
    @property
    def taskKind(self) -> ElabSystemTaskKind:
        ...
class ElabSystemTaskSyntax(MemberSyntax):
    arguments: ArgumentListSyntax
    name: Token
    semi: Token
class ElementSelectExpression(Expression):
    @property
    def selector(self) -> Expression:
        ...
    @property
    def value(self) -> Expression:
        ...
class ElementSelectExpressionSyntax(ExpressionSyntax):
    left: ExpressionSyntax
    select: ElementSelectSyntax
class ElementSelectSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax
class ElseClauseSyntax(SyntaxNode):
    clause: SyntaxNode
    elseKeyword: Token
class ElseConstraintClauseSyntax(SyntaxNode):
    constraints: ConstraintItemSyntax
    elseKeyword: Token
class ElsePropertyClauseSyntax(SyntaxNode):
    elseKeyword: Token
    expr: PropertyExprSyntax
class EmptyArgumentExpression(Expression):
    pass
class EmptyArgumentSyntax(ArgumentSyntax):
    placeholder: Token
class EmptyIdentifierNameSyntax(NameSyntax):
    placeholder: Token
class EmptyMemberSymbol(Symbol):
    pass
class EmptyMemberSyntax(MemberSyntax):
    qualifiers: TokenList
    semi: Token
class EmptyNonAnsiPortSyntax(NonAnsiPortSyntax):
    placeholder: Token
class EmptyPortConnectionSyntax(PortConnectionSyntax):
    placeholder: Token
class EmptyQueueExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    openBrace: Token
class EmptyStatement(Statement):
    pass
class EmptyStatementSyntax(StatementSyntax):
    semicolon: Token
class EmptyTimingCheckArgSyntax(TimingCheckArgSyntax):
    placeholder: Token
class EnumType(IntegralType, Scope):
    @property
    def baseType(self) -> Type:
        ...
    @property
    def systemId(self) -> int:
        ...
class EnumTypeSyntax(DataTypeSyntax):
    baseType: DataTypeSyntax
    closeBrace: Token
    dimensions: SyntaxList[VariableDimensionSyntax]
    keyword: Token
    members: SeparatedSyntaxList[DeclaratorSyntax]
    openBrace: Token
class EnumValueSymbol(ValueSymbol):
    @property
    def value(self) -> ConstantValue:
        ...
class EqualsAssertionArgClauseSyntax(SyntaxNode):
    equals: Token
    expr: PropertyExprSyntax
class EqualsTypeClauseSyntax(SyntaxNode):
    equals: Token
    type: DataTypeSyntax
class EqualsValueClauseSyntax(SyntaxNode):
    equals: Token
    expr: ExpressionSyntax
class ErrorType(Type):
    pass
class EvalContext:
    class Frame:
        @property
        def callLocation(self) -> SourceLocation:
            ...
        @property
        def lookupLocation(self) -> 'LookupLocation':
            ...
        @property
        def subroutine(self) -> SubroutineSymbol:
            ...
        @property
        def temporaries(self) -> dict[ValueSymbol, ConstantValue]:
            ...
    queueTarget: ConstantValue
    def __init__(self, astCtx: ASTContext, flags: EvalFlags = EvalFlags()) -> None:
        ...
    def createLocal(self, symbol: ValueSymbol, value: ConstantValue = None) -> ConstantValue:
        ...
    def deleteLocal(self, symbol: ValueSymbol) -> None:
        ...
    def dumpStack(self) -> str:
        ...
    def findLocal(self, symbol: ValueSymbol) -> ConstantValue:
        ...
    def popFrame(self) -> None:
        ...
    def popLValue(self) -> None:
        ...
    def pushEmptyFrame(self) -> None:
        ...
    def pushFrame(self, subroutine: SubroutineSymbol, callLocation: SourceLocation, lookupLocation: 'LookupLocation') -> bool:
        ...
    def pushLValue(self, lval: LValue) -> None:
        ...
    def setDisableTarget(self, arg0: Symbol, arg1: SourceRange) -> None:
        ...
    def step(self, loc: SourceLocation) -> bool:
        ...
    @property
    def cacheResults(self) -> bool:
        ...
    @property
    def diagnostics(self) -> Diagnostics:
        ...
    @property
    def disableRange(self) -> SourceRange:
        ...
    @property
    def disableTarget(self) -> Symbol:
        ...
    @property
    def flags(self) -> EvalFlags:
        ...
    @property
    def inFunction(self) -> bool:
        ...
    @property
    def topFrame(self) -> EvalContext.Frame:
        ...
    @property
    def topLValue(self) -> LValue:
        ...
class EvalFlags:
    AllowUnboundedPlaceholder: typing.ClassVar[EvalFlags]  # value = <EvalFlags.AllowUnboundedPlaceholder: 16>
    CacheResults: typing.ClassVar[EvalFlags]  # value = <EvalFlags.CacheResults: 2>
    CovergroupExpr: typing.ClassVar[EvalFlags]  # value = <EvalFlags.CovergroupExpr: 8>
    IsScript: typing.ClassVar[EvalFlags]  # value = <EvalFlags.IsScript: 1>
    None_: typing.ClassVar[EvalFlags]  # value = <EvalFlags.None: 0>
    SpecparamsAllowed: typing.ClassVar[EvalFlags]  # value = <EvalFlags.SpecparamsAllowed: 4>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class EvaluatedDimension:
    @property
    def associativeType(self) -> Type:
        ...
    @property
    def isRange(self) -> bool:
        ...
    @property
    def kind(self) -> DimensionKind:
        ...
    @property
    def queueMaxSize(self) -> int:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class EventControlSyntax(TimingControlSyntax):
    at: Token
    eventName: ExpressionSyntax
class EventControlWithExpressionSyntax(TimingControlSyntax):
    at: Token
    expr: EventExpressionSyntax
class EventExpressionSyntax(SequenceExprSyntax):
    pass
class EventListControl(TimingControl):
    @property
    def events(self) -> span[TimingControl]:
        ...
class EventTriggerStatement(Statement):
    @property
    def isNonBlocking(self) -> bool:
        ...
    @property
    def target(self) -> Expression:
        ...
    @property
    def timing(self) -> TimingControl:
        ...
class EventTriggerStatementSyntax(StatementSyntax):
    name: NameSyntax
    semi: Token
    timing: TimingControlSyntax
    trigger: Token
class EventType(Type):
    pass
class ExplicitAnsiPortSyntax(MemberSyntax):
    closeParen: Token
    direction: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
class ExplicitImportSymbol(Symbol):
    @property
    def importName(self) -> str:
        ...
    @property
    def importedSymbol(self) -> Symbol:
        ...
    @property
    def isFromExport(self) -> bool:
        ...
    @property
    def package(self) -> PackageSymbol:
        ...
    @property
    def packageName(self) -> str:
        ...
class ExplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    closeParen: Token
    dot: Token
    expr: PortExpressionSyntax
    name: Token
    openParen: Token
class Expression:
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext) -> ConstantValue:
        ...
    def evalLValue(self, context: EvalContext) -> LValue:
        ...
    def getSymbolReference(self, allowPacked: bool = True) -> Symbol:
        ...
    def isImplicitlyAssignableTo(self, compilation: Compilation, type: Type) -> bool:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def constant(self) -> ConstantValue:
        ...
    @property
    def effectiveWidth(self) -> int | None:
        ...
    @property
    def hasHierarchicalReference(self) -> bool:
        ...
    @property
    def isImplicitString(self) -> bool:
        ...
    @property
    def isUnsizedInteger(self) -> bool:
        ...
    @property
    def kind(self) -> ExpressionKind:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
    @property
    def syntax(self) -> ExpressionSyntax:
        ...
    @property
    def type(self) -> Type:
        ...
class ExpressionConstraint(Constraint):
    @property
    def expr(self) -> Expression:
        ...
    @property
    def isSoft(self) -> bool:
        ...
class ExpressionConstraintSyntax(ConstraintItemSyntax):
    expr: ExpressionSyntax
    semi: Token
    soft: Token
class ExpressionCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    expr: ExpressionSyntax
class ExpressionKind:
    ArbitrarySymbol: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ArbitrarySymbol: 25>
    AssertionInstance: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.AssertionInstance: 39>
    Assignment: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Assignment: 14>
    BinaryOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.BinaryOp: 11>
    Call: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Call: 21>
    ClockingEvent: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ClockingEvent: 38>
    Concatenation: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Concatenation: 15>
    ConditionalOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ConditionalOp: 12>
    Conversion: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Conversion: 22>
    CopyClass: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.CopyClass: 36>
    DataType: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.DataType: 23>
    Dist: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Dist: 32>
    ElementSelect: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ElementSelect: 18>
    EmptyArgument: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.EmptyArgument: 30>
    HierarchicalValue: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.HierarchicalValue: 9>
    Inside: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Inside: 13>
    IntegerLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.IntegerLiteral: 1>
    Invalid: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Invalid: 0>
    LValueReference: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.LValueReference: 26>
    MemberAccess: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.MemberAccess: 20>
    MinTypMax: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.MinTypMax: 37>
    NamedValue: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NamedValue: 8>
    NewArray: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewArray: 33>
    NewClass: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewClass: 34>
    NewCovergroup: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NewCovergroup: 35>
    NullLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.NullLiteral: 5>
    RangeSelect: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.RangeSelect: 19>
    RealLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.RealLiteral: 2>
    ReplicatedAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ReplicatedAssignmentPattern: 29>
    Replication: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Replication: 16>
    SimpleAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.SimpleAssignmentPattern: 27>
    Streaming: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.Streaming: 17>
    StringLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.StringLiteral: 7>
    StructuredAssignmentPattern: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.StructuredAssignmentPattern: 28>
    TaggedUnion: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TaggedUnion: 40>
    TimeLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TimeLiteral: 3>
    TypeReference: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.TypeReference: 24>
    UnaryOp: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnaryOp: 10>
    UnbasedUnsizedIntegerLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnbasedUnsizedIntegerLiteral: 4>
    UnboundedLiteral: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.UnboundedLiteral: 6>
    ValueRange: typing.ClassVar[ExpressionKind]  # value = <ExpressionKind.ValueRange: 31>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ExpressionOrDistSyntax(ExpressionSyntax):
    distribution: DistConstraintListSyntax
    expr: ExpressionSyntax
class ExpressionPatternSyntax(PatternSyntax):
    expr: ExpressionSyntax
class ExpressionStatement(Statement):
    @property
    def expr(self) -> Expression:
        ...
class ExpressionStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    semi: Token
class ExpressionSyntax(SyntaxNode):
    pass
class ExpressionTimingCheckArgSyntax(TimingCheckArgSyntax):
    expr: ExpressionSyntax
class ExtendsClauseSyntax(SyntaxNode):
    arguments: ArgumentListSyntax
    baseName: NameSyntax
    defaultedArg: DefaultExtendsClauseArgSyntax
    keyword: Token
class ExternInterfaceMethodSyntax(MemberSyntax):
    externKeyword: Token
    forkJoin: Token
    prototype: FunctionPrototypeSyntax
    semi: Token
class ExternModuleDeclSyntax(MemberSyntax):
    actualAttributes: SyntaxList[AttributeInstanceSyntax]
    externKeyword: Token
    header: ModuleHeaderSyntax
class ExternUdpDeclSyntax(MemberSyntax):
    actualAttributes: SyntaxList[AttributeInstanceSyntax]
    externKeyword: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token
class FieldSymbol(VariableSymbol):
    @property
    def bitOffset(self) -> int:
        ...
    @property
    def fieldIndex(self) -> int:
        ...
    @property
    def randMode(self) -> RandMode:
        ...
class FilePathSpecSyntax(SyntaxNode):
    path: Token
class FirstMatchAssertionExpr(AssertionExpr):
    @property
    def matchItems(self) -> span[Expression]:
        ...
    @property
    def seq(self) -> AssertionExpr:
        ...
class FirstMatchSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    first_match: Token
    matchList: SequenceMatchListSyntax
    openParen: Token
class FixedSizeUnpackedArrayType(Type):
    @property
    def elementType(self) -> Type:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class FloatingType(Type):
    class Kind:
        Real: typing.ClassVar[FloatingType.Kind]  # value = <Kind.Real: 0>
        RealTime: typing.ClassVar[FloatingType.Kind]  # value = <Kind.RealTime: 2>
        ShortReal: typing.ClassVar[FloatingType.Kind]  # value = <Kind.ShortReal: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Real: typing.ClassVar[FloatingType.Kind]  # value = <Kind.Real: 0>
    RealTime: typing.ClassVar[FloatingType.Kind]  # value = <Kind.RealTime: 2>
    ShortReal: typing.ClassVar[FloatingType.Kind]  # value = <Kind.ShortReal: 1>
    @property
    def floatKind(self) -> FloatingType.Kind:
        ...
class ForLoopStatement(Statement):
    @property
    def body(self) -> Statement:
        ...
    @property
    def initializers(self) -> span[Expression]:
        ...
    @property
    def loopVars(self) -> span[VariableSymbol]:
        ...
    @property
    def steps(self) -> span[Expression]:
        ...
    @property
    def stopExpr(self) -> Expression:
        ...
class ForLoopStatementSyntax(StatementSyntax):
    closeParen: Token
    forKeyword: Token
    initializers: SeparatedSyntaxList[SyntaxNode]
    openParen: Token
    semi1: Token
    semi2: Token
    statement: StatementSyntax
    steps: SeparatedSyntaxList[ExpressionSyntax]
    stopExpr: ExpressionSyntax
class ForVariableDeclarationSyntax(SyntaxNode):
    declarator: DeclaratorSyntax
    type: DataTypeSyntax
    varKeyword: Token
class ForeachConstraint(Constraint):
    @property
    def arrayRef(self) -> Expression:
        ...
    @property
    def body(self) -> Constraint:
        ...
    @property
    def loopDims(self) -> span[ForeachLoopStatement.LoopDim]:
        ...
class ForeachLoopListSyntax(SyntaxNode):
    arrayName: NameSyntax
    closeBracket: Token
    closeParen: Token
    loopVariables: SeparatedSyntaxList[NameSyntax]
    openBracket: Token
    openParen: Token
class ForeachLoopStatement(Statement):
    class LoopDim:
        @property
        def loopVar(self) -> IteratorSymbol:
            ...
        @property
        def range(self) -> ConstantRange | None:
            ...
    @property
    def arrayRef(self) -> Expression:
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def loopDims(self) -> span[ForeachLoopStatement::LoopDim]:
        ...
class ForeachLoopStatementSyntax(StatementSyntax):
    keyword: Token
    loopList: ForeachLoopListSyntax
    statement: StatementSyntax
class ForeverLoopStatement(Statement):
    @property
    def body(self) -> Statement:
        ...
class ForeverStatementSyntax(StatementSyntax):
    foreverKeyword: Token
    statement: StatementSyntax
class FormalArgumentSymbol(VariableSymbol):
    @property
    def defaultValue(self) -> Expression:
        ...
    @property
    def direction(self) -> ArgumentDirection:
        ...
class ForwardTypeRestriction:
    Class: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Class: 4>
    Enum: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Enum: 1>
    InterfaceClass: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.InterfaceClass: 5>
    None_: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.None: 0>
    Struct: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Struct: 2>
    Union: typing.ClassVar[ForwardTypeRestriction]  # value = <ForwardTypeRestriction.Union: 3>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ForwardTypeRestrictionSyntax(SyntaxNode):
    keyword1: Token
    keyword2: Token
class ForwardTypedefDeclarationSyntax(MemberSyntax):
    name: Token
    semi: Token
    typeRestriction: ForwardTypeRestrictionSyntax
    typedefKeyword: Token
class ForwardingTypedefSymbol(Symbol):
    @property
    def nextForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def typeRestriction(self) -> ForwardTypeRestriction:
        ...
    @property
    def visibility(self) -> Visibility | None:
        ...
class FunctionDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    items: SyntaxList[SyntaxNode]
    prototype: FunctionPrototypeSyntax
    semi: Token
class FunctionPortBaseSyntax(SyntaxNode):
    pass
class FunctionPortListSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[FunctionPortBaseSyntax]
class FunctionPortSyntax(FunctionPortBaseSyntax):
    attributes: SyntaxList[AttributeInstanceSyntax]
    constKeyword: Token
    dataType: DataTypeSyntax
    declarator: DeclaratorSyntax
    direction: Token
    staticKeyword: Token
    varKeyword: Token
class FunctionPrototypeSyntax(SyntaxNode):
    keyword: Token
    lifetime: Token
    name: NameSyntax
    portList: FunctionPortListSyntax
    returnType: DataTypeSyntax
    specifiers: SyntaxList[ClassSpecifierSyntax]
class GenerateBlockArraySymbol(Symbol, Scope):
    @property
    def constructIndex(self) -> int:
        ...
    @property
    def entries(self) -> span[GenerateBlockSymbol]:
        ...
    @property
    def externalName(self) -> str:
        ...
    @property
    def valid(self) -> bool:
        ...
class GenerateBlockSymbol(Symbol, Scope):
    @property
    def arrayIndex(self) -> SVInt:
        ...
    @property
    def constructIndex(self) -> int:
        ...
    @property
    def externalName(self) -> str:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
class GenerateBlockSyntax(MemberSyntax):
    begin: Token
    beginName: NamedBlockClauseSyntax
    end: Token
    endName: NamedBlockClauseSyntax
    label: NamedLabelSyntax
    members: SyntaxList[MemberSyntax]
class GenerateRegionSyntax(MemberSyntax):
    endgenerate: Token
    keyword: Token
    members: SyntaxList[MemberSyntax]
class GenericClassDefSymbol(Symbol):
    @property
    def defaultSpecialization(self) -> Type:
        ...
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def invalidSpecialization(self) -> Type:
        ...
    @property
    def isInterface(self) -> bool:
        ...
class GenvarDeclarationSyntax(MemberSyntax):
    identifiers: SeparatedSyntaxList[IdentifierNameSyntax]
    keyword: Token
    semi: Token
class GenvarSymbol(Symbol):
    pass
class HierarchicalInstanceSyntax(SyntaxNode):
    closeParen: Token
    connections: SeparatedSyntaxList[PortConnectionSyntax]
    decl: InstanceNameSyntax
    openParen: Token
class HierarchicalValueExpression(ValueExpressionBase):
    pass
class HierarchyInstantiationSyntax(MemberSyntax):
    instances: SeparatedSyntaxList[HierarchicalInstanceSyntax]
    parameters: ParameterValueAssignmentSyntax
    semi: Token
    type: Token
class IdWithExprCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    id: Token
    withClause: WithClauseSyntax
class IdentifierNameSyntax(NameSyntax):
    identifier: Token
class IdentifierSelectNameSyntax(NameSyntax):
    identifier: Token
    selectors: SyntaxList[ElementSelectSyntax]
class IfGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: ElseClauseSyntax
    keyword: Token
    openParen: Token
class IfNonePathDeclarationSyntax(MemberSyntax):
    keyword: Token
    path: PathDeclarationSyntax
class IffEventClauseSyntax(SyntaxNode):
    expr: ExpressionSyntax
    iff: Token
class ImmediateAssertionMemberSyntax(MemberSyntax):
    statement: ImmediateAssertionStatementSyntax
class ImmediateAssertionStatement(Statement):
    @property
    def assertionKind(self) -> AssertionKind:
        ...
    @property
    def cond(self) -> Expression:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
    @property
    def isDeferred(self) -> bool:
        ...
    @property
    def isFinal(self) -> bool:
        ...
class ImmediateAssertionStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    delay: DeferredAssertionSyntax
    expr: ParenthesizedExpressionSyntax
    keyword: Token
class ImplementsClauseSyntax(SyntaxNode):
    interfaces: SeparatedSyntaxList[NameSyntax]
    keyword: Token
class ImplicationConstraint(Constraint):
    @property
    def body(self) -> Constraint:
        ...
    @property
    def predicate(self) -> Expression:
        ...
class ImplicationConstraintSyntax(ConstraintItemSyntax):
    arrow: Token
    constraints: ConstraintItemSyntax
    left: ExpressionSyntax
class ImplicitAnsiPortSyntax(MemberSyntax):
    declarator: DeclaratorSyntax
    header: PortHeaderSyntax
class ImplicitEventControl(TimingControl):
    pass
class ImplicitEventControlSyntax(TimingControlSyntax):
    at: Token
    closeParen: Token
    openParen: Token
    star: Token
class ImplicitNonAnsiPortSyntax(NonAnsiPortSyntax):
    expr: PortExpressionSyntax
class ImplicitTypeSyntax(DataTypeSyntax):
    dimensions: SyntaxList[VariableDimensionSyntax]
    placeholder: Token
    signing: Token
class IncludeDirectiveSyntax(DirectiveSyntax):
    fileName: Token
class InsideExpression(Expression):
    @property
    def left(self) -> Expression:
        ...
    @property
    def rangeList(self) -> span[Expression]:
        ...
class InsideExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    inside: Token
    ranges: RangeListSyntax
class InstanceArraySymbol(Symbol, Scope):
    @property
    def arrayName(self) -> str:
        ...
    @property
    def elements(self) -> span[Symbol]:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class InstanceBodySymbol(Symbol, Scope):
    def findPort(self, portName: str) -> Symbol:
        ...
    def hasSameType(self, other: InstanceBodySymbol) -> bool:
        ...
    @property
    def definition(self) -> DefinitionSymbol:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
    @property
    def parameters(self) -> span[ParameterSymbolBase]:
        ...
    @property
    def parentInstance(self) -> InstanceSymbol:
        ...
    @property
    def portList(self) -> span[Symbol]:
        ...
class InstanceConfigRuleSyntax(ConfigRuleSyntax):
    instance: Token
    instanceNames: SyntaxList[ConfigInstanceIdentifierSyntax]
    ruleClause: ConfigRuleClauseSyntax
    semi: Token
    topModule: Token
class InstanceNameSyntax(SyntaxNode):
    dimensions: SyntaxList[VariableDimensionSyntax]
    name: Token
class InstanceSymbol(InstanceSymbolBase):
    @typing.overload
    def getPortConnection(self, port: PortSymbol) -> PortConnection:
        ...
    @typing.overload
    def getPortConnection(self, port: MultiPortSymbol) -> PortConnection:
        ...
    @typing.overload
    def getPortConnection(self, port: InterfacePortSymbol) -> PortConnection:
        ...
    @property
    def body(self) -> InstanceBodySymbol:
        ...
    @property
    def definition(self) -> DefinitionSymbol:
        ...
    @property
    def isInterface(self) -> bool:
        ...
    @property
    def isModule(self) -> bool:
        ...
    @property
    def portConnections(self) -> span[PortConnection]:
        ...
class InstanceSymbolBase(Symbol):
    @property
    def arrayName(self) -> str:
        ...
    @property
    def arrayPath(self) -> span[int]:
        ...
class IntegerLiteral(Expression):
    @property
    def isDeclaredUnsized(self) -> bool:
        ...
    @property
    def value(self) -> SVInt:
        ...
class IntegerTypeSyntax(DataTypeSyntax):
    dimensions: SyntaxList[VariableDimensionSyntax]
    keyword: Token
    signing: Token
class IntegerVectorExpressionSyntax(PrimaryExpressionSyntax):
    base: Token
    size: Token
    value: Token
class IntegralFlags:
    FourState: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.FourState: 2>
    Reg: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Reg: 4>
    Signed: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Signed: 1>
    TwoState: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Unsigned: 0>
    Unsigned: typing.ClassVar[IntegralFlags]  # value = <IntegralFlags.Unsigned: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class IntegralType(Type):
    def getBitVectorRange(self) -> ConstantRange:
        ...
    def isDeclaredReg(self) -> bool:
        ...
class InterfacePortHeaderSyntax(PortHeaderSyntax):
    modport: DotMemberClauseSyntax
    nameOrKeyword: Token
class InterfacePortSymbol(Symbol):
    @property
    def connection(self) -> tuple[Symbol, ModportSymbol]:
        ...
    @property
    def declaredRange(self) -> span[ConstantRange] | None:
        ...
    @property
    def interfaceDef(self) -> DefinitionSymbol:
        ...
    @property
    def isGeneric(self) -> bool:
        ...
    @property
    def isInvalid(self) -> bool:
        ...
    @property
    def modport(self) -> str:
        ...
class IntersectClauseSyntax(SyntaxNode):
    intersect: Token
    ranges: RangeListSyntax
class InvalidAssertionExpr(AssertionExpr):
    pass
class InvalidBinsSelectExpr(BinsSelectExpr):
    pass
class InvalidConstraint(Constraint):
    pass
class InvalidExpression(Expression):
    pass
class InvalidPattern(Pattern):
    pass
class InvalidStatement(Statement):
    pass
class InvalidTimingControl(TimingControl):
    pass
class InvocationExpressionSyntax(ExpressionSyntax):
    arguments: ArgumentListSyntax
    attributes: SyntaxList[AttributeInstanceSyntax]
    left: ExpressionSyntax
class IteratorSymbol(TempVarSymbol):
    pass
class JumpStatementSyntax(StatementSyntax):
    breakOrContinue: Token
    semi: Token
class KeywordNameSyntax(NameSyntax):
    keyword: Token
class KeywordTypeSyntax(DataTypeSyntax):
    keyword: Token
class LValue:
    def __init__(self) -> None:
        ...
    def bad(self) -> bool:
        ...
    def load(self) -> ConstantValue:
        ...
    def resolve(self) -> ConstantValue:
        ...
    def store(self, value: ConstantValue) -> None:
        ...
class LValueReferenceExpression(Expression):
    pass
class LanguageVersion:
    Default: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2017: 0>
    v1800_2017: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2017: 0>
    v1800_2023: typing.ClassVar[LanguageVersion]  # value = <LanguageVersion.v1800_2023: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LetDeclSymbol(Symbol, Scope):
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class LetDeclarationSyntax(MemberSyntax):
    equals: Token
    expr: ExpressionSyntax
    identifier: Token
    let: Token
    portList: AssertionItemPortListSyntax
    semi: Token
class LexerOptions:
    languageVersion: LanguageVersion
    maxErrors: int
    def __init__(self) -> None:
        ...
class LibraryDeclarationSyntax(MemberSyntax):
    filePaths: SeparatedSyntaxList[FilePathSpecSyntax]
    incDirClause: LibraryIncDirClauseSyntax
    library: Token
    name: Token
    semi: Token
class LibraryIncDirClauseSyntax(SyntaxNode):
    filePaths: SeparatedSyntaxList[FilePathSpecSyntax]
    incdir: Token
    minus: Token
class LibraryIncludeStatementSyntax(MemberSyntax):
    filePath: FilePathSpecSyntax
    include: Token
    semi: Token
class LibraryMapSyntax(SyntaxNode):
    endOfFile: Token
    members: SyntaxList[MemberSyntax]
class LineDirectiveSyntax(DirectiveSyntax):
    fileName: Token
    level: Token
    lineNumber: Token
class LiteralBase:
    Binary: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Binary: 0>
    Decimal: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Decimal: 2>
    Hex: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Hex: 3>
    Octal: typing.ClassVar[LiteralBase]  # value = <LiteralBase.Octal: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LiteralExpressionSyntax(PrimaryExpressionSyntax):
    literal: Token
class LocalAssertionVarSymbol(VariableSymbol):
    pass
class LocalVariableDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    semi: Token
    type: DataTypeSyntax
    var: Token
class Lookup:
    @staticmethod
    def ensureAccessible(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def ensureVisible(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def findAssertionLocalVar(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def findClass(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def findTempVar(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getContainingClass(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getVisibility(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def isAccessibleFrom(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def isVisibleFrom(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def name(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def unqualified(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def unqualifiedAt(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def withinClassRandomize(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
class LookupFlags:
    AllowDeclaredAfter: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowDeclaredAfter: 2>
    AllowIncompleteForwardTypedefs: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowIncompleteForwardTypedefs: 32>
    AllowRoot: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AllowRoot: 256>
    AlwaysAllowUpward: typing.ClassVar[LookupFlags]  # value = <LookupFlags.AlwaysAllowUpward: 4096>
    DisallowWildcardImport: typing.ClassVar[LookupFlags]  # value = <LookupFlags.DisallowWildcardImport: 4>
    ForceHierarchical: typing.ClassVar[LookupFlags]  # value = <LookupFlags.ForceHierarchical: 18>
    IfacePortConn: typing.ClassVar[LookupFlags]  # value = <LookupFlags.IfacePortConn: 512>
    NoParentScope: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoParentScope: 64>
    NoSelectors: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoSelectors: 128>
    NoUndeclaredError: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoUndeclaredError: 8>
    NoUndeclaredErrorIfUninstantiated: typing.ClassVar[LookupFlags]  # value = <LookupFlags.NoUndeclaredErrorIfUninstantiated: 16>
    None_: typing.ClassVar[LookupFlags]  # value = <LookupFlags.None: 0>
    StaticInitializer: typing.ClassVar[LookupFlags]  # value = <LookupFlags.StaticInitializer: 1024>
    Type: typing.ClassVar[LookupFlags]  # value = <LookupFlags.Type: 1>
    TypeReference: typing.ClassVar[LookupFlags]  # value = <LookupFlags.TypeReference: 2048>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LookupLocation:
    __hash__: typing.ClassVar[None] = None
    @staticmethod
    def after(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def before(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __eq__(self, arg0: LookupLocation) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, scope: 'Scope', index: int) -> None:
        ...
    def __ne__(self, arg0: LookupLocation) -> bool:
        ...
    @property
    def index(self) -> SymbolIndex:
        ...
    @property
    def max(self) -> LookupLocation:
        ...
    @property
    def min(self) -> LookupLocation:
        ...
    @property
    def scope(self) -> 'Scope':
        ...
class LookupResult:
    class MemberSelector:
        @property
        def dotLocation(self) -> SourceLocation:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def nameRange(self) -> SourceRange:
            ...
    def __init__(self) -> None:
        ...
    def clear(self) -> None:
        ...
    def errorIfSelectors(self, context: ASTContext) -> None:
        ...
    def reportDiags(self, context: ASTContext) -> None:
        ...
    @property
    def diagnostics(self) -> Diagnostics:
        ...
    @property
    def flags(self) -> LookupResultFlags:
        ...
    @property
    def found(self) -> Symbol:
        ...
    @property
    def hasError(self) -> bool:
        ...
    @property
    def selectors(self) -> tuple[ElementSelectSyntax | LookupResult.MemberSelector]:
        ...
    @property
    def systemSubroutine(self) -> SystemSubroutine:
        ...
    @property
    def upwardCount(self) -> int:
        ...
class LookupResultFlags:
    FromForwardTypedef: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.FromForwardTypedef: 16>
    FromTypeParam: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.FromTypeParam: 8>
    IsHierarchical: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.IsHierarchical: 2>
    None_: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.None: 0>
    SuppressUndeclared: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.SuppressUndeclared: 4>
    WasImported: typing.ClassVar[LookupResultFlags]  # value = <LookupResultFlags.WasImported: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class LoopConstraintSyntax(ConstraintItemSyntax):
    constraints: ConstraintItemSyntax
    foreachKeyword: Token
    loopList: ForeachLoopListSyntax
class LoopGenerateSyntax(MemberSyntax):
    block: MemberSyntax
    closeParen: Token
    equals: Token
    genvar: Token
    identifier: Token
    initialExpr: ExpressionSyntax
    iterationExpr: ExpressionSyntax
    keyword: Token
    openParen: Token
    semi1: Token
    semi2: Token
    stopExpr: ExpressionSyntax
class LoopStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    repeatOrWhile: Token
    statement: StatementSyntax
class MacroActualArgumentListSyntax(SyntaxNode):
    args: SeparatedSyntaxList[MacroActualArgumentSyntax]
    closeParen: Token
    openParen: Token
class MacroActualArgumentSyntax(SyntaxNode):
    tokens: TokenList
class MacroArgumentDefaultSyntax(SyntaxNode):
    equals: Token
    tokens: TokenList
class MacroFormalArgumentListSyntax(SyntaxNode):
    args: SeparatedSyntaxList[MacroFormalArgumentSyntax]
    closeParen: Token
    openParen: Token
class MacroFormalArgumentSyntax(SyntaxNode):
    defaultValue: MacroArgumentDefaultSyntax
    name: Token
class MacroUsageSyntax(DirectiveSyntax):
    args: MacroActualArgumentListSyntax
class MatchesClauseSyntax(SyntaxNode):
    matchesKeyword: Token
    pattern: PatternSyntax
class MemberAccessExpression(Expression):
    @property
    def member(self) -> Symbol:
        ...
    @property
    def value(self) -> Expression:
        ...
class MemberAccessExpressionSyntax(ExpressionSyntax):
    dot: Token
    left: ExpressionSyntax
    name: Token
class MemberSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
class MethodFlags:
    BuiltIn: typing.ClassVar[MethodFlags]  # value = <MethodFlags.BuiltIn: 512>
    Constructor: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Constructor: 8>
    DPIContext: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DPIContext: 256>
    DPIImport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DPIImport: 128>
    DefaultedSuperArg: typing.ClassVar[MethodFlags]  # value = <MethodFlags.DefaultedSuperArg: 4096>
    Extends: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Extends: 16384>
    Final: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Final: 32768>
    ForkJoin: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ForkJoin: 2048>
    Initial: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Initial: 8192>
    InterfaceExtern: typing.ClassVar[MethodFlags]  # value = <MethodFlags.InterfaceExtern: 16>
    ModportExport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ModportExport: 64>
    ModportImport: typing.ClassVar[MethodFlags]  # value = <MethodFlags.ModportImport: 32>
    None_: typing.ClassVar[MethodFlags]  # value = <MethodFlags.None: 0>
    Pure: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Pure: 2>
    Randomize: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Randomize: 1024>
    Static: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Static: 4>
    Virtual: typing.ClassVar[MethodFlags]  # value = <MethodFlags.Virtual: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MethodPrototypeSymbol(Symbol, Scope):
    class ExternImpl:
        @property
        def impl(self) -> SubroutineSymbol:
            ...
        @property
        def nextImpl(self) -> MethodPrototypeSymbol.ExternImpl:
            ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def firstExternImpl(self) -> MethodPrototypeSymbol.ExternImpl:
        ...
    @property
    def flags(self) -> MethodFlags:
        ...
    @property
    def isVirtual(self) -> bool:
        ...
    @property
    def override(self) -> Symbol:
        ...
    @property
    def returnType(self) -> Type:
        ...
    @property
    def subroutine(self) -> SubroutineSymbol:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class MinTypMax:
    Max: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Max: 2>
    Min: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Min: 0>
    Typ: typing.ClassVar[MinTypMax]  # value = <MinTypMax.Typ: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class MinTypMaxExpression(Expression):
    @property
    def max(self) -> Expression:
        ...
    @property
    def min(self) -> Expression:
        ...
    @property
    def selected(self) -> Expression:
        ...
    @property
    def typ(self) -> Expression:
        ...
class MinTypMaxExpressionSyntax(ExpressionSyntax):
    colon1: Token
    colon2: Token
    max: ExpressionSyntax
    min: ExpressionSyntax
    typ: ExpressionSyntax
class ModportClockingPortSyntax(MemberSyntax):
    clocking: Token
    name: Token
class ModportClockingSymbol(Symbol):
    @property
    def target(self) -> Symbol:
        ...
class ModportDeclarationSyntax(MemberSyntax):
    items: SeparatedSyntaxList[ModportItemSyntax]
    keyword: Token
    semi: Token
class ModportExplicitPortSyntax(ModportPortSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
class ModportItemSyntax(SyntaxNode):
    name: Token
    ports: AnsiPortListSyntax
class ModportNamedPortSyntax(ModportPortSyntax):
    name: Token
class ModportPortSymbol(ValueSymbol):
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def explicitConnection(self) -> Expression:
        ...
    @property
    def internalSymbol(self) -> Symbol:
        ...
class ModportPortSyntax(SyntaxNode):
    pass
class ModportSimplePortListSyntax(MemberSyntax):
    direction: Token
    ports: SeparatedSyntaxList[ModportPortSyntax]
class ModportSubroutinePortListSyntax(MemberSyntax):
    importExport: Token
    ports: SeparatedSyntaxList[ModportPortSyntax]
class ModportSubroutinePortSyntax(ModportPortSyntax):
    prototype: FunctionPrototypeSyntax
class ModportSymbol(Symbol, Scope):
    @property
    def hasExports(self) -> bool:
        ...
class ModuleDeclarationSyntax(MemberSyntax):
    blockName: NamedBlockClauseSyntax
    endmodule: Token
    header: ModuleHeaderSyntax
    members: SyntaxList[MemberSyntax]
class ModuleHeaderSyntax(SyntaxNode):
    imports: SyntaxList[PackageImportDeclarationSyntax]
    lifetime: Token
    moduleKeyword: Token
    name: Token
    parameters: ParameterPortListSyntax
    ports: PortListSyntax
    semi: Token
class MultiPortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def isNullPort(self) -> bool:
        ...
    @property
    def ports(self) -> span[PortSymbol]:
        ...
    @property
    def type(self) -> Type:
        ...
class MultipleConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    concatenation: ConcatenationExpressionSyntax
    expression: ExpressionSyntax
    openBrace: Token
class NameSyntax(ExpressionSyntax):
    pass
class NameValuePragmaExpressionSyntax(PragmaExpressionSyntax):
    equals: Token
    name: Token
    value: PragmaExpressionSyntax
class NamedArgumentSyntax(ArgumentSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token
class NamedBlockClauseSyntax(SyntaxNode):
    colon: Token
    name: Token
class NamedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    name: Token
class NamedLabelSyntax(SyntaxNode):
    colon: Token
    name: Token
class NamedParamAssignmentSyntax(ParamAssignmentSyntax):
    closeParen: Token
    dot: Token
    expr: ExpressionSyntax
    name: Token
    openParen: Token
class NamedPortConnectionSyntax(PortConnectionSyntax):
    closeParen: Token
    dot: Token
    expr: PropertyExprSyntax
    name: Token
    openParen: Token
class NamedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    colon: Token
    name: Token
    pattern: PatternSyntax
class NamedTypeSyntax(DataTypeSyntax):
    name: NameSyntax
class NamedValueExpression(ValueExpressionBase):
    pass
class NetAliasSymbol(Symbol):
    @property
    def netReferences(self) -> span[Expression]:
        ...
class NetAliasSyntax(MemberSyntax):
    keyword: Token
    nets: SeparatedSyntaxList[ExpressionSyntax]
    semi: Token
class NetDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    delay: TimingControlSyntax
    expansionHint: Token
    netType: Token
    semi: Token
    strength: NetStrengthSyntax
    type: DataTypeSyntax
class NetPortHeaderSyntax(PortHeaderSyntax):
    dataType: DataTypeSyntax
    direction: Token
    netType: Token
class NetStrengthSyntax(SyntaxNode):
    pass
class NetSymbol(ValueSymbol):
    class ExpansionHint:
        None_: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.None: 0>
        Scalared: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Scalared: 2>
        Vectored: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Vectored: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    None_: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.None: 0>
    Scalared: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Scalared: 2>
    Vectored: typing.ClassVar[NetSymbol.ExpansionHint]  # value = <ExpansionHint.Vectored: 1>
    @property
    def chargeStrength(self) -> ChargeStrength | None:
        ...
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[DriveStrength | None, DriveStrength | None]:
        ...
    @property
    def expansionHint(self) -> NetSymbol.ExpansionHint:
        ...
    @property
    def isImplicit(self) -> bool:
        ...
    @property
    def netType(self) -> NetType:
        ...
class NetType(Symbol):
    class NetKind:
        Interconnect: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Interconnect: 13>
        Supply0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply0: 10>
        Supply1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply1: 11>
        Tri: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri: 4>
        Tri0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri0: 7>
        Tri1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri1: 8>
        TriAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriAnd: 5>
        TriOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriOr: 6>
        TriReg: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriReg: 9>
        UWire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UWire: 12>
        Unknown: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Unknown: 0>
        UserDefined: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UserDefined: 14>
        WAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WAnd: 2>
        WOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WOr: 3>
        Wire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Wire: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Interconnect: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Interconnect: 13>
    Supply0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply0: 10>
    Supply1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Supply1: 11>
    Tri: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri: 4>
    Tri0: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri0: 7>
    Tri1: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Tri1: 8>
    TriAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriAnd: 5>
    TriOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriOr: 6>
    TriReg: typing.ClassVar[NetType.NetKind]  # value = <NetKind.TriReg: 9>
    UWire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UWire: 12>
    Unknown: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Unknown: 0>
    UserDefined: typing.ClassVar[NetType.NetKind]  # value = <NetKind.UserDefined: 14>
    WAnd: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WAnd: 2>
    WOr: typing.ClassVar[NetType.NetKind]  # value = <NetKind.WOr: 3>
    Wire: typing.ClassVar[NetType.NetKind]  # value = <NetKind.Wire: 1>
    @staticmethod
    def getSimulatedNetType(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @property
    def declaredType(self) -> DeclaredType:
        ...
    @property
    def isBuiltIn(self) -> bool:
        ...
    @property
    def isError(self) -> bool:
        ...
    @property
    def netKind(self) -> NetType.NetKind:
        ...
    @property
    def resolutionFunction(self) -> SubroutineSymbol:
        ...
class NetTypeDeclarationSyntax(MemberSyntax):
    keyword: Token
    name: Token
    semi: Token
    type: DataTypeSyntax
    withFunction: WithFunctionClauseSyntax
class NewArrayExpression(Expression):
    @property
    def initExpr(self) -> Expression:
        ...
    @property
    def sizeExpr(self) -> Expression:
        ...
class NewArrayExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    initializer: ParenthesizedExpressionSyntax
    newKeyword: NameSyntax
    openBracket: Token
    sizeExpr: ExpressionSyntax
class NewClassExpression(Expression):
    @property
    def constructorCall(self) -> Expression:
        ...
    @property
    def isSuperClass(self) -> bool:
        ...
class NewClassExpressionSyntax(ExpressionSyntax):
    argList: ArgumentListSyntax
    scopedNew: NameSyntax
class NewCovergroupExpression(Expression):
    @property
    def arguments(self) -> span[Expression]:
        ...
class NonAnsiPortListSyntax(PortListSyntax):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[NonAnsiPortSyntax]
class NonAnsiPortSyntax(SyntaxNode):
    pass
class NonAnsiUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    openParen: Token
    ports: SeparatedSyntaxList[IdentifierNameSyntax]
    semi: Token
class NonConstantFunction(SimpleSystemSubroutine):
    def __init__(self, name: str, returnType: Type, requiredArgs: int = 0, argTypes: list[Type] = [], isMethod: bool = False) -> None:
        ...
class Null:
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class NullLiteral(Expression):
    pass
class NullType(Type):
    pass
class NumberPragmaExpressionSyntax(PragmaExpressionSyntax):
    base: Token
    size: Token
    value: Token
class OneStepDelayControl(TimingControl):
    pass
class OneStepDelaySyntax(TimingControlSyntax):
    hash: Token
    oneStep: Token
class OrderedArgumentSyntax(ArgumentSyntax):
    expr: PropertyExprSyntax
class OrderedParamAssignmentSyntax(ParamAssignmentSyntax):
    expr: ExpressionSyntax
class OrderedPortConnectionSyntax(PortConnectionSyntax):
    expr: PropertyExprSyntax
class OrderedStructurePatternMemberSyntax(StructurePatternMemberSyntax):
    pattern: PatternSyntax
class PackageExportAllDeclarationSyntax(MemberSyntax):
    doubleColon: Token
    keyword: Token
    semi: Token
    star1: Token
    star2: Token
class PackageExportDeclarationSyntax(MemberSyntax):
    items: SeparatedSyntaxList[PackageImportItemSyntax]
    keyword: Token
    semi: Token
class PackageImportDeclarationSyntax(MemberSyntax):
    items: SeparatedSyntaxList[PackageImportItemSyntax]
    keyword: Token
    semi: Token
class PackageImportItemSyntax(SyntaxNode):
    doubleColon: Token
    item: Token
    package: Token
class PackageSymbol(Symbol, Scope):
    def findForImport(self, name: str) -> Symbol:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def defaultNetType(self) -> NetType:
        ...
    @property
    def exportDecls(self) -> span[PackageImportItemSyntax]:
        ...
    @property
    def hasExportAll(self) -> bool:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class PackedArrayType(IntegralType):
    @property
    def elementType(self) -> Type:
        ...
    @property
    def range(self) -> ConstantRange:
        ...
class PackedStructType(IntegralType, Scope):
    @property
    def systemId(self) -> int:
        ...
class PackedUnionType(IntegralType, Scope):
    @property
    def isSoft(self) -> bool:
        ...
    @property
    def isTagged(self) -> bool:
        ...
    @property
    def systemId(self) -> int:
        ...
    @property
    def tagBits(self) -> int:
        ...
class ParamAssignmentSyntax(SyntaxNode):
    pass
class ParameterDeclarationBaseSyntax(SyntaxNode):
    keyword: Token
class ParameterDeclarationStatementSyntax(MemberSyntax):
    parameter: ParameterDeclarationBaseSyntax
    semi: Token
class ParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    type: DataTypeSyntax
class ParameterPortListSyntax(SyntaxNode):
    closeParen: Token
    declarations: SeparatedSyntaxList[ParameterDeclarationBaseSyntax]
    hash: Token
    openParen: Token
class ParameterSymbol(ValueSymbol, ParameterSymbolBase):
    @property
    def isOverridden(self) -> bool:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class ParameterSymbolBase:
    @property
    def hasDefault(self) -> bool:
        ...
    @property
    def isBodyParam(self) -> bool:
        ...
    @property
    def isLocalParam(self) -> bool:
        ...
    @property
    def isPortParam(self) -> bool:
        ...
class ParameterValueAssignmentSyntax(SyntaxNode):
    closeParen: Token
    hash: Token
    openParen: Token
    parameters: SeparatedSyntaxList[ParamAssignmentSyntax]
class ParenExpressionListSyntax(SyntaxNode):
    closeParen: Token
    expressions: SeparatedSyntaxList[ExpressionSyntax]
    openParen: Token
class ParenPragmaExpressionSyntax(PragmaExpressionSyntax):
    closeParen: Token
    openParen: Token
    values: SeparatedSyntaxList[PragmaExpressionSyntax]
class ParenthesizedBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    closeParen: Token
    expr: BinsSelectExpressionSyntax
    openParen: Token
class ParenthesizedConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    closeParen: Token
    openParen: Token
    operand: ConditionalDirectiveExpressionSyntax
class ParenthesizedEventExpressionSyntax(EventExpressionSyntax):
    closeParen: Token
    expr: EventExpressionSyntax
    openParen: Token
class ParenthesizedExpressionSyntax(PrimaryExpressionSyntax):
    closeParen: Token
    expression: ExpressionSyntax
    openParen: Token
class ParenthesizedPatternSyntax(PatternSyntax):
    closeParen: Token
    openParen: Token
    pattern: PatternSyntax
class ParenthesizedPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: PropertyExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token
class ParenthesizedSequenceExprSyntax(SequenceExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    matchList: SequenceMatchListSyntax
    openParen: Token
    repetition: SequenceRepetitionSyntax
class ParserOptions:
    languageVersion: LanguageVersion
    maxRecursionDepth: int
    def __init__(self) -> None:
        ...
class PathDeclarationSyntax(MemberSyntax):
    closeParen: Token
    delays: SeparatedSyntaxList[ExpressionSyntax]
    desc: PathDescriptionSyntax
    equals: Token
    openParen: Token
    semi: Token
class PathDescriptionSyntax(SyntaxNode):
    closeParen: Token
    edgeIdentifier: Token
    inputs: SeparatedSyntaxList[NameSyntax]
    openParen: Token
    pathOperator: Token
    polarityOperator: Token
    suffix: PathSuffixSyntax
class PathSuffixSyntax(SyntaxNode):
    pass
class Pattern:
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext, value: ConstantValue, conditionKind: CaseStatementCondition) -> ConstantValue:
        ...
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> PatternKind:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
    @property
    def syntax(self) -> SyntaxNode:
        ...
class PatternCaseItemSyntax(CaseItemSyntax):
    colon: Token
    expr: ExpressionSyntax
    pattern: PatternSyntax
    statement: StatementSyntax
    tripleAnd: Token
class PatternCaseStatement(Statement):
    class ItemGroup:
        @property
        def filter(self) -> Expression:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @property
    def check(self) -> UniquePriorityCheck:
        ...
    @property
    def condition(self) -> CaseStatementCondition:
        ...
    @property
    def defaultCase(self) -> Statement:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def items(self) -> span[PatternCaseStatement::ItemGroup]:
        ...
class PatternKind:
    Constant: typing.ClassVar[PatternKind]  # value = <PatternKind.Constant: 2>
    Invalid: typing.ClassVar[PatternKind]  # value = <PatternKind.Invalid: 0>
    Structure: typing.ClassVar[PatternKind]  # value = <PatternKind.Structure: 5>
    Tagged: typing.ClassVar[PatternKind]  # value = <PatternKind.Tagged: 4>
    Variable: typing.ClassVar[PatternKind]  # value = <PatternKind.Variable: 3>
    Wildcard: typing.ClassVar[PatternKind]  # value = <PatternKind.Wildcard: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PatternSyntax(SyntaxNode):
    pass
class PatternVarSymbol(TempVarSymbol):
    pass
class PortConcatenationSyntax(PortExpressionSyntax):
    closeBrace: Token
    openBrace: Token
    references: SeparatedSyntaxList[PortReferenceSyntax]
class PortConnection:
    @property
    def expression(self) -> Expression:
        ...
    @property
    def ifaceConn(self) -> tuple[Symbol, ModportSymbol]:
        ...
    @property
    def port(self) -> Symbol:
        ...
class PortConnectionSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
class PortDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    header: PortHeaderSyntax
    semi: Token
class PortExpressionSyntax(SyntaxNode):
    pass
class PortHeaderSyntax(SyntaxNode):
    pass
class PortListSyntax(SyntaxNode):
    pass
class PortReferenceSyntax(PortExpressionSyntax):
    name: Token
    select: ElementSelectSyntax
class PortSymbol(Symbol):
    @property
    def direction(self) -> ArgumentDirection:
        ...
    @property
    def externalLoc(self) -> SourceLocation:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def internalExpr(self) -> Expression:
        ...
    @property
    def internalSymbol(self) -> Symbol:
        ...
    @property
    def isAnsiPort(self) -> bool:
        ...
    @property
    def isNetPort(self) -> bool:
        ...
    @property
    def isNullPort(self) -> bool:
        ...
    @property
    def type(self) -> Type:
        ...
class PostfixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: SyntaxList[AttributeInstanceSyntax]
    operand: ExpressionSyntax
    operatorToken: Token
class PragmaDirectiveSyntax(DirectiveSyntax):
    args: SeparatedSyntaxList[PragmaExpressionSyntax]
    name: Token
class PragmaExpressionSyntax(SyntaxNode):
    pass
class PredefinedIntegerType(IntegralType):
    class Kind:
        Byte: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Byte: 3>
        Int: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Int: 1>
        Integer: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Integer: 4>
        LongInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.LongInt: 2>
        ShortInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.ShortInt: 0>
        Time: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Time: 5>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Byte: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Byte: 3>
    Int: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Int: 1>
    Integer: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Integer: 4>
    LongInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.LongInt: 2>
    ShortInt: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.ShortInt: 0>
    Time: typing.ClassVar[PredefinedIntegerType.Kind]  # value = <Kind.Time: 5>
    @property
    def integerKind(self) -> PredefinedIntegerType.Kind:
        ...
class PrefixUnaryExpressionSyntax(ExpressionSyntax):
    attributes: SyntaxList[AttributeInstanceSyntax]
    operand: ExpressionSyntax
    operatorToken: Token
class PreprocessorOptions:
    additionalIncludePaths: list[os.PathLike]
    ignoreDirectives: set[str]
    languageVersion: LanguageVersion
    maxIncludeDepth: int
    predefineSource: str
    predefines: list[str]
    undefines: list[str]
    def __init__(self) -> None:
        ...
class PrimaryBlockEventExpressionSyntax(BlockEventExpressionSyntax):
    keyword: Token
    name: NameSyntax
class PrimaryExpressionSyntax(ExpressionSyntax):
    pass
class PrimitiveInstanceSymbol(InstanceSymbolBase):
    @property
    def delay(self) -> TimingControl:
        ...
    @property
    def driveStrength(self) -> tuple[DriveStrength | None, DriveStrength | None]:
        ...
    @property
    def portConnections(self) -> span[Expression]:
        ...
    @property
    def primitiveType(self) -> PrimitiveSymbol:
        ...
class PrimitiveInstantiationSyntax(MemberSyntax):
    delay: TimingControlSyntax
    instances: SeparatedSyntaxList[HierarchicalInstanceSyntax]
    semi: Token
    strength: NetStrengthSyntax
    type: Token
class PrimitivePortDirection:
    In: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.In: 0>
    InOut: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.InOut: 3>
    Out: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.Out: 1>
    OutReg: typing.ClassVar[PrimitivePortDirection]  # value = <PrimitivePortDirection.OutReg: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PrimitivePortSymbol(ValueSymbol):
    @property
    def direction(self) -> PrimitivePortDirection:
        ...
class PrimitiveSymbol(Symbol, Scope):
    class PrimitiveKind:
        Fixed: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.Fixed: 1>
        NInput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NInput: 2>
        NOutput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NOutput: 3>
        UserDefined: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.UserDefined: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class TableEntry:
        @property
        def inputs(self) -> str:
            ...
        @property
        def output(self) -> str:
            ...
        @property
        def state(self) -> str:
            ...
    Fixed: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.Fixed: 1>
    NInput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NInput: 2>
    NOutput: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.NOutput: 3>
    UserDefined: typing.ClassVar[PrimitiveSymbol.PrimitiveKind]  # value = <PrimitiveKind.UserDefined: 0>
    @property
    def initVal(self) -> ConstantValue:
        ...
    @property
    def isSequential(self) -> bool:
        ...
    @property
    def ports(self) -> span[PrimitivePortSymbol]:
        ...
    @property
    def primitiveKind(self) -> PrimitiveSymbol.PrimitiveKind:
        ...
    @property
    def table(self) -> span[PrimitiveSymbol::TableEntry]:
        ...
class ProceduralAssignStatement(Statement):
    @property
    def assignment(self) -> Expression:
        ...
    @property
    def isForce(self) -> bool:
        ...
class ProceduralAssignStatementSyntax(StatementSyntax):
    expr: ExpressionSyntax
    keyword: Token
    semi: Token
class ProceduralBlockKind:
    Always: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Always: 2>
    AlwaysComb: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysComb: 3>
    AlwaysFF: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysFF: 5>
    AlwaysLatch: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.AlwaysLatch: 4>
    Final: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Final: 1>
    Initial: typing.ClassVar[ProceduralBlockKind]  # value = <ProceduralBlockKind.Initial: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ProceduralBlockSymbol(Symbol):
    @property
    def body(self) -> Statement:
        ...
    @property
    def isSingleDriverBlock(self) -> bool:
        ...
    @property
    def procedureKind(self) -> ProceduralBlockKind:
        ...
class ProceduralBlockSyntax(MemberSyntax):
    keyword: Token
    statement: StatementSyntax
class ProceduralCheckerStatement(Statement):
    @property
    def instances(self) -> span[Symbol]:
        ...
class ProceduralDeassignStatement(Statement):
    @property
    def isRelease(self) -> bool:
        ...
    @property
    def lvalue(self) -> Expression:
        ...
class ProceduralDeassignStatementSyntax(StatementSyntax):
    keyword: Token
    semi: Token
    variable: ExpressionSyntax
class ProductionSyntax(SyntaxNode):
    colon: Token
    dataType: DataTypeSyntax
    name: Token
    portList: FunctionPortListSyntax
    rules: SeparatedSyntaxList[RsRuleSyntax]
    semi: Token
class PropertyCaseItemSyntax(SyntaxNode):
    pass
class PropertyDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    propertySpec: PropertySpecSyntax
    semi: Token
    variables: SyntaxList[LocalVariableDeclarationSyntax]
class PropertyExprSyntax(SyntaxNode):
    pass
class PropertySpecSyntax(SyntaxNode):
    clocking: TimingControlSyntax
    disable: DisableIffSyntax
    expr: PropertyExprSyntax
class PropertySymbol(Symbol, Scope):
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class PropertyType(Type):
    pass
class PullStrengthSyntax(NetStrengthSyntax):
    closeParen: Token
    openParen: Token
    strength: Token
class PulseStyleDeclarationSyntax(MemberSyntax):
    inputs: SeparatedSyntaxList[NameSyntax]
    keyword: Token
    semi: Token
class PulseStyleKind:
    NoShowCancelled: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.NoShowCancelled: 3>
    OnDetect: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.OnDetect: 1>
    OnEvent: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.OnEvent: 0>
    ShowCancelled: typing.ClassVar[PulseStyleKind]  # value = <PulseStyleKind.ShowCancelled: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class PulseStyleSymbol(Symbol):
    @property
    def pulseStyleKind(self) -> PulseStyleKind:
        ...
    @property
    def terminals(self) -> span[Expression]:
        ...
class QueueDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    dollar: Token
    maxSizeClause: ColonExpressionClauseSyntax
class QueueType(Type):
    @property
    def elementType(self) -> Type:
        ...
    @property
    def maxBound(self) -> int:
        ...
class RandCaseItemSyntax(SyntaxNode):
    colon: Token
    expr: ExpressionSyntax
    statement: StatementSyntax
class RandCaseStatement(Statement):
    class Item:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def stmt(self) -> Statement:
            ...
    @property
    def items(self) -> span[RandCaseStatement::Item]:
        ...
class RandCaseStatementSyntax(StatementSyntax):
    endCase: Token
    items: SyntaxList[RandCaseItemSyntax]
    randCase: Token
class RandJoinClauseSyntax(SyntaxNode):
    expr: ParenthesizedExpressionSyntax
    join: Token
    rand: Token
class RandMode:
    None_: typing.ClassVar[RandMode]  # value = <RandMode.None: 0>
    Rand: typing.ClassVar[RandMode]  # value = <RandMode.Rand: 1>
    RandC: typing.ClassVar[RandMode]  # value = <RandMode.RandC: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RandSeqProductionSymbol(Symbol, Scope):
    class CaseItem:
        @property
        def expressions(self) -> span[Expression]:
            ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class CaseProd(RandSeqProductionSymbol.ProdBase):
        @property
        def defaultItem(self) -> RandSeqProductionSymbol.ProdItem | None:
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def items(self) -> span[RandSeqProductionSymbol.CaseItem]:
            ...
    class CodeBlockProd(RandSeqProductionSymbol.ProdBase):
        @property
        def block(self) -> StatementBlockSymbol:
            ...
    class IfElseProd(RandSeqProductionSymbol.ProdBase):
        @property
        def elseItem(self) -> RandSeqProductionSymbol.ProdItem | None:
            ...
        @property
        def expr(self) -> Expression:
            ...
        @property
        def ifItem(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class ProdBase:
        @property
        def kind(self) -> RandSeqProductionSymbol.ProdKind:
            ...
    class ProdItem(RandSeqProductionSymbol.ProdBase):
        @property
        def args(self) -> span[Expression]:
            ...
        @property
        def target(self) -> RandSeqProductionSymbol:
            ...
    class ProdKind:
        Case: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Case: 4>
        CodeBlock: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.CodeBlock: 1>
        IfElse: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.IfElse: 2>
        Item: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Item: 0>
        Repeat: typing.ClassVar[RandSeqProductionSymbol.ProdKind]  # value = <ProdKind.Repeat: 3>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class RepeatProd(RandSeqProductionSymbol.ProdBase):
        @property
        def expr(self) -> Expression:
            ...
        @property
        def item(self) -> RandSeqProductionSymbol.ProdItem:
            ...
    class Rule:
        @property
        def codeBlock(self) -> RandSeqProductionSymbol.CodeBlockProd | None:
            ...
        @property
        def isRandJoin(self) -> bool:
            ...
        @property
        def prods(self) -> span[RandSeqProductionSymbol.ProdBase]:
            ...
        @property
        def randJoinExpr(self) -> Expression:
            ...
        @property
        def ruleBlock(self) -> StatementBlockSymbol:
            ...
        @property
        def weightExpr(self) -> Expression:
            ...
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def returnType(self) -> Type:
        ...
    @property
    def rules(self) -> span[RandSeqProductionSymbol::Rule]:
        ...
class RandSequenceStatement(Statement):
    @property
    def firstProduction(self) -> RandSeqProductionSymbol:
        ...
class RandSequenceStatementSyntax(StatementSyntax):
    closeParen: Token
    endsequence: Token
    firstProduction: Token
    openParen: Token
    productions: SyntaxList[ProductionSyntax]
    randsequence: Token
class RangeCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    ranges: RangeListSyntax
    withClause: WithClauseSyntax
class RangeDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    selector: SelectorSyntax
class RangeListSyntax(SyntaxNode):
    closeBrace: Token
    openBrace: Token
    valueRanges: SeparatedSyntaxList[ExpressionSyntax]
class RangeSelectExpression(Expression):
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
    @property
    def selectionKind(self) -> RangeSelectionKind:
        ...
    @property
    def value(self) -> Expression:
        ...
class RangeSelectSyntax(SelectorSyntax):
    left: ExpressionSyntax
    range: Token
    right: ExpressionSyntax
class RangeSelectionKind:
    IndexedDown: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.IndexedDown: 2>
    IndexedUp: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.IndexedUp: 1>
    Simple: typing.ClassVar[RangeSelectionKind]  # value = <RangeSelectionKind.Simple: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class RealLiteral(Expression):
    @property
    def value(self) -> float:
        ...
class RepeatLoopStatement(Statement):
    @property
    def body(self) -> Statement:
        ...
    @property
    def count(self) -> Expression:
        ...
class RepeatedEventControl(TimingControl):
    @property
    def event(self) -> TimingControl:
        ...
    @property
    def expr(self) -> Expression:
        ...
class RepeatedEventControlSyntax(TimingControlSyntax):
    closeParen: Token
    eventControl: TimingControlSyntax
    expr: ExpressionSyntax
    openParen: Token
    repeat: Token
class ReplicatedAssignmentPatternExpression(AssignmentPatternExpressionBase):
    @property
    def count(self) -> Expression:
        ...
class ReplicatedAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    countExpr: ExpressionSyntax
    innerCloseBrace: Token
    innerOpenBrace: Token
    items: SeparatedSyntaxList[ExpressionSyntax]
    openBrace: Token
class ReplicationExpression(Expression):
    @property
    def concat(self) -> Expression:
        ...
    @property
    def count(self) -> Expression:
        ...
class ReportedDiagnostic:
    @property
    def expansionLocs(self) -> span[SourceLocation]:
        ...
    @property
    def formattedMessage(self) -> str:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def originalDiagnostic(self) -> Diagnostic:
        ...
    @property
    def ranges(self) -> span[SourceRange]:
        ...
    @property
    def severity(self) -> DiagnosticSeverity:
        ...
    @property
    def shouldShowIncludeStack(self) -> bool:
        ...
class ReturnStatement(Statement):
    @property
    def expr(self) -> Expression:
        ...
class ReturnStatementSyntax(StatementSyntax):
    returnKeyword: Token
    returnValue: ExpressionSyntax
    semi: Token
class RootSymbol(Symbol, Scope):
    @property
    def compilationUnits(self) -> span[CompilationUnitSymbol]:
        ...
    @property
    def topInstances(self) -> span[InstanceSymbol]:
        ...
class RsCaseItemSyntax(SyntaxNode):
    pass
class RsCaseSyntax(RsProdSyntax):
    closeParen: Token
    endcase: Token
    expr: ExpressionSyntax
    items: SyntaxList[RsCaseItemSyntax]
    keyword: Token
    openParen: Token
class RsCodeBlockSyntax(RsProdSyntax):
    closeBrace: Token
    items: SyntaxList[SyntaxNode]
    openBrace: Token
class RsElseClauseSyntax(SyntaxNode):
    item: RsProdItemSyntax
    keyword: Token
class RsIfElseSyntax(RsProdSyntax):
    closeParen: Token
    condition: ExpressionSyntax
    elseClause: RsElseClauseSyntax
    ifItem: RsProdItemSyntax
    keyword: Token
    openParen: Token
class RsProdItemSyntax(RsProdSyntax):
    argList: ArgumentListSyntax
    name: Token
class RsProdSyntax(SyntaxNode):
    pass
class RsRepeatSyntax(RsProdSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    item: RsProdItemSyntax
    keyword: Token
    openParen: Token
class RsRuleSyntax(SyntaxNode):
    prods: SyntaxList[RsProdSyntax]
    randJoin: RandJoinClauseSyntax
    weightClause: RsWeightClauseSyntax
class RsWeightClauseSyntax(SyntaxNode):
    codeBlock: RsProdSyntax
    colonEqual: Token
    weight: ExpressionSyntax
class SVInt:
    @staticmethod
    def concat(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def conditional(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def createFillX(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def createFillZ(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromDigits(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromDouble(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromFloat(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def logicalEquiv(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def logicalImpl(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @typing.overload
    def __add__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __add__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __and__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __and__(self, arg0: int) -> SVInt:
        ...
    def __bool__(self) -> bool:
        ...
    @typing.overload
    def __eq__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __eq__(self, arg0: int) -> logic_t:
        ...
    def __float__(self) -> float:
        ...
    @typing.overload
    def __ge__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __ge__(self, arg0: int) -> logic_t:
        ...
    def __getitem__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __gt__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __gt__(self, arg0: int) -> logic_t:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __iadd__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __iadd__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __iand__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __iand__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __imod__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __imod__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __imul__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __imul__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, bit: logic_t) -> None:
        ...
    @typing.overload
    def __init__(self, bits: int, value: int, isSigned: bool) -> None:
        ...
    @typing.overload
    def __init__(self, bits: int, bytes: span[int], isSigned: bool) -> None:
        ...
    @typing.overload
    def __init__(self, str: str) -> None:
        ...
    @typing.overload
    def __init__(self, value: float) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> SVInt:
        ...
    @typing.overload
    def __ior__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __ior__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __isub__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __isub__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __itruediv__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __itruediv__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __ixor__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __ixor__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __le__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __le__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __lt__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __lt__(self, arg0: int) -> logic_t:
        ...
    @typing.overload
    def __mod__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __mod__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __mul__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __mul__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __ne__(self, arg0: SVInt) -> logic_t:
        ...
    @typing.overload
    def __ne__(self, arg0: int) -> logic_t:
        ...
    def __neg__(self) -> SVInt:
        ...
    @typing.overload
    def __or__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __or__(self, arg0: int) -> SVInt:
        ...
    def __pow__(self, arg0: SVInt) -> SVInt:
        ...
    def __radd__(self, arg0: int) -> SVInt:
        ...
    def __rand__(self, arg0: int) -> SVInt:
        ...
    def __rdiv__(self, arg0: int) -> SVInt:
        ...
    def __repr__(self) -> str:
        ...
    def __rmod__(self, arg0: int) -> SVInt:
        ...
    def __rmul__(self, arg0: int) -> SVInt:
        ...
    def __ror__(self, arg0: int) -> SVInt:
        ...
    def __rsub__(self, arg0: int) -> SVInt:
        ...
    def __rxor__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __sub__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __sub__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __truediv__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __truediv__(self, arg0: int) -> SVInt:
        ...
    @typing.overload
    def __xor__(self, arg0: SVInt) -> SVInt:
        ...
    @typing.overload
    def __xor__(self, arg0: int) -> SVInt:
        ...
    def ashr(self, rhs: SVInt) -> SVInt:
        ...
    def countLeadingOnes(self) -> int:
        ...
    def countLeadingZeros(self) -> int:
        ...
    def countOnes(self) -> int:
        ...
    def countXs(self) -> int:
        ...
    def countZeros(self) -> int:
        ...
    def countZs(self) -> int:
        ...
    def extend(self, bits: int, isSigned: bool) -> SVInt:
        ...
    def flattenUnknowns(self) -> None:
        ...
    def getActiveBits(self) -> int:
        ...
    def getMinRepresentedBits(self) -> int:
        ...
    def isEven(self) -> bool:
        ...
    def isNegative(self) -> bool:
        ...
    def isOdd(self) -> bool:
        ...
    def isSignExtendedFrom(self, msb: int) -> bool:
        ...
    def lshr(self, rhs: SVInt) -> SVInt:
        ...
    def reductionAnd(self) -> logic_t:
        ...
    def reductionOr(self) -> logic_t:
        ...
    def reductionXor(self) -> logic_t:
        ...
    def replicate(self, times: SVInt) -> SVInt:
        ...
    def resize(self, bits: int) -> SVInt:
        ...
    def reverse(self) -> SVInt:
        ...
    def set(self, msb: int, lsb: int, value: SVInt) -> None:
        ...
    def setAllOnes(self) -> None:
        ...
    def setAllX(self) -> None:
        ...
    def setAllZ(self) -> None:
        ...
    def setAllZeros(self) -> None:
        ...
    def setSigned(self, isSigned: bool) -> None:
        ...
    def sext(self, bits: int) -> SVInt:
        ...
    def shl(self, rhs: SVInt) -> SVInt:
        ...
    def shrinkToFit(self) -> None:
        ...
    def signExtendFrom(self, msb: int) -> None:
        ...
    def slice(self, msb: int, lsb: int) -> SVInt:
        ...
    def toString(self, base: LiteralBase, includeBase: bool, abbreviateThresholdBits: int = 16777215) -> str:
        ...
    def trunc(self, bits: int) -> SVInt:
        ...
    def xnor(self, rhs: SVInt) -> SVInt:
        ...
    def zext(self, bits: int) -> SVInt:
        ...
    @property
    def bitWidth(self) -> int:
        ...
    @property
    def hasUnknown(self) -> bool:
        ...
    @property
    def isSigned(self) -> bool:
        ...
class ScalarType(IntegralType):
    class Kind:
        Bit: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Bit: 0>
        Logic: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Logic: 1>
        Reg: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Reg: 2>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Bit: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Bit: 0>
    Logic: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Logic: 1>
    Reg: typing.ClassVar[ScalarType.Kind]  # value = <Kind.Reg: 2>
    @property
    def scalarKind(self) -> ScalarType.Kind:
        ...
class Scope:
    def __getitem__(self, arg0: int) -> typing.Any:
        ...
    def __iter__(self) -> typing.Iterator[Symbol]:
        ...
    def __len__(self) -> int:
        ...
    def find(self, arg0: str) -> Symbol:
        ...
    def lookupName(self, name: str, location: LookupLocation = LookupLocation(), flags: LookupFlags = LookupFlags.None_) -> Symbol:
        ...
    @property
    def compilation(self) -> Compilation:
        ...
    @property
    def containingInstance(self) -> InstanceBodySymbol:
        ...
    @property
    def defaultNetType(self) -> NetType:
        ...
    @property
    def isProceduralContext(self) -> bool:
        ...
    @property
    def isUninstantiated(self) -> bool:
        ...
    @property
    def timeScale(self) -> TimeScale | None:
        ...
class ScopedNameSyntax(NameSyntax):
    left: NameSyntax
    right: NameSyntax
    separator: Token
class ScriptSession:
    def __init__(self) -> None:
        ...
    def eval(self, text: str) -> ConstantValue:
        ...
    def evalExpression(self, expr: ExpressionSyntax) -> ConstantValue:
        ...
    def evalStatement(self, expr: StatementSyntax) -> None:
        ...
    def getDiagnostics(self) -> Diagnostics:
        ...
    @property
    def compilation(self) -> Compilation:
        ...
class SelectorSyntax(SyntaxNode):
    pass
class SequenceConcatExpr(AssertionExpr):
    class Element:
        @property
        def delay(self) -> SequenceRange:
            ...
        @property
        def sequence(self) -> AssertionExpr:
            ...
    @property
    def elements(self) -> span[SequenceConcatExpr::Element]:
        ...
class SequenceDeclarationSyntax(MemberSyntax):
    end: Token
    endBlockName: NamedBlockClauseSyntax
    keyword: Token
    name: Token
    optionalSemi: Token
    portList: AssertionItemPortListSyntax
    semi: Token
    seqExpr: SequenceExprSyntax
    variables: SyntaxList[LocalVariableDeclarationSyntax]
class SequenceExprSyntax(SyntaxNode):
    pass
class SequenceMatchListSyntax(SyntaxNode):
    comma: Token
    items: SeparatedSyntaxList[PropertyExprSyntax]
class SequenceRange:
    @property
    def max(self) -> int | None:
        ...
    @property
    def min(self) -> int:
        ...
class SequenceRepetition:
    class AdmitsEmpty:
        Depends: typing.ClassVar[SequenceRepetition.AdmitsEmpty]  # value = <AdmitsEmpty.Depends: 2>
        No: typing.ClassVar[SequenceRepetition.AdmitsEmpty]  # value = <AdmitsEmpty.No: 1>
        Yes: typing.ClassVar[SequenceRepetition.AdmitsEmpty]  # value = <AdmitsEmpty.Yes: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class Kind:
        Consecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Consecutive: 0>
        GoTo: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.GoTo: 2>
        Nonconsecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Nonconsecutive: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Consecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Consecutive: 0>
    GoTo: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.GoTo: 2>
    Nonconsecutive: typing.ClassVar[SequenceRepetition.Kind]  # value = <Kind.Nonconsecutive: 1>
    @property
    def admitsEmpty(self) -> SequenceRepetition.AdmitsEmpty:
        ...
    @property
    def kind(self) -> SequenceRepetition.Kind:
        ...
    @property
    def range(self) -> SequenceRange:
        ...
class SequenceRepetitionSyntax(SyntaxNode):
    closeBracket: Token
    op: Token
    openBracket: Token
    selector: SelectorSyntax
class SequenceSymbol(Symbol, Scope):
    @property
    def ports(self) -> span[AssertionPortSymbol]:
        ...
class SequenceType(Type):
    pass
class SequenceWithMatchExpr(AssertionExpr):
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def matchItems(self) -> span[Expression]:
        ...
    @property
    def repetition(self) -> SequenceRepetition | None:
        ...
class SetExprBinsSelectExpr(BinsSelectExpr):
    @property
    def expr(self) -> Expression:
        ...
    @property
    def matchesExpr(self) -> Expression:
        ...
class SignalEventControl(TimingControl):
    @property
    def edge(self) -> EdgeKind:
        ...
    @property
    def expr(self) -> Expression:
        ...
    @property
    def iffCondition(self) -> Expression:
        ...
class SignalEventExpressionSyntax(EventExpressionSyntax):
    edge: Token
    expr: ExpressionSyntax
    iffClause: IffEventClauseSyntax
class SignedCastExpressionSyntax(ExpressionSyntax):
    apostrophe: Token
    inner: ParenthesizedExpressionSyntax
    signing: Token
class SimpleAssertionExpr(AssertionExpr):
    @property
    def expr(self) -> Expression:
        ...
    @property
    def repetition(self) -> SequenceRepetition | None:
        ...
class SimpleAssignmentPatternExpression(AssignmentPatternExpressionBase):
    pass
class SimpleAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: SeparatedSyntaxList[ExpressionSyntax]
    openBrace: Token
class SimpleBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: ExpressionSyntax
    matchesClause: MatchesClauseSyntax
class SimpleDirectiveSyntax(DirectiveSyntax):
    pass
class SimplePathSuffixSyntax(PathSuffixSyntax):
    outputs: SeparatedSyntaxList[NameSyntax]
class SimplePragmaExpressionSyntax(PragmaExpressionSyntax):
    value: Token
class SimplePropertyExprSyntax(PropertyExprSyntax):
    expr: SequenceExprSyntax
class SimpleSequenceExprSyntax(SequenceExprSyntax):
    expr: ExpressionSyntax
    repetition: SequenceRepetitionSyntax
class SimpleSystemSubroutine(SystemSubroutine):
    def __init__(self, name: str, kind: SubroutineKind, requiredArgs: int, argTypes: list[Type], returnType: Type, isMethod: bool, isFirstArgLValue: bool = False) -> None:
        ...
class SolveBeforeConstraint(Constraint):
    @property
    def after(self) -> span[Expression]:
        ...
    @property
    def solve(self) -> span[Expression]:
        ...
class SolveBeforeConstraintSyntax(ConstraintItemSyntax):
    afterExpr: SeparatedSyntaxList[ExpressionSyntax]
    before: Token
    beforeExpr: SeparatedSyntaxList[ExpressionSyntax]
    semi: Token
    solve: Token
class SourceBuffer:
    def __bool__(self) -> bool:
        ...
    def __init__(self) -> None:
        ...
    @property
    def data(self) -> str:
        ...
    @property
    def id(self) -> BufferID:
        ...
    @property
    def library(self) -> SourceLibrary:
        ...
class SourceLibrary:
    def __init__(self) -> None:
        ...
    @property
    def name(self) -> str:
        ...
class SourceLoader:
    def __init__(self, sourceManager: SourceManager) -> None:
        ...
    def addFiles(self, pattern: str) -> None:
        ...
    def addLibraryFiles(self, libraryName: str, pattern: str) -> None:
        ...
    def addLibraryMaps(self, pattern: str, basePath: os.PathLike, optionBag: Bag) -> None:
        ...
    def addSearchDirectories(self, pattern: str) -> None:
        ...
    def addSearchExtension(self, extension: str) -> None:
        ...
    def addSeparateUnit(self, filePatterns: span[str], includePaths: list[str], defines: list[str], libraryName: str) -> None:
        ...
    def loadAndParseSources(self, optionBag: Bag) -> list[SyntaxTree]:
        ...
    def loadSources(self) -> list[SourceBuffer]:
        ...
    @property
    def errors(self) -> span[str]:
        ...
    @property
    def hasFiles(self) -> bool:
        ...
    @property
    def libraryMaps(self) -> list[SyntaxTree]:
        ...
class SourceLocation:
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: SourceLocation) -> bool:
        ...
    def __ge__(self, arg0: SourceLocation) -> bool:
        ...
    def __gt__(self, arg0: SourceLocation) -> bool:
        ...
    def __hash__(self) -> int:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, buffer: BufferID, offset: int) -> None:
        ...
    def __le__(self, arg0: SourceLocation) -> bool:
        ...
    def __lt__(self, arg0: SourceLocation) -> bool:
        ...
    def __ne__(self, arg0: SourceLocation) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    @property
    def NoLocation(self) -> SourceLocation:
        ...
    @property
    def buffer(self) -> BufferID:
        ...
    @property
    def offset(self) -> int:
        ...
class SourceManager:
    def __init__(self) -> None:
        ...
    def addDiagnosticDirective(self, location: SourceLocation, name: str, severity: DiagnosticSeverity) -> None:
        ...
    def addLineDirective(self, location: SourceLocation, lineNum: int, name: str, level: int) -> None:
        ...
    def addSystemDirectories(self, path: str) -> None:
        ...
    def addUserDirectories(self, path: str) -> None:
        ...
    @typing.overload
    def assignText(self, text: str, includedFrom: SourceLocation = ..., library: SourceLibrary = None) -> SourceBuffer:
        ...
    @typing.overload
    def assignText(self, path: str, text: str, includedFrom: SourceLocation = ..., library: SourceLibrary = None) -> SourceBuffer:
        ...
    def getAllBuffers(self) -> list[BufferID]:
        ...
    def getColumnNumber(self, location: SourceLocation) -> int:
        ...
    def getExpansionLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getExpansionRange(self, location: SourceLocation) -> SourceRange:
        ...
    def getFileName(self, location: SourceLocation) -> str:
        ...
    def getFullPath(self, buffer: BufferID) -> os.PathLike:
        ...
    def getFullyExpandedLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getFullyOriginalLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getIncludedFrom(self, buffer: BufferID) -> SourceLocation:
        ...
    def getLineNumber(self, location: SourceLocation) -> int:
        ...
    def getMacroName(self, location: SourceLocation) -> str:
        ...
    def getOriginalLoc(self, location: SourceLocation) -> SourceLocation:
        ...
    def getRawFileName(self, buffer: BufferID) -> str:
        ...
    def getSourceText(self, buffer: BufferID) -> str:
        ...
    def isCached(self, path: os.PathLike) -> bool:
        ...
    def isFileLoc(self, location: SourceLocation) -> bool:
        ...
    def isIncludedFileLoc(self, location: SourceLocation) -> bool:
        ...
    def isMacroArgLoc(self, location: SourceLocation) -> bool:
        ...
    def isMacroLoc(self, location: SourceLocation) -> bool:
        ...
    def isPreprocessedLoc(self, location: SourceLocation) -> bool:
        ...
    def readHeader(self, path: str, includedFrom: SourceLocation, library: SourceLibrary, isSystemPath: bool) -> SourceBuffer:
        ...
    def readSource(self, path: os.PathLike, library: SourceLibrary = None) -> SourceBuffer:
        ...
    def setDisableProximatePaths(self, set: bool) -> None:
        ...
class SourceOptions:
    librariesInheritMacros: bool
    numThreads: int | None
    onlyLint: bool
    singleUnit: bool
    def __init__(self) -> None:
        ...
class SourceRange:
    __hash__: typing.ClassVar[None] = None
    def __eq__(self, arg0: SourceRange) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, startLoc: SourceLocation, endLoc: SourceLocation) -> None:
        ...
    def __ne__(self, arg0: SourceRange) -> bool:
        ...
    @property
    def end(self) -> SourceLocation:
        ...
    @property
    def start(self) -> SourceLocation:
        ...
class SpecifyBlockSymbol(Symbol, Scope):
    pass
class SpecifyBlockSyntax(MemberSyntax):
    endspecify: Token
    items: SyntaxList[MemberSyntax]
    specify: Token
class SpecparamDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[SpecparamDeclaratorSyntax]
    keyword: Token
    semi: Token
    type: ImplicitTypeSyntax
class SpecparamDeclaratorSyntax(SyntaxNode):
    closeParen: Token
    comma: Token
    equals: Token
    name: Token
    openParen: Token
    value1: ExpressionSyntax
    value2: ExpressionSyntax
class SpecparamSymbol(ValueSymbol):
    @property
    def isPathPulse(self) -> bool:
        ...
    @property
    def pathDest(self) -> Symbol:
        ...
    @property
    def pathSource(self) -> Symbol:
        ...
    @property
    def pulseErrorLimit(self) -> ConstantValue:
        ...
    @property
    def pulseRejectLimit(self) -> ConstantValue:
        ...
    @property
    def value(self) -> ConstantValue:
        ...
class StandardCaseItemSyntax(CaseItemSyntax):
    clause: SyntaxNode
    colon: Token
    expressions: SeparatedSyntaxList[ExpressionSyntax]
class StandardPropertyCaseItemSyntax(PropertyCaseItemSyntax):
    colon: Token
    expr: PropertyExprSyntax
    expressions: SeparatedSyntaxList[ExpressionSyntax]
    semi: Token
class StandardRsCaseItemSyntax(RsCaseItemSyntax):
    colon: Token
    expressions: SeparatedSyntaxList[ExpressionSyntax]
    item: RsProdItemSyntax
    semi: Token
class Statement:
    class EvalResult:
        Break: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Break: 3>
        Continue: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Continue: 4>
        Disable: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Disable: 5>
        Fail: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Fail: 0>
        Return: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Return: 2>
        Success: typing.ClassVar[Statement.EvalResult]  # value = <EvalResult.Success: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    def __repr__(self) -> str:
        ...
    def eval(self, context: EvalContext) -> Statement.EvalResult:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> StatementKind:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
    @property
    def syntax(self) -> StatementSyntax:
        ...
class StatementBlockKind:
    JoinAll: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinAll: 1>
    JoinAny: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinAny: 2>
    JoinNone: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.JoinNone: 3>
    Sequential: typing.ClassVar[StatementBlockKind]  # value = <StatementBlockKind.Sequential: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StatementBlockSymbol(Symbol, Scope):
    @property
    def blockKind(self) -> StatementBlockKind:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
class StatementKind:
    Block: typing.ClassVar[StatementKind]  # value = <StatementKind.Block: 3>
    Break: typing.ClassVar[StatementKind]  # value = <StatementKind.Break: 8>
    Case: typing.ClassVar[StatementKind]  # value = <StatementKind.Case: 11>
    ConcurrentAssertion: typing.ClassVar[StatementKind]  # value = <StatementKind.ConcurrentAssertion: 21>
    Conditional: typing.ClassVar[StatementKind]  # value = <StatementKind.Conditional: 10>
    Continue: typing.ClassVar[StatementKind]  # value = <StatementKind.Continue: 7>
    Disable: typing.ClassVar[StatementKind]  # value = <StatementKind.Disable: 9>
    DisableFork: typing.ClassVar[StatementKind]  # value = <StatementKind.DisableFork: 22>
    DoWhileLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.DoWhileLoop: 17>
    Empty: typing.ClassVar[StatementKind]  # value = <StatementKind.Empty: 1>
    EventTrigger: typing.ClassVar[StatementKind]  # value = <StatementKind.EventTrigger: 26>
    ExpressionStatement: typing.ClassVar[StatementKind]  # value = <StatementKind.ExpressionStatement: 4>
    ForLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForLoop: 13>
    ForeachLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForeachLoop: 15>
    ForeverLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.ForeverLoop: 18>
    ImmediateAssertion: typing.ClassVar[StatementKind]  # value = <StatementKind.ImmediateAssertion: 20>
    Invalid: typing.ClassVar[StatementKind]  # value = <StatementKind.Invalid: 0>
    List: typing.ClassVar[StatementKind]  # value = <StatementKind.List: 2>
    PatternCase: typing.ClassVar[StatementKind]  # value = <StatementKind.PatternCase: 12>
    ProceduralAssign: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralAssign: 27>
    ProceduralChecker: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralChecker: 31>
    ProceduralDeassign: typing.ClassVar[StatementKind]  # value = <StatementKind.ProceduralDeassign: 28>
    RandCase: typing.ClassVar[StatementKind]  # value = <StatementKind.RandCase: 29>
    RandSequence: typing.ClassVar[StatementKind]  # value = <StatementKind.RandSequence: 30>
    RepeatLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.RepeatLoop: 14>
    Return: typing.ClassVar[StatementKind]  # value = <StatementKind.Return: 6>
    Timed: typing.ClassVar[StatementKind]  # value = <StatementKind.Timed: 19>
    VariableDeclaration: typing.ClassVar[StatementKind]  # value = <StatementKind.VariableDeclaration: 5>
    Wait: typing.ClassVar[StatementKind]  # value = <StatementKind.Wait: 23>
    WaitFork: typing.ClassVar[StatementKind]  # value = <StatementKind.WaitFork: 24>
    WaitOrder: typing.ClassVar[StatementKind]  # value = <StatementKind.WaitOrder: 25>
    WhileLoop: typing.ClassVar[StatementKind]  # value = <StatementKind.WhileLoop: 16>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class StatementList(Statement):
    @property
    def list(self) -> span[Statement]:
        ...
class StatementSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
    label: NamedLabelSyntax
class StreamExpressionSyntax(SyntaxNode):
    expression: ExpressionSyntax
    withRange: StreamExpressionWithRangeSyntax
class StreamExpressionWithRangeSyntax(SyntaxNode):
    range: ElementSelectSyntax
    withKeyword: Token
class StreamingConcatenationExpression(Expression):
    class StreamExpression:
        @property
        def constantWithWidth(self) -> int | None:
            ...
        @property
        def operand(self) -> Expression:
            ...
        @property
        def withExpr(self) -> Expression:
            ...
    @property
    def bitstreamWidth(self) -> int:
        ...
    @property
    def isFixedSize(self) -> bool:
        ...
    @property
    def sliceSize(self) -> int:
        ...
    @property
    def streams(self) -> span[StreamingConcatenationExpression::StreamExpression]:
        ...
class StreamingConcatenationExpressionSyntax(PrimaryExpressionSyntax):
    closeBrace: Token
    expressions: SeparatedSyntaxList[StreamExpressionSyntax]
    innerCloseBrace: Token
    innerOpenBrace: Token
    openBrace: Token
    operatorToken: Token
    sliceSize: ExpressionSyntax
class StringLiteral(Expression):
    @property
    def intValue(self) -> ConstantValue:
        ...
    @property
    def rawValue(self) -> str:
        ...
    @property
    def value(self) -> str:
        ...
class StringType(Type):
    pass
class StrongWeakAssertionExpr(AssertionExpr):
    class Strength:
        Strong: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Strong: 0>
        Weak: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Weak: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Strong: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Strong: 0>
    Weak: typing.ClassVar[StrongWeakAssertionExpr.Strength]  # value = <Strength.Weak: 1>
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def strength(self) -> StrongWeakAssertionExpr.Strength:
        ...
class StrongWeakPropertyExprSyntax(PropertyExprSyntax):
    closeParen: Token
    expr: SequenceExprSyntax
    keyword: Token
    openParen: Token
class StructUnionMemberSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    randomQualifier: Token
    semi: Token
    type: DataTypeSyntax
class StructUnionTypeSyntax(DataTypeSyntax):
    closeBrace: Token
    dimensions: SyntaxList[VariableDimensionSyntax]
    keyword: Token
    members: SyntaxList[StructUnionMemberSyntax]
    openBrace: Token
    packed: Token
    signing: Token
    taggedOrSoft: Token
class StructurePattern(Pattern):
    class FieldPattern:
        @property
        def field(self) -> FieldSymbol:
            ...
        @property
        def pattern(self) -> Pattern:
            ...
    @property
    def patterns(self) -> span[StructurePattern::FieldPattern]:
        ...
class StructurePatternMemberSyntax(SyntaxNode):
    pass
class StructurePatternSyntax(PatternSyntax):
    closeBrace: Token
    members: SeparatedSyntaxList[StructurePatternMemberSyntax]
    openBrace: Token
class StructuredAssignmentPatternExpression(AssignmentPatternExpressionBase):
    class IndexSetter:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def index(self) -> Expression:
            ...
    class MemberSetter:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def member(self) -> Symbol:
            ...
    class TypeSetter:
        @property
        def expr(self) -> Expression:
            ...
        @property
        def type(self) -> Type:
            ...
    @property
    def defaultSetter(self) -> Expression:
        ...
    @property
    def indexSetters(self) -> span[StructuredAssignmentPatternExpression::IndexSetter]:
        ...
    @property
    def memberSetters(self) -> span[StructuredAssignmentPatternExpression::MemberSetter]:
        ...
    @property
    def typeSetters(self) -> span[StructuredAssignmentPatternExpression::TypeSetter]:
        ...
class StructuredAssignmentPatternSyntax(AssignmentPatternSyntax):
    closeBrace: Token
    items: SeparatedSyntaxList[AssignmentPatternItemSyntax]
    openBrace: Token
class SubroutineKind:
    Function: typing.ClassVar[SubroutineKind]  # value = <SubroutineKind.Function: 0>
    Task: typing.ClassVar[SubroutineKind]  # value = <SubroutineKind.Task: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SubroutineSymbol(Symbol, Scope):
    @property
    def arguments(self) -> span[FormalArgumentSymbol]:
        ...
    @property
    def body(self) -> Statement:
        ...
    @property
    def defaultLifetime(self) -> VariableLifetime:
        ...
    @property
    def flags(self) -> MethodFlags:
        ...
    @property
    def isVirtual(self) -> bool:
        ...
    @property
    def override(self) -> SubroutineSymbol:
        ...
    @property
    def prototype(self) -> MethodPrototypeSymbol:
        ...
    @property
    def returnType(self) -> Type:
        ...
    @property
    def subroutineKind(self) -> SubroutineKind:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class SuperNewDefaultedArgsExpressionSyntax(ExpressionSyntax):
    closeParen: Token
    defaultKeyword: Token
    openParen: Token
    scopedNew: NameSyntax
class Symbol:
    def __repr__(self) -> str:
        ...
    @typing.overload
    def isDeclaredBefore(self, target: Symbol) -> bool | None:
        ...
    @typing.overload
    def isDeclaredBefore(self, location: LookupLocation) -> bool | None:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def declaredType(self) -> DeclaredType:
        ...
    @property
    def declaringDefinition(self) -> DefinitionSymbol:
        ...
    @property
    def hierarchicalPath(self) -> str:
        ...
    @property
    def isScope(self) -> bool:
        ...
    @property
    def isType(self) -> bool:
        ...
    @property
    def isValue(self) -> bool:
        ...
    @property
    def kind(self) -> SymbolKind:
        ...
    @property
    def lexicalPath(self) -> str:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def nextSibling(self) -> Symbol:
        ...
    @property
    def parentScope(self) -> 'Scope':
        ...
    @property
    def randMode(self) -> RandMode:
        ...
    @property
    def sourceLibrary(self) -> SourceLibrary:
        ...
    @property
    def syntax(self) -> SyntaxNode:
        ...
class SymbolKind:
    AnonymousProgram: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AnonymousProgram: 98>
    AssertionPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AssertionPort: 81>
    AssociativeArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.AssociativeArrayType: 16>
    Attribute: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Attribute: 53>
    CHandleType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CHandleType: 26>
    Checker: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Checker: 86>
    CheckerInstance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CheckerInstance: 87>
    CheckerInstanceBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CheckerInstanceBody: 88>
    ClassProperty: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClassProperty: 63>
    ClassType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClassType: 22>
    ClockVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClockVar: 83>
    ClockingBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ClockingBlock: 82>
    CompilationUnit: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CompilationUnit: 3>
    ConfigBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ConfigBlock: 100>
    ConstraintBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ConstraintBlock: 72>
    ContinuousAssign: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ContinuousAssign: 65>
    CoverCross: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverCross: 92>
    CoverCrossBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverCrossBody: 93>
    CoverageBin: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CoverageBin: 94>
    CovergroupBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CovergroupBody: 90>
    CovergroupType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.CovergroupType: 23>
    Coverpoint: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Coverpoint: 91>
    DPIOpenArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DPIOpenArrayType: 15>
    DefParam: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DefParam: 73>
    DeferredMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DeferredMember: 4>
    Definition: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Definition: 2>
    DynamicArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.DynamicArrayType: 14>
    ElabSystemTask: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ElabSystemTask: 66>
    EmptyMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EmptyMember: 6>
    EnumType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EnumType: 10>
    EnumValue: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EnumValue: 11>
    ErrorType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ErrorType: 36>
    EventType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.EventType: 28>
    ExplicitImport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ExplicitImport: 51>
    Field: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Field: 62>
    FixedSizeUnpackedArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FixedSizeUnpackedArrayType: 13>
    FloatingType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FloatingType: 9>
    FormalArgument: typing.ClassVar[SymbolKind]  # value = <SymbolKind.FormalArgument: 61>
    ForwardingTypedef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ForwardingTypedef: 37>
    GenerateBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenerateBlock: 55>
    GenerateBlockArray: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenerateBlockArray: 56>
    GenericClassDef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.GenericClassDef: 67>
    Genvar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Genvar: 54>
    Instance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Instance: 47>
    InstanceArray: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InstanceArray: 49>
    InstanceBody: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InstanceBody: 48>
    InterfacePort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.InterfacePort: 43>
    Iterator: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Iterator: 70>
    LetDecl: typing.ClassVar[SymbolKind]  # value = <SymbolKind.LetDecl: 85>
    LocalAssertionVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.LocalAssertionVar: 84>
    MethodPrototype: typing.ClassVar[SymbolKind]  # value = <SymbolKind.MethodPrototype: 68>
    Modport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Modport: 44>
    ModportClocking: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ModportClocking: 46>
    ModportPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ModportPort: 45>
    MultiPort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.MultiPort: 42>
    Net: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Net: 59>
    NetAlias: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NetAlias: 99>
    NetType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NetType: 38>
    NullType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.NullType: 25>
    Package: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Package: 50>
    PackedArrayType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedArrayType: 12>
    PackedStructType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedStructType: 18>
    PackedUnionType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PackedUnionType: 20>
    Parameter: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Parameter: 39>
    PatternVar: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PatternVar: 71>
    Port: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Port: 41>
    PredefinedIntegerType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PredefinedIntegerType: 7>
    Primitive: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Primitive: 75>
    PrimitiveInstance: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PrimitiveInstance: 77>
    PrimitivePort: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PrimitivePort: 76>
    ProceduralBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ProceduralBlock: 57>
    Property: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Property: 80>
    PropertyType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PropertyType: 33>
    PulseStyle: typing.ClassVar[SymbolKind]  # value = <SymbolKind.PulseStyle: 96>
    QueueType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.QueueType: 17>
    RandSeqProduction: typing.ClassVar[SymbolKind]  # value = <SymbolKind.RandSeqProduction: 89>
    Root: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Root: 1>
    ScalarType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.ScalarType: 8>
    Sequence: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Sequence: 79>
    SequenceType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SequenceType: 32>
    SpecifyBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SpecifyBlock: 78>
    Specparam: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Specparam: 74>
    StatementBlock: typing.ClassVar[SymbolKind]  # value = <SymbolKind.StatementBlock: 58>
    StringType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.StringType: 27>
    Subroutine: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Subroutine: 64>
    SystemTimingCheck: typing.ClassVar[SymbolKind]  # value = <SymbolKind.SystemTimingCheck: 97>
    TimingPath: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TimingPath: 95>
    TransparentMember: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TransparentMember: 5>
    TypeAlias: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeAlias: 35>
    TypeParameter: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeParameter: 40>
    TypeRefType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.TypeRefType: 30>
    UnboundedType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnboundedType: 29>
    UninstantiatedDef: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UninstantiatedDef: 69>
    Unknown: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Unknown: 0>
    UnpackedStructType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnpackedStructType: 19>
    UnpackedUnionType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UnpackedUnionType: 21>
    UntypedType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.UntypedType: 31>
    Variable: typing.ClassVar[SymbolKind]  # value = <SymbolKind.Variable: 60>
    VirtualInterfaceType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.VirtualInterfaceType: 34>
    VoidType: typing.ClassVar[SymbolKind]  # value = <SymbolKind.VoidType: 24>
    WildcardImport: typing.ClassVar[SymbolKind]  # value = <SymbolKind.WildcardImport: 52>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SyntaxKind:
    AcceptOnPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AcceptOnPropertyExpr: 4>
    ActionBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ActionBlock: 5>
    AddAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AddAssignmentExpression: 6>
    AddExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AddExpression: 7>
    AlwaysBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysBlock: 8>
    AlwaysCombBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysCombBlock: 9>
    AlwaysFFBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysFFBlock: 10>
    AlwaysLatchBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AlwaysLatchBlock: 11>
    AndAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndAssignmentExpression: 12>
    AndPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndPropertyExpr: 13>
    AndSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AndSequenceExpr: 14>
    AnonymousProgram: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnonymousProgram: 15>
    AnsiPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnsiPortList: 16>
    AnsiUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AnsiUdpPortList: 17>
    ArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArgumentList: 18>
    ArithmeticLeftShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticLeftShiftAssignmentExpression: 19>
    ArithmeticRightShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticRightShiftAssignmentExpression: 20>
    ArithmeticShiftLeftExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticShiftLeftExpression: 21>
    ArithmeticShiftRightExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArithmeticShiftRightExpression: 22>
    ArrayAndMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayAndMethod: 23>
    ArrayOrMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayOrMethod: 24>
    ArrayOrRandomizeMethodExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayOrRandomizeMethodExpression: 25>
    ArrayUniqueMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayUniqueMethod: 26>
    ArrayXorMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ArrayXorMethod: 27>
    AscendingRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AscendingRangeSelect: 28>
    AssertPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertPropertyStatement: 29>
    AssertionItemPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertionItemPort: 30>
    AssertionItemPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssertionItemPortList: 31>
    AssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentExpression: 32>
    AssignmentPatternExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentPatternExpression: 33>
    AssignmentPatternItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssignmentPatternItem: 34>
    AssumePropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AssumePropertyStatement: 35>
    AttributeInstance: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AttributeInstance: 36>
    AttributeSpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.AttributeSpec: 37>
    BadExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BadExpression: 38>
    BeginKeywordsDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BeginKeywordsDirective: 39>
    BinSelectWithFilterExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinSelectWithFilterExpr: 40>
    BinaryAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryAndExpression: 41>
    BinaryBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryBinsSelectExpr: 42>
    BinaryBlockEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryBlockEventExpression: 43>
    BinaryConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryConditionalDirectiveExpression: 44>
    BinaryEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryEventExpression: 45>
    BinaryOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryOrExpression: 46>
    BinaryXnorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryXnorExpression: 47>
    BinaryXorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinaryXorExpression: 48>
    BindDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BindDirective: 49>
    BindTargetList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BindTargetList: 50>
    BinsSelectConditionExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinsSelectConditionExpr: 51>
    BinsSelection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BinsSelection: 52>
    BitSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BitSelect: 53>
    BitType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BitType: 54>
    BlockCoverageEvent: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BlockCoverageEvent: 55>
    BlockingEventTriggerStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.BlockingEventTriggerStatement: 56>
    ByteType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ByteType: 57>
    CHandleType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CHandleType: 58>
    CaseEqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseEqualityExpression: 59>
    CaseGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseGenerate: 60>
    CaseInequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseInequalityExpression: 61>
    CasePropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CasePropertyExpr: 62>
    CaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CaseStatement: 63>
    CastExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CastExpression: 64>
    CellConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CellConfigRule: 65>
    CellDefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CellDefineDirective: 66>
    ChargeStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ChargeStrength: 67>
    CheckerDataDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerDataDeclaration: 68>
    CheckerDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerDeclaration: 69>
    CheckerInstanceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerInstanceStatement: 70>
    CheckerInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CheckerInstantiation: 71>
    ClassDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassDeclaration: 72>
    ClassMethodDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassMethodDeclaration: 73>
    ClassMethodPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassMethodPrototype: 74>
    ClassName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassName: 75>
    ClassPropertyDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassPropertyDeclaration: 76>
    ClassSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClassSpecifier: 77>
    ClockingDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingDeclaration: 78>
    ClockingDirection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingDirection: 79>
    ClockingItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingItem: 80>
    ClockingPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingPropertyExpr: 81>
    ClockingSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingSequenceExpr: 82>
    ClockingSkew: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ClockingSkew: 83>
    ColonExpressionClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ColonExpressionClause: 84>
    CompilationUnit: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CompilationUnit: 85>
    ConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConcatenationExpression: 86>
    ConcurrentAssertionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConcurrentAssertionMember: 87>
    ConditionalConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalConstraint: 88>
    ConditionalExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalExpression: 89>
    ConditionalPathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPathDeclaration: 90>
    ConditionalPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPattern: 91>
    ConditionalPredicate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPredicate: 92>
    ConditionalPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalPropertyExpr: 93>
    ConditionalStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConditionalStatement: 94>
    ConfigCellIdentifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigCellIdentifier: 95>
    ConfigDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigDeclaration: 96>
    ConfigInstanceIdentifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigInstanceIdentifier: 97>
    ConfigLiblist: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigLiblist: 98>
    ConfigUseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConfigUseClause: 99>
    ConstraintBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintBlock: 100>
    ConstraintDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintDeclaration: 101>
    ConstraintPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstraintPrototype: 102>
    ConstructorName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ConstructorName: 103>
    ContinuousAssign: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ContinuousAssign: 104>
    CopyClassExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CopyClassExpression: 105>
    CoverCross: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverCross: 106>
    CoverPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverPropertyStatement: 107>
    CoverSequenceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverSequenceStatement: 108>
    CoverageBins: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageBins: 109>
    CoverageBinsArraySize: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageBinsArraySize: 110>
    CoverageIffClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageIffClause: 111>
    CoverageOption: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CoverageOption: 112>
    CovergroupDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CovergroupDeclaration: 113>
    Coverpoint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Coverpoint: 114>
    CycleDelay: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.CycleDelay: 115>
    DPIExport: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DPIExport: 116>
    DPIImport: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DPIImport: 117>
    DataDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DataDeclaration: 118>
    Declarator: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Declarator: 119>
    DefParam: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefParam: 120>
    DefParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefParamAssignment: 121>
    DefaultCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultCaseItem: 122>
    DefaultClockingReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultClockingReference: 123>
    DefaultConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultConfigRule: 124>
    DefaultCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultCoverageBinInitializer: 125>
    DefaultDisableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultDisableDeclaration: 126>
    DefaultExtendsClauseArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultExtendsClauseArg: 127>
    DefaultFunctionPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultFunctionPort: 128>
    DefaultNetTypeDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultNetTypeDirective: 129>
    DefaultPatternKeyExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultPatternKeyExpression: 130>
    DefaultPropertyCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultPropertyCaseItem: 131>
    DefaultRsCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultRsCaseItem: 132>
    DefaultSkewItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefaultSkewItem: 133>
    DeferredAssertion: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DeferredAssertion: 134>
    DefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DefineDirective: 135>
    Delay3: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Delay3: 136>
    DelayControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayControl: 137>
    DelayedSequenceElement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayedSequenceElement: 138>
    DelayedSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DelayedSequenceExpr: 139>
    DescendingRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DescendingRangeSelect: 140>
    DisableConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableConstraint: 141>
    DisableForkStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableForkStatement: 142>
    DisableIff: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableIff: 143>
    DisableStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DisableStatement: 144>
    DistConstraintList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistConstraintList: 145>
    DistItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistItem: 146>
    DistWeight: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DistWeight: 147>
    DivideAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DivideAssignmentExpression: 148>
    DivideExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DivideExpression: 149>
    DividerClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DividerClause: 150>
    DoWhileStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DoWhileStatement: 151>
    DotMemberClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DotMemberClause: 152>
    DriveStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.DriveStrength: 153>
    EdgeControlSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeControlSpecifier: 154>
    EdgeDescriptor: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeDescriptor: 155>
    EdgeSensitivePathSuffix: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EdgeSensitivePathSuffix: 156>
    ElabSystemTask: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElabSystemTask: 157>
    ElementSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElementSelect: 158>
    ElementSelectExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElementSelectExpression: 159>
    ElsIfDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElsIfDirective: 160>
    ElseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseClause: 161>
    ElseConstraintClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseConstraintClause: 162>
    ElseDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElseDirective: 163>
    ElsePropertyClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ElsePropertyClause: 164>
    EmptyArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyArgument: 165>
    EmptyIdentifierName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyIdentifierName: 166>
    EmptyMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyMember: 167>
    EmptyNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyNonAnsiPort: 168>
    EmptyPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyPortConnection: 169>
    EmptyQueueExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyQueueExpression: 170>
    EmptyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyStatement: 171>
    EmptyTimingCheckArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EmptyTimingCheckArg: 172>
    EndCellDefineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndCellDefineDirective: 173>
    EndIfDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndIfDirective: 174>
    EndKeywordsDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EndKeywordsDirective: 175>
    EnumType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EnumType: 176>
    EqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualityExpression: 177>
    EqualsAssertionArgClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsAssertionArgClause: 178>
    EqualsTypeClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsTypeClause: 179>
    EqualsValueClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EqualsValueClause: 180>
    EventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventControl: 181>
    EventControlWithExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventControlWithExpression: 182>
    EventType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.EventType: 183>
    ExpectPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpectPropertyStatement: 184>
    ExplicitAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExplicitAnsiPort: 185>
    ExplicitNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExplicitNonAnsiPort: 186>
    ExpressionConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionConstraint: 187>
    ExpressionCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionCoverageBinInitializer: 188>
    ExpressionOrDist: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionOrDist: 189>
    ExpressionPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionPattern: 190>
    ExpressionStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionStatement: 191>
    ExpressionTimingCheckArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExpressionTimingCheckArg: 192>
    ExtendsClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExtendsClause: 193>
    ExternInterfaceMethod: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternInterfaceMethod: 194>
    ExternModuleDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternModuleDecl: 195>
    ExternUdpDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ExternUdpDecl: 196>
    FilePathSpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FilePathSpec: 197>
    FinalBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FinalBlock: 198>
    FirstMatchSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FirstMatchSequenceExpr: 199>
    FollowedByPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FollowedByPropertyExpr: 200>
    ForLoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForLoopStatement: 201>
    ForVariableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForVariableDeclaration: 202>
    ForeachLoopList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeachLoopList: 203>
    ForeachLoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeachLoopStatement: 204>
    ForeverStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForeverStatement: 205>
    ForwardTypeRestriction: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForwardTypeRestriction: 206>
    ForwardTypedefDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ForwardTypedefDeclaration: 207>
    FunctionDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionDeclaration: 208>
    FunctionPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPort: 209>
    FunctionPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPortList: 210>
    FunctionPrototype: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.FunctionPrototype: 211>
    GenerateBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenerateBlock: 212>
    GenerateRegion: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenerateRegion: 213>
    GenvarDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GenvarDeclaration: 214>
    GreaterThanEqualExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GreaterThanEqualExpression: 215>
    GreaterThanExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.GreaterThanExpression: 216>
    HierarchicalInstance: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.HierarchicalInstance: 217>
    HierarchyInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.HierarchyInstantiation: 218>
    IdWithExprCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdWithExprCoverageBinInitializer: 219>
    IdentifierName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdentifierName: 220>
    IdentifierSelectName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IdentifierSelectName: 221>
    IfDefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfDefDirective: 222>
    IfGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfGenerate: 223>
    IfNDefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfNDefDirective: 224>
    IfNonePathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IfNonePathDeclaration: 225>
    IffEventClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IffEventClause: 226>
    IffPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IffPropertyExpr: 227>
    ImmediateAssertStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssertStatement: 228>
    ImmediateAssertionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssertionMember: 229>
    ImmediateAssumeStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateAssumeStatement: 230>
    ImmediateCoverStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImmediateCoverStatement: 231>
    ImplementsClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplementsClause: 232>
    ImplicationConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicationConstraint: 233>
    ImplicationPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicationPropertyExpr: 234>
    ImplicitAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitAnsiPort: 235>
    ImplicitEventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitEventControl: 236>
    ImplicitNonAnsiPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitNonAnsiPort: 237>
    ImplicitType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImplicitType: 238>
    ImpliesPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ImpliesPropertyExpr: 239>
    IncludeDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IncludeDirective: 240>
    InequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InequalityExpression: 241>
    InitialBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InitialBlock: 242>
    InsideExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InsideExpression: 243>
    InstanceConfigRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InstanceConfigRule: 244>
    InstanceName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InstanceName: 245>
    IntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntType: 246>
    IntegerLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerLiteralExpression: 247>
    IntegerType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerType: 248>
    IntegerVectorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntegerVectorExpression: 249>
    InterfaceDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfaceDeclaration: 250>
    InterfaceHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfaceHeader: 251>
    InterfacePortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InterfacePortHeader: 252>
    IntersectClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntersectClause: 253>
    IntersectSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.IntersectSequenceExpr: 254>
    InvocationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.InvocationExpression: 255>
    JumpStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.JumpStatement: 256>
    LessThanEqualExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LessThanEqualExpression: 257>
    LessThanExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LessThanExpression: 258>
    LetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LetDeclaration: 259>
    LibraryDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryDeclaration: 260>
    LibraryIncDirClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryIncDirClause: 261>
    LibraryIncludeStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryIncludeStatement: 262>
    LibraryMap: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LibraryMap: 263>
    LineDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LineDirective: 264>
    LocalScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LocalScope: 265>
    LocalVariableDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LocalVariableDeclaration: 266>
    LogicType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicType: 267>
    LogicalAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalAndExpression: 268>
    LogicalEquivalenceExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalEquivalenceExpression: 269>
    LogicalImplicationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalImplicationExpression: 270>
    LogicalLeftShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalLeftShiftAssignmentExpression: 271>
    LogicalOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalOrExpression: 272>
    LogicalRightShiftAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalRightShiftAssignmentExpression: 273>
    LogicalShiftLeftExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalShiftLeftExpression: 274>
    LogicalShiftRightExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LogicalShiftRightExpression: 275>
    LongIntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LongIntType: 276>
    LoopConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopConstraint: 277>
    LoopGenerate: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopGenerate: 278>
    LoopStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.LoopStatement: 279>
    MacroActualArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroActualArgument: 280>
    MacroActualArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroActualArgumentList: 281>
    MacroArgumentDefault: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroArgumentDefault: 282>
    MacroFormalArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroFormalArgument: 283>
    MacroFormalArgumentList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroFormalArgumentList: 284>
    MacroUsage: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MacroUsage: 285>
    MatchesClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MatchesClause: 286>
    MemberAccessExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MemberAccessExpression: 287>
    MinTypMaxExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MinTypMaxExpression: 288>
    ModAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModAssignmentExpression: 289>
    ModExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModExpression: 290>
    ModportClockingPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportClockingPort: 291>
    ModportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportDeclaration: 292>
    ModportExplicitPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportExplicitPort: 293>
    ModportItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportItem: 294>
    ModportNamedPort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportNamedPort: 295>
    ModportSimplePortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSimplePortList: 296>
    ModportSubroutinePort: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSubroutinePort: 297>
    ModportSubroutinePortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModportSubroutinePortList: 298>
    ModuleDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModuleDeclaration: 299>
    ModuleHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ModuleHeader: 300>
    MultipleConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultipleConcatenationExpression: 301>
    MultiplyAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultiplyAssignmentExpression: 302>
    MultiplyExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.MultiplyExpression: 303>
    NameValuePragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NameValuePragmaExpression: 304>
    NamedArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedArgument: 305>
    NamedBlockClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedBlockClause: 306>
    NamedConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedConditionalDirectiveExpression: 307>
    NamedLabel: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedLabel: 308>
    NamedParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedParamAssignment: 309>
    NamedPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedPortConnection: 310>
    NamedStructurePatternMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedStructurePatternMember: 311>
    NamedType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NamedType: 312>
    NetAlias: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetAlias: 313>
    NetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetDeclaration: 314>
    NetPortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetPortHeader: 315>
    NetTypeDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NetTypeDeclaration: 316>
    NewArrayExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NewArrayExpression: 317>
    NewClassExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NewClassExpression: 318>
    NoUnconnectedDriveDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NoUnconnectedDriveDirective: 319>
    NonAnsiPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonAnsiPortList: 320>
    NonAnsiUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonAnsiUdpPortList: 321>
    NonblockingAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonblockingAssignmentExpression: 322>
    NonblockingEventTriggerStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NonblockingEventTriggerStatement: 323>
    NullLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NullLiteralExpression: 324>
    NumberPragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.NumberPragmaExpression: 325>
    OneStepDelay: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OneStepDelay: 326>
    OrAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrAssignmentExpression: 327>
    OrPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrPropertyExpr: 328>
    OrSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrSequenceExpr: 329>
    OrderedArgument: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedArgument: 330>
    OrderedParamAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedParamAssignment: 331>
    OrderedPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedPortConnection: 332>
    OrderedStructurePatternMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.OrderedStructurePatternMember: 333>
    PackageDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageDeclaration: 334>
    PackageExportAllDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageExportAllDeclaration: 335>
    PackageExportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageExportDeclaration: 336>
    PackageHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageHeader: 337>
    PackageImportDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageImportDeclaration: 338>
    PackageImportItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PackageImportItem: 339>
    ParallelBlockStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParallelBlockStatement: 340>
    ParameterDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterDeclaration: 341>
    ParameterDeclarationStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterDeclarationStatement: 342>
    ParameterPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterPortList: 343>
    ParameterValueAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParameterValueAssignment: 344>
    ParenExpressionList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenExpressionList: 345>
    ParenPragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenPragmaExpression: 346>
    ParenthesizedBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedBinsSelectExpr: 347>
    ParenthesizedConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedConditionalDirectiveExpression: 348>
    ParenthesizedEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedEventExpression: 349>
    ParenthesizedExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedExpression: 350>
    ParenthesizedPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedPattern: 351>
    ParenthesizedPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedPropertyExpr: 352>
    ParenthesizedSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ParenthesizedSequenceExpr: 353>
    PathDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PathDeclaration: 354>
    PathDescription: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PathDescription: 355>
    PatternCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PatternCaseItem: 356>
    PortConcatenation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortConcatenation: 357>
    PortDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortDeclaration: 358>
    PortReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PortReference: 359>
    PostdecrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PostdecrementExpression: 360>
    PostincrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PostincrementExpression: 361>
    PowerExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PowerExpression: 362>
    PragmaDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PragmaDirective: 363>
    PrimaryBlockEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PrimaryBlockEventExpression: 364>
    PrimitiveInstantiation: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PrimitiveInstantiation: 365>
    ProceduralAssignStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralAssignStatement: 366>
    ProceduralDeassignStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralDeassignStatement: 367>
    ProceduralForceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralForceStatement: 368>
    ProceduralReleaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProceduralReleaseStatement: 369>
    Production: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Production: 370>
    ProgramDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProgramDeclaration: 371>
    ProgramHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ProgramHeader: 372>
    PropertyDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertyDeclaration: 373>
    PropertySpec: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertySpec: 374>
    PropertyType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PropertyType: 375>
    PullStrength: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PullStrength: 376>
    PulseStyleDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.PulseStyleDeclaration: 377>
    QueueDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.QueueDimensionSpecifier: 378>
    RandCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandCaseItem: 379>
    RandCaseStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandCaseStatement: 380>
    RandJoinClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandJoinClause: 381>
    RandSequenceStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RandSequenceStatement: 382>
    RangeCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeCoverageBinInitializer: 383>
    RangeDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeDimensionSpecifier: 384>
    RangeList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RangeList: 385>
    RealLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealLiteralExpression: 386>
    RealTimeType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealTimeType: 387>
    RealType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RealType: 388>
    RegType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RegType: 389>
    RepeatedEventControl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RepeatedEventControl: 390>
    ReplicatedAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ReplicatedAssignmentPattern: 391>
    ResetAllDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ResetAllDirective: 392>
    RestrictPropertyStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RestrictPropertyStatement: 393>
    ReturnStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ReturnStatement: 394>
    RootScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RootScope: 395>
    RsCase: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsCase: 396>
    RsCodeBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsCodeBlock: 397>
    RsElseClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsElseClause: 398>
    RsIfElse: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsIfElse: 399>
    RsProdItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsProdItem: 400>
    RsRepeat: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsRepeat: 401>
    RsRule: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsRule: 402>
    RsWeightClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.RsWeightClause: 403>
    SUntilPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SUntilPropertyExpr: 404>
    SUntilWithPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SUntilWithPropertyExpr: 405>
    ScopedName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ScopedName: 406>
    SeparatedList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SeparatedList: 3>
    SequenceDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceDeclaration: 407>
    SequenceMatchList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceMatchList: 408>
    SequenceRepetition: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceRepetition: 409>
    SequenceType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequenceType: 410>
    SequentialBlockStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SequentialBlockStatement: 411>
    ShortIntType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ShortIntType: 412>
    ShortRealType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ShortRealType: 413>
    SignalEventExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SignalEventExpression: 414>
    SignedCastExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SignedCastExpression: 415>
    SimpleAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleAssignmentPattern: 416>
    SimpleBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleBinsSelectExpr: 417>
    SimplePathSuffix: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePathSuffix: 418>
    SimplePragmaExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePragmaExpression: 419>
    SimplePropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimplePropertyExpr: 420>
    SimpleRangeSelect: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleRangeSelect: 421>
    SimpleSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SimpleSequenceExpr: 422>
    SolveBeforeConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SolveBeforeConstraint: 423>
    SpecifyBlock: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecifyBlock: 424>
    SpecparamDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecparamDeclaration: 425>
    SpecparamDeclarator: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SpecparamDeclarator: 426>
    StandardCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardCaseItem: 427>
    StandardPropertyCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardPropertyCaseItem: 428>
    StandardRsCaseItem: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StandardRsCaseItem: 429>
    StreamExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamExpression: 430>
    StreamExpressionWithRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamExpressionWithRange: 431>
    StreamingConcatenationExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StreamingConcatenationExpression: 432>
    StringLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StringLiteralExpression: 433>
    StringType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StringType: 434>
    StrongWeakPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StrongWeakPropertyExpr: 435>
    StructType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructType: 436>
    StructUnionMember: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructUnionMember: 437>
    StructurePattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructurePattern: 438>
    StructuredAssignmentPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.StructuredAssignmentPattern: 439>
    SubtractAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SubtractAssignmentExpression: 440>
    SubtractExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SubtractExpression: 441>
    SuperHandle: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SuperHandle: 442>
    SuperNewDefaultedArgsExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SuperNewDefaultedArgsExpression: 443>
    SyntaxList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SyntaxList: 1>
    SystemName: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SystemName: 444>
    SystemTimingCheck: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.SystemTimingCheck: 445>
    TaggedPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaggedPattern: 446>
    TaggedUnionExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaggedUnionExpression: 447>
    TaskDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TaskDeclaration: 448>
    ThisHandle: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ThisHandle: 449>
    ThroughoutSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ThroughoutSequenceExpr: 450>
    TimeLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeLiteralExpression: 451>
    TimeScaleDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeScaleDirective: 452>
    TimeType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeType: 453>
    TimeUnitsDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimeUnitsDeclaration: 454>
    TimingCheckEventArg: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingCheckEventArg: 455>
    TimingCheckEventCondition: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingCheckEventCondition: 456>
    TimingControlExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingControlExpression: 457>
    TimingControlStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TimingControlStatement: 458>
    TokenList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TokenList: 2>
    TransListCoverageBinInitializer: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransListCoverageBinInitializer: 459>
    TransRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransRange: 460>
    TransRepeatRange: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransRepeatRange: 461>
    TransSet: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TransSet: 462>
    TypeAssignment: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeAssignment: 463>
    TypeParameterDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeParameterDeclaration: 464>
    TypeReference: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypeReference: 465>
    TypedefDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.TypedefDeclaration: 466>
    UdpBody: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpBody: 467>
    UdpDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpDeclaration: 468>
    UdpEdgeField: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpEdgeField: 469>
    UdpEntry: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpEntry: 470>
    UdpInitialStmt: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpInitialStmt: 471>
    UdpInputPortDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpInputPortDecl: 472>
    UdpOutputPortDecl: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpOutputPortDecl: 473>
    UdpSimpleField: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UdpSimpleField: 474>
    UnaryBinsSelectExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBinsSelectExpr: 475>
    UnaryBitwiseAndExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseAndExpression: 476>
    UnaryBitwiseNandExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNandExpression: 477>
    UnaryBitwiseNorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNorExpression: 478>
    UnaryBitwiseNotExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseNotExpression: 479>
    UnaryBitwiseOrExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseOrExpression: 480>
    UnaryBitwiseXnorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseXnorExpression: 481>
    UnaryBitwiseXorExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryBitwiseXorExpression: 482>
    UnaryConditionalDirectiveExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryConditionalDirectiveExpression: 483>
    UnaryLogicalNotExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryLogicalNotExpression: 484>
    UnaryMinusExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryMinusExpression: 485>
    UnaryPlusExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPlusExpression: 486>
    UnaryPredecrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPredecrementExpression: 487>
    UnaryPreincrementExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPreincrementExpression: 488>
    UnaryPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnaryPropertyExpr: 489>
    UnarySelectPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnarySelectPropertyExpr: 490>
    UnbasedUnsizedLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnbasedUnsizedLiteralExpression: 491>
    UnconnectedDriveDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnconnectedDriveDirective: 492>
    UndefDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UndefDirective: 493>
    UndefineAllDirective: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UndefineAllDirective: 494>
    UnionType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnionType: 495>
    UniquenessConstraint: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UniquenessConstraint: 496>
    UnitScope: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UnitScope: 497>
    Unknown: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Unknown: 0>
    UntilPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UntilPropertyExpr: 498>
    UntilWithPropertyExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UntilWithPropertyExpr: 499>
    Untyped: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.Untyped: 500>
    UserDefinedNetDeclaration: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.UserDefinedNetDeclaration: 501>
    ValueRangeExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.ValueRangeExpression: 502>
    VariableDimension: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariableDimension: 503>
    VariablePattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariablePattern: 504>
    VariablePortHeader: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VariablePortHeader: 505>
    VirtualInterfaceType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VirtualInterfaceType: 506>
    VoidCastedCallStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VoidCastedCallStatement: 507>
    VoidType: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.VoidType: 508>
    WaitForkStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitForkStatement: 509>
    WaitOrderStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitOrderStatement: 510>
    WaitStatement: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WaitStatement: 511>
    WildcardDimensionSpecifier: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardDimensionSpecifier: 512>
    WildcardEqualityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardEqualityExpression: 513>
    WildcardInequalityExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardInequalityExpression: 514>
    WildcardLiteralExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardLiteralExpression: 515>
    WildcardPattern: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPattern: 516>
    WildcardPortConnection: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPortConnection: 517>
    WildcardPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardPortList: 518>
    WildcardUdpPortList: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WildcardUdpPortList: 519>
    WithClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithClause: 520>
    WithFunctionClause: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithFunctionClause: 521>
    WithFunctionSample: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithFunctionSample: 522>
    WithinSequenceExpr: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.WithinSequenceExpr: 523>
    XorAssignmentExpression: typing.ClassVar[SyntaxKind]  # value = <SyntaxKind.XorAssignmentExpression: 524>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SyntaxNode:
    def __getitem__(self, arg0: int) -> typing.Any:
        ...
    def __iter__(self) -> typing.Iterator[typing.Any]:
        ...
    def __len__(self) -> int:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    def getFirstToken(self) -> Token:
        ...
    def getLastToken(self) -> Token:
        ...
    def isEquivalentTo(self, other: SyntaxNode) -> bool:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def kind(self) -> SyntaxKind:
        ...
    @property
    def parent(self) -> SyntaxNode:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
class SyntaxPrinter:
    @staticmethod
    def printFile(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, sourceManager: SourceManager) -> None:
        ...
    def append(self, text: str) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, trivia: Trivia) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, token: Token) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, node: SyntaxNode) -> SyntaxPrinter:
        ...
    @typing.overload
    def print(self, tree: SyntaxTree) -> SyntaxPrinter:
        ...
    def setIncludeComments(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeDirectives(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeMissing(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludePreprocessed(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeSkipped(self, include: bool) -> SyntaxPrinter:
        ...
    def setIncludeTrivia(self, include: bool) -> SyntaxPrinter:
        ...
    def setSquashNewlines(self, include: bool) -> SyntaxPrinter:
        ...
    def str(self) -> str:
        ...
class SyntaxTree:
    @staticmethod
    def fromBuffer(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromBuffers(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromFile(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromFileInMemory(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromFiles(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromLibraryMapBuffer(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromLibraryMapFile(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromLibraryMapText(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromText(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getDefaultSourceManager(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @property
    def diagnostics(self) -> Diagnostics:
        ...
    @property
    def isLibraryUnit(self) -> bool:
        ...
    @property
    def options(self) -> Bag:
        ...
    @property
    def root(self) -> SyntaxNode:
        ...
    @property
    def sourceLibrary(self) -> SourceLibrary:
        ...
    @property
    def sourceManager(self) -> SourceManager:
        ...
class SystemNameSyntax(NameSyntax):
    systemIdentifier: Token
class SystemSubroutine:
    class WithClauseMode:
        Iterator: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.Iterator: 1>
        None_: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.None: 0>
        Randomize: typing.ClassVar[SystemSubroutine.WithClauseMode]  # value = <WithClauseMode.Randomize: 2>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    hasOutputArgs: bool
    kind: SubroutineKind
    name: str
    withClauseMode: SystemSubroutine.WithClauseMode
    @staticmethod
    def unevaluatedContext(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __init__(self, name: str, kind: SubroutineKind) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def allowClockingArgument(self, argIndex: int) -> bool:
        ...
    def allowEmptyArgument(self, argIndex: int) -> bool:
        ...
    def badArg(self, context: ASTContext, arg: Expression) -> Type:
        ...
    def bindArgument(self, argIndex: int, context: ASTContext, syntax: ExpressionSyntax, previousArgs: span[Expression]) -> Expression:
        ...
    def checkArgCount(self, context: ASTContext, isMethod: bool, args: span[Expression], callRange: SourceRange, min: int, max: int) -> bool:
        ...
    def checkArguments(self, context: ASTContext, args: span[Expression], range: SourceRange, iterOrThis: Expression) -> Type:
        ...
    def eval(self, context: EvalContext, args: span[Expression], range: SourceRange, callInfo: CallExpression.SystemCallInfo) -> ConstantValue:
        ...
    def kindStr(self) -> str:
        ...
    def noHierarchical(self, context: EvalContext, expr: Expression) -> bool:
        ...
    def notConst(self, context: EvalContext, range: SourceRange) -> bool:
        ...
class SystemTimingCheckKind:
    FullSkew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.FullSkew: 9>
    Hold: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Hold: 2>
    NoChange: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.NoChange: 12>
    Period: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Period: 10>
    RecRem: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.RecRem: 6>
    Recovery: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Recovery: 4>
    Removal: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Removal: 5>
    Setup: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Setup: 1>
    SetupHold: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.SetupHold: 3>
    Skew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Skew: 7>
    TimeSkew: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.TimeSkew: 8>
    Unknown: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Unknown: 0>
    Width: typing.ClassVar[SystemTimingCheckKind]  # value = <SystemTimingCheckKind.Width: 11>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class SystemTimingCheckSymbol(Symbol):
    class Arg:
        @property
        def condition(self) -> Expression:
            ...
        @property
        def edge(self) -> EdgeKind:
            ...
        @property
        def edgeDescriptors(self) -> span[typing.Annotated[list[str], pybind11_stubgen.typing_ext.FixedSize(2)]]:
            ...
        @property
        def expr(self) -> Expression:
            ...
    @property
    def arguments(self) -> span[SystemTimingCheckSymbol::Arg]:
        ...
    @property
    def timingCheckKind(self) -> SystemTimingCheckKind:
        ...
class SystemTimingCheckSyntax(MemberSyntax):
    args: SeparatedSyntaxList[TimingCheckArgSyntax]
    closeParen: Token
    name: Token
    openParen: Token
    semi: Token
class TaggedPattern(Pattern):
    @property
    def member(self) -> FieldSymbol:
        ...
    @property
    def valuePattern(self) -> Pattern:
        ...
class TaggedPatternSyntax(PatternSyntax):
    memberName: Token
    pattern: PatternSyntax
    tagged: Token
class TaggedUnionExpression(Expression):
    @property
    def member(self) -> Symbol:
        ...
    @property
    def valueExpr(self) -> Expression:
        ...
class TaggedUnionExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    member: Token
    tagged: Token
class TempVarSymbol(VariableSymbol):
    pass
class TextDiagnosticClient(DiagnosticClient):
    def __init__(self) -> None:
        ...
    def clear(self) -> None:
        ...
    def getString(self) -> str:
        ...
    def report(self, diag: ReportedDiagnostic) -> None:
        ...
    def showColors(self, show: bool) -> None:
        ...
    def showColumn(self, show: bool) -> None:
        ...
    def showHierarchyInstance(self, show: ShowHierarchyPathOption) -> None:
        ...
    def showIncludeStack(self, show: bool) -> None:
        ...
    def showLocation(self, show: bool) -> None:
        ...
    def showMacroExpansion(self, show: bool) -> None:
        ...
    def showOptionName(self, show: bool) -> None:
        ...
    def showSourceLine(self, show: bool) -> None:
        ...
class TimeLiteral(Expression):
    @property
    def value(self) -> float:
        ...
class TimeScale:
    __hash__: typing.ClassVar[None] = None
    base: TimeScaleValue
    precision: TimeScaleValue
    @staticmethod
    def fromString(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __eq__(self, arg0: TimeScale) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, base: TimeScaleValue, precision: TimeScaleValue) -> None:
        ...
    def __ne__(self, arg0: TimeScale) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def apply(self, value: float, unit: TimeUnit, roundToPrecision: bool) -> float:
        ...
class TimeScaleDirectiveSyntax(DirectiveSyntax):
    slash: Token
    timePrecision: Token
    timeUnit: Token
class TimeScaleMagnitude:
    Hundred: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.Hundred: 100>
    One: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.One: 1>
    Ten: typing.ClassVar[TimeScaleMagnitude]  # value = <TimeScaleMagnitude.Ten: 10>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimeScaleValue:
    __hash__: typing.ClassVar[None] = None
    magnitude: TimeScaleMagnitude
    unit: TimeUnit
    @staticmethod
    def fromLiteral(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def fromString(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __eq__(self, arg0: TimeScaleValue) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, unit: TimeUnit, magnitude: TimeScaleMagnitude) -> None:
        ...
    def __ne__(self, arg0: TimeScaleValue) -> bool:
        ...
    def __repr__(self) -> str:
        ...
class TimeUnit:
    Femtoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Femtoseconds: 5>
    Microseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Microseconds: 2>
    Milliseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Milliseconds: 1>
    Nanoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Nanoseconds: 3>
    Picoseconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Picoseconds: 4>
    Seconds: typing.ClassVar[TimeUnit]  # value = <TimeUnit.Seconds: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimeUnitsDeclarationSyntax(MemberSyntax):
    divider: DividerClauseSyntax
    keyword: Token
    semi: Token
    time: Token
class TimedStatement(Statement):
    @property
    def stmt(self) -> Statement:
        ...
    @property
    def timing(self) -> TimingControl:
        ...
class TimingCheckArgSyntax(SyntaxNode):
    pass
class TimingCheckEventArgSyntax(TimingCheckArgSyntax):
    condition: TimingCheckEventConditionSyntax
    controlSpecifier: EdgeControlSpecifierSyntax
    edge: Token
    terminal: ExpressionSyntax
class TimingCheckEventConditionSyntax(SyntaxNode):
    expr: ExpressionSyntax
    tripleAnd: Token
class TimingControl:
    def __repr__(self) -> str:
        ...
    def visit(self, f: typing.Any) -> None:
        """
        Visit a pyslang object with a callback f.

        If f ever returns pyslang.VisitAction.Interrupt, the visit is aborted, and no additional nodes are visited. If f returns pyslang.VisitAction.Skip, then no child nodes of the current node are visited, but otherwise the visit continues. Any other return value, including pslang.VisitAction.Advance is ignored, and the walk continues.
        """
    @property
    def bad(self) -> bool:
        ...
    @property
    def kind(self) -> TimingControlKind:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
    @property
    def syntax(self) -> SyntaxNode:
        ...
class TimingControlExpressionSyntax(ExpressionSyntax):
    expr: ExpressionSyntax
    timing: TimingControlSyntax
class TimingControlKind:
    BlockEventList: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.BlockEventList: 9>
    CycleDelay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.CycleDelay: 8>
    Delay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Delay: 1>
    Delay3: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Delay3: 6>
    EventList: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.EventList: 3>
    ImplicitEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.ImplicitEvent: 4>
    Invalid: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.Invalid: 0>
    OneStepDelay: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.OneStepDelay: 7>
    RepeatedEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.RepeatedEvent: 5>
    SignalEvent: typing.ClassVar[TimingControlKind]  # value = <TimingControlKind.SignalEvent: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TimingControlStatementSyntax(StatementSyntax):
    statement: StatementSyntax
    timingControl: TimingControlSyntax
class TimingControlSyntax(SyntaxNode):
    pass
class TimingPathSymbol(Symbol):
    class ConnectionKind:
        Full: typing.ClassVar[TimingPathSymbol.ConnectionKind]  # value = <ConnectionKind.Full: 0>
        Parallel: typing.ClassVar[TimingPathSymbol.ConnectionKind]  # value = <ConnectionKind.Parallel: 1>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    class Polarity:
        Negative: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Negative: 2>
        Positive: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Positive: 1>
        Unknown: typing.ClassVar[TimingPathSymbol.Polarity]  # value = <Polarity.Unknown: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    @property
    def conditionExpr(self) -> Expression:
        ...
    @property
    def connectionKind(self) -> TimingPathSymbol.ConnectionKind:
        ...
    @property
    def delays(self) -> span[Expression]:
        ...
    @property
    def edgeIdentifier(self) -> EdgeKind:
        ...
    @property
    def edgePolarity(self) -> TimingPathSymbol.Polarity:
        ...
    @property
    def edgeSourceExpr(self) -> Expression:
        ...
    @property
    def inputs(self) -> span[Expression]:
        ...
    @property
    def isStateDependent(self) -> bool:
        ...
    @property
    def outputs(self) -> span[Expression]:
        ...
    @property
    def polarity(self) -> TimingPathSymbol.Polarity:
        ...
class Token:
    __hash__: typing.ClassVar[None] = None
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: Token) -> bool:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, strText: str) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, directive: SyntaxKind) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, bit: logic_t) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, value: SVInt) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, value: float, outOfRange: bool, timeUnit: TimeUnit | None) -> None:
        ...
    @typing.overload
    def __init__(self, alloc: BumpAllocator, kind: TokenKind, trivia: span[Trivia], rawText: str, location: SourceLocation, base: LiteralBase, isSigned: bool) -> None:
        ...
    def __ne__(self, arg0: Token) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __str__(self) -> str:
        ...
    @property
    def isMissing(self) -> bool:
        ...
    @property
    def isOnSameLine(self) -> bool:
        ...
    @property
    def kind(self) -> TokenKind:
        ...
    @property
    def location(self) -> SourceLocation:
        ...
    @property
    def range(self) -> SourceRange:
        ...
    @property
    def rawText(self) -> str:
        ...
    @property
    def trivia(self) -> span[Trivia]:
        ...
    @property
    def value(self) -> typing.Any:
        ...
    @property
    def valueText(self) -> str:
        ...
class TokenKind:
    AcceptOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AcceptOnKeyword: 96>
    AliasKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AliasKeyword: 97>
    AlwaysCombKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysCombKeyword: 99>
    AlwaysFFKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysFFKeyword: 100>
    AlwaysKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysKeyword: 98>
    AlwaysLatchKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AlwaysLatchKeyword: 101>
    And: typing.ClassVar[TokenKind]  # value = <TokenKind.And: 92>
    AndEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.AndEqual: 64>
    AndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AndKeyword: 102>
    Apostrophe: typing.ClassVar[TokenKind]  # value = <TokenKind.Apostrophe: 11>
    ApostropheOpenBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.ApostropheOpenBrace: 12>
    AssertKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssertKeyword: 103>
    AssignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssignKeyword: 104>
    AssumeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AssumeKeyword: 105>
    At: typing.ClassVar[TokenKind]  # value = <TokenKind.At: 90>
    AutomaticKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.AutomaticKeyword: 106>
    BeforeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BeforeKeyword: 107>
    BeginKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BeginKeyword: 108>
    BindKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BindKeyword: 109>
    BinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BinsKeyword: 110>
    BinsOfKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BinsOfKeyword: 111>
    BitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BitKeyword: 112>
    BreakKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BreakKeyword: 113>
    BufIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufIf0Keyword: 115>
    BufIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufIf1Keyword: 116>
    BufKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.BufKeyword: 114>
    ByteKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ByteKeyword: 117>
    CHandleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CHandleKeyword: 122>
    CaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseKeyword: 118>
    CaseXKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseXKeyword: 119>
    CaseZKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CaseZKeyword: 120>
    CellKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CellKeyword: 121>
    CheckerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CheckerKeyword: 123>
    ClassKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ClassKeyword: 124>
    ClockingKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ClockingKeyword: 125>
    CloseBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseBrace: 14>
    CloseBracket: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseBracket: 16>
    CloseParenthesis: typing.ClassVar[TokenKind]  # value = <TokenKind.CloseParenthesis: 19>
    CmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CmosKeyword: 126>
    Colon: typing.ClassVar[TokenKind]  # value = <TokenKind.Colon: 22>
    ColonEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ColonEquals: 23>
    ColonSlash: typing.ClassVar[TokenKind]  # value = <TokenKind.ColonSlash: 24>
    Comma: typing.ClassVar[TokenKind]  # value = <TokenKind.Comma: 26>
    ConfigKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConfigKeyword: 127>
    ConstKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConstKeyword: 128>
    ConstraintKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ConstraintKeyword: 129>
    ContextKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ContextKeyword: 130>
    ContinueKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ContinueKeyword: 131>
    CoverGroupKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverGroupKeyword: 133>
    CoverKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverKeyword: 132>
    CoverPointKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CoverPointKeyword: 134>
    CrossKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.CrossKeyword: 135>
    DeassignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DeassignKeyword: 136>
    DefParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DefParamKeyword: 138>
    DefaultKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DefaultKeyword: 137>
    DesignKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DesignKeyword: 139>
    Directive: typing.ClassVar[TokenKind]  # value = <TokenKind.Directive: 346>
    DisableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DisableKeyword: 140>
    DistKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DistKeyword: 141>
    DoKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.DoKeyword: 142>
    Dollar: typing.ClassVar[TokenKind]  # value = <TokenKind.Dollar: 47>
    Dot: typing.ClassVar[TokenKind]  # value = <TokenKind.Dot: 28>
    DotStar: typing.ClassVar[TokenKind]  # value = <TokenKind.DotStar: 27>
    DoubleAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleAnd: 93>
    DoubleAt: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleAt: 91>
    DoubleColon: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleColon: 25>
    DoubleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleEquals: 56>
    DoubleEqualsQuestion: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleEqualsQuestion: 57>
    DoubleHash: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleHash: 50>
    DoubleMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleMinus: 39>
    DoubleOr: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleOr: 87>
    DoublePlus: typing.ClassVar[TokenKind]  # value = <TokenKind.DoublePlus: 34>
    DoubleStar: typing.ClassVar[TokenKind]  # value = <TokenKind.DoubleStar: 31>
    EdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EdgeKeyword: 143>
    ElseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ElseKeyword: 144>
    EmptyMacroArgument: typing.ClassVar[TokenKind]  # value = <TokenKind.EmptyMacroArgument: 353>
    EndCaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndCaseKeyword: 146>
    EndCheckerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndCheckerKeyword: 147>
    EndClassKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndClassKeyword: 148>
    EndClockingKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndClockingKeyword: 149>
    EndConfigKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndConfigKeyword: 150>
    EndFunctionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndFunctionKeyword: 151>
    EndGenerateKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndGenerateKeyword: 152>
    EndGroupKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndGroupKeyword: 153>
    EndInterfaceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndInterfaceKeyword: 154>
    EndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndKeyword: 145>
    EndModuleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndModuleKeyword: 155>
    EndOfFile: typing.ClassVar[TokenKind]  # value = <TokenKind.EndOfFile: 1>
    EndPackageKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPackageKeyword: 156>
    EndPrimitiveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPrimitiveKeyword: 157>
    EndProgramKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndProgramKeyword: 158>
    EndPropertyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndPropertyKeyword: 159>
    EndSequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndSequenceKeyword: 161>
    EndSpecifyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndSpecifyKeyword: 160>
    EndTableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndTableKeyword: 162>
    EndTaskKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EndTaskKeyword: 163>
    EnumKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EnumKeyword: 164>
    Equals: typing.ClassVar[TokenKind]  # value = <TokenKind.Equals: 55>
    EqualsArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.EqualsArrow: 59>
    EventKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EventKeyword: 165>
    EventuallyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.EventuallyKeyword: 166>
    Exclamation: typing.ClassVar[TokenKind]  # value = <TokenKind.Exclamation: 76>
    ExclamationDoubleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationDoubleEquals: 79>
    ExclamationEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationEquals: 77>
    ExclamationEqualsQuestion: typing.ClassVar[TokenKind]  # value = <TokenKind.ExclamationEqualsQuestion: 78>
    ExpectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExpectKeyword: 167>
    ExportKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExportKeyword: 168>
    ExtendsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExtendsKeyword: 169>
    ExternKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ExternKeyword: 170>
    FinalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FinalKeyword: 171>
    FirstMatchKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FirstMatchKeyword: 172>
    ForKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForKeyword: 173>
    ForceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForceKeyword: 174>
    ForeachKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForeachKeyword: 175>
    ForeverKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForeverKeyword: 176>
    ForkJoinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForkJoinKeyword: 178>
    ForkKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ForkKeyword: 177>
    FunctionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.FunctionKeyword: 179>
    GenVarKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GenVarKeyword: 181>
    GenerateKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GenerateKeyword: 180>
    GlobalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.GlobalKeyword: 182>
    GreaterThan: typing.ClassVar[TokenKind]  # value = <TokenKind.GreaterThan: 84>
    GreaterThanEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.GreaterThanEquals: 85>
    Hash: typing.ClassVar[TokenKind]  # value = <TokenKind.Hash: 49>
    HashEqualsHash: typing.ClassVar[TokenKind]  # value = <TokenKind.HashEqualsHash: 52>
    HashMinusHash: typing.ClassVar[TokenKind]  # value = <TokenKind.HashMinusHash: 51>
    HighZ0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.HighZ0Keyword: 183>
    HighZ1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.HighZ1Keyword: 184>
    Identifier: typing.ClassVar[TokenKind]  # value = <TokenKind.Identifier: 2>
    IfKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IfKeyword: 185>
    IfNoneKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IfNoneKeyword: 187>
    IffKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IffKeyword: 186>
    IgnoreBinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IgnoreBinsKeyword: 188>
    IllegalBinsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IllegalBinsKeyword: 189>
    ImplementsKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImplementsKeyword: 190>
    ImpliesKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImpliesKeyword: 191>
    ImportKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ImportKeyword: 192>
    InOutKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InOutKeyword: 196>
    IncDirKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IncDirKeyword: 193>
    IncludeFileName: typing.ClassVar[TokenKind]  # value = <TokenKind.IncludeFileName: 347>
    IncludeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IncludeKeyword: 194>
    InitialKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InitialKeyword: 195>
    InputKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InputKeyword: 197>
    InsideKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InsideKeyword: 198>
    InstanceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InstanceKeyword: 199>
    IntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntKeyword: 200>
    IntegerBase: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerBase: 6>
    IntegerKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerKeyword: 201>
    IntegerLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.IntegerLiteral: 5>
    InterconnectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InterconnectKeyword: 202>
    InterfaceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.InterfaceKeyword: 203>
    IntersectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.IntersectKeyword: 204>
    JoinAnyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinAnyKeyword: 206>
    JoinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinKeyword: 205>
    JoinNoneKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.JoinNoneKeyword: 207>
    LargeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LargeKeyword: 208>
    LeftShift: typing.ClassVar[TokenKind]  # value = <TokenKind.LeftShift: 72>
    LeftShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.LeftShiftEqual: 68>
    LessThan: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThan: 81>
    LessThanEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThanEquals: 82>
    LessThanMinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.LessThanMinusArrow: 83>
    LetKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LetKeyword: 209>
    LibListKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LibListKeyword: 210>
    LibraryKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LibraryKeyword: 211>
    LineContinuation: typing.ClassVar[TokenKind]  # value = <TokenKind.LineContinuation: 354>
    LocalKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LocalKeyword: 212>
    LocalParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LocalParamKeyword: 213>
    LogicKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LogicKeyword: 214>
    LongIntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.LongIntKeyword: 215>
    MacroEscapedQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroEscapedQuote: 351>
    MacroPaste: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroPaste: 352>
    MacroQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroQuote: 349>
    MacroTripleQuote: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroTripleQuote: 350>
    MacroUsage: typing.ClassVar[TokenKind]  # value = <TokenKind.MacroUsage: 348>
    MacromoduleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MacromoduleKeyword: 216>
    MatchesKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MatchesKeyword: 217>
    MediumKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.MediumKeyword: 218>
    Minus: typing.ClassVar[TokenKind]  # value = <TokenKind.Minus: 38>
    MinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusArrow: 41>
    MinusColon: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusColon: 40>
    MinusDoubleArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusDoubleArrow: 42>
    MinusEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.MinusEqual: 61>
    ModPortKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ModPortKeyword: 219>
    ModuleKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ModuleKeyword: 220>
    NandKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NandKeyword: 221>
    NegEdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NegEdgeKeyword: 222>
    NetTypeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NetTypeKeyword: 223>
    NewKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NewKeyword: 224>
    NextTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NextTimeKeyword: 225>
    NmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NmosKeyword: 226>
    NoShowCancelledKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NoShowCancelledKeyword: 228>
    NorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NorKeyword: 227>
    NotIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotIf0Keyword: 230>
    NotIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotIf1Keyword: 231>
    NotKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NotKeyword: 229>
    NullKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.NullKeyword: 232>
    OneStep: typing.ClassVar[TokenKind]  # value = <TokenKind.OneStep: 95>
    OpenBrace: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenBrace: 13>
    OpenBracket: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenBracket: 15>
    OpenParenthesis: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenParenthesis: 17>
    OpenParenthesisStar: typing.ClassVar[TokenKind]  # value = <TokenKind.OpenParenthesisStar: 18>
    Or: typing.ClassVar[TokenKind]  # value = <TokenKind.Or: 86>
    OrEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.OrEqual: 65>
    OrEqualsArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.OrEqualsArrow: 89>
    OrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.OrKeyword: 233>
    OrMinusArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.OrMinusArrow: 88>
    OutputKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.OutputKeyword: 234>
    PackageKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PackageKeyword: 235>
    PackedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PackedKeyword: 236>
    ParameterKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ParameterKeyword: 237>
    Percent: typing.ClassVar[TokenKind]  # value = <TokenKind.Percent: 80>
    PercentEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.PercentEqual: 66>
    Placeholder: typing.ClassVar[TokenKind]  # value = <TokenKind.Placeholder: 10>
    Plus: typing.ClassVar[TokenKind]  # value = <TokenKind.Plus: 33>
    PlusColon: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusColon: 35>
    PlusDivMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusDivMinus: 36>
    PlusEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusEqual: 60>
    PlusModMinus: typing.ClassVar[TokenKind]  # value = <TokenKind.PlusModMinus: 37>
    PmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PmosKeyword: 238>
    PosEdgeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PosEdgeKeyword: 239>
    PrimitiveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PrimitiveKeyword: 240>
    PriorityKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PriorityKeyword: 241>
    ProgramKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ProgramKeyword: 242>
    PropertyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PropertyKeyword: 243>
    ProtectedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ProtectedKeyword: 244>
    Pull0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Pull0Keyword: 245>
    Pull1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Pull1Keyword: 246>
    PullDownKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PullDownKeyword: 247>
    PullUpKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PullUpKeyword: 248>
    PulseStyleOnDetectKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PulseStyleOnDetectKeyword: 249>
    PulseStyleOnEventKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PulseStyleOnEventKeyword: 250>
    PureKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.PureKeyword: 251>
    Question: typing.ClassVar[TokenKind]  # value = <TokenKind.Question: 48>
    RandCKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandCKeyword: 253>
    RandCaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandCaseKeyword: 254>
    RandKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandKeyword: 252>
    RandSequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RandSequenceKeyword: 255>
    RcmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RcmosKeyword: 256>
    RealKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RealKeyword: 257>
    RealLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.RealLiteral: 8>
    RealTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RealTimeKeyword: 258>
    RefKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RefKeyword: 259>
    RegKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RegKeyword: 260>
    RejectOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RejectOnKeyword: 261>
    ReleaseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ReleaseKeyword: 262>
    RepeatKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RepeatKeyword: 263>
    RestrictKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RestrictKeyword: 264>
    ReturnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ReturnKeyword: 265>
    RightShift: typing.ClassVar[TokenKind]  # value = <TokenKind.RightShift: 73>
    RightShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.RightShiftEqual: 70>
    RnmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RnmosKeyword: 266>
    RootSystemName: typing.ClassVar[TokenKind]  # value = <TokenKind.RootSystemName: 345>
    RpmosKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RpmosKeyword: 267>
    RtranIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranIf0Keyword: 269>
    RtranIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranIf1Keyword: 270>
    RtranKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.RtranKeyword: 268>
    SAlwaysKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SAlwaysKeyword: 271>
    SEventuallyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SEventuallyKeyword: 272>
    SNextTimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SNextTimeKeyword: 273>
    SUntilKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SUntilKeyword: 274>
    SUntilWithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SUntilWithKeyword: 275>
    ScalaredKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ScalaredKeyword: 276>
    Semicolon: typing.ClassVar[TokenKind]  # value = <TokenKind.Semicolon: 21>
    SequenceKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SequenceKeyword: 277>
    ShortIntKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShortIntKeyword: 278>
    ShortRealKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShortRealKeyword: 279>
    ShowCancelledKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ShowCancelledKeyword: 280>
    SignedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SignedKeyword: 281>
    Slash: typing.ClassVar[TokenKind]  # value = <TokenKind.Slash: 29>
    SlashEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.SlashEqual: 62>
    SmallKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SmallKeyword: 282>
    SoftKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SoftKeyword: 283>
    SolveKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SolveKeyword: 284>
    SpecParamKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SpecParamKeyword: 286>
    SpecifyKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SpecifyKeyword: 285>
    Star: typing.ClassVar[TokenKind]  # value = <TokenKind.Star: 30>
    StarArrow: typing.ClassVar[TokenKind]  # value = <TokenKind.StarArrow: 32>
    StarCloseParenthesis: typing.ClassVar[TokenKind]  # value = <TokenKind.StarCloseParenthesis: 20>
    StarEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.StarEqual: 63>
    StaticKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StaticKeyword: 287>
    StringKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StringKeyword: 288>
    StringLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.StringLiteral: 4>
    Strong0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Strong0Keyword: 290>
    Strong1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Strong1Keyword: 291>
    StrongKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StrongKeyword: 289>
    StructKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.StructKeyword: 292>
    SuperKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SuperKeyword: 293>
    Supply0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Supply0Keyword: 294>
    Supply1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Supply1Keyword: 295>
    SyncAcceptOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SyncAcceptOnKeyword: 296>
    SyncRejectOnKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.SyncRejectOnKeyword: 297>
    SystemIdentifier: typing.ClassVar[TokenKind]  # value = <TokenKind.SystemIdentifier: 3>
    TableKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TableKeyword: 298>
    TaggedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TaggedKeyword: 299>
    TaskKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TaskKeyword: 300>
    ThisKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ThisKeyword: 301>
    ThroughoutKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.ThroughoutKeyword: 302>
    Tilde: typing.ClassVar[TokenKind]  # value = <TokenKind.Tilde: 43>
    TildeAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeAnd: 44>
    TildeOr: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeOr: 45>
    TildeXor: typing.ClassVar[TokenKind]  # value = <TokenKind.TildeXor: 46>
    TimeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeKeyword: 303>
    TimeLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeLiteral: 9>
    TimePrecisionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimePrecisionKeyword: 304>
    TimeUnitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TimeUnitKeyword: 305>
    TranIf0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranIf0Keyword: 307>
    TranIf1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranIf1Keyword: 308>
    TranKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TranKeyword: 306>
    Tri0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Tri0Keyword: 310>
    Tri1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Tri1Keyword: 311>
    TriAndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriAndKeyword: 312>
    TriKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriKeyword: 309>
    TriOrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriOrKeyword: 313>
    TriRegKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TriRegKeyword: 314>
    TripleAnd: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleAnd: 94>
    TripleEquals: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleEquals: 58>
    TripleLeftShift: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleLeftShift: 74>
    TripleLeftShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleLeftShiftEqual: 69>
    TripleRightShift: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleRightShift: 75>
    TripleRightShiftEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.TripleRightShiftEqual: 71>
    TypeKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TypeKeyword: 315>
    TypedefKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.TypedefKeyword: 316>
    UWireKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UWireKeyword: 325>
    UnbasedUnsizedLiteral: typing.ClassVar[TokenKind]  # value = <TokenKind.UnbasedUnsizedLiteral: 7>
    UnionKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UnionKeyword: 317>
    Unique0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Unique0Keyword: 319>
    UniqueKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UniqueKeyword: 318>
    UnitSystemName: typing.ClassVar[TokenKind]  # value = <TokenKind.UnitSystemName: 344>
    Unknown: typing.ClassVar[TokenKind]  # value = <TokenKind.Unknown: 0>
    UnsignedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UnsignedKeyword: 320>
    UntilKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntilKeyword: 321>
    UntilWithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntilWithKeyword: 322>
    UntypedKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UntypedKeyword: 323>
    UseKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.UseKeyword: 324>
    VarKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VarKeyword: 326>
    VectoredKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VectoredKeyword: 327>
    VirtualKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VirtualKeyword: 328>
    VoidKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.VoidKeyword: 329>
    WAndKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WAndKeyword: 332>
    WOrKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WOrKeyword: 341>
    WaitKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WaitKeyword: 330>
    WaitOrderKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WaitOrderKeyword: 331>
    Weak0Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Weak0Keyword: 334>
    Weak1Keyword: typing.ClassVar[TokenKind]  # value = <TokenKind.Weak1Keyword: 335>
    WeakKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WeakKeyword: 333>
    WhileKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WhileKeyword: 336>
    WildcardKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WildcardKeyword: 337>
    WireKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WireKeyword: 338>
    WithKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WithKeyword: 339>
    WithinKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.WithinKeyword: 340>
    XnorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.XnorKeyword: 342>
    Xor: typing.ClassVar[TokenKind]  # value = <TokenKind.Xor: 53>
    XorEqual: typing.ClassVar[TokenKind]  # value = <TokenKind.XorEqual: 67>
    XorKeyword: typing.ClassVar[TokenKind]  # value = <TokenKind.XorKeyword: 343>
    XorTilde: typing.ClassVar[TokenKind]  # value = <TokenKind.XorTilde: 54>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class TransListCoverageBinInitializerSyntax(CoverageBinInitializerSyntax):
    sets: SeparatedSyntaxList[TransSetSyntax]
class TransRangeSyntax(SyntaxNode):
    items: SeparatedSyntaxList[ExpressionSyntax]
    repeat: TransRepeatRangeSyntax
class TransRepeatRangeSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    selector: SelectorSyntax
    specifier: Token
class TransSetSyntax(SyntaxNode):
    closeParen: Token
    openParen: Token
    ranges: SeparatedSyntaxList[TransRangeSyntax]
class TransparentMemberSymbol(Symbol):
    @property
    def wrapped(self) -> Symbol:
        ...
class Trivia:
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, kind: TriviaKind, rawText: str) -> None:
        ...
    def __repr__(self) -> str:
        ...
    def getExplicitLocation(self) -> SourceLocation | None:
        ...
    def getRawText(self) -> str:
        ...
    def getSkippedTokens(self) -> span[Token]:
        ...
    def syntax(self) -> SyntaxNode:
        ...
    @property
    def kind(self) -> TriviaKind:
        ...
class TriviaKind:
    BlockComment: typing.ClassVar[TriviaKind]  # value = <TriviaKind.BlockComment: 4>
    Directive: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Directive: 8>
    DisabledText: typing.ClassVar[TriviaKind]  # value = <TriviaKind.DisabledText: 5>
    EndOfLine: typing.ClassVar[TriviaKind]  # value = <TriviaKind.EndOfLine: 2>
    LineComment: typing.ClassVar[TriviaKind]  # value = <TriviaKind.LineComment: 3>
    SkippedSyntax: typing.ClassVar[TriviaKind]  # value = <TriviaKind.SkippedSyntax: 7>
    SkippedTokens: typing.ClassVar[TriviaKind]  # value = <TriviaKind.SkippedTokens: 6>
    Unknown: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Unknown: 0>
    Whitespace: typing.ClassVar[TriviaKind]  # value = <TriviaKind.Whitespace: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class Type(Symbol):
    @staticmethod
    def getCommonBase(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    def __repr__(self) -> str:
        ...
    def coerceValue(self, rhs: ConstantValue) -> ConstantValue:
        ...
    def implements(self, rhs: Type) -> bool:
        ...
    def isAssignmentCompatible(self, rhs: Type) -> bool:
        ...
    def isBitstreamCastable(self, rhs: Type) -> bool:
        ...
    def isBitstreamType(self, destination: bool = False) -> bool:
        ...
    def isCastCompatible(self, rhs: Type) -> bool:
        ...
    def isDerivedFrom(self, rhs: Type) -> bool:
        ...
    def isEquivalent(self, rhs: Type) -> bool:
        ...
    def isMatching(self, rhs: Type) -> bool:
        ...
    def isValidForRand(self, rhs: RandMode) -> bool:
        ...
    @property
    def arrayElementType(self) -> Type:
        ...
    @property
    def associativeIndexType(self) -> Type:
        ...
    @property
    def bitWidth(self) -> int:
        ...
    @property
    def bitstreamWidth(self) -> int:
        ...
    @property
    def canBeStringLike(self) -> bool:
        ...
    @property
    def canonicalType(self) -> Type:
        ...
    @property
    def defaultValue(self) -> ConstantValue:
        ...
    @property
    def fixedRange(self) -> ConstantRange:
        ...
    @property
    def hasFixedRange(self) -> bool:
        ...
    @property
    def integralFlags(self) -> IntegralFlags:
        ...
    @property
    def isAggregate(self) -> bool:
        ...
    @property
    def isAlias(self) -> bool:
        ...
    @property
    def isArray(self) -> bool:
        ...
    @property
    def isAssociativeArray(self) -> bool:
        ...
    @property
    def isBooleanConvertible(self) -> bool:
        ...
    @property
    def isByteArray(self) -> bool:
        ...
    @property
    def isCHandle(self) -> bool:
        ...
    @property
    def isClass(self) -> bool:
        ...
    @property
    def isCovergroup(self) -> bool:
        ...
    @property
    def isDynamicallySizedArray(self) -> bool:
        ...
    @property
    def isEnum(self) -> bool:
        ...
    @property
    def isError(self) -> bool:
        ...
    @property
    def isEvent(self) -> bool:
        ...
    @property
    def isFixedSize(self) -> bool:
        ...
    @property
    def isFloating(self) -> bool:
        ...
    @property
    def isFourState(self) -> bool:
        ...
    @property
    def isIntegral(self) -> bool:
        ...
    @property
    def isIterable(self) -> bool:
        ...
    @property
    def isNull(self) -> bool:
        ...
    @property
    def isNumeric(self) -> bool:
        ...
    @property
    def isPackedArray(self) -> bool:
        ...
    @property
    def isPackedUnion(self) -> bool:
        ...
    @property
    def isPredefinedInteger(self) -> bool:
        ...
    @property
    def isPropertyType(self) -> bool:
        ...
    @property
    def isQueue(self) -> bool:
        ...
    @property
    def isScalar(self) -> bool:
        ...
    @property
    def isSequenceType(self) -> bool:
        ...
    @property
    def isSigned(self) -> bool:
        ...
    @property
    def isSimpleBitVector(self) -> bool:
        ...
    @property
    def isSimpleType(self) -> bool:
        ...
    @property
    def isSingular(self) -> bool:
        ...
    @property
    def isString(self) -> bool:
        ...
    @property
    def isStruct(self) -> bool:
        ...
    @property
    def isTaggedUnion(self) -> bool:
        ...
    @property
    def isTypeRefType(self) -> bool:
        ...
    @property
    def isUnbounded(self) -> bool:
        ...
    @property
    def isUnpackedArray(self) -> bool:
        ...
    @property
    def isUnpackedStruct(self) -> bool:
        ...
    @property
    def isUnpackedUnion(self) -> bool:
        ...
    @property
    def isUntypedType(self) -> bool:
        ...
    @property
    def isValidForDPIArg(self) -> bool:
        ...
    @property
    def isValidForDPIReturn(self) -> bool:
        ...
    @property
    def isValidForSequence(self) -> bool:
        ...
    @property
    def isVirtualInterface(self) -> bool:
        ...
    @property
    def isVoid(self) -> bool:
        ...
    @property
    def selectableWidth(self) -> int:
        ...
class TypeAliasType(Type):
    @property
    def firstForwardDecl(self) -> ForwardingTypedefSymbol:
        ...
    @property
    def targetType(self) -> DeclaredType:
        ...
    @property
    def visibility(self) -> Visibility:
        ...
class TypeAssignmentSyntax(SyntaxNode):
    assignment: EqualsTypeClauseSyntax
    name: Token
class TypeParameterDeclarationSyntax(ParameterDeclarationBaseSyntax):
    declarators: SeparatedSyntaxList[TypeAssignmentSyntax]
    typeKeyword: Token
    typeRestriction: ForwardTypeRestrictionSyntax
class TypeParameterSymbol(Symbol, ParameterSymbolBase):
    @property
    def isOverridden(self) -> bool:
        ...
    @property
    def targetType(self) -> DeclaredType:
        ...
    @property
    def typeAlias(self) -> Type:
        ...
class TypePrinter:
    options: TypePrintingOptions
    def __init__(self) -> None:
        ...
    def append(self, type: Type) -> None:
        ...
    def clear(self) -> None:
        ...
    def toString(self) -> str:
        ...
class TypePrintingOptions:
    class AnonymousTypeStyle:
        FriendlyName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.FriendlyName: 1>
        SystemName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.SystemName: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    FriendlyName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.FriendlyName: 1>
    SystemName: typing.ClassVar[TypePrintingOptions.AnonymousTypeStyle]  # value = <AnonymousTypeStyle.SystemName: 0>
    addSingleQuotes: bool
    anonymousTypeStyle: TypePrintingOptions.AnonymousTypeStyle
    elideScopeNames: bool
    fullEnumType: TypePrintingOptions.AnonymousTypeStyle
    printAKA: bool
    skipScopedTypeNames: TypePrintingOptions.AnonymousTypeStyle
class TypeRefType(Type):
    pass
class TypeReferenceExpression(Expression):
    @property
    def targetType(self) -> Type:
        ...
class TypeReferenceSyntax(DataTypeSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    typeKeyword: Token
class TypedefDeclarationSyntax(MemberSyntax):
    dimensions: SyntaxList[VariableDimensionSyntax]
    name: Token
    semi: Token
    type: DataTypeSyntax
    typedefKeyword: Token
class UdpBodySyntax(SyntaxNode):
    endtable: Token
    entries: SyntaxList[UdpEntrySyntax]
    initialStmt: UdpInitialStmtSyntax
    portDecls: SeparatedSyntaxList[UdpPortDeclSyntax]
    table: Token
class UdpDeclarationSyntax(MemberSyntax):
    body: UdpBodySyntax
    endBlockName: NamedBlockClauseSyntax
    endprimitive: Token
    name: Token
    portList: UdpPortListSyntax
    primitive: Token
class UdpEdgeFieldSyntax(UdpFieldBaseSyntax):
    closeParen: Token
    first: Token
    openParen: Token
    second: Token
class UdpEntrySyntax(SyntaxNode):
    colon1: Token
    colon2: Token
    current: UdpFieldBaseSyntax
    inputs: SyntaxList[UdpFieldBaseSyntax]
    next: UdpFieldBaseSyntax
    semi: Token
class UdpFieldBaseSyntax(SyntaxNode):
    pass
class UdpInitialStmtSyntax(SyntaxNode):
    equals: Token
    initial: Token
    name: Token
    semi: Token
    value: ExpressionSyntax
class UdpInputPortDeclSyntax(UdpPortDeclSyntax):
    keyword: Token
    names: SeparatedSyntaxList[IdentifierNameSyntax]
class UdpOutputPortDeclSyntax(UdpPortDeclSyntax):
    initializer: EqualsValueClauseSyntax
    keyword: Token
    name: Token
    reg: Token
class UdpPortDeclSyntax(SyntaxNode):
    attributes: SyntaxList[AttributeInstanceSyntax]
class UdpPortListSyntax(SyntaxNode):
    pass
class UdpSimpleFieldSyntax(UdpFieldBaseSyntax):
    field: Token
class UnaryAssertionExpr(AssertionExpr):
    @property
    def expr(self) -> AssertionExpr:
        ...
    @property
    def op(self) -> UnaryAssertionOperator:
        ...
    @property
    def range(self) -> SequenceRange | None:
        ...
class UnaryAssertionOperator:
    Always: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Always: 3>
    Eventually: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Eventually: 5>
    NextTime: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.NextTime: 1>
    Not: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.Not: 0>
    SAlways: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SAlways: 4>
    SEventually: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SEventually: 6>
    SNextTime: typing.ClassVar[UnaryAssertionOperator]  # value = <UnaryAssertionOperator.SNextTime: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnaryBinsSelectExpr(BinsSelectExpr):
    class Op:
        Negation: typing.ClassVar[UnaryBinsSelectExpr.Op]  # value = <Op.Negation: 0>
        def __eq__(self, other: typing.Any) -> bool:
            ...
        def __getstate__(self) -> int:
            ...
        def __hash__(self) -> int:
            ...
        def __index__(self) -> int:
            ...
        def __init__(self, value: int) -> None:
            ...
        def __int__(self) -> int:
            ...
        def __ne__(self, other: typing.Any) -> bool:
            ...
        def __repr__(self) -> str:
            ...
        def __setstate__(self, state: int) -> None:
            ...
        def __str__(self) -> str:
            ...
        @property
        def __doc__(self) -> str:
            ...
        @property
        def __members__(self) -> dict:
            ...
        @property
        def name(self) -> str:
            ...
        @property
        def value(self) -> int:
            ...
    Negation: typing.ClassVar[UnaryBinsSelectExpr.Op]  # value = <Op.Negation: 0>
    @property
    def expr(self) -> BinsSelectExpr:
        ...
    @property
    def op(self) -> UnaryBinsSelectExpr.Op:
        ...
class UnaryBinsSelectExprSyntax(BinsSelectExpressionSyntax):
    expr: BinsSelectConditionExprSyntax
    op: Token
class UnaryConditionalDirectiveExpressionSyntax(ConditionalDirectiveExpressionSyntax):
    op: Token
    operand: ConditionalDirectiveExpressionSyntax
class UnaryExpression(Expression):
    @property
    def op(self) -> UnaryOperator:
        ...
    @property
    def operand(self) -> Expression:
        ...
class UnaryOperator:
    BitwiseAnd: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseAnd: 3>
    BitwiseNand: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNand: 6>
    BitwiseNor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNor: 7>
    BitwiseNot: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseNot: 2>
    BitwiseOr: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseOr: 4>
    BitwiseXnor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseXnor: 8>
    BitwiseXor: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.BitwiseXor: 5>
    LogicalNot: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.LogicalNot: 9>
    Minus: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Minus: 1>
    Plus: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Plus: 0>
    Postdecrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Postdecrement: 13>
    Postincrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Postincrement: 12>
    Predecrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Predecrement: 11>
    Preincrement: typing.ClassVar[UnaryOperator]  # value = <UnaryOperator.Preincrement: 10>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnaryPropertyExprSyntax(PropertyExprSyntax):
    expr: PropertyExprSyntax
    op: Token
class UnarySelectPropertyExprSyntax(PropertyExprSyntax):
    closeBracket: Token
    expr: PropertyExprSyntax
    op: Token
    openBracket: Token
    selector: SelectorSyntax
class UnbasedUnsizedIntegerLiteral(Expression):
    @property
    def literalValue(self) -> logic_t:
        ...
    @property
    def value(self) -> SVInt:
        ...
class Unbounded:
    def __init__(self) -> None:
        ...
    def __repr__(self) -> str:
        ...
class UnboundedLiteral(Expression):
    pass
class UnboundedType(Type):
    pass
class UnconditionalBranchDirectiveSyntax(DirectiveSyntax):
    disabledTokens: TokenList
class UnconnectedDrive:
    None_: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.None: 0>
    Pull0: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.Pull0: 1>
    Pull1: typing.ClassVar[UnconnectedDrive]  # value = <UnconnectedDrive.Pull1: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UnconnectedDriveDirectiveSyntax(DirectiveSyntax):
    strength: Token
class UndefDirectiveSyntax(DirectiveSyntax):
    name: Token
class UninstantiatedDefSymbol(Symbol):
    @property
    def definitionName(self) -> str:
        ...
    @property
    def isChecker(self) -> bool:
        ...
    @property
    def paramExpressions(self) -> span[Expression]:
        ...
    @property
    def portConnections(self) -> span[AssertionExpr]:
        ...
    @property
    def portNames(self) -> span[str]:
        ...
class UniquePriorityCheck:
    None_: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.None: 0>
    Priority: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Priority: 3>
    Unique: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Unique: 1>
    Unique0: typing.ClassVar[UniquePriorityCheck]  # value = <UniquePriorityCheck.Unique0: 2>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class UniquenessConstraint(Constraint):
    @property
    def items(self) -> span[Expression]:
        ...
class UniquenessConstraintSyntax(ConstraintItemSyntax):
    ranges: RangeListSyntax
    semi: Token
    unique: Token
class UnpackedStructType(Type, Scope):
    @property
    def systemId(self) -> int:
        ...
class UnpackedUnionType(Type, Scope):
    @property
    def isTagged(self) -> bool:
        ...
    @property
    def systemId(self) -> int:
        ...
class UntypedType(Type):
    pass
class UserDefinedNetDeclarationSyntax(MemberSyntax):
    declarators: SeparatedSyntaxList[DeclaratorSyntax]
    delay: TimingControlSyntax
    netType: Token
    semi: Token
class ValueDriver:
    @property
    def containingSymbol(self) -> Symbol:
        ...
    @property
    def flags(self) -> AssignFlags:
        ...
    @property
    def isClockVar(self) -> bool:
        ...
    @property
    def isInInitialBlock(self) -> bool:
        ...
    @property
    def isInSingleDriverProcedure(self) -> bool:
        ...
    @property
    def isInSubroutine(self) -> bool:
        ...
    @property
    def isInputPort(self) -> bool:
        ...
    @property
    def isLocalVarFormalArg(self) -> bool:
        ...
    @property
    def isUnidirectionalPort(self) -> bool:
        ...
    @property
    def kind(self) -> DriverKind:
        ...
    @property
    def prefixExpression(self) -> Expression:
        ...
    @property
    def procCallExpression(self) -> Expression:
        ...
    @property
    def sourceRange(self) -> SourceRange:
        ...
class ValueExpressionBase(Expression):
    @property
    def symbol(self) -> ValueSymbol:
        ...
class ValueRangeExpression(Expression):
    @property
    def left(self) -> Expression:
        ...
    @property
    def right(self) -> Expression:
        ...
class ValueRangeExpressionSyntax(ExpressionSyntax):
    closeBracket: Token
    left: ExpressionSyntax
    op: Token
    openBracket: Token
    right: ExpressionSyntax
class ValueRangeKind:
    AbsoluteTolerance: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.AbsoluteTolerance: 1>
    RelativeTolerance: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.RelativeTolerance: 2>
    Simple: typing.ClassVar[ValueRangeKind]  # value = <ValueRangeKind.Simple: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class ValueSymbol(Symbol):
    def __iter__(self) -> typing.Iterator[ValueDriver]:
        ...
    @property
    def initializer(self) -> Expression:
        ...
    @property
    def type(self) -> Type:
        ...
class VariableDeclStatement(Statement):
    @property
    def symbol(self) -> VariableSymbol:
        ...
class VariableDimensionSyntax(SyntaxNode):
    closeBracket: Token
    openBracket: Token
    specifier: DimensionSpecifierSyntax
class VariableFlags:
    CheckerFreeVariable: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CheckerFreeVariable: 16>
    CompilerGenerated: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CompilerGenerated: 2>
    Const: typing.ClassVar[VariableFlags]  # value = <VariableFlags.Const: 1>
    CoverageSampleFormal: typing.ClassVar[VariableFlags]  # value = <VariableFlags.CoverageSampleFormal: 8>
    ImmutableCoverageOption: typing.ClassVar[VariableFlags]  # value = <VariableFlags.ImmutableCoverageOption: 4>
    None_: typing.ClassVar[VariableFlags]  # value = <VariableFlags.None: 0>
    RefStatic: typing.ClassVar[VariableFlags]  # value = <VariableFlags.RefStatic: 32>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VariableLifetime:
    Automatic: typing.ClassVar[VariableLifetime]  # value = <VariableLifetime.Automatic: 0>
    Static: typing.ClassVar[VariableLifetime]  # value = <VariableLifetime.Static: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VariablePattern(Pattern):
    @property
    def variable(self) -> PatternVarSymbol:
        ...
class VariablePatternSyntax(PatternSyntax):
    dot: Token
    variableName: Token
class VariablePortHeaderSyntax(PortHeaderSyntax):
    constKeyword: Token
    dataType: DataTypeSyntax
    direction: Token
    varKeyword: Token
class VariableSymbol(ValueSymbol):
    @property
    def flags(self) -> VariableFlags:
        ...
    @property
    def lifetime(self) -> VariableLifetime:
        ...
class VersionInfo:
    @staticmethod
    def getHash(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getMajor(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getMinor(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
    @staticmethod
    def getPatch(*args, **kwargs):
        """
        staticmethod(function) -> method

        Convert a function to be a static method.

        A static method does not receive an implicit first argument.
        To declare a static method, use this idiom:

             class C:
                 @staticmethod
                 def f(arg1, arg2, argN):
                     ...

        It can be called either on the class (e.g. C.f()) or on an instance
        (e.g. C().f()). Both the class and the instance are ignored, and
        neither is passed implicitly as the first argument to the method.

        Static methods in Python are similar to those found in Java or C++.
        For a more advanced concept, see the classmethod builtin.
        """
class VirtualInterfaceType(Type):
    @property
    def iface(self) -> InstanceSymbol:
        ...
    @property
    def modport(self) -> ModportSymbol:
        ...
class VirtualInterfaceTypeSyntax(DataTypeSyntax):
    interfaceKeyword: Token
    modport: DotMemberClauseSyntax
    name: Token
    parameters: ParameterValueAssignmentSyntax
    virtualKeyword: Token
class Visibility:
    Local: typing.ClassVar[Visibility]  # value = <Visibility.Local: 2>
    Protected: typing.ClassVar[Visibility]  # value = <Visibility.Protected: 1>
    Public: typing.ClassVar[Visibility]  # value = <Visibility.Public: 0>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VisitAction:
    Advance: typing.ClassVar[VisitAction]  # value = <VisitAction.Advance: 0>
    Interrupt: typing.ClassVar[VisitAction]  # value = <VisitAction.Interrupt: 2>
    Skip: typing.ClassVar[VisitAction]  # value = <VisitAction.Skip: 1>
    def __eq__(self, other: typing.Any) -> bool:
        ...
    def __getstate__(self) -> int:
        ...
    def __hash__(self) -> int:
        ...
    def __index__(self) -> int:
        ...
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __ne__(self, other: typing.Any) -> bool:
        ...
    def __repr__(self) -> str:
        ...
    def __setstate__(self, state: int) -> None:
        ...
    def __str__(self) -> str:
        ...
    @property
    def __doc__(self) -> str:
        ...
    @property
    def __members__(self) -> dict:
        ...
    @property
    def name(self) -> str:
        ...
    @property
    def value(self) -> int:
        ...
class VoidCastedCallStatementSyntax(StatementSyntax):
    apostrophe: Token
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    semi: Token
    voidKeyword: Token
class VoidType(Type):
    pass
class WaitForkStatement(Statement):
    pass
class WaitForkStatementSyntax(StatementSyntax):
    fork: Token
    semi: Token
    wait: Token
class WaitOrderStatement(Statement):
    @property
    def events(self) -> span[Expression]:
        ...
    @property
    def ifFalse(self) -> Statement:
        ...
    @property
    def ifTrue(self) -> Statement:
        ...
class WaitOrderStatementSyntax(StatementSyntax):
    action: ActionBlockSyntax
    closeParen: Token
    names: SeparatedSyntaxList[NameSyntax]
    openParen: Token
    wait_order: Token
class WaitStatement(Statement):
    @property
    def cond(self) -> Expression:
        ...
    @property
    def stmt(self) -> Statement:
        ...
class WaitStatementSyntax(StatementSyntax):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    statement: StatementSyntax
    wait: Token
class WhileLoopStatement(Statement):
    @property
    def body(self) -> Statement:
        ...
    @property
    def cond(self) -> Expression:
        ...
class WildcardDimensionSpecifierSyntax(DimensionSpecifierSyntax):
    star: Token
class WildcardImportSymbol(Symbol):
    @property
    def isFromExport(self) -> bool:
        ...
    @property
    def package(self) -> PackageSymbol:
        ...
    @property
    def packageName(self) -> str:
        ...
class WildcardPattern(Pattern):
    pass
class WildcardPatternSyntax(PatternSyntax):
    dotStar: Token
class WildcardPortConnectionSyntax(PortConnectionSyntax):
    dotStar: Token
class WildcardPortListSyntax(PortListSyntax):
    closeParen: Token
    dotStar: Token
    openParen: Token
class WildcardUdpPortListSyntax(UdpPortListSyntax):
    closeParen: Token
    dotStar: Token
    openParen: Token
    semi: Token
class WithClauseSyntax(SyntaxNode):
    closeParen: Token
    expr: ExpressionSyntax
    openParen: Token
    with_: Token
class WithFunctionClauseSyntax(SyntaxNode):
    name: NameSyntax
    with_: Token
class WithFunctionSampleSyntax(SyntaxNode):
    function: Token
    portList: FunctionPortListSyntax
    sample: Token
    with_: Token
class logic_t:
    __hash__: typing.ClassVar[None] = None
    value: int
    def __and__(self, arg0: logic_t) -> logic_t:
        ...
    def __bool__(self) -> bool:
        ...
    def __eq__(self, arg0: logic_t) -> logic_t:
        ...
    @typing.overload
    def __init__(self) -> None:
        ...
    @typing.overload
    def __init__(self, value: int) -> None:
        ...
    def __int__(self) -> int:
        ...
    def __invert__(self) -> logic_t:
        ...
    def __ne__(self, arg0: logic_t) -> logic_t:
        ...
    def __or__(self, arg0: logic_t) -> logic_t:
        ...
    def __repr__(self) -> str:
        ...
    def __xor__(self, arg0: logic_t) -> logic_t:
        ...
    @property
    def isUnknown(self) -> bool:
        ...
    @property
    def x(self) -> logic_t:
        ...
    @property
    def z(self) -> logic_t:
        ...
def clog2(value: SVInt) -> int:
    ...
def literalBaseFromChar(base: str, result: LiteralBase) -> bool:
    ...
__version__: str = '6.0.0'


# manual additions:
class SyntaxList[Inner: SyntaxNode](SyntaxNode): ...
class SeparatedSyntaxList[Inner: SyntaxNode](SyntaxNode): ...
span = tuple

__all__ += [ "SyntaxList", "SeparatedSyntaxList" ]
