// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataBrew.Inputs
{

    public sealed class RecipeRecipeParametersArgs : Pulumi.ResourceArgs
    {
        [Input("aggregateFunction")]
        public Input<string>? AggregateFunction { get; set; }

        [Input("base")]
        public Input<string>? Base { get; set; }

        [Input("caseStatement")]
        public Input<string>? CaseStatement { get; set; }

        [Input("categoryMap")]
        public Input<string>? CategoryMap { get; set; }

        [Input("charsToRemove")]
        public Input<string>? CharsToRemove { get; set; }

        [Input("collapseConsecutiveWhitespace")]
        public Input<string>? CollapseConsecutiveWhitespace { get; set; }

        [Input("columnDataType")]
        public Input<string>? ColumnDataType { get; set; }

        [Input("columnRange")]
        public Input<string>? ColumnRange { get; set; }

        [Input("count")]
        public Input<string>? Count { get; set; }

        [Input("customCharacters")]
        public Input<string>? CustomCharacters { get; set; }

        [Input("customStopWords")]
        public Input<string>? CustomStopWords { get; set; }

        [Input("customValue")]
        public Input<string>? CustomValue { get; set; }

        [Input("datasetsColumns")]
        public Input<string>? DatasetsColumns { get; set; }

        [Input("dateAddValue")]
        public Input<string>? DateAddValue { get; set; }

        [Input("dateTimeFormat")]
        public Input<string>? DateTimeFormat { get; set; }

        [Input("dateTimeParameters")]
        public Input<string>? DateTimeParameters { get; set; }

        [Input("deleteOtherRows")]
        public Input<string>? DeleteOtherRows { get; set; }

        [Input("delimiter")]
        public Input<string>? Delimiter { get; set; }

        [Input("endPattern")]
        public Input<string>? EndPattern { get; set; }

        [Input("endPosition")]
        public Input<string>? EndPosition { get; set; }

        [Input("endValue")]
        public Input<string>? EndValue { get; set; }

        [Input("expandContractions")]
        public Input<string>? ExpandContractions { get; set; }

        [Input("exponent")]
        public Input<string>? Exponent { get; set; }

        [Input("falseString")]
        public Input<string>? FalseString { get; set; }

        [Input("groupByAggFunctionOptions")]
        public Input<string>? GroupByAggFunctionOptions { get; set; }

        [Input("groupByColumns")]
        public Input<string>? GroupByColumns { get; set; }

        [Input("hiddenColumns")]
        public Input<string>? HiddenColumns { get; set; }

        [Input("ignoreCase")]
        public Input<string>? IgnoreCase { get; set; }

        [Input("includeInSplit")]
        public Input<string>? IncludeInSplit { get; set; }

        /// <summary>
        /// Input
        /// </summary>
        [Input("input")]
        public Input<object>? Input { get; set; }

        [Input("interval")]
        public Input<string>? Interval { get; set; }

        [Input("isText")]
        public Input<string>? IsText { get; set; }

        [Input("joinKeys")]
        public Input<string>? JoinKeys { get; set; }

        [Input("joinType")]
        public Input<string>? JoinType { get; set; }

        [Input("leftColumns")]
        public Input<string>? LeftColumns { get; set; }

        [Input("limit")]
        public Input<string>? Limit { get; set; }

        [Input("lowerBound")]
        public Input<string>? LowerBound { get; set; }

        [Input("mapType")]
        public Input<string>? MapType { get; set; }

        [Input("modeType")]
        public Input<string>? ModeType { get; set; }

        [Input("multiLine")]
        public Input<bool>? MultiLine { get; set; }

        [Input("numRows")]
        public Input<string>? NumRows { get; set; }

        [Input("numRowsAfter")]
        public Input<string>? NumRowsAfter { get; set; }

        [Input("numRowsBefore")]
        public Input<string>? NumRowsBefore { get; set; }

        [Input("orderByColumn")]
        public Input<string>? OrderByColumn { get; set; }

        [Input("orderByColumns")]
        public Input<string>? OrderByColumns { get; set; }

        [Input("other")]
        public Input<string>? Other { get; set; }

        [Input("pattern")]
        public Input<string>? Pattern { get; set; }

        [Input("patternOption1")]
        public Input<string>? PatternOption1 { get; set; }

        [Input("patternOption2")]
        public Input<string>? PatternOption2 { get; set; }

        [Input("patternOptions")]
        public Input<string>? PatternOptions { get; set; }

        [Input("period")]
        public Input<string>? Period { get; set; }

        [Input("position")]
        public Input<string>? Position { get; set; }

        [Input("removeAllPunctuation")]
        public Input<string>? RemoveAllPunctuation { get; set; }

        [Input("removeAllQuotes")]
        public Input<string>? RemoveAllQuotes { get; set; }

        [Input("removeAllWhitespace")]
        public Input<string>? RemoveAllWhitespace { get; set; }

        [Input("removeCustomCharacters")]
        public Input<string>? RemoveCustomCharacters { get; set; }

        [Input("removeCustomValue")]
        public Input<string>? RemoveCustomValue { get; set; }

        [Input("removeLeadingAndTrailingPunctuation")]
        public Input<string>? RemoveLeadingAndTrailingPunctuation { get; set; }

        [Input("removeLeadingAndTrailingQuotes")]
        public Input<string>? RemoveLeadingAndTrailingQuotes { get; set; }

        [Input("removeLeadingAndTrailingWhitespace")]
        public Input<string>? RemoveLeadingAndTrailingWhitespace { get; set; }

        [Input("removeLetters")]
        public Input<string>? RemoveLetters { get; set; }

        [Input("removeNumbers")]
        public Input<string>? RemoveNumbers { get; set; }

        [Input("removeSourceColumn")]
        public Input<string>? RemoveSourceColumn { get; set; }

        [Input("removeSpecialCharacters")]
        public Input<string>? RemoveSpecialCharacters { get; set; }

        [Input("rightColumns")]
        public Input<string>? RightColumns { get; set; }

        [Input("sampleSize")]
        public Input<string>? SampleSize { get; set; }

        [Input("sampleType")]
        public Input<string>? SampleType { get; set; }

        [Input("secondInput")]
        public Input<string>? SecondInput { get; set; }

        [Input("secondaryInputs")]
        private InputList<Inputs.RecipeSecondaryInputArgs>? _secondaryInputs;
        public InputList<Inputs.RecipeSecondaryInputArgs> SecondaryInputs
        {
            get => _secondaryInputs ?? (_secondaryInputs = new InputList<Inputs.RecipeSecondaryInputArgs>());
            set => _secondaryInputs = value;
        }

        [Input("sheetIndexes")]
        private InputList<int>? _sheetIndexes;
        public InputList<int> SheetIndexes
        {
            get => _sheetIndexes ?? (_sheetIndexes = new InputList<int>());
            set => _sheetIndexes = value;
        }

        [Input("sheetNames")]
        private InputList<string>? _sheetNames;
        public InputList<string> SheetNames
        {
            get => _sheetNames ?? (_sheetNames = new InputList<string>());
            set => _sheetNames = value;
        }

        [Input("sourceColumn")]
        public Input<string>? SourceColumn { get; set; }

        [Input("sourceColumn1")]
        public Input<string>? SourceColumn1 { get; set; }

        [Input("sourceColumn2")]
        public Input<string>? SourceColumn2 { get; set; }

        [Input("sourceColumns")]
        public Input<string>? SourceColumns { get; set; }

        [Input("startColumnIndex")]
        public Input<string>? StartColumnIndex { get; set; }

        [Input("startPattern")]
        public Input<string>? StartPattern { get; set; }

        [Input("startPosition")]
        public Input<string>? StartPosition { get; set; }

        [Input("startValue")]
        public Input<string>? StartValue { get; set; }

        [Input("stemmingMode")]
        public Input<string>? StemmingMode { get; set; }

        [Input("stepCount")]
        public Input<string>? StepCount { get; set; }

        [Input("stepIndex")]
        public Input<string>? StepIndex { get; set; }

        [Input("stopWordsMode")]
        public Input<string>? StopWordsMode { get; set; }

        [Input("strategy")]
        public Input<string>? Strategy { get; set; }

        [Input("targetColumn")]
        public Input<string>? TargetColumn { get; set; }

        [Input("targetColumnNames")]
        public Input<string>? TargetColumnNames { get; set; }

        [Input("targetDateFormat")]
        public Input<string>? TargetDateFormat { get; set; }

        [Input("targetIndex")]
        public Input<string>? TargetIndex { get; set; }

        [Input("timeZone")]
        public Input<string>? TimeZone { get; set; }

        [Input("tokenizerPattern")]
        public Input<string>? TokenizerPattern { get; set; }

        [Input("trueString")]
        public Input<string>? TrueString { get; set; }

        [Input("udfLang")]
        public Input<string>? UdfLang { get; set; }

        [Input("units")]
        public Input<string>? Units { get; set; }

        [Input("unpivotColumn")]
        public Input<string>? UnpivotColumn { get; set; }

        [Input("upperBound")]
        public Input<string>? UpperBound { get; set; }

        [Input("useNewDataFrame")]
        public Input<string>? UseNewDataFrame { get; set; }

        [Input("value")]
        public Input<string>? Value { get; set; }

        [Input("value1")]
        public Input<string>? Value1 { get; set; }

        [Input("value2")]
        public Input<string>? Value2 { get; set; }

        [Input("valueColumn")]
        public Input<string>? ValueColumn { get; set; }

        [Input("viewFrame")]
        public Input<string>? ViewFrame { get; set; }

        public RecipeRecipeParametersArgs()
        {
        }
    }
}
