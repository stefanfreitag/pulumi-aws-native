// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Oam
{
    /// <summary>
    /// Definition of AWS::Oam::Link Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:oam:Link")]
    public partial class Link : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("label")]
        public Output<string> Label { get; private set; } = null!;

        [Output("labelTemplate")]
        public Output<string?> LabelTemplate { get; private set; } = null!;

        [Output("resourceTypes")]
        public Output<ImmutableArray<Pulumi.AwsNative.Oam.LinkResourceType>> ResourceTypes { get; private set; } = null!;

        [Output("sinkIdentifier")]
        public Output<string> SinkIdentifier { get; private set; } = null!;

        /// <summary>
        /// Tags to apply to the link
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Oam::Link` for more information about the expected schema for this property.
        /// </summary>
        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Link resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Link(string name, LinkArgs args, CustomResourceOptions? options = null)
            : base("aws-native:oam:Link", name, args ?? new LinkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Link(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:oam:Link", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "labelTemplate",
                    "sinkIdentifier",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Link resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Link Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Link(name, id, options);
        }
    }

    public sealed class LinkArgs : global::Pulumi.ResourceArgs
    {
        [Input("labelTemplate")]
        public Input<string>? LabelTemplate { get; set; }

        [Input("resourceTypes", required: true)]
        private InputList<Pulumi.AwsNative.Oam.LinkResourceType>? _resourceTypes;
        public InputList<Pulumi.AwsNative.Oam.LinkResourceType> ResourceTypes
        {
            get => _resourceTypes ?? (_resourceTypes = new InputList<Pulumi.AwsNative.Oam.LinkResourceType>());
            set => _resourceTypes = value;
        }

        [Input("sinkIdentifier", required: true)]
        public Input<string> SinkIdentifier { get; set; } = null!;

        /// <summary>
        /// Tags to apply to the link
        /// 
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::Oam::Link` for more information about the expected schema for this property.
        /// </summary>
        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public LinkArgs()
        {
        }
        public static new LinkArgs Empty => new LinkArgs();
    }
}
