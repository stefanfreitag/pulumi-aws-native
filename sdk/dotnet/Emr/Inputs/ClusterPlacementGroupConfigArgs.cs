// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Emr.Inputs
{

    public sealed class ClusterPlacementGroupConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("instanceRole", required: true)]
        public Input<string> InstanceRole { get; set; } = null!;

        [Input("placementStrategy")]
        public Input<string>? PlacementStrategy { get; set; }

        public ClusterPlacementGroupConfigArgs()
        {
        }
        public static new ClusterPlacementGroupConfigArgs Empty => new ClusterPlacementGroupConfigArgs();
    }
}
