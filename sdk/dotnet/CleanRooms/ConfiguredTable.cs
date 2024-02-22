// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CleanRooms
{
    /// <summary>
    /// Represents a table that can be associated with collaborations
    /// </summary>
    [AwsNativeResourceType("aws-native:cleanrooms:ConfiguredTable")]
    public partial class ConfiguredTable : global::Pulumi.CustomResource
    {
        [Output("allowedColumns")]
        public Output<ImmutableArray<string>> AllowedColumns { get; private set; } = null!;

        [Output("analysisMethod")]
        public Output<Pulumi.AwsNative.CleanRooms.ConfiguredTableAnalysisMethod> AnalysisMethod { get; private set; } = null!;

        [Output("analysisRules")]
        public Output<ImmutableArray<Outputs.ConfiguredTableAnalysisRule>> AnalysisRules { get; private set; } = null!;

        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("configuredTableIdentifier")]
        public Output<string> ConfiguredTableIdentifier { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("tableReference")]
        public Output<Outputs.ConfiguredTableTableReference> TableReference { get; private set; } = null!;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ConfiguredTable resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConfiguredTable(string name, ConfiguredTableArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:ConfiguredTable", name, args ?? new ConfiguredTableArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConfiguredTable(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:ConfiguredTable", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "allowedColumns[*]",
                    "analysisMethod",
                    "tableReference",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ConfiguredTable resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConfiguredTable Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConfiguredTable(name, id, options);
        }
    }

    public sealed class ConfiguredTableArgs : global::Pulumi.ResourceArgs
    {
        [Input("allowedColumns", required: true)]
        private InputList<string>? _allowedColumns;
        public InputList<string> AllowedColumns
        {
            get => _allowedColumns ?? (_allowedColumns = new InputList<string>());
            set => _allowedColumns = value;
        }

        [Input("analysisMethod", required: true)]
        public Input<Pulumi.AwsNative.CleanRooms.ConfiguredTableAnalysisMethod> AnalysisMethod { get; set; } = null!;

        [Input("analysisRules")]
        private InputList<Inputs.ConfiguredTableAnalysisRuleArgs>? _analysisRules;
        public InputList<Inputs.ConfiguredTableAnalysisRuleArgs> AnalysisRules
        {
            get => _analysisRules ?? (_analysisRules = new InputList<Inputs.ConfiguredTableAnalysisRuleArgs>());
            set => _analysisRules = value;
        }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tableReference", required: true)]
        public Input<Inputs.ConfiguredTableTableReferenceArgs> TableReference { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public ConfiguredTableArgs()
        {
        }
        public static new ConfiguredTableArgs Empty => new ConfiguredTableArgs();
    }
}
