// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.BillingConductor
{
    public static class GetPricingPlan
    {
        /// <summary>
        /// Pricing Plan enables you to customize your billing details consistent with the usage that accrues in each of your billing groups.
        /// </summary>
        public static Task<GetPricingPlanResult> InvokeAsync(GetPricingPlanArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPricingPlanResult>("aws-native:billingconductor:getPricingPlan", args ?? new GetPricingPlanArgs(), options.WithDefaults());

        /// <summary>
        /// Pricing Plan enables you to customize your billing details consistent with the usage that accrues in each of your billing groups.
        /// </summary>
        public static Output<GetPricingPlanResult> Invoke(GetPricingPlanInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPricingPlanResult>("aws-native:billingconductor:getPricingPlan", args ?? new GetPricingPlanInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPricingPlanArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Pricing Plan ARN
        /// </summary>
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetPricingPlanArgs()
        {
        }
        public static new GetPricingPlanArgs Empty => new GetPricingPlanArgs();
    }

    public sealed class GetPricingPlanInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Pricing Plan ARN
        /// </summary>
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetPricingPlanInvokeArgs()
        {
        }
        public static new GetPricingPlanInvokeArgs Empty => new GetPricingPlanInvokeArgs();
    }


    [OutputType]
    public sealed class GetPricingPlanResult
    {
        /// <summary>
        /// Pricing Plan ARN
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// Creation timestamp in UNIX epoch time format
        /// </summary>
        public readonly int? CreationTime;
        public readonly string? Description;
        /// <summary>
        /// Latest modified timestamp in UNIX epoch time format
        /// </summary>
        public readonly int? LastModifiedTime;
        public readonly string? Name;
        public readonly ImmutableArray<string> PricingRuleArns;
        /// <summary>
        /// Number of associated pricing rules
        /// </summary>
        public readonly int? Size;
        public readonly ImmutableArray<Outputs.PricingPlanTag> Tags;

        [OutputConstructor]
        private GetPricingPlanResult(
            string? arn,

            int? creationTime,

            string? description,

            int? lastModifiedTime,

            string? name,

            ImmutableArray<string> pricingRuleArns,

            int? size,

            ImmutableArray<Outputs.PricingPlanTag> tags)
        {
            Arn = arn;
            CreationTime = creationTime;
            Description = description;
            LastModifiedTime = lastModifiedTime;
            Name = name;
            PricingRuleArns = pricingRuleArns;
            Size = size;
            Tags = tags;
        }
    }
}
