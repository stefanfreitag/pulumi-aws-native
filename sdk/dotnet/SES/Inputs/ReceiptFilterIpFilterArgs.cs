// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SES.Inputs
{

    public sealed class ReceiptFilterIpFilterArgs : global::Pulumi.ResourceArgs
    {
        [Input("cidr", required: true)]
        public Input<string> Cidr { get; set; } = null!;

        [Input("policy", required: true)]
        public Input<string> Policy { get; set; } = null!;

        public ReceiptFilterIpFilterArgs()
        {
        }
        public static new ReceiptFilterIpFilterArgs Empty => new ReceiptFilterIpFilterArgs();
    }
}
