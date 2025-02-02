// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Connect
{
    /// <summary>
    /// Resource Type definition for AWS::Connect::InstanceStorageConfig
    /// </summary>
    [AwsNativeResourceType("aws-native:connect:InstanceStorageConfig")]
    public partial class InstanceStorageConfig : global::Pulumi.CustomResource
    {
        [Output("associationId")]
        public Output<string> AssociationId { get; private set; } = null!;

        /// <summary>
        /// Connect Instance ID with which the storage config will be associated
        /// </summary>
        [Output("instanceArn")]
        public Output<string> InstanceArn { get; private set; } = null!;

        [Output("kinesisFirehoseConfig")]
        public Output<Outputs.InstanceStorageConfigKinesisFirehoseConfig?> KinesisFirehoseConfig { get; private set; } = null!;

        [Output("kinesisStreamConfig")]
        public Output<Outputs.InstanceStorageConfigKinesisStreamConfig?> KinesisStreamConfig { get; private set; } = null!;

        [Output("kinesisVideoStreamConfig")]
        public Output<Outputs.InstanceStorageConfigKinesisVideoStreamConfig?> KinesisVideoStreamConfig { get; private set; } = null!;

        [Output("resourceType")]
        public Output<Pulumi.AwsNative.Connect.InstanceStorageConfigInstanceStorageResourceType> ResourceType { get; private set; } = null!;

        [Output("s3Config")]
        public Output<Outputs.InstanceStorageConfigS3Config?> S3Config { get; private set; } = null!;

        [Output("storageType")]
        public Output<Pulumi.AwsNative.Connect.InstanceStorageConfigStorageType> StorageType { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceStorageConfig resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceStorageConfig(string name, InstanceStorageConfigArgs args, CustomResourceOptions? options = null)
            : base("aws-native:connect:InstanceStorageConfig", name, args ?? new InstanceStorageConfigArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceStorageConfig(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:connect:InstanceStorageConfig", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "instanceArn",
                    "resourceType",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InstanceStorageConfig resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceStorageConfig Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new InstanceStorageConfig(name, id, options);
        }
    }

    public sealed class InstanceStorageConfigArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Connect Instance ID with which the storage config will be associated
        /// </summary>
        [Input("instanceArn", required: true)]
        public Input<string> InstanceArn { get; set; } = null!;

        [Input("kinesisFirehoseConfig")]
        public Input<Inputs.InstanceStorageConfigKinesisFirehoseConfigArgs>? KinesisFirehoseConfig { get; set; }

        [Input("kinesisStreamConfig")]
        public Input<Inputs.InstanceStorageConfigKinesisStreamConfigArgs>? KinesisStreamConfig { get; set; }

        [Input("kinesisVideoStreamConfig")]
        public Input<Inputs.InstanceStorageConfigKinesisVideoStreamConfigArgs>? KinesisVideoStreamConfig { get; set; }

        [Input("resourceType", required: true)]
        public Input<Pulumi.AwsNative.Connect.InstanceStorageConfigInstanceStorageResourceType> ResourceType { get; set; } = null!;

        [Input("s3Config")]
        public Input<Inputs.InstanceStorageConfigS3ConfigArgs>? S3Config { get; set; }

        [Input("storageType", required: true)]
        public Input<Pulumi.AwsNative.Connect.InstanceStorageConfigStorageType> StorageType { get; set; } = null!;

        public InstanceStorageConfigArgs()
        {
        }
        public static new InstanceStorageConfigArgs Empty => new InstanceStorageConfigArgs();
    }
}
