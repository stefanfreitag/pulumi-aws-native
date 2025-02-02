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
    public sealed class DashboardPivotTableVisual
    {
        public readonly ImmutableArray<Outputs.DashboardVisualCustomAction> Actions;
        public readonly Outputs.DashboardPivotTableConfiguration? ChartConfiguration;
        public readonly Outputs.DashboardPivotTableConditionalFormatting? ConditionalFormatting;
        public readonly Outputs.DashboardVisualSubtitleLabelOptions? Subtitle;
        public readonly Outputs.DashboardVisualTitleLabelOptions? Title;
        public readonly string VisualId;

        [OutputConstructor]
        private DashboardPivotTableVisual(
            ImmutableArray<Outputs.DashboardVisualCustomAction> actions,

            Outputs.DashboardPivotTableConfiguration? chartConfiguration,

            Outputs.DashboardPivotTableConditionalFormatting? conditionalFormatting,

            Outputs.DashboardVisualSubtitleLabelOptions? subtitle,

            Outputs.DashboardVisualTitleLabelOptions? title,

            string visualId)
        {
            Actions = actions;
            ChartConfiguration = chartConfiguration;
            ConditionalFormatting = conditionalFormatting;
            Subtitle = subtitle;
            Title = title;
            VisualId = visualId;
        }
    }
}
