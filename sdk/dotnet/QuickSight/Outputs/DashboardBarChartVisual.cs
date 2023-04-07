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
    public sealed class DashboardBarChartVisual
    {
        public readonly ImmutableArray<Outputs.DashboardVisualCustomAction> Actions;
        public readonly Outputs.DashboardBarChartConfiguration? ChartConfiguration;
        public readonly ImmutableArray<Outputs.DashboardColumnHierarchy> ColumnHierarchies;
        public readonly Outputs.DashboardVisualSubtitleLabelOptions? Subtitle;
        public readonly Outputs.DashboardVisualTitleLabelOptions? Title;
        public readonly string VisualId;

        [OutputConstructor]
        private DashboardBarChartVisual(
            ImmutableArray<Outputs.DashboardVisualCustomAction> actions,

            Outputs.DashboardBarChartConfiguration? chartConfiguration,

            ImmutableArray<Outputs.DashboardColumnHierarchy> columnHierarchies,

            Outputs.DashboardVisualSubtitleLabelOptions? subtitle,

            Outputs.DashboardVisualTitleLabelOptions? title,

            string visualId)
        {
            Actions = actions;
            ChartConfiguration = chartConfiguration;
            ColumnHierarchies = columnHierarchies;
            Subtitle = subtitle;
            Title = title;
            VisualId = visualId;
        }
    }
}
