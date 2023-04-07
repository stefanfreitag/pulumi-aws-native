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
    public sealed class TemplateRadarChartAggregatedFieldWells
    {
        public readonly ImmutableArray<Outputs.TemplateDimensionField> Category;
        public readonly ImmutableArray<Outputs.TemplateDimensionField> Color;
        public readonly ImmutableArray<Outputs.TemplateMeasureField> Values;

        [OutputConstructor]
        private TemplateRadarChartAggregatedFieldWells(
            ImmutableArray<Outputs.TemplateDimensionField> category,

            ImmutableArray<Outputs.TemplateDimensionField> color,

            ImmutableArray<Outputs.TemplateMeasureField> values)
        {
            Category = category;
            Color = color;
            Values = values;
        }
    }
}
