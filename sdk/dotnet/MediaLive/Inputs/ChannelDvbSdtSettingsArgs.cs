// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaLive.Inputs
{

    public sealed class ChannelDvbSdtSettingsArgs : global::Pulumi.ResourceArgs
    {
        [Input("outputSdt")]
        public Input<string>? OutputSdt { get; set; }

        [Input("repInterval")]
        public Input<int>? RepInterval { get; set; }

        [Input("serviceName")]
        public Input<string>? ServiceName { get; set; }

        [Input("serviceProviderName")]
        public Input<string>? ServiceProviderName { get; set; }

        public ChannelDvbSdtSettingsArgs()
        {
        }
        public static new ChannelDvbSdtSettingsArgs Empty => new ChannelDvbSdtSettingsArgs();
    }
}
