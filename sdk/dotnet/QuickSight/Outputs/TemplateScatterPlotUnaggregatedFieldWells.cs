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
    public sealed class TemplateScatterPlotUnaggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.TemplateDimensionField> Category;
        public readonly ImmutableArray<Outputs.TemplateDimensionField> Label;
        public readonly ImmutableArray<Outputs.TemplateMeasureField> Size;
        public readonly ImmutableArray<Outputs.TemplateDimensionField> XAxis;
        public readonly ImmutableArray<Outputs.TemplateDimensionField> YAxis;

        [OutputConstructor]
        private TemplateScatterPlotUnaggregatedFieldWells(
            ImmutableArray<Outputs.TemplateDimensionField> category,

            ImmutableArray<Outputs.TemplateDimensionField> label,

            ImmutableArray<Outputs.TemplateMeasureField> size,

            ImmutableArray<Outputs.TemplateDimensionField> xAxis,

            ImmutableArray<Outputs.TemplateDimensionField> yAxis)
        {
            Category = category;
            Label = label;
            Size = size;
            XAxis = xAxis;
            YAxis = yAxis;
        }
    }
}
