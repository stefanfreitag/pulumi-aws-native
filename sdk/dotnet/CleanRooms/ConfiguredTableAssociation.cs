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
    /// Represents a table that can be queried within a collaboration
    /// </summary>
    [AwsNativeResourceType("aws-native:cleanrooms:ConfiguredTableAssociation")]
    public partial class ConfiguredTableAssociation : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("configuredTableAssociationIdentifier")]
        public Output<string> ConfiguredTableAssociationIdentifier { get; private set; } = null!;

        [Output("configuredTableIdentifier")]
        public Output<string> ConfiguredTableIdentifier { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("membershipIdentifier")]
        public Output<string> MembershipIdentifier { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ConfiguredTableAssociationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ConfiguredTableAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConfiguredTableAssociation(string name, ConfiguredTableAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:ConfiguredTableAssociation", name, args ?? new ConfiguredTableAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConfiguredTableAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:cleanrooms:ConfiguredTableAssociation", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ConfiguredTableAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConfiguredTableAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConfiguredTableAssociation(name, id, options);
        }
    }

    public sealed class ConfiguredTableAssociationArgs : global::Pulumi.ResourceArgs
    {
        [Input("configuredTableIdentifier", required: true)]
        public Input<string> ConfiguredTableIdentifier { get; set; } = null!;

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("membershipIdentifier", required: true)]
        public Input<string> MembershipIdentifier { get; set; } = null!;

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ConfiguredTableAssociationTagArgs>? _tags;

        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this cleanrooms collaboration.
        /// </summary>
        public InputList<Inputs.ConfiguredTableAssociationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ConfiguredTableAssociationTagArgs>());
            set => _tags = value;
        }

        public ConfiguredTableAssociationArgs()
        {
        }
        public static new ConfiguredTableAssociationArgs Empty => new ConfiguredTableAssociationArgs();
    }
}
