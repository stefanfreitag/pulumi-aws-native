// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolEmailConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("configurationSet")]
        public Input<string>? ConfigurationSet { get; set; }

        [Input("emailSendingAccount")]
        public Input<string>? EmailSendingAccount { get; set; }

        [Input("from")]
        public Input<string>? From { get; set; }

        [Input("replyToEmailAddress")]
        public Input<string>? ReplyToEmailAddress { get; set; }

        [Input("sourceArn")]
        public Input<string>? SourceArn { get; set; }

        public UserPoolEmailConfigurationArgs()
        {
        }
        public static new UserPoolEmailConfigurationArgs Empty => new UserPoolEmailConfigurationArgs();
    }
}
