// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Redshift
{
    /// <summary>
    /// Specifies an Amazon Redshift subnet group.
    /// </summary>
    [AwsNativeResourceType("aws-native:redshift:ClusterSubnetGroup")]
    public partial class ClusterSubnetGroup : global::Pulumi.CustomResource
    {
        /// <summary>
        /// This name must be unique for all subnet groups that are created by your AWS account. If costumer do not provide it, cloudformation will generate it. Must not be "Default". 
        /// </summary>
        [Output("clusterSubnetGroupName")]
        public Output<string> ClusterSubnetGroupName { get; private set; } = null!;

        /// <summary>
        /// The description of the parameter group.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The list of VPC subnet IDs
        /// </summary>
        [Output("subnetIds")]
        public Output<ImmutableArray<string>> SubnetIds { get; private set; } = null!;

        /// <summary>
        /// The list of tags for the cluster parameter group.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.ClusterSubnetGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterSubnetGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterSubnetGroup(string name, ClusterSubnetGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ClusterSubnetGroup", name, args ?? new ClusterSubnetGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterSubnetGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ClusterSubnetGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterSubnetGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterSubnetGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ClusterSubnetGroup(name, id, options);
        }
    }

    public sealed class ClusterSubnetGroupArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of the parameter group.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("subnetIds", required: true)]
        private InputList<string>? _subnetIds;

        /// <summary>
        /// The list of VPC subnet IDs
        /// </summary>
        public InputList<string> SubnetIds
        {
            get => _subnetIds ?? (_subnetIds = new InputList<string>());
            set => _subnetIds = value;
        }

        [Input("tags")]
        private InputList<Inputs.ClusterSubnetGroupTagArgs>? _tags;

        /// <summary>
        /// The list of tags for the cluster parameter group.
        /// </summary>
        public InputList<Inputs.ClusterSubnetGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ClusterSubnetGroupTagArgs>());
            set => _tags = value;
        }

        public ClusterSubnetGroupArgs()
        {
        }
        public static new ClusterSubnetGroupArgs Empty => new ClusterSubnetGroupArgs();
    }
}
