// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElasticLoadBalancingV2.Inputs
{

    public sealed class ListenerTargetGroupStickinessConfigArgs : Pulumi.ResourceArgs
    {
        [Input("durationSeconds")]
        public Input<int>? DurationSeconds { get; set; }

        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        public ListenerTargetGroupStickinessConfigArgs()
        {
        }
    }
}
