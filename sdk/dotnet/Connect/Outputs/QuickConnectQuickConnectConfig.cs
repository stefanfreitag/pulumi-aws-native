// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect.Outputs
{

    /// <summary>
    /// Configuration settings for the quick connect.
    /// </summary>
    [OutputType]
    public sealed class QuickConnectQuickConnectConfig
    {
        public readonly Outputs.QuickConnectPhoneNumberQuickConnectConfig? PhoneConfig;
        public readonly Outputs.QuickConnectQueueQuickConnectConfig? QueueConfig;
        public readonly Pulumi.AwsNative.Connect.QuickConnectQuickConnectType QuickConnectType;
        public readonly Outputs.QuickConnectUserQuickConnectConfig? UserConfig;

        [OutputConstructor]
        private QuickConnectQuickConnectConfig(
            Outputs.QuickConnectPhoneNumberQuickConnectConfig? phoneConfig,

            Outputs.QuickConnectQueueQuickConnectConfig? queueConfig,

            Pulumi.AwsNative.Connect.QuickConnectQuickConnectType quickConnectType,

            Outputs.QuickConnectUserQuickConnectConfig? userConfig)
        {
            PhoneConfig = phoneConfig;
            QueueConfig = queueConfig;
            QuickConnectType = quickConnectType;
            UserConfig = userConfig;
        }
    }
}
