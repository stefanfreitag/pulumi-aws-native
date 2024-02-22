// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Rds
{
    /// <summary>
    /// An example resource schema demonstrating some basic constructs and validation rules.
    /// </summary>
    [AwsNativeResourceType("aws-native:rds:Integration")]
    public partial class Integration : global::Pulumi.CustomResource
    {
        [Output("additionalEncryptionContext")]
        public Output<Outputs.IntegrationEncryptionContextMap?> AdditionalEncryptionContext { get; private set; } = null!;

        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The ARN of the integration.
        /// </summary>
        [Output("integrationArn")]
        public Output<string> IntegrationArn { get; private set; } = null!;

        /// <summary>
        /// The name of the integration.
        /// </summary>
        [Output("integrationName")]
        public Output<string?> IntegrationName { get; private set; } = null!;

        /// <summary>
        /// An optional AWS Key Management System (AWS KMS) key ARN for the key used to to encrypt the integration. The resource accepts the key ID and the key ARN forms. The key ID form can be used if the KMS key is owned by te same account. If the KMS key belongs to a different account than the calling account, the full key ARN must be specified. Do not use the key alias or the key alias ARN as this will cause a false drift of the resource.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Aurora DB cluster to use as the source for replication.
        /// </summary>
        [Output("sourceArn")]
        public Output<string> SourceArn { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ARN of the Redshift data warehouse to use as the target for replication.
        /// </summary>
        [Output("targetArn")]
        public Output<string> TargetArn { get; private set; } = null!;


        /// <summary>
        /// Create a Integration resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Integration(string name, IntegrationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:rds:Integration", name, args ?? new IntegrationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Integration(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:rds:Integration", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "additionalEncryptionContext",
                    "integrationName",
                    "kmsKeyId",
                    "sourceArn",
                    "targetArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Integration resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Integration Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Integration(name, id, options);
        }
    }

    public sealed class IntegrationArgs : global::Pulumi.ResourceArgs
    {
        [Input("additionalEncryptionContext")]
        public Input<Inputs.IntegrationEncryptionContextMapArgs>? AdditionalEncryptionContext { get; set; }

        /// <summary>
        /// The name of the integration.
        /// </summary>
        [Input("integrationName")]
        public Input<string>? IntegrationName { get; set; }

        /// <summary>
        /// An optional AWS Key Management System (AWS KMS) key ARN for the key used to to encrypt the integration. The resource accepts the key ID and the key ARN forms. The key ID form can be used if the KMS key is owned by te same account. If the KMS key belongs to a different account than the calling account, the full key ARN must be specified. Do not use the key alias or the key alias ARN as this will cause a false drift of the resource.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Aurora DB cluster to use as the source for replication.
        /// </summary>
        [Input("sourceArn", required: true)]
        public Input<string> SourceArn { get; set; } = null!;

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

        /// <summary>
        /// The ARN of the Redshift data warehouse to use as the target for replication.
        /// </summary>
        [Input("targetArn", required: true)]
        public Input<string> TargetArn { get; set; } = null!;

        public IntegrationArgs()
        {
        }
        public static new IntegrationArgs Empty => new IntegrationArgs();
    }
}
