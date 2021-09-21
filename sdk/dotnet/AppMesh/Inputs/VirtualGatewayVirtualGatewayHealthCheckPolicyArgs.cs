// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualGatewayVirtualGatewayHealthCheckPolicyArgs : Pulumi.ResourceArgs
    {
        [Input("healthyThreshold", required: true)]
        public Input<int> HealthyThreshold { get; set; } = null!;

        [Input("intervalMillis", required: true)]
        public Input<int> IntervalMillis { get; set; } = null!;

        [Input("path")]
        public Input<string>? Path { get; set; }

        [Input("port")]
        public Input<int>? Port { get; set; }

        [Input("protocol", required: true)]
        public Input<string> Protocol { get; set; } = null!;

        [Input("timeoutMillis", required: true)]
        public Input<int> TimeoutMillis { get; set; } = null!;

        [Input("unhealthyThreshold", required: true)]
        public Input<int> UnhealthyThreshold { get; set; } = null!;

        public VirtualGatewayVirtualGatewayHealthCheckPolicyArgs()
        {
        }
    }
}
