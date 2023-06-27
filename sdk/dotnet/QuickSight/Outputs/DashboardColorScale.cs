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
    public sealed class DashboardColorScale
    {
        public readonly Pulumi.AwsNative.QuickSight.DashboardColorFillType ColorFillType;
        public readonly ImmutableArray<Outputs.DashboardDataColor> Colors;
        public readonly Outputs.DashboardDataColor? NullValueColor;

        [OutputConstructor]
        private DashboardColorScale(
            Pulumi.AwsNative.QuickSight.DashboardColorFillType colorFillType,

            ImmutableArray<Outputs.DashboardDataColor> colors,

            Outputs.DashboardDataColor? nullValueColor)
        {
            ColorFillType = colorFillType;
            Colors = colors;
            NullValueColor = nullValueColor;
        }
    }
}
