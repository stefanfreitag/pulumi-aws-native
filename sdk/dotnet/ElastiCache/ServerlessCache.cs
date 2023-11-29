// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ElastiCache
{
    /// <summary>
    /// The AWS::ElastiCache::ServerlessCache resource creates an Amazon ElastiCache Serverless Cache.
    /// </summary>
    [AwsNativeResourceType("aws-native:elasticache:ServerlessCache")]
    public partial class ServerlessCache : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the Serverless Cache.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("cacheUsageLimits")]
        public Output<Outputs.ServerlessCacheCacheUsageLimits?> CacheUsageLimits { get; private set; } = null!;

        /// <summary>
        /// The creation time of the Serverless Cache.
        /// </summary>
        [Output("createTime")]
        public Output<string> CreateTime { get; private set; } = null!;

        /// <summary>
        /// The daily time range (in UTC) during which the service takes automatic snapshot of the Serverless Cache.
        /// </summary>
        [Output("dailySnapshotTime")]
        public Output<string?> DailySnapshotTime { get; private set; } = null!;

        /// <summary>
        /// The description of the Serverless Cache.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("endpoint")]
        public Output<Outputs.ServerlessCacheEndpoint> Endpoint { get; private set; } = null!;

        /// <summary>
        /// The engine name of the Serverless Cache.
        /// </summary>
        [Output("engine")]
        public Output<string> Engine { get; private set; } = null!;

        /// <summary>
        /// The final snapshot name which is taken before Serverless Cache is deleted.
        /// </summary>
        [Output("finalSnapshotName")]
        public Output<string?> FinalSnapshotName { get; private set; } = null!;

        /// <summary>
        /// The full engine version of the Serverless Cache.
        /// </summary>
        [Output("fullEngineVersion")]
        public Output<string> FullEngineVersion { get; private set; } = null!;

        /// <summary>
        /// The ID of the KMS key used to encrypt the cluster.
        /// </summary>
        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        /// <summary>
        /// The major engine version of the Serverless Cache.
        /// </summary>
        [Output("majorEngineVersion")]
        public Output<string?> MajorEngineVersion { get; private set; } = null!;

        [Output("readerEndpoint")]
        public Output<Outputs.ServerlessCacheEndpoint> ReaderEndpoint { get; private set; } = null!;

        /// <summary>
        /// One or more Amazon VPC security groups associated with this Serverless Cache.
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// The name of the Serverless Cache. This value must be unique.
        /// </summary>
        [Output("serverlessCacheName")]
        public Output<string> ServerlessCacheName { get; private set; } = null!;

        /// <summary>
        /// The ARN's of snapshot to restore Serverless Cache.
        /// </summary>
        [Output("snapshotArnsToRestore")]
        public Output<ImmutableArray<string>> SnapshotArnsToRestore { get; private set; } = null!;

        /// <summary>
        /// The snapshot retention limit of the Serverless Cache.
        /// </summary>
        [Output("snapshotRetentionLimit")]
        public Output<int?> SnapshotRetentionLimit { get; private set; } = null!;

        /// <summary>
        /// The status of the Serverless Cache.
        /// </summary>
        [Output("status")]
        public Output<string> Status { get; private set; } = null!;

        /// <summary>
        /// The subnet id's of the Serverless Cache.
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this Serverless Cache.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ServerlessCacheTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID of the user group.
        /// </summary>
        [Output("userGroupId")]
        public Output<string?> UserGroupId { get; private set; } = null!;


        /// <summary>
        /// Create a ServerlessCache resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ServerlessCache(string name, ServerlessCacheArgs args, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:ServerlessCache", name, args ?? new ServerlessCacheArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ServerlessCache(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:elasticache:ServerlessCache", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "engine",
                    "kmsKeyId",
                    "majorEngineVersion",
                    "serverlessCacheName",
                    "snapshotArnsToRestore[*]",
                    "subnetIds[*]",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ServerlessCache resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ServerlessCache Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ServerlessCache(name, id, options);
        }
    }

    public sealed class ServerlessCacheArgs : global::Pulumi.ResourceArgs
    {
        [Input("cacheUsageLimits")]
        public Input<Inputs.ServerlessCacheCacheUsageLimitsArgs>? CacheUsageLimits { get; set; }

        /// <summary>
        /// The daily time range (in UTC) during which the service takes automatic snapshot of the Serverless Cache.
        /// </summary>
        [Input("dailySnapshotTime")]
        public Input<string>? DailySnapshotTime { get; set; }

        /// <summary>
        /// The description of the Serverless Cache.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The engine name of the Serverless Cache.
        /// </summary>
        [Input("engine", required: true)]
        public Input<string> Engine { get; set; } = null!;

        /// <summary>
        /// The final snapshot name which is taken before Serverless Cache is deleted.
        /// </summary>
        [Input("finalSnapshotName")]
        public Input<string>? FinalSnapshotName { get; set; }

        /// <summary>
        /// The ID of the KMS key used to encrypt the cluster.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The major engine version of the Serverless Cache.
        /// </summary>
        [Input("majorEngineVersion")]
        public Input<string>? MajorEngineVersion { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// One or more Amazon VPC security groups associated with this Serverless Cache.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// The name of the Serverless Cache. This value must be unique.
        /// </summary>
        [Input("serverlessCacheName")]
        public Input<string>? ServerlessCacheName { get; set; }

        [Input("snapshotArnsToRestore")]
        private InputList<string>? _snapshotArnsToRestore;

        /// <summary>
        /// The ARN's of snapshot to restore Serverless Cache.
        /// </summary>
        public InputList<string> SnapshotArnsToRestore
        {
            get => _snapshotArnsToRestore ?? (_snapshotArnsToRestore = new InputList<string>());
            set => _snapshotArnsToRestore = value;
        }

        /// <summary>
        /// The snapshot retention limit of the Serverless Cache.
        /// </summary>
        [Input("snapshotRetentionLimit")]
        public Input<int>? SnapshotRetentionLimit { get; set; }

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// The subnet id's of the Serverless Cache.
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.ServerlessCacheTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this Serverless Cache.
        /// </summary>
        public InputList<Inputs.ServerlessCacheTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ServerlessCacheTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID of the user group.
        /// </summary>
        [Input("userGroupId")]
        public Input<string>? UserGroupId { get; set; }

        public ServerlessCacheArgs()
        {
        }
        public static new ServerlessCacheArgs Empty => new ServerlessCacheArgs();
    }
}
