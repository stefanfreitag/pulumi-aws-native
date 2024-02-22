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
    /// An object representing an Amazon EKS cluster.
    /// </summary>
    [AwsNativeResourceType("aws-native:eks:Cluster")]
    public partial class Cluster : global::Pulumi.CustomResource
    {
        [Output("accessConfig")]
        public Output<Outputs.ClusterAccessConfig?> AccessConfig { get; private set; } = null!;

        /// <summary>
        /// The ARN of the cluster, such as arn:aws:eks:us-west-2:666666666666:cluster/prod.
        /// </summary>
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        /// <summary>
        /// The certificate-authority-data for your cluster.
        /// </summary>
        [Output("certificateAuthorityData")]
        public Output<string> CertificateAuthorityData { get; private set; } = null!;

        /// <summary>
        /// The cluster security group that was created by Amazon EKS for the cluster. Managed node groups use this security group for control plane to data plane communication.
        /// </summary>
        [Output("clusterSecurityGroupId")]
        public Output<string> ClusterSecurityGroupId { get; private set; } = null!;

        [Output("encryptionConfig")]
        public Output<ImmutableArray<Outputs.ClusterEncryptionConfig>> EncryptionConfig { get; private set; } = null!;

        /// <summary>
        /// Amazon Resource Name (ARN) or alias of the customer master key (CMK).
        /// </summary>
        [Output("encryptionConfigKeyArn")]
        public Output<string> EncryptionConfigKeyArn { get; private set; } = null!;

        /// <summary>
        /// The endpoint for your Kubernetes API server, such as https://5E1D0CEXAMPLEA591B746AFC5AB30262.yl4.us-west-2.eks.amazonaws.com.
        /// </summary>
        [Output("endpoint")]
        public Output<string> Endpoint { get; private set; } = null!;

        [Output("kubernetesNetworkConfig")]
        public Output<Outputs.ClusterKubernetesNetworkConfig?> KubernetesNetworkConfig { get; private set; } = null!;

        [Output("logging")]
        public Output<Outputs.Logging?> Logging { get; private set; } = null!;

        /// <summary>
        /// The unique name to give to your cluster.
        /// </summary>
        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        /// <summary>
        /// The issuer URL for the cluster's OIDC identity provider, such as https://oidc.eks.us-west-2.amazonaws.com/id/EXAMPLED539D4633E53DE1B716D3041E. If you need to remove https:// from this output value, you can include the following code in your template.
        /// </summary>
        [Output("openIdConnectIssuerUrl")]
        public Output<string> OpenIdConnectIssuerUrl { get; private set; } = null!;

        [Output("outpostConfig")]
        public Output<Outputs.ClusterOutpostConfig?> OutpostConfig { get; private set; } = null!;

        [Output("resourcesVpcConfig")]
        public Output<Outputs.ClusterResourcesVpcConfig> ResourcesVpcConfig { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        /// </summary>
        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        /// </summary>
        [Output("version")]
        public Output<string?> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Cluster resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Cluster(string name, ClusterArgs args, CustomResourceOptions? options = null)
            : base("aws-native:eks:Cluster", name, args ?? new ClusterArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Cluster(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:eks:Cluster", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "accessConfig.bootstrapClusterCreatorAdminPermissions",
                    "encryptionConfig[*]",
                    "kubernetesNetworkConfig",
                    "name",
                    "outpostConfig",
                    "roleArn",
                },
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
        [Input("accessConfig")]
        public Input<Inputs.ClusterAccessConfigArgs>? AccessConfig { get; set; }

        [Input("encryptionConfig")]
        private InputList<Inputs.ClusterEncryptionConfigArgs>? _encryptionConfig;
        public InputList<Inputs.ClusterEncryptionConfigArgs> EncryptionConfig
        {
            get => _encryptionConfig ?? (_encryptionConfig = new InputList<Inputs.ClusterEncryptionConfigArgs>());
            set => _encryptionConfig = value;
        }

        [Input("kubernetesNetworkConfig")]
        public Input<Inputs.ClusterKubernetesNetworkConfigArgs>? KubernetesNetworkConfig { get; set; }

        [Input("logging")]
        public Input<Inputs.LoggingArgs>? Logging { get; set; }

        /// <summary>
        /// The unique name to give to your cluster.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("outpostConfig")]
        public Input<Inputs.ClusterOutpostConfigArgs>? OutpostConfig { get; set; }

        [Input("resourcesVpcConfig", required: true)]
        public Input<Inputs.ClusterResourcesVpcConfigArgs> ResourcesVpcConfig { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the IAM role that provides permissions for the Kubernetes control plane to make calls to AWS API operations on your behalf.
        /// </summary>
        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

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
        /// The desired Kubernetes version for your cluster. If you don't specify a value here, the latest version available in Amazon EKS is used.
        /// </summary>
        [Input("version")]
        public Input<string>? Version { get; set; }

        public ClusterArgs()
        {
        }
        public static new ClusterArgs Empty => new ClusterArgs();
    }
}
