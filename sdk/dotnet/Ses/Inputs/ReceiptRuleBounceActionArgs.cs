// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ses.Inputs
{

    public sealed class ReceiptRuleBounceActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("message", required: true)]
        public Input<string> Message { get; set; } = null!;

        [Input("sender", required: true)]
        public Input<string> Sender { get; set; } = null!;

        [Input("smtpReplyCode", required: true)]
        public Input<string> SmtpReplyCode { get; set; } = null!;

        [Input("statusCode")]
        public Input<string>? StatusCode { get; set; }

        [Input("topicArn")]
        public Input<string>? TopicArn { get; set; }

        public ReceiptRuleBounceActionArgs()
        {
        }
        public static new ReceiptRuleBounceActionArgs Empty => new ReceiptRuleBounceActionArgs();
    }
}
