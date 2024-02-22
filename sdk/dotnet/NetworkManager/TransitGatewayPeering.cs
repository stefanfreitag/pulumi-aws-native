// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    /// <summary>
    /// AWS::NetworkManager::TransitGatewayPeering Resoruce Type.
    /// </summary>
    [AwsNativeResourceType("aws-native:networkmanager:TransitGatewayPeering")]
    public partial class TransitGatewayPeering : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN (Amazon Resource Name) of the core network that you want to peer a transit gateway to.
        /// </summary>
        [Output("coreNetworkArn")]
        public Output<string> CoreNetworkArn { get; private set; } = null!;

        /// <summary>
        /// The Id of the core network that you want to peer a transit gateway to.
        /// </summary>
        [Output("coreNetworkId")]
        public Output<string> CoreNetworkId { get; private set; } = null!;

        /// <summary>
        /// The creation time of the transit gateway peering
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The location of the transit gateway peering
        /// </summary>
        [Output("edgeLocation")]
        public Output<string> EdgeLocation { get; private set; } = null!;

        /// <summary>
        /// Peering owner account Id
        /// </summary>
        [Output("ownerAccountId")]
        public Output<string> OwnerAccountId { get; private set; } = null!;

        /// <summary>
        /// The Id of the transit gateway peering
        /// </summary>
        [Output("peeringId")]
        public Output<string> PeeringId { get; private set; } = null!;

        /// <summary>
        /// Peering type (TransitGatewayPeering)
        /// </summary>
        [Output("peeringType")]
        public Output<string> PeeringType { get; private set; } = null!;

        /// <summary>
        /// The ARN (Amazon Resource Name) of the resource that you will peer to a core network
        /// </summary>
        [Output("resourceArn")]
        public Output<string> ResourceArn { get; private set; } = null!;

        /// <summary>
        /// The state of the transit gateway peering
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ARN (Amazon Resource Name) of the transit gateway that you will peer to a core network
        /// </summary>
        [Output("transitGatewayArn")]
        public Output<string> TransitGatewayArn { get; private set; } = null!;

        /// <summary>
        /// The ID of the TransitGatewayPeeringAttachment
        /// </summary>
        [Output("transitGatewayPeeringAttachmentId")]
        public Output<string> TransitGatewayPeeringAttachmentId { get; private set; } = null!;


        /// <summary>
        /// Create a TransitGatewayPeering resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TransitGatewayPeering(string name, TransitGatewayPeeringArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:TransitGatewayPeering", name, args ?? new TransitGatewayPeeringArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TransitGatewayPeering(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:TransitGatewayPeering", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "coreNetworkId",
                    "transitGatewayArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TransitGatewayPeering resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TransitGatewayPeering Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TransitGatewayPeering(name, id, options);
        }
    }

    public sealed class TransitGatewayPeeringArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Id of the core network that you want to peer a transit gateway to.
        /// </summary>
        [Input("coreNetworkId", required: true)]
        public Input<string> CoreNetworkId { get; set; } = null!;

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
        /// The ARN (Amazon Resource Name) of the transit gateway that you will peer to a core network
        /// </summary>
        [Input("transitGatewayArn", required: true)]
        public Input<string> TransitGatewayArn { get; set; } = null!;

        public TransitGatewayPeeringArgs()
        {
        }
        public static new TransitGatewayPeeringArgs Empty => new TransitGatewayPeeringArgs();
    }
}
