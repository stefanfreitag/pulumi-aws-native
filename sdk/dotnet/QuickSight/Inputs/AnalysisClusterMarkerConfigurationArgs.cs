// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.QuickSight.Inputs
{

    public sealed class AnalysisClusterMarkerConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("clusterMarker")]
        public Input<Inputs.AnalysisClusterMarkerArgs>? ClusterMarker { get; set; }

        public AnalysisClusterMarkerConfigurationArgs()
        {
        }
        public static new AnalysisClusterMarkerConfigurationArgs Empty => new AnalysisClusterMarkerConfigurationArgs();
    }
}
