// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudFront.Inputs
{

    public sealed class MonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("realtimeMetricsSubscriptionStatus", required: true)]
        public Input<Pulumi.AwsNative.CloudFront.MonitoringSubscriptionRealtimeMetricsSubscriptionConfigRealtimeMetricsSubscriptionStatus> RealtimeMetricsSubscriptionStatus { get; set; } = null!;

        public MonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs()
        {
        }
        public static new MonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs Empty => new MonitoringSubscriptionRealtimeMetricsSubscriptionConfigArgs();
    }
}
