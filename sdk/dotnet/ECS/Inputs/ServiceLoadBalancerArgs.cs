// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ECS.Inputs
{

    public sealed class ServiceLoadBalancerArgs : global::Pulumi.ResourceArgs
    {
        [Input("containerName")]
        public Input<string>? ContainerName { get; set; }

        [Input("containerPort")]
        public Input<int>? ContainerPort { get; set; }

        [Input("loadBalancerName")]
        public Input<string>? LoadBalancerName { get; set; }

        [Input("targetGroupArn")]
        public Input<string>? TargetGroupArn { get; set; }

        public ServiceLoadBalancerArgs()
        {
        }
        public static new ServiceLoadBalancerArgs Empty => new ServiceLoadBalancerArgs();
    }
}
