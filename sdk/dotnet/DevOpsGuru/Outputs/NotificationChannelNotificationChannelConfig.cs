// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DevOpsGuru.Outputs
{

    /// <summary>
    /// Information about notification channels you have configured with DevOps Guru.
    /// </summary>
    [OutputType]
    public sealed class NotificationChannelNotificationChannelConfig
    {
        public readonly Outputs.NotificationChannelSnsChannelConfig? Sns;

        [OutputConstructor]
        private NotificationChannelNotificationChannelConfig(Outputs.NotificationChannelSnsChannelConfig? sns)
        {
            Sns = sns;
        }
    }
}
