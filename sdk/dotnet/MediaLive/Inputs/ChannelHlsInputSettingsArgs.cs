// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelHlsInputSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("bandwidth")]
        public Input<int>? Bandwidth { get; set; }

        [Input("bufferSegments")]
        public Input<int>? BufferSegments { get; set; }

        [Input("retries")]
        public Input<int>? Retries { get; set; }

        [Input("retryInterval")]
        public Input<int>? RetryInterval { get; set; }

        [Input("scte35Source")]
        public Input<string>? Scte35Source { get; set; }

        public ChannelHlsInputSettingsArgs()
        {
        }
        public static new ChannelHlsInputSettingsArgs Empty => new ChannelHlsInputSettingsArgs();
    }
}
