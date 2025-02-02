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
    public sealed class DashboardScatterPlotCategoricallyAggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.DashboardDimensionField> Category;
        public readonly ImmutableArray<Outputs.DashboardDimensionField> Label;
        public readonly ImmutableArray<Outputs.DashboardMeasureField> Size;
        public readonly ImmutableArray<Outputs.DashboardMeasureField> XAxis;
        public readonly ImmutableArray<Outputs.DashboardMeasureField> YAxis;

        [OutputConstructor]
        private DashboardScatterPlotCategoricallyAggregatedFieldWells(
            ImmutableArray<Outputs.DashboardDimensionField> category,

            ImmutableArray<Outputs.DashboardDimensionField> label,

            ImmutableArray<Outputs.DashboardMeasureField> size,

            ImmutableArray<Outputs.DashboardMeasureField> xAxis,

            ImmutableArray<Outputs.DashboardMeasureField> yAxis)
        {
            Category = category;
            Label = label;
            Size = size;
            XAxis = xAxis;
            YAxis = yAxis;
        }
    }
}
