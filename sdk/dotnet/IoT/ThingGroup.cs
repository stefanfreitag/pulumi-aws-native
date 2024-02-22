// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    /// <summary>
    /// Resource Type definition for AWS::IoT::ThingGroup
    /// </summary>
    [AwsNativeResourceType("aws-native:iot:ThingGroup")]
    public partial class ThingGroup : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("parentGroupName")]
        public Output<string?> ParentGroupName { get; private set; } = null!;

        [Output("queryString")]
        public Output<string?> QueryString { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("thingGroupName")]
        public Output<string?> ThingGroupName { get; private set; } = null!;

        [Output("thingGroupProperties")]
        public Output<Outputs.ThingGroupPropertiesProperties?> ThingGroupProperties { get; private set; } = null!;


        /// <summary>
        /// Create a ThingGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ThingGroup(string name, ThingGroupArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:iot:ThingGroup", name, args ?? new ThingGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ThingGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iot:ThingGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "parentGroupName",
                    "thingGroupName",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ThingGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ThingGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ThingGroup(name, id, options);
        }
    }

    public sealed class ThingGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("parentGroupName")]
        public Input<string>? ParentGroupName { get; set; }

        [Input("queryString")]
        public Input<string>? QueryString { get; set; }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("thingGroupName")]
        public Input<string>? ThingGroupName { get; set; }

        [Input("thingGroupProperties")]
        public Input<Inputs.ThingGroupPropertiesPropertiesArgs>? ThingGroupProperties { get; set; }

        public ThingGroupArgs()
        {
        }
        public static new ThingGroupArgs Empty => new ThingGroupArgs();
    }
}
