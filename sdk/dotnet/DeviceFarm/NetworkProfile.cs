// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DeviceFarm
{
    /// <summary>
    /// AWS::DeviceFarm::NetworkProfile creates a new DF Network Profile
    /// </summary>
    [AwsNativeResourceType("aws-native:devicefarm:NetworkProfile")]
    public partial class NetworkProfile : global::Pulumi.CustomResource
    {
        [Output("arn")]
        public Output<string> Arn { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("downlinkBandwidthBits")]
        public Output<int?> DownlinkBandwidthBits { get; private set; } = null!;

        [Output("downlinkDelayMs")]
        public Output<int?> DownlinkDelayMs { get; private set; } = null!;

        [Output("downlinkJitterMs")]
        public Output<int?> DownlinkJitterMs { get; private set; } = null!;

        [Output("downlinkLossPercent")]
        public Output<int?> DownlinkLossPercent { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("projectArn")]
        public Output<string> ProjectArn { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("uplinkBandwidthBits")]
        public Output<int?> UplinkBandwidthBits { get; private set; } = null!;

        [Output("uplinkDelayMs")]
        public Output<int?> UplinkDelayMs { get; private set; } = null!;

        [Output("uplinkJitterMs")]
        public Output<int?> UplinkJitterMs { get; private set; } = null!;

        [Output("uplinkLossPercent")]
        public Output<int?> UplinkLossPercent { get; private set; } = null!;


        /// <summary>
        /// Create a NetworkProfile resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NetworkProfile(string name, NetworkProfileArgs args, CustomResourceOptions? options = null)
            : base("aws-native:devicefarm:NetworkProfile", name, args ?? new NetworkProfileArgs(), MakeResourceOptions(options, ""))
        {
        }

        private NetworkProfile(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:devicefarm:NetworkProfile", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "projectArn",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing NetworkProfile resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NetworkProfile Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new NetworkProfile(name, id, options);
        }
    }

    public sealed class NetworkProfileArgs : global::Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("downlinkBandwidthBits")]
        public Input<int>? DownlinkBandwidthBits { get; set; }

        [Input("downlinkDelayMs")]
        public Input<int>? DownlinkDelayMs { get; set; }

        [Input("downlinkJitterMs")]
        public Input<int>? DownlinkJitterMs { get; set; }

        [Input("downlinkLossPercent")]
        public Input<int>? DownlinkLossPercent { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("projectArn", required: true)]
        public Input<string> ProjectArn { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("uplinkBandwidthBits")]
        public Input<int>? UplinkBandwidthBits { get; set; }

        [Input("uplinkDelayMs")]
        public Input<int>? UplinkDelayMs { get; set; }

        [Input("uplinkJitterMs")]
        public Input<int>? UplinkJitterMs { get; set; }

        [Input("uplinkLossPercent")]
        public Input<int>? UplinkLossPercent { get; set; }

        public NetworkProfileArgs()
        {
        }
        public static new NetworkProfileArgs Empty => new NetworkProfileArgs();
    }
}
