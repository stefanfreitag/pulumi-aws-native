// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.RDS
{
    /// <summary>
    /// Resource Type definition for AWS::RDS::OptionGroup
    /// </summary>
    [Obsolete(@"OptionGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:rds:OptionGroup")]
    public partial class OptionGroup : global::Pulumi.CustomResource
    {
        [Output("engineName")]
        public Output<string> EngineName { get; private set; } = null!;

        [Output("majorEngineVersion")]
        public Output<string> MajorEngineVersion { get; private set; } = null!;

        [Output("optionConfigurations")]
        public Output<ImmutableArray<Outputs.OptionGroupOptionConfiguration>> OptionConfigurations { get; private set; } = null!;

        [Output("optionGroupDescription")]
        public Output<string> OptionGroupDescription { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.OptionGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a OptionGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public OptionGroup(string name, OptionGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:rds:OptionGroup", name, args ?? new OptionGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private OptionGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:OptionGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing OptionGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static OptionGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new OptionGroup(name, id, options);
        }
    }

    public sealed class OptionGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("engineName", required: true)]
        public Input<string> EngineName { get; set; } = null!;

        [Input("majorEngineVersion", required: true)]
        public Input<string> MajorEngineVersion { get; set; } = null!;

        [Input("optionConfigurations", required: true)]
        private InputList<Inputs.OptionGroupOptionConfigurationArgs>? _optionConfigurations;
        public InputList<Inputs.OptionGroupOptionConfigurationArgs> OptionConfigurations
        {
            get => _optionConfigurations ?? (_optionConfigurations = new InputList<Inputs.OptionGroupOptionConfigurationArgs>());
            set => _optionConfigurations = value;
        }

        [Input("optionGroupDescription", required: true)]
        public Input<string> OptionGroupDescription { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.OptionGroupTagArgs>? _tags;
        public InputList<Inputs.OptionGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.OptionGroupTagArgs>());
            set => _tags = value;
        }

        public OptionGroupArgs()
        {
        }
        public static new OptionGroupArgs Empty => new OptionGroupArgs();
    }
}
