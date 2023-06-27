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
    public sealed class TemplateVisualPalette
    {
        public readonly string? ChartColor;
        public readonly ImmutableArray<Outputs.TemplateDataPathColor> ColorMap;

        [OutputConstructor]
        private TemplateVisualPalette(
            string? chartColor,

            ImmutableArray<Outputs.TemplateDataPathColor> colorMap)
        {
            ChartColor = chartColor;
            ColorMap = colorMap;
        }
    }
}
