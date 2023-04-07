// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.XRay
{
    /// <summary>
    /// This schema provides construct and validation rules for AWS-XRay Group resource parameters.
    /// </summary>
    [AwsNativeResourceType("aws-native:xray:Group")]
    public partial class Group : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The filter expression defining criteria by which to group traces.
        /// </summary>
        [Output("filterExpression")]
        public Output<string?> FilterExpression { get; private set; } = null!;

        /// <summary>
        /// The ARN of the group that was generated on creation.
        /// </summary>
        [Output("groupARN")]
        public Output<string> GroupARN { get; private set; } = null!;

        /// <summary>
        /// The case-sensitive name of the new group. Names must be unique.
        /// </summary>
        [Output("groupName")]
        public Output<string?> GroupName { get; private set; } = null!;

        [Output("insightsConfiguration")]
        public Output<Outputs.GroupInsightsConfiguration?> InsightsConfiguration { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.TagsItemProperties>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Group resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Group(string name, GroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:xray:Group", name, args ?? new GroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Group(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:xray:Group", name, null, MakeResourceOptions(options, id))
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
        /// <summary>
        /// The filter expression defining criteria by which to group traces.
        /// </summary>
        [Input("filterExpression")]
        public Input<string>? FilterExpression { get; set; }

        /// <summary>
        /// The case-sensitive name of the new group. Names must be unique.
        /// </summary>
        [Input("groupName")]
        public Input<string>? GroupName { get; set; }

        [Input("insightsConfiguration")]
        public Input<Inputs.GroupInsightsConfigurationArgs>? InsightsConfiguration { get; set; }

        [Input("tags")]
        private InputList<Inputs.TagsItemPropertiesArgs>? _tags;
        public InputList<Inputs.TagsItemPropertiesArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.TagsItemPropertiesArgs>());
            set => _tags = value;
        }

        public GroupArgs()
        {
        }
        public static new GroupArgs Empty => new GroupArgs();
    }
}
