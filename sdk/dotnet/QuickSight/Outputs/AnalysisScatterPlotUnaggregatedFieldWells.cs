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
    public sealed class AnalysisScatterPlotUnaggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> Category;
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> Label;
        public readonly ImmutableArray<Outputs.AnalysisMeasureField> Size;
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> XAxis;
        public readonly ImmutableArray<Outputs.AnalysisDimensionField> YAxis;

        [OutputConstructor]
        private AnalysisScatterPlotUnaggregatedFieldWells(
            ImmutableArray<Outputs.AnalysisDimensionField> category,

            ImmutableArray<Outputs.AnalysisDimensionField> label,

            ImmutableArray<Outputs.AnalysisMeasureField> size,

            ImmutableArray<Outputs.AnalysisDimensionField> xAxis,

            ImmutableArray<Outputs.AnalysisDimensionField> yAxis)
        {
            Category = category;
            Label = label;
            Size = size;
            XAxis = xAxis;
            YAxis = yAxis;
        }
    }
}
