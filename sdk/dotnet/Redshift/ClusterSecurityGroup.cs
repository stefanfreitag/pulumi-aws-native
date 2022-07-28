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
    /// Resource Type definition for AWS::Redshift::ClusterSecurityGroup
    /// </summary>
    [Obsolete(@"ClusterSecurityGroup is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:redshift:ClusterSecurityGroup")]
    public partial class ClusterSecurityGroup : global::Pulumi.CustomResource
    {
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.ClusterSecurityGroupTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ClusterSecurityGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ClusterSecurityGroup(string name, ClusterSecurityGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ClusterSecurityGroup", name, args ?? new ClusterSecurityGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ClusterSecurityGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:redshift:ClusterSecurityGroup", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing ClusterSecurityGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ClusterSecurityGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ClusterSecurityGroup(name, id, options);
        }
    }

    public sealed class ClusterSecurityGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.ClusterSecurityGroupTagArgs>? _tags;
        public InputList<Inputs.ClusterSecurityGroupTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.ClusterSecurityGroupTagArgs>());
            set => _tags = value;
        }

        public ClusterSecurityGroupArgs()
        {
        }
        public static new ClusterSecurityGroupArgs Empty => new ClusterSecurityGroupArgs();
    }
}
