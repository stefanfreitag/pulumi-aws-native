// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GlobalAccelerator.Inputs
{

    /// <summary>
    /// listener to endpoint port mapping.
    /// </summary>
    public sealed class EndpointGroupPortOverrideArgs : global::Pulumi.ResourceArgs
    {
        [Input("endpointPort", required: true)]
        public Input<int> EndpointPort { get; set; } = null!;

        [Input("listenerPort", required: true)]
        public Input<int> ListenerPort { get; set; } = null!;

        public EndpointGroupPortOverrideArgs()
        {
        }
        public static new EndpointGroupPortOverrideArgs Empty => new EndpointGroupPortOverrideArgs();
    }
}
