// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DocDBElastic
{
    /// <summary>
    /// The AWS::DocDBElastic::Cluster Amazon DocumentDB (with MongoDB compatibility) Elastic Scale resource describes a Cluster
    /// </summary>
    [AwsNativeResourceType("aws-native:docdbelastic:Cluster")]
    public partial class Cluster : global::Pulumi.CustomResource
    {
        [Output("adminUserName")]
        public Output<string> AdminUserName { get; private set; } = null!;

        [Output("adminUserPassword")]
        public Output<string?> AdminUserPassword { get; private set; } = null!;

        [Output("authType")]
        public Output<string> AuthType { get; private set; } = null!;

        [Output("clusterArn")]
        public Output<string> ClusterArn { get; private set; } = null!;

        [Output("clusterEndpoint")]
        public Output<string> ClusterEndpoint { get; private set; } = null!;

        [Output("clusterName")]
        public Output<string> ClusterName { get; private set; } = null!;

        [Output("kmsKeyId")]
        public Output<string?> KmsKeyId { get; private set; } = null!;

        [Output("preferredMaintenanceWindow")]
        public Output<string?> PreferredMaintenanceWindow { get; private set; } = null!;

        [Output("shardCapacity")]
        public Output<int> ShardCapacity { get; private set; } = null!;

        [Output("shardCount")]
        public Output<int> ShardCount { get; private set; } = null!;

        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ClusterTag>> Tags { get; private set; } = null!;

        [Output("vpcSecurityGroupIds")]
        public Output<ImmutableArray<string>> VpcSecurityGroupIds { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:docdbelastic:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:docdbelastic:Cluster", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Cluster resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Cluster Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Cluster(name, id, options);
        }
    }

    public sealed class ClusterArgs : global::Pulumi.ResourceArgs
    {
        [Input("adminUserName", required: true)]
        public Input<string> AdminUserName { get; set; } = null!;

        [Input("adminUserPassword")]
        public Input<string>? AdminUserPassword { get; set; }

        [Input("authType", required: true)]
        public Input<string> AuthType { get; set; } = null!;

        [Input("clusterName")]
        public Input<string>? ClusterName { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("preferredMaintenanceWindow")]
        public Input<string>? PreferredMaintenanceWindow { get; set; }

        [Input("shardCapacity", required: true)]
        public Input<int> ShardCapacity { get; set; } = null!;

        [Input("shardCount", required: true)]
        public Input<int> ShardCount { get; set; } = null!;

        [Input("subnetIds")]
        private InputList<string>? _subnetIds;
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.ClusterTagArgs>? _tags;
        public InputList<Inputs.ClusterTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ClusterTagArgs>());
            set => _tags = value;
        }

        [Input("vpcSecurityGroupIds")]
        private InputList<string>? _vpcSecurityGroupIds;
        public InputList<string> VpcSecurityGroupIds
        {
            get => _vpcSecurityGroupIds ?? (_vpcSecurityGroupIds = new InputList<string>());
            set => _vpcSecurityGroupIds = value;
        }

        public ClusterArgs()
        {
        }
        public static new ClusterArgs Empty => new ClusterArgs();
    }
}
