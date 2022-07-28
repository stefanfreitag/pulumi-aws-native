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
    /// AWS::NetworkManager::CoreNetwork Resource Type Definition.
    /// </summary>
    [Obsolete(@"CoreNetwork is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:networkmanager:CoreNetwork")]
    public partial class CoreNetwork : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The ARN (Amazon resource name) of core network
        /// </summary>
        [Output("coreNetworkArn")]
        public Output<string> CoreNetworkArn { get; private set; } = null!;

        /// <summary>
        /// The Id of core network
        /// </summary>
        [Output("coreNetworkId")]
        public Output<string> CoreNetworkId { get; private set; } = null!;

        /// <summary>
        /// The creation time of core network
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The description of core network
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// The edges within a core network.
        /// </summary>
        [Output("edges")]
        public Output<ImmutableArray<Outputs.CoreNetworkEdge>> Edges { get; private set; } = null!;

        /// <summary>
        /// The ID of the global network that your core network is a part of.
        /// </summary>
        [Output("globalNetworkId")]
        public Output<string> GlobalNetworkId { get; private set; } = null!;

        /// <summary>
        /// Owner of the core network
        /// </summary>
        [Output("ownerAccount")]
        public Output<string> OwnerAccount { get; private set; } = null!;

        /// <summary>
        /// Live policy document for the core network, you must provide PolicyDocument in Json Format
        /// </summary>
        [Output("policyDocument")]
        public Output<object?> PolicyDocument { get; private set; } = null!;

        /// <summary>
        /// The segments within a core network.
        /// </summary>
        [Output("segments")]
        public Output<ImmutableArray<Outputs.CoreNetworkSegment>> Segments { get; private set; } = null!;

        /// <summary>
        /// The state of core network
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The tags for the global network.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.CoreNetworkTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a CoreNetwork resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CoreNetwork(string name, CoreNetworkArgs args, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:CoreNetwork", name, args ?? new CoreNetworkArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CoreNetwork(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:networkmanager:CoreNetwork", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing CoreNetwork resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CoreNetwork Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CoreNetwork(name, id, options);
        }
    }

    public sealed class CoreNetworkArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The description of core network
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// The ID of the global network that your core network is a part of.
        /// </summary>
        [Input("globalNetworkId", required: true)]
        public Input<string> GlobalNetworkId { get; set; } = null!;

        /// <summary>
        /// Live policy document for the core network, you must provide PolicyDocument in Json Format
        /// </summary>
        [Input("policyDocument")]
        public Input<object>? PolicyDocument { get; set; }

        [Input("tags")]
        private InputList<Inputs.CoreNetworkTagArgs>? _tags;

        /// <summary>
        /// The tags for the global network.
        /// </summary>
        public InputList<Inputs.CoreNetworkTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CoreNetworkTagArgs>());
            set => _tags = value;
        }

        public CoreNetworkArgs()
        {
        }
        public static new CoreNetworkArgs Empty => new CoreNetworkArgs();
    }
}
