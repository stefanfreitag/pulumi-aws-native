// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::InstanceConnectEndpoint
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:InstanceConnectEndpoint")]
    public partial class InstanceConnectEndpoint : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The client token of the instance connect endpoint.
        /// </summary>
        [Output("clientToken")]
        public Output<string?> ClientToken { get; private set; } = null!;

        /// <summary>
        /// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
        /// </summary>
        [Output("preserveClientIp")]
        public Output<bool?> PreserveClientIp { get; private set; } = null!;

        /// <summary>
        /// The security group IDs of the instance connect endpoint.
        /// </summary>
        [Output("securityGroupIds")]
        public Output<ImmutableArray<string>> SecurityGroupIds { get; private set; } = null!;

        /// <summary>
        /// The subnet id of the instance connect endpoint
        /// </summary>
        [Output("subnetId")]
        public Output<string> SubnetId { get; private set; } = null!;

        /// <summary>
        /// The tags of the instance connect endpoint.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceConnectEndpoint resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceConnectEndpoint(string name, InstanceConnectEndpointArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:InstanceConnectEndpoint", name, args ?? new InstanceConnectEndpointArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceConnectEndpoint(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:InstanceConnectEndpoint", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "clientToken",
                    "preserveClientIp",
                    "securityGroupIds[*]",
                    "subnetId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing InstanceConnectEndpoint resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceConnectEndpoint Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new InstanceConnectEndpoint(name, id, options);
        }
    }

    public sealed class InstanceConnectEndpointArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The client token of the instance connect endpoint.
        /// </summary>
        [Input("clientToken")]
        public Input<string>? ClientToken { get; set; }

        /// <summary>
        /// If true, the address of the instance connect endpoint client is preserved when connecting to the end resource
        /// </summary>
        [Input("preserveClientIp")]
        public Input<bool>? PreserveClientIp { get; set; }

        [Input("securityGroupIds")]
        private InputList<string>? _securityGroupIds;

        /// <summary>
        /// The security group IDs of the instance connect endpoint.
        /// </summary>
        public InputList<string> SecurityGroupIds
        {
            get => _securityGroupIds ?? (_securityGroupIds = new InputList<string>());
            set => _securityGroupIds = value;
        }

        /// <summary>
        /// The subnet id of the instance connect endpoint
        /// </summary>
        [Input("subnetId", required: true)]
        public Input<string> SubnetId { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags of the instance connect endpoint.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        public InstanceConnectEndpointArgs()
        {
        }
        public static new InstanceConnectEndpointArgs Empty => new InstanceConnectEndpointArgs();
    }
}
