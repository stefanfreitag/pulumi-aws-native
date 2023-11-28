// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Eks
{
    /// <summary>
    /// An object representing an Amazon EKS PodIdentityAssociation.
    /// </summary>
    [AwsNativeResourceType("aws-native:eks:PodIdentityAssociation")]
    public partial class PodIdentityAssociation : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN of the pod identity association.
        /// </summary>
        [Output("associationArn")]
        public Output<string> AssociationArn { get; private set; } = null!;

        /// <summary>
        /// The ID of the pod identity association.
        /// </summary>
        [Output("associationId")]
        public Output<string> AssociationId { get; private set; } = null!;

        /// <summary>
        /// The cluster that the pod identity association is created for.
        /// </summary>
        [Output("clusterName")]
        public Output<string> ClusterName { get; private set; } = null!;

        /// <summary>
        /// The Kubernetes namespace that the pod identity association is created for.
        /// </summary>
        [Output("namespace")]
        public Output<string> Namespace { get; private set; } = null!;

        /// <summary>
        /// The IAM role ARN that the pod identity association is created for.
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// The Kubernetes service account that the pod identity association is created for.
        /// </summary>
        [Output("serviceAccount")]
        public Output<string> ServiceAccount { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.PodIdentityAssociationTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a PodIdentityAssociation resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public PodIdentityAssociation(string name, PodIdentityAssociationArgs args, CustomResourceOptions? options = null)
            : base("aws-native:eks:PodIdentityAssociation", name, args ?? new PodIdentityAssociationArgs(), MakeResourceOptions(options, ""))
        {
        }

        private PodIdentityAssociation(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:eks:PodIdentityAssociation", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "clusterName",
                    "namespace",
                    "serviceAccount",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing PodIdentityAssociation resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static PodIdentityAssociation Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new PodIdentityAssociation(name, id, options);
        }
    }

    public sealed class PodIdentityAssociationArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The cluster that the pod identity association is created for.
        /// </summary>
        [Input("clusterName", required: true)]
        public Input<string> ClusterName { get; set; } = null!;

        /// <summary>
        /// The Kubernetes namespace that the pod identity association is created for.
        /// </summary>
        [Input("namespace", required: true)]
        public Input<string> Namespace { get; set; } = null!;

        /// <summary>
        /// The IAM role ARN that the pod identity association is created for.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        /// <summary>
        /// The Kubernetes service account that the pod identity association is created for.
        /// </summary>
        [Input("serviceAccount", required: true)]
        public Input<string> ServiceAccount { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.PodIdentityAssociationTagArgs>? _tags;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public InputList<Inputs.PodIdentityAssociationTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.PodIdentityAssociationTagArgs>());
            set => _tags = value;
        }

        public PodIdentityAssociationArgs()
        {
        }
        public static new PodIdentityAssociationArgs Empty => new PodIdentityAssociationArgs();
    }
}
