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
    /// Contains information about which channels are supported, and how many contacts an agent can have on a channel simultaneously.
    /// </summary>
    [OutputType]
    public sealed class RoutingProfileMediaConcurrency
    {
        public readonly Pulumi.AwsNative.Connect.RoutingProfileChannel Channel;
        public readonly int Concurrency;
        public readonly Outputs.RoutingProfileCrossChannelBehavior? CrossChannelBehavior;

        [OutputConstructor]
        private RoutingProfileMediaConcurrency(
            Pulumi.AwsNative.Connect.RoutingProfileChannel channel,

            int concurrency,

            Outputs.RoutingProfileCrossChannelBehavior? crossChannelBehavior)
        {
            Channel = channel;
            Concurrency = concurrency;
            CrossChannelBehavior = crossChannelBehavior;
        }
    }
}
