// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    public static class GetDistribution
    {
        /// <summary>
        /// Resource Type definition for AWS::Lightsail::Distribution
        /// </summary>
        public static Task<GetDistributionResult> InvokeAsync(GetDistributionArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetDistributionResult>("aws-native:lightsail:getDistribution", args ?? new GetDistributionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Lightsail::Distribution
        /// </summary>
        public static Output<GetDistributionResult> Invoke(GetDistributionInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetDistributionResult>("aws-native:lightsail:getDistribution", args ?? new GetDistributionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDistributionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name for the distribution.
        /// </summary>
        [Input("distributionName", required: true)]
        public string DistributionName { get; set; } = null!;

        public GetDistributionArgs()
        {
        }
        public static new GetDistributionArgs Empty => new GetDistributionArgs();
    }

    public sealed class GetDistributionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name for the distribution.
        /// </summary>
        [Input("distributionName", required: true)]
        public Input<string> DistributionName { get; set; } = null!;

        public GetDistributionInvokeArgs()
        {
        }
        public static new GetDistributionInvokeArgs Empty => new GetDistributionInvokeArgs();
    }


    [OutputType]
    public sealed class GetDistributionResult
    {
        /// <summary>
        /// Indicates whether the bundle that is currently applied to your distribution, specified using the distributionName parameter, can be changed to another bundle.
        /// </summary>
        public readonly bool? AbleToUpdateBundle;
        /// <summary>
        /// The bundle ID to use for the distribution.
        /// </summary>
        public readonly string? BundleId;
        /// <summary>
        /// An object that describes the cache behavior settings for the distribution.
        /// </summary>
        public readonly Outputs.DistributionCacheSettings? CacheBehaviorSettings;
        /// <summary>
        /// An array of objects that describe the per-path cache behavior for the distribution.
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionCacheBehaviorPerPath> CacheBehaviors;
        /// <summary>
        /// The certificate attached to the Distribution.
        /// </summary>
        public readonly string? CertificateName;
        /// <summary>
        /// An object that describes the default cache behavior for the distribution.
        /// </summary>
        public readonly Outputs.DistributionCacheBehavior? DefaultCacheBehavior;
        public readonly string? DistributionArn;
        /// <summary>
        /// Indicates whether the distribution is enabled.
        /// </summary>
        public readonly bool? IsEnabled;
        /// <summary>
        /// An object that describes the origin resource for the distribution, such as a Lightsail instance or load balancer.
        /// </summary>
        public readonly Outputs.DistributionInputOrigin? Origin;
        /// <summary>
        /// The status of the distribution.
        /// </summary>
        public readonly string? Status;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.DistributionTag> Tags;

        [OutputConstructor]
        private GetDistributionResult(
            bool? ableToUpdateBundle,

            string? bundleId,

            Outputs.DistributionCacheSettings? cacheBehaviorSettings,

            ImmutableArray<Outputs.DistributionCacheBehaviorPerPath> cacheBehaviors,

            string? certificateName,

            Outputs.DistributionCacheBehavior? defaultCacheBehavior,

            string? distributionArn,

            bool? isEnabled,

            Outputs.DistributionInputOrigin? origin,

            string? status,

            ImmutableArray<Outputs.DistributionTag> tags)
        {
            AbleToUpdateBundle = ableToUpdateBundle;
            BundleId = bundleId;
            CacheBehaviorSettings = cacheBehaviorSettings;
            CacheBehaviors = cacheBehaviors;
            CertificateName = certificateName;
            DefaultCacheBehavior = defaultCacheBehavior;
            DistributionArn = distributionArn;
            IsEnabled = isEnabled;
            Origin = origin;
            Status = status;
            Tags = tags;
        }
    }
}
