// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateGeospatialHeatmapDataColorArgs : global::Pulumi.ResourceArgs
    {
        [Input("color", required: true)]
        public Input<string> Color { get; set; } = null!;

        public TemplateGeospatialHeatmapDataColorArgs()
        {
        }
        public static new TemplateGeospatialHeatmapDataColorArgs Empty => new TemplateGeospatialHeatmapDataColorArgs();
    }
}
