// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class ResponseHeadersPolicyCorsConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("accessControlAllowCredentials", required: true)]
        public Input<bool> AccessControlAllowCredentials { get; set; } = null!;

        [Input("accessControlAllowHeaders", required: true)]
        public Input<Inputs.ResponseHeadersPolicyAccessControlAllowHeadersArgs> AccessControlAllowHeaders { get; set; } = null!;

        [Input("accessControlAllowMethods", required: true)]
        public Input<Inputs.ResponseHeadersPolicyAccessControlAllowMethodsArgs> AccessControlAllowMethods { get; set; } = null!;

        [Input("accessControlAllowOrigins", required: true)]
        public Input<Inputs.ResponseHeadersPolicyAccessControlAllowOriginsArgs> AccessControlAllowOrigins { get; set; } = null!;

        [Input("accessControlExposeHeaders")]
        public Input<Inputs.ResponseHeadersPolicyAccessControlExposeHeadersArgs>? AccessControlExposeHeaders { get; set; }

        [Input("accessControlMaxAgeSec")]
        public Input<int>? AccessControlMaxAgeSec { get; set; }

        [Input("originOverride", required: true)]
        public Input<bool> OriginOverride { get; set; } = null!;

        public ResponseHeadersPolicyCorsConfigArgs()
        {
        }
        public static new ResponseHeadersPolicyCorsConfigArgs Empty => new ResponseHeadersPolicyCorsConfigArgs();
    }
}
