// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker.Inputs
{

    public sealed class EndpointTrafficRoutingConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("canarySize")]
        public Input<Inputs.EndpointCapacitySizeArgs>? CanarySize { get; set; }

        [Input("linearStepSize")]
        public Input<Inputs.EndpointCapacitySizeArgs>? LinearStepSize { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        [Input("waitIntervalInSeconds")]
        public Input<int>? WaitIntervalInSeconds { get; set; }

        public EndpointTrafficRoutingConfigArgs()
        {
        }
        public static new EndpointTrafficRoutingConfigArgs Empty => new EndpointTrafficRoutingConfigArgs();
    }
}
