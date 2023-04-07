// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisVideo
{
    /// <summary>
    /// Resource Type Definition for AWS::KinesisVideo::Stream
    /// </summary>
    [AwsNativeResourceType("aws-native:kinesisvideo:Stream")]
    public partial class Stream : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Kinesis Video stream.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The number of hours till which Kinesis Video will retain the data in the stream
        /// </summary>
        [Output("dataRetentionInHours")]
        public Output<int?> DataRetentionInHours { get; private set; } = null!;

        /// <summary>
        /// The name of the device that is writing to the stream.
        /// </summary>
        [Output("deviceName")]
        public Output<string?> DeviceName { get; private set; } = null!;

        /// <summary>
        /// AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The media type of the stream. Consumers of the stream can use this information when processing the stream.
        /// </summary>
        [Output("mediaType")]
        public Output<string?> MediaType { get; private set; } = null!;

        /// <summary>
        /// The name of the Kinesis Video stream.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs associated with the Kinesis Video Stream.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.StreamTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Stream resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Stream(string name, StreamArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:kinesisvideo:Stream", name, args ?? new StreamArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Stream(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:kinesisvideo:Stream", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Stream resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Stream Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Stream(name, id, options);
        }
    }

    public sealed class StreamArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The number of hours till which Kinesis Video will retain the data in the stream
        /// </summary>
        [Input("dataRetentionInHours")]
        public Input<int>? DataRetentionInHours { get; set; }

        /// <summary>
        /// The name of the device that is writing to the stream.
        /// </summary>
        [Input("deviceName")]
        public Input<string>? DeviceName { get; set; }

        /// <summary>
        /// AWS KMS key ID that Kinesis Video Streams uses to encrypt stream data.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The media type of the stream. Consumers of the stream can use this information when processing the stream.
        /// </summary>
        [Input("mediaType")]
        public Input<string>? MediaType { get; set; }

        /// <summary>
        /// The name of the Kinesis Video stream.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("tags")]
        private InputList<Inputs.StreamTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs associated with the Kinesis Video Stream.
        /// </summary>
        public InputList<Inputs.StreamTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.StreamTagArgs>());
            set => _tags = value;
        }

        public StreamArgs()
        {
        }
        public static new StreamArgs Empty => new StreamArgs();
    }
}
