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
    public sealed class AnalysisInsightVisual
    {
        public readonly ImmutableArray<Outputs.AnalysisVisualCustomAction> Actions;
        public readonly string DataSetIdentifier;
        public readonly Outputs.AnalysisInsightConfiguration? InsightConfiguration;
        public readonly Outputs.AnalysisVisualSubtitleLabelOptions? Subtitle;
        public readonly Outputs.AnalysisVisualTitleLabelOptions? Title;
        public readonly string VisualId;

        [OutputConstructor]
        private AnalysisInsightVisual(
            ImmutableArray<Outputs.AnalysisVisualCustomAction> actions,

            string dataSetIdentifier,

            Outputs.AnalysisInsightConfiguration? insightConfiguration,

            Outputs.AnalysisVisualSubtitleLabelOptions? subtitle,

            Outputs.AnalysisVisualTitleLabelOptions? title,

            string visualId)
        {
            Actions = actions;
            DataSetIdentifier = dataSetIdentifier;
            InsightConfiguration = insightConfiguration;
            Subtitle = subtitle;
            Title = title;
            VisualId = visualId;
        }
    }
}
