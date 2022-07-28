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
    /// Configuration settings for the quick connect.
    /// </summary>
    public sealed class QuickConnectConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("phoneConfig")]
        public Input<Inputs.QuickConnectPhoneNumberQuickConnectConfigArgs>? PhoneConfig { get; set; }

        [Input("queueConfig")]
        public Input<Inputs.QuickConnectQueueQuickConnectConfigArgs>? QueueConfig { get; set; }

        [Input("quickConnectType", required: true)]
        public Input<Pulumi.AwsNative.Connect.QuickConnectType> QuickConnectType { get; set; } = null!;

        [Input("userConfig")]
        public Input<Inputs.QuickConnectUserQuickConnectConfigArgs>? UserConfig { get; set; }

        public QuickConnectConfigArgs()
        {
        }
        public static new QuickConnectConfigArgs Empty => new QuickConnectConfigArgs();
    }
}
