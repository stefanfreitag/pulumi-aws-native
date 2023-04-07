// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR.Inputs
{

    public sealed class ClusterSimpleScalingPolicyConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("adjustmentType")]
        public Input<string>? AdjustmentType { get; set; }

        [Input("coolDown")]
        public Input<int>? CoolDown { get; set; }

        [Input("scalingAdjustment", required: true)]
        public Input<int> ScalingAdjustment { get; set; } = null!;

        public ClusterSimpleScalingPolicyConfigurationArgs()
        {
        }
        public static new ClusterSimpleScalingPolicyConfigurationArgs Empty => new ClusterSimpleScalingPolicyConfigurationArgs();
    }
}
