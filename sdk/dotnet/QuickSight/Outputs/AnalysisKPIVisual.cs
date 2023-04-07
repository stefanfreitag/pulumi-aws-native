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
    public sealed class AnalysisKPIVisual
    {
        public readonly ImmutableArray<Outputs.AnalysisVisualCustomAction> Actions;
        public readonly Outputs.AnalysisKPIConfiguration? ChartConfiguration;
        public readonly ImmutableArray<Outputs.AnalysisColumnHierarchy> ColumnHierarchies;
        public readonly Outputs.AnalysisKPIConditionalFormatting? ConditionalFormatting;
        public readonly Outputs.AnalysisVisualSubtitleLabelOptions? Subtitle;
        public readonly Outputs.AnalysisVisualTitleLabelOptions? Title;
        public readonly string VisualId;

        [OutputConstructor]
        private AnalysisKPIVisual(
            ImmutableArray<Outputs.AnalysisVisualCustomAction> actions,

            Outputs.AnalysisKPIConfiguration? chartConfiguration,

            ImmutableArray<Outputs.AnalysisColumnHierarchy> columnHierarchies,

            Outputs.AnalysisKPIConditionalFormatting? conditionalFormatting,

            Outputs.AnalysisVisualSubtitleLabelOptions? subtitle,

            Outputs.AnalysisVisualTitleLabelOptions? title,

            string visualId)
        {
            Actions = actions;
            ChartConfiguration = chartConfiguration;
            ColumnHierarchies = columnHierarchies;
            ConditionalFormatting = conditionalFormatting;
            Subtitle = subtitle;
            Title = title;
            VisualId = visualId;
        }
    }
}
