// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Outputs
{

    [OutputType]
    public sealed class DecoderManifestCanInterface
    {
        public readonly string Name;
        public readonly string? ProtocolName;
        public readonly string? ProtocolVersion;

        [OutputConstructor]
        private DecoderManifestCanInterface(
            string name,

            string? protocolName,

            string? protocolVersion)
        {
            Name = name;
            ProtocolName = protocolName;
            ProtocolVersion = protocolVersion;
        }
    }
}
