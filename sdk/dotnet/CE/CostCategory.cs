// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CE
{
    /// <summary>
    /// Cost Category enables you to map your cost and usage into meaningful categories. You can use Cost Category to organize your costs using a rule-based engine.
    /// </summary>
    [AwsNativeResourceType("aws-native:ce:CostCategory")]
    public partial class CostCategory : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Cost category ARN
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The default value for the cost category
        /// </summary>
        [Output("defaultValue")]
        public Output<string?> DefaultValue { get; private set; } = null!;

        [Output("effectiveStart")]
        public Output<string> EffectiveStart { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("ruleVersion")]
        public Output<Pulumi.AwsNative.CE.CostCategoryRuleVersion> RuleVersion { get; private set; } = null!;

        /// <summary>
        /// JSON array format of Expression in Billing and Cost Management API
        /// </summary>
        [Output("rules")]
        public Output<string> Rules { get; private set; } = null!;

        /// <summary>
        /// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        /// </summary>
        [Output("splitChargeRules")]
        public Output<string?> SplitChargeRules { get; private set; } = null!;


        /// <summary>
        /// Create a CostCategory resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CostCategory(string name, CostCategoryArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ce:CostCategory", name, args ?? new CostCategoryArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CostCategory(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ce:CostCategory", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CostCategory resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CostCategory Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CostCategory(name, id, options);
        }
    }

    public sealed class CostCategoryArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The default value for the cost category
        /// </summary>
        [Input("defaultValue")]
        public Input<string>? DefaultValue { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("ruleVersion", required: true)]
        public Input<Pulumi.AwsNative.CE.CostCategoryRuleVersion> RuleVersion { get; set; } = null!;

        /// <summary>
        /// JSON array format of Expression in Billing and Cost Management API
        /// </summary>
        [Input("rules", required: true)]
        public Input<string> Rules { get; set; } = null!;

        /// <summary>
        /// Json array format of CostCategorySplitChargeRule in Billing and Cost Management API
        /// </summary>
        [Input("splitChargeRules")]
        public Input<string>? SplitChargeRules { get; set; }

        public CostCategoryArgs()
        {
        }
        public static new CostCategoryArgs Empty => new CostCategoryArgs();
    }
}
