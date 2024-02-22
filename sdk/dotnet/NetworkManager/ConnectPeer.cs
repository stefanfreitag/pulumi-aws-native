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
    /// AWS::NetworkManager::ConnectPeer Resource Type Definition.
    /// </summary>
    [AwsNativeResourceType("aws-native:networkmanager:ConnectPeer")]
    public partial class ConnectPeer : global::Pulumi.CustomResource
    {
        /// <summary>
        /// Bgp options for connect peer.
        /// </summary>
        [Output("bgpOptions")]
        public Output<Outputs.ConnectPeerBgpOptions?> BgpOptions { get; private set; } = null!;

        /// <summary>
        /// Configuration of the connect peer.
        /// </summary>
        [Output("configuration")]
        public Output<Outputs.ConnectPeerConfiguration> Configuration { get; private set; } = null!;

        /// <summary>
        /// The ID of the attachment to connect.
        /// </summary>
        [Output("connectAttachmentId")]
        public Output<string> ConnectAttachmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the Connect peer.
        /// </summary>
        [Output("connectPeerId")]
        public Output<string> ConnectPeerId { get; private set; } = null!;

        /// <summary>
        /// The IP address of a core network.
        /// </summary>
        [Output("coreNetworkAddress")]
        public Output<string?> CoreNetworkAddress { get; private set; } = null!;

        /// <summary>
        /// The ID of the core network.
        /// </summary>
        [Output("coreNetworkId")]
        public Output<string> CoreNetworkId { get; private set; } = null!;

        /// <summary>
        /// Connect peer creation time.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The Connect peer Regions where edges are located.
        /// </summary>
        [Output("edgeLocation")]
        public Output<string> EdgeLocation { get; private set; } = null!;

        /// <summary>
        /// The inside IP addresses used for a Connect peer configuration.
        /// </summary>
        [Output("insideCidrBlocks")]
        public Output<ImmutableArray<string>> InsideCidrBlocks { get; private set; } = null!;

        /// <summary>
        /// The IP address of the Connect peer.
        /// </summary>
        [Output("peerAddress")]
        public Output<string> PeerAddress { get; private set; } = null!;

        /// <summary>
        /// State of the connect peer.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The subnet ARN for the connect peer.
        /// </summary>
        [Output("subnetArn")]
        public Output<string?> SubnetArn { get; private set; } = null!;

        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a ConnectPeer resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ConnectPeer(string name, ConnectPeerArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:ConnectPeer", name, args ?? new ConnectPeerArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ConnectPeer(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:ConnectPeer", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "bgpOptions",
                    "connectAttachmentId",
                    "coreNetworkAddress",
                    "insideCidrBlocks[*]",
                    "peerAddress",
                    "subnetArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing ConnectPeer resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ConnectPeer Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new ConnectPeer(name, id, options);
        }
    }

    public sealed class ConnectPeerArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Bgp options for connect peer.
        /// </summary>
        [Input("bgpOptions")]
        public Input<Inputs.ConnectPeerBgpOptionsArgs>? BgpOptions { get; set; }

        /// <summary>
        /// The ID of the attachment to connect.
        /// </summary>
        [Input("connectAttachmentId", required: true)]
        public Input<string> ConnectAttachmentId { get; set; } = null!;

        /// <summary>
        /// The IP address of a core network.
        /// </summary>
        [Input("coreNetworkAddress")]
        public Input<string>? CoreNetworkAddress { get; set; }

        [Input("insideCidrBlocks")]
        private InputList<string>? _insideCidrBlocks;

        /// <summary>
        /// The inside IP addresses used for a Connect peer configuration.
        /// </summary>
        public InputList<string> InsideCidrBlocks
        {
            get => _insideCidrBlocks ?? (_insideCidrBlocks = new InputList<string>());
            set => _insideCidrBlocks = value;
        }

        /// <summary>
        /// The IP address of the Connect peer.
        /// </summary>
        [Input("peerAddress", required: true)]
        public Input<string> PeerAddress { get; set; } = null!;

        /// <summary>
        /// The subnet ARN for the connect peer.
        /// </summary>
        [Input("subnetArn")]
        public Input<string>? SubnetArn { get; set; }

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

        public ConnectPeerArgs()
        {
        }
        public static new ConnectPeerArgs Empty => new ConnectPeerArgs();
    }
}
