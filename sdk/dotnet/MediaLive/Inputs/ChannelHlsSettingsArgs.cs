// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelHlsSettingsArgs : Pulumi.ResourceArgs
    {
        [Input("audioOnlyHlsSettings")]
        public Input<Inputs.ChannelAudioOnlyHlsSettingsArgs>? AudioOnlyHlsSettings { get; set; }

        [Input("fmp4HlsSettings")]
        public Input<Inputs.ChannelFmp4HlsSettingsArgs>? Fmp4HlsSettings { get; set; }

        [Input("frameCaptureHlsSettings")]
        public Input<Inputs.ChannelFrameCaptureHlsSettingsArgs>? FrameCaptureHlsSettings { get; set; }

        [Input("standardHlsSettings")]
        public Input<Inputs.ChannelStandardHlsSettingsArgs>? StandardHlsSettings { get; set; }

        public ChannelHlsSettingsArgs()
        {
        }
    }
}
