// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Cognito.Inputs
{

    public sealed class UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypeArgs : global::Pulumi.ResourceArgs
    {
        [Input("actions", required: true)]
        public Input<Inputs.UserPoolRiskConfigurationAttachmentAccountTakeoverActionsTypeArgs> Actions { get; set; } = null!;

        [Input("notifyConfiguration")]
        public Input<Inputs.UserPoolRiskConfigurationAttachmentNotifyConfigurationTypeArgs>? NotifyConfiguration { get; set; }

        public UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypeArgs()
        {
        }
        public static new UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypeArgs Empty => new UserPoolRiskConfigurationAttachmentAccountTakeoverRiskConfigurationTypeArgs();
    }
}
