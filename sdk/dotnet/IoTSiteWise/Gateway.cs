// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise
{
    /// <summary>
    /// Resource schema for AWS::IoTSiteWise::Gateway
    /// </summary>
    [AwsNativeResourceType("aws-native:iotsitewise:Gateway")]
    public partial class Gateway : Pulumi.CustomResource
    {
        /// <summary>
        /// A list of gateway capability summaries that each contain a namespace and status.
        /// </summary>
        [Output("gatewayCapabilitySummaries")]
        public Output<ImmutableArray<Outputs.GatewayGatewayCapabilitySummary>> GatewayCapabilitySummaries { get; private set; } = null!;

        /// <summary>
        /// The ID of the gateway device.
        /// </summary>
        [Output("gatewayId")]
        public Output<string> GatewayId { get; private set; } = null!;

        /// <summary>
        /// A unique, friendly name for the gateway.
        /// </summary>
        [Output("gatewayName")]
        public Output<string> GatewayName { get; private set; } = null!;

        /// <summary>
        /// The gateway's platform. You can only specify one platform in a gateway.
        /// </summary>
        [Output("gatewayPlatform")]
        public Output<Outputs.GatewayGatewayPlatform> GatewayPlatform { get; private set; } = null!;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the gateway.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.GatewayTag>> Tags { get; private set; } = null!;


        /// <summary>
        /// Create a Gateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Gateway(string name, GatewayArgs args, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Gateway", name, args ?? new GatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Gateway(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:iotsitewise:Gateway", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Gateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Gateway Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Gateway(name, id, options);
        }
    }

    public sealed class GatewayArgs : Pulumi.ResourceArgs
    {
        [Input("gatewayCapabilitySummaries")]
        private InputList<Inputs.GatewayGatewayCapabilitySummaryArgs>? _gatewayCapabilitySummaries;

        /// <summary>
        /// A list of gateway capability summaries that each contain a namespace and status.
        /// </summary>
        public InputList<Inputs.GatewayGatewayCapabilitySummaryArgs> GatewayCapabilitySummaries
        {
            get => _gatewayCapabilitySummaries ?? (_gatewayCapabilitySummaries = new InputList<Inputs.GatewayGatewayCapabilitySummaryArgs>());
            set => _gatewayCapabilitySummaries = value;
        }

        /// <summary>
        /// A unique, friendly name for the gateway.
        /// </summary>
        [Input("gatewayName", required: true)]
        public Input<string> GatewayName { get; set; } = null!;

        /// <summary>
        /// The gateway's platform. You can only specify one platform in a gateway.
        /// </summary>
        [Input("gatewayPlatform", required: true)]
        public Input<Inputs.GatewayGatewayPlatformArgs> GatewayPlatform { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.GatewayTagArgs>? _tags;

        /// <summary>
        /// A list of key-value pairs that contain metadata for the gateway.
        /// </summary>
        public InputList<Inputs.GatewayTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.GatewayTagArgs>());
            set => _tags = value;
        }

        public GatewayArgs()
        {
        }
    }
}
