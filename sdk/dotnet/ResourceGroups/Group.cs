// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ResourceGroups
{
    /// <summary>
    /// Schema for ResourceGroups::Group
    /// </summary>
    [AwsNativeResourceType("aws-native:resourcegroups:Group")]
    public partial class Group : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Resource Group ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("configuration")]
        public Output<ImmutableArray<Outputs.GroupConfigurationItem>> Configuration { get; private set; } = null!;

        /// <summary>
        /// The description of the resource group
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The name of the resource group
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("resourceQuery")]
        public Output<Outputs.GroupResourceQuery?> ResourceQuery { get; private set; } = null!;

        [Output("resources")]
        public Output<ImmutableArray<string>> Resources { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Group resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Group(string name, GroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:resourcegroups:Group", name, args ?? new GroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Group(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:resourcegroups:Group", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Group resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Group Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Group(name, id, options);
        }
    }

    public sealed class GroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("configuration")]
        private InputList<Inputs.GroupConfigurationItemArgs>? _configuration;
        public InputList<Inputs.GroupConfigurationItemArgs> Configuration
        {
            get => _configuration ?? (_configuration = new InputList<Inputs.GroupConfigurationItemArgs>());
            set => _configuration = value;
        }

        /// <summary>
        /// The description of the resource group
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The name of the resource group
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("resourceQuery")]
        public Input<Inputs.GroupResourceQueryArgs>? ResourceQuery { get; set; }

        [Input("resources")]
        private InputList<string>? _resources;
        public InputList<string> Resources
        {
            get => _resources ?? (_resources = new InputList<string>());
            set => _resources = value;
        }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public GroupArgs()
        {
        }
        public static new GroupArgs Empty => new GroupArgs();
    }
}
