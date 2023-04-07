// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ImageBuilder
{
    /// <summary>
    /// Resource schema for AWS::ImageBuilder::DistributionConfiguration
    /// </summary>
    [AwsNativeResourceType("aws-native:imagebuilder:DistributionConfiguration")]
    public partial class DistributionConfiguration : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the distribution configuration.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The description of the distribution configuration.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The distributions of the distribution configuration.
        /// </summary>
        [Output("distributions")]
        public Output<ImmutableArray<Outputs.DistributionConfigurationDistribution>> Distributions { get; private set; } = null!;

        /// <summary>
        /// The name of the distribution configuration.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The tags associated with the component.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a DistributionConfiguration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public DistributionConfiguration(string name, DistributionConfigurationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:imagebuilder:DistributionConfiguration", name, args ?? new DistributionConfigurationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private DistributionConfiguration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:imagebuilder:DistributionConfiguration", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing DistributionConfiguration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static DistributionConfiguration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new DistributionConfiguration(name, id, options);
        }
    }

    public sealed class DistributionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the distribution configuration.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("distributions", required: true)]
        private InputList<Inputs.DistributionConfigurationDistributionArgs>? _distributions;

        /// <summary>
        /// The distributions of the distribution configuration.
        /// </summary>
        public InputList<Inputs.DistributionConfigurationDistributionArgs> Distributions
        {
            get => _distributions ?? (_distributions = new InputList<Inputs.DistributionConfigurationDistributionArgs>());
            set => _distributions = value;
        }

        /// <summary>
        /// The name of the distribution configuration.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The tags associated with the component.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public DistributionConfigurationArgs()
        {
        }
        public static new DistributionConfigurationArgs Empty => new DistributionConfigurationArgs();
    }
}
