// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Outputs
{

    [OutputType]
    public sealed class TopicCalculatedField
    {
        public readonly Pulumi.AwsNative.QuickSight.TopicDefaultAggregation? Aggregation;
        public readonly ImmutableArray<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> AllowedAggregations;
        public readonly string? CalculatedFieldDescription;
        public readonly string CalculatedFieldName;
        public readonly ImmutableArray<string> CalculatedFieldSynonyms;
        public readonly ImmutableArray<Outputs.TopicCellValueSynonym> CellValueSynonyms;
        public readonly Pulumi.AwsNative.QuickSight.TopicColumnDataRole? ColumnDataRole;
        public readonly Outputs.TopicComparativeOrder? ComparativeOrder;
        public readonly Outputs.TopicDefaultFormatting? DefaultFormatting;
        public readonly string Expression;
        public readonly bool? IsIncludedInTopic;
        public readonly bool? NeverAggregateInFilter;
        public readonly bool? NonAdditive;
        public readonly ImmutableArray<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> NotAllowedAggregations;
        public readonly Outputs.TopicSemanticType? SemanticType;
        public readonly Pulumi.AwsNative.QuickSight.TopicTimeGranularity? TimeGranularity;

        [OutputConstructor]
        private TopicCalculatedField(
            Pulumi.AwsNative.QuickSight.TopicDefaultAggregation? aggregation,

            ImmutableArray<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> allowedAggregations,

            string? calculatedFieldDescription,

            string calculatedFieldName,

            ImmutableArray<string> calculatedFieldSynonyms,

            ImmutableArray<Outputs.TopicCellValueSynonym> cellValueSynonyms,

            Pulumi.AwsNative.QuickSight.TopicColumnDataRole? columnDataRole,

            Outputs.TopicComparativeOrder? comparativeOrder,

            Outputs.TopicDefaultFormatting? defaultFormatting,

            string expression,

            bool? isIncludedInTopic,

            bool? neverAggregateInFilter,

            bool? nonAdditive,

            ImmutableArray<Pulumi.AwsNative.QuickSight.TopicAuthorSpecifiedAggregation> notAllowedAggregations,

            Outputs.TopicSemanticType? semanticType,

            Pulumi.AwsNative.QuickSight.TopicTimeGranularity? timeGranularity)
        {
            Aggregation = aggregation;
            AllowedAggregations = allowedAggregations;
            CalculatedFieldDescription = calculatedFieldDescription;
            CalculatedFieldName = calculatedFieldName;
            CalculatedFieldSynonyms = calculatedFieldSynonyms;
            CellValueSynonyms = cellValueSynonyms;
            ColumnDataRole = columnDataRole;
            ComparativeOrder = comparativeOrder;
            DefaultFormatting = defaultFormatting;
            Expression = expression;
            IsIncludedInTopic = isIncludedInTopic;
            NeverAggregateInFilter = neverAggregateInFilter;
            NonAdditive = nonAdditive;
            NotAllowedAggregations = notAllowedAggregations;
            SemanticType = semanticType;
            TimeGranularity = timeGranularity;
        }
    }
}
