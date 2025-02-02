// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class TemplateGeospatialPointStyleOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("clusterMarkerConfiguration")]
        public Input<Inputs.TemplateClusterMarkerConfigurationArgs>? ClusterMarkerConfiguration { get; set; }

        [Input("heatmapConfiguration")]
        public Input<Inputs.TemplateGeospatialHeatmapConfigurationArgs>? HeatmapConfiguration { get; set; }

        [Input("selectedPointStyle")]
        public Input<Pulumi.AwsNative.QuickSight.TemplateGeospatialSelectedPointStyle>? SelectedPointStyle { get; set; }

        public TemplateGeospatialPointStyleOptionsArgs()
        {
        }
        public static new TemplateGeospatialPointStyleOptionsArgs Empty => new TemplateGeospatialPointStyleOptionsArgs();
    }
}
