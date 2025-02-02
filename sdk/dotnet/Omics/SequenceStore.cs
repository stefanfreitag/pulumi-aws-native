// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Omics
{
    /// <summary>
    /// Definition of AWS::Omics::SequenceStore Resource Type
    /// </summary>
    [AwsNativeResourceType("aws-native:omics:SequenceStore")]
    public partial class SequenceStore : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The store's ARN.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// When the store was created.
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        /// <summary>
        /// A description for the store.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// An S3 URI representing the bucket and folder to store failed read set uploads.
        /// </summary>
        [Output("fallbackLocation")]
        public Output<string?> FallbackLocation { get; private set; } = null!;

        /// <summary>
        /// A name for the store.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("sequenceStoreId")]
        public Output<string> SequenceStoreId { get; private set; } = null!;

        [Output("sseConfig")]
        public Output<Outputs.SequenceStoreSseConfig?> SseConfig { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableDictionary<string, string>?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a SequenceStore resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SequenceStore(string name, SequenceStoreArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:omics:SequenceStore", name, args ?? new SequenceStoreArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SequenceStore(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:omics:SequenceStore", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "description",
                    "fallbackLocation",
                    "name",
                    "sseConfig",
                    "tags.*",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SequenceStore resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SequenceStore Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SequenceStore(name, id, options);
        }
    }

    public sealed class SequenceStoreArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// A description for the store.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// An S3 URI representing the bucket and folder to store failed read set uploads.
        /// </summary>
        [Input("fallbackLocation")]
        public Input<string>? FallbackLocation { get; set; }

        /// <summary>
        /// A name for the store.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("sseConfig")]
        public Input<Inputs.SequenceStoreSseConfigArgs>? SseConfig { get; set; }

        [Input("tags")]
        private InputMap<string>? _tags;
        public InputMap<string> Tags
        {
            get => _tags ?? (_tags = new InputMap<string>());
            set => _tags = value;
        }

        public SequenceStoreArgs()
        {
        }
        public static new SequenceStoreArgs Empty => new SequenceStoreArgs();
    }
}
