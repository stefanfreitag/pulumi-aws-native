// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Inputs
{

    /// <summary>
    /// The user configuration. This is required only if QuickConnectType is USER.
    /// </summary>
    public sealed class QuickConnectUserQuickConnectConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("contactFlowArn", required: true)]
        public Input<string> ContactFlowArn { get; set; } = null!;

        [Input("userArn", required: true)]
        public Input<string> UserArn { get; set; } = null!;

        public QuickConnectUserQuickConnectConfigArgs()
        {
        }
        public static new QuickConnectUserQuickConnectConfigArgs Empty => new QuickConnectUserQuickConnectConfigArgs();
    }
}
