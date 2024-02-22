// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs
{
    /// <summary>
    /// Resource Type definition for AWS::ECS::CapacityProvider.
    /// </summary>
    [AwsNativeResourceType("aws-native:ecs:CapacityProvider")]
    public partial class CapacityProvider : global::Pulumi.CustomResource
    {
        [Output("autoScalingGroupProvider")]
        public Output<Outputs.CapacityProviderAutoScalingGroupProvider> AutoScalingGroupProvider { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a CapacityProvider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CapacityProvider(string name, CapacityProviderArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ecs:CapacityProvider", name, args ?? new CapacityProviderArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CapacityProvider(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ecs:CapacityProvider", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "autoScalingGroupProvider.autoScalingGroupArn",
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing CapacityProvider resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CapacityProvider Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CapacityProvider(name, id, options);
        }
    }

    public sealed class CapacityProviderArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoScalingGroupProvider", required: true)]
        public Input<Inputs.CapacityProviderAutoScalingGroupProviderArgs> AutoScalingGroupProvider { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public CapacityProviderArgs()
        {
        }
        public static new CapacityProviderArgs Empty => new CapacityProviderArgs();
    }
}
