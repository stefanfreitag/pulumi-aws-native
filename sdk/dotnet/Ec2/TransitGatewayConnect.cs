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
    /// The AWS::EC2::TransitGatewayConnect type
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:TransitGatewayConnect")]
    public partial class TransitGatewayConnect : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The creation time.
        /// </summary>
        [Output("creationTime")]
        public Output<string> CreationTime { get; private set; } = null!;

        /// <summary>
        /// The Connect attachment options.
        /// </summary>
        [Output("options")]
        public Output<Outputs.TransitGatewayConnectOptions> Options { get; private set; } = null!;

        /// <summary>
        /// The state of the attachment.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The tags for the attachment.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The ID of the Connect attachment.
        /// </summary>
        [Output("transitGatewayAttachmentId")]
        public Output<string> TransitGatewayAttachmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the transit gateway.
        /// </summary>
        [Output("transitGatewayId")]
        public Output<string> TransitGatewayId { get; private set; } = null!;

        /// <summary>
        /// The ID of the attachment from which the Connect attachment was created.
        /// </summary>
        [Output("transportTransitGatewayAttachmentId")]
        public Output<string> TransportTransitGatewayAttachmentId { get; private set; } = null!;


        /// <summary>
        /// Create a TransitGatewayConnect resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public TransitGatewayConnect(string name, TransitGatewayConnectArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:TransitGatewayConnect", name, args ?? new TransitGatewayConnectArgs(), MakeResourceOptions(options, ""))
        {
        }

        private TransitGatewayConnect(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:TransitGatewayConnect", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "options",
                    "transportTransitGatewayAttachmentId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing TransitGatewayConnect resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static TransitGatewayConnect Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new TransitGatewayConnect(name, id, options);
        }
    }

    public sealed class TransitGatewayConnectArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The Connect attachment options.
        /// </summary>
        [Input("options", required: true)]
        public Input<Inputs.TransitGatewayConnectOptionsArgs> Options { get; set; } = null!;

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;

        /// <summary>
        /// The tags for the attachment.
        /// </summary>
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The ID of the attachment from which the Connect attachment was created.
        /// </summary>
        [Input("transportTransitGatewayAttachmentId", required: true)]
        public Input<string> TransportTransitGatewayAttachmentId { get; set; } = null!;

        public TransitGatewayConnectArgs()
        {
        }
        public static new TransitGatewayConnectArgs Empty => new TransitGatewayConnectArgs();
    }
}
