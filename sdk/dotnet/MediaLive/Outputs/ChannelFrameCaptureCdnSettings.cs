// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Outputs
{

    [OutputType]
    public sealed class ChannelFrameCaptureCdnSettings
    {
        public readonly Outputs.ChannelFrameCaptureS3Settings? FrameCaptureS3Settings;

        [OutputConstructor]
        private ChannelFrameCaptureCdnSettings(Outputs.ChannelFrameCaptureS3Settings? frameCaptureS3Settings)
        {
            FrameCaptureS3Settings = frameCaptureS3Settings;
        }
    }
}
