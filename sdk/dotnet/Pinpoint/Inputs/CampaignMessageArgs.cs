// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Pinpoint.Inputs
{

    public sealed class CampaignMessageArgs : global::Pulumi.ResourceArgs
    {
        [Input("action")]
        public Input<string>? Action { get; set; }

        [Input("body")]
        public Input<string>? Body { get; set; }

        [Input("imageIconUrl")]
        public Input<string>? ImageIconUrl { get; set; }

        [Input("imageSmallIconUrl")]
        public Input<string>? ImageSmallIconUrl { get; set; }

        [Input("imageUrl")]
        public Input<string>? ImageUrl { get; set; }

        [Input("jsonBody")]
        public Input<string>? JsonBody { get; set; }

        [Input("mediaUrl")]
        public Input<string>? MediaUrl { get; set; }

        [Input("rawContent")]
        public Input<string>? RawContent { get; set; }

        [Input("silentPush")]
        public Input<bool>? SilentPush { get; set; }

        [Input("timeToLive")]
        public Input<int>? TimeToLive { get; set; }

        [Input("title")]
        public Input<string>? Title { get; set; }

        [Input("url")]
        public Input<string>? Url { get; set; }

        public CampaignMessageArgs()
        {
        }
        public static new CampaignMessageArgs Empty => new CampaignMessageArgs();
    }
}
