// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ConnectCampaigns.Outputs
{

    /// <summary>
    /// Predictive Dialer config
    /// </summary>
    [OutputType]
    public sealed class CampaignPredictiveDialerConfig
    {
        /// <summary>
        /// The bandwidth allocation of a queue resource.
        /// </summary>
        public readonly double BandwidthAllocation;
        /// <summary>
        /// Allocates dialing capacity for this campaign between multiple active campaigns.
        /// </summary>
        public readonly double? DialingCapacity;

        [OutputConstructor]
        private CampaignPredictiveDialerConfig(
            double bandwidthAllocation,

            double? dialingCapacity)
        {
            BandwidthAllocation = bandwidthAllocation;
            DialingCapacity = dialingCapacity;
        }
    }
}
