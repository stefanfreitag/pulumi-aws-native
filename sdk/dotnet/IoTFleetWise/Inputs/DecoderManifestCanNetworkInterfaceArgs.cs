// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Inputs
{

    public sealed class DecoderManifestCanNetworkInterfaceArgs : global::Pulumi.ResourceArgs
    {
        [Input("canInterface", required: true)]
        public Input<Inputs.DecoderManifestCanInterfaceArgs> CanInterface { get; set; } = null!;

        [Input("interfaceId", required: true)]
        public Input<string> InterfaceId { get; set; } = null!;

        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.IoTFleetWise.DecoderManifestCanNetworkInterfaceType> Type { get; set; } = null!;

        public DecoderManifestCanNetworkInterfaceArgs()
        {
        }
        public static new DecoderManifestCanNetworkInterfaceArgs Empty => new DecoderManifestCanNetworkInterfaceArgs();
    }
}
