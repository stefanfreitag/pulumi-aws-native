// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Glue
{
    /// <summary>
    /// Resource Type definition for AWS::Glue::DataQualityRuleset
    /// </summary>
    [Obsolete(@"DataQualityRuleset is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:glue:DataQualityRuleset")]
    public partial class DataQualityRuleset : global::Pulumi.CustomResource
    {
        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("ruleset")]
        public Output<string?> Ruleset { get; private set; } = null!;

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;

        [Output("targetTable")]
        public Output<Outputs.DataQualityRulesetDataQualityTargetTable?> TargetTable { get; private set; } = null!;


        /// <summary>
        /// Create a DataQualityRuleset resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DataQualityRuleset(string name, DataQualityRulesetArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:glue:DataQualityRuleset", name, args ?? new DataQualityRulesetArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DataQualityRuleset(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:glue:DataQualityRuleset", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DataQualityRuleset resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DataQualityRuleset Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DataQualityRuleset(name, id, options);
        }
    }

    public sealed class DataQualityRulesetArgs : global::Pulumi.ResourceArgs
    {
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("ruleset")]
        public Input<string>? Ruleset { get; set; }

        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Glue::DataQualityRuleset` for more information about the expected schema for this property.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        [Input("targetTable")]
        public Input<Inputs.DataQualityRulesetDataQualityTargetTableArgs>? TargetTable { get; set; }

        public DataQualityRulesetArgs()
        {
        }
        public static new DataQualityRulesetArgs Empty => new DataQualityRulesetArgs();
    }
}
