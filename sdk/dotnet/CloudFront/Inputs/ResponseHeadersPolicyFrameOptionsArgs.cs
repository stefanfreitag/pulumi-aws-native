// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class ResponseHeadersPolicyFrameOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("frameOption", required: true)]
        public Input<string> FrameOption { get; set; } = null!;

        [Input("override", required: true)]
        public Input<bool> Override { get; set; } = null!;

        public ResponseHeadersPolicyFrameOptionsArgs()
        {
        }
        public static new ResponseHeadersPolicyFrameOptionsArgs Empty => new ResponseHeadersPolicyFrameOptionsArgs();
    }
}
