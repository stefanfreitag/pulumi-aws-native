// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DevOpsGuru.Inputs
{

    /// <summary>
    /// Information about notification channels you have configured with DevOps Guru.
    /// </summary>
    public sealed class NotificationChannelConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("sns")]
        public Input<Inputs.NotificationChannelSnsChannelConfigArgs>? Sns { get; set; }

        public NotificationChannelConfigArgs()
        {
        }
        public static new NotificationChannelConfigArgs Empty => new NotificationChannelConfigArgs();
    }
}
