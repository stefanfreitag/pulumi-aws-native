// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio
{
    /// <summary>
    /// Resource schema for AWS::NimbleStudio::StreamingImage.
    /// </summary>
    [AwsNativeResourceType("aws-native:nimblestudio:StreamingImage")]
    public partial class StreamingImage : Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("ec2ImageId")]
        public Output<string> Ec2ImageId { get; private set; } = null!;

        [Output("encryptionConfiguration")]
        public Output<Outputs.StreamingImageStreamingImageEncryptionConfiguration> EncryptionConfiguration { get; private set; } = null!;

        [Output("eulaIds")]
        public Output<ImmutableArray<string>> EulaIds { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("owner")]
        public Output<string> Owner { get; private set; } = null!;

        [Output("platform")]
        public Output<string> Platform { get; private set; } = null!;

        [Output("streamingImageId")]
        public Output<string> StreamingImageId { get; private set; } = null!;

        [Output("studioId")]
        public Output<string> StudioId { get; private set; } = null!;

        [Output("tags")]
        public Output<object?> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a StreamingImage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public StreamingImage(string name, StreamingImageArgs args, CustomResourceOptions? options = null)
            : base("aws-native:nimblestudio:StreamingImage", name, args ?? new StreamingImageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private StreamingImage(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:nimblestudio:StreamingImage", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing StreamingImage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static StreamingImage Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new StreamingImage(name, id, options);
        }
    }

    public sealed class StreamingImageArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("ec2ImageId", required: true)]
        public Input<string> Ec2ImageId { get; set; } = null!;

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("studioId", required: true)]
        public Input<string> StudioId { get; set; } = null!;

        [Input("tags")]
        public Input<object>? Tags { get; set; }

        public StreamingImageArgs()
        {
        }
    }
}
