// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MediaConnect
{
    /// <summary>
    /// Resource schema for AWS::MediaConnect::Bridge
    /// </summary>
    [AwsNativeResourceType("aws-native:mediaconnect:Bridge")]
    public partial class Bridge : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The Amazon Resource Number (ARN) of the bridge.
        /// </summary>
        [Output("bridgeArn")]
        public Output<string> BridgeArn { get; private set; } = null!;

        [Output("bridgeState")]
        public Output<Pulumi.AwsNative.MediaConnect.BridgeStateEnum> BridgeState { get; private set; } = null!;

        [Output("egressGatewayBridge")]
        public Output<Outputs.BridgeEgressGatewayBridge?> EgressGatewayBridge { get; private set; } = null!;

        [Output("ingressGatewayBridge")]
        public Output<Outputs.BridgeIngressGatewayBridge?> IngressGatewayBridge { get; private set; } = null!;

        /// <summary>
        /// The name of the bridge.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The outputs on this bridge.
        /// </summary>
        [Output("outputs")]
        public Output<ImmutableArray<Outputs.BridgeOutput>> Outputs { get; private set; } = null!;

        /// <summary>
        /// The placement Amazon Resource Number (ARN) of the bridge.
        /// </summary>
        [Output("placementArn")]
        public Output<string> PlacementArn { get; private set; } = null!;

        [Output("sourceFailoverConfig")]
        public Output<Outputs.BridgeFailoverConfig?> SourceFailoverConfig { get; private set; } = null!;

        /// <summary>
        /// The sources on this bridge.
        /// </summary>
        [Output("sources")]
        public Output<ImmutableArray<Outputs.BridgeSource>> Sources { get; private set; } = null!;


        /// <summary>
        /// Create a Bridge resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Bridge(string name, BridgeArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:Bridge", name, args ?? new BridgeArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Bridge(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:Bridge", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Bridge resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Bridge Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Bridge(name, id, options);
        }
    }

    public sealed class BridgeArgs : global::Pulumi.ResourceArgs
    {
        [Input("egressGatewayBridge")]
        public Input<Inputs.BridgeEgressGatewayBridgeArgs>? EgressGatewayBridge { get; set; }

        [Input("ingressGatewayBridge")]
        public Input<Inputs.BridgeIngressGatewayBridgeArgs>? IngressGatewayBridge { get; set; }

        /// <summary>
        /// The name of the bridge.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("outputs")]
        private InputList<Inputs.BridgeOutputArgs>? _outputs;

        /// <summary>
        /// The outputs on this bridge.
        /// </summary>
        public InputList<Inputs.BridgeOutputArgs> Outputs
        {
            get => _outputs ?? (_outputs = new InputList<Inputs.BridgeOutputArgs>());
            set => _outputs = value;
        }

        /// <summary>
        /// The placement Amazon Resource Number (ARN) of the bridge.
        /// </summary>
        [Input("placementArn", required: true)]
        public Input<string> PlacementArn { get; set; } = null!;

        [Input("sourceFailoverConfig")]
        public Input<Inputs.BridgeFailoverConfigArgs>? SourceFailoverConfig { get; set; }

        [Input("sources", required: true)]
        private InputList<Inputs.BridgeSourceArgs>? _sources;

        /// <summary>
        /// The sources on this bridge.
        /// </summary>
        public InputList<Inputs.BridgeSourceArgs> Sources
        {
            get => _sources ?? (_sources = new InputList<Inputs.BridgeSourceArgs>());
            set => _sources = value;
        }

        public BridgeArgs()
        {
        }
        public static new BridgeArgs Empty => new BridgeArgs();
    }
}
