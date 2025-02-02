// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTFleetWise.Inputs
{

    public sealed class DecoderManifestObdInterfaceArgs : global::Pulumi.ResourceArgs
    {
        [Input("dtcRequestIntervalSeconds")]
        public Input<int>? DtcRequestIntervalSeconds { get; set; }

        [Input("hasTransmissionEcu")]
        public Input<bool>? HasTransmissionEcu { get; set; }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("obdStandard")]
        public Input<string>? ObdStandard { get; set; }

        [Input("pidRequestIntervalSeconds")]
        public Input<int>? PidRequestIntervalSeconds { get; set; }

        [Input("requestMessageId", required: true)]
        public Input<int> RequestMessageId { get; set; } = null!;

        [Input("useExtendedIds")]
        public Input<bool>? UseExtendedIds { get; set; }

        public DecoderManifestObdInterfaceArgs()
        {
        }
        public static new DecoderManifestObdInterfaceArgs Empty => new DecoderManifestObdInterfaceArgs();
    }
}
