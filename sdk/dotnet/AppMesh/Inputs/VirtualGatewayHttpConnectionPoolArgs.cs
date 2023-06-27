// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppMesh.Inputs
{

    public sealed class VirtualGatewayHttpConnectionPoolArgs : global::Pulumi.ResourceArgs
    {
        [Input("maxConnections", required: true)]
        public Input<int> MaxConnections { get; set; } = null!;

        [Input("maxPendingRequests")]
        public Input<int>? MaxPendingRequests { get; set; }

        public VirtualGatewayHttpConnectionPoolArgs()
        {
        }
        public static new VirtualGatewayHttpConnectionPoolArgs Empty => new VirtualGatewayHttpConnectionPoolArgs();
    }
}
