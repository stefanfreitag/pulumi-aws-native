// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.BillingConductor
{
    /// <summary>
    /// A markup/discount that is defined for a specific set of services that can later be associated with a pricing plan.
    /// </summary>
    [Obsolete(@"PricingRule is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:billingconductor:PricingRule")]
    public partial class PricingRule : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Pricing rule ARN
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The number of pricing plans associated with pricing rule
        /// </summary>
        [Output("associatedPricingPlanCount")]
        public Output<int> AssociatedPricingPlanCount { get; private set; } = null!;

        /// <summary>
        /// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
        /// </summary>
        [Output("billingEntity")]
        public Output<Pulumi.AwsNative.BillingConductor.PricingRuleBillingEntity?> BillingEntity { get; private set; } = null!;

        /// <summary>
        /// Creation timestamp in UNIX epoch time format
        /// </summary>
        [Output("creationTime")]
        public Output<int> CreationTime { get; private set; } = null!;

        /// <summary>
        /// Pricing rule description
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Latest modified timestamp in UNIX epoch time format
        /// </summary>
        [Output("lastModifiedTime")]
        public Output<int> LastModifiedTime { get; private set; } = null!;

        /// <summary>
        /// Pricing rule modifier percentage
        /// </summary>
        [Output("modifierPercentage")]
        public Output<double?> ModifierPercentage { get; private set; } = null!;

        /// <summary>
        /// Pricing rule name
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The Operation which a SKU pricing rule is modifying
        /// </summary>
        [Output("operation")]
        public Output<string?> Operation { get; private set; } = null!;

        /// <summary>
        /// A term used to categorize the granularity of a Pricing Rule.
        /// </summary>
        [Output("scope")]
        public Output<Pulumi.AwsNative.BillingConductor.PricingRuleScope> Scope { get; private set; } = null!;

        /// <summary>
        /// The service which a pricing rule is applied on
        /// </summary>
        [Output("service")]
        public Output<string?> Service { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The set of tiering configurations for the pricing rule.
        /// </summary>
        [Output("tiering")]
        public Output<Outputs.TieringProperties?> Tiering { get; private set; } = null!;

        /// <summary>
        /// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
        /// </summary>
        [Output("type")]
        public Output<Pulumi.AwsNative.BillingConductor.PricingRuleType> Type { get; private set; } = null!;

        /// <summary>
        /// The UsageType which a SKU pricing rule is modifying
        /// </summary>
        [Output("usageType")]
        public Output<string?> UsageType { get; private set; } = null!;


        /// <summary>
        /// Create a PricingRule resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PricingRule(string name, PricingRuleArgs args, CustomResourceOptions? options = null)
            : base("aws-native:billingconductor:PricingRule", name, args ?? new PricingRuleArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PricingRule(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:billingconductor:PricingRule", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "billingEntity",
                    "operation",
                    "scope",
                    "service",
                    "usageType",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PricingRule resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PricingRule Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PricingRule(name, id, options);
        }
    }

    public sealed class PricingRuleArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The seller of services provided by AWS, their affiliates, or third-party providers selling services via AWS Marketplaces. Supported billing entities are AWS, AWS Marketplace, and AISPL.
        /// </summary>
        [Input("billingEntity")]
        public Input<Pulumi.AwsNative.BillingConductor.PricingRuleBillingEntity>? BillingEntity { get; set; }

        /// <summary>
        /// Pricing rule description
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Pricing rule modifier percentage
        /// </summary>
        [Input("modifierPercentage")]
        public Input<double>? ModifierPercentage { get; set; }

        /// <summary>
        /// Pricing rule name
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The Operation which a SKU pricing rule is modifying
        /// </summary>
        [Input("operation")]
        public Input<string>? Operation { get; set; }

        /// <summary>
        /// A term used to categorize the granularity of a Pricing Rule.
        /// </summary>
        [Input("scope", required: true)]
        public Input<Pulumi.AwsNative.BillingConductor.PricingRuleScope> Scope { get; set; } = null!;

        /// <summary>
        /// The service which a pricing rule is applied on
        /// </summary>
        [Input("service")]
        public Input<string>? Service { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The set of tiering configurations for the pricing rule.
        /// </summary>
        [Input("tiering")]
        public Input<Inputs.TieringPropertiesArgs>? Tiering { get; set; }

        /// <summary>
        /// One of MARKUP, DISCOUNT or TIERING that describes the behaviour of the pricing rule.
        /// </summary>
        [Input("type", required: true)]
        public Input<Pulumi.AwsNative.BillingConductor.PricingRuleType> Type { get; set; } = null!;

        /// <summary>
        /// The UsageType which a SKU pricing rule is modifying
        /// </summary>
        [Input("usageType")]
        public Input<string>? UsageType { get; set; }

        public PricingRuleArgs()
        {
        }
        public static new PricingRuleArgs Empty => new PricingRuleArgs();
    }
}
