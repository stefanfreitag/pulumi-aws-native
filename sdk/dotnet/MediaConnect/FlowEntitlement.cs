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
    /// Resource schema for AWS::MediaConnect::FlowEntitlement
    /// </summary>
    [AwsNativeResourceType("aws-native:mediaconnect:FlowEntitlement")]
    public partial class FlowEntitlement : Pulumi.CustomResource
    {
        /// <summary>
        /// Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
        /// </summary>
        [Output("dataTransferSubscriberFeePercent")]
        public Output<int?> DataTransferSubscriberFeePercent { get; private set; } = null!;

        /// <summary>
        /// A description of the entitlement.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// The type of encryption that will be used on the output that is associated with this entitlement.
        /// </summary>
        [Output("encryption")]
        public Output<Outputs.FlowEntitlementEncryption?> Encryption { get; private set; } = null!;

        /// <summary>
        /// The ARN of the entitlement.
        /// </summary>
        [Output("entitlementArn")]
        public Output<string> EntitlementArn { get; private set; } = null!;

        /// <summary>
        ///  An indication of whether the entitlement is enabled.
        /// </summary>
        [Output("entitlementStatus")]
        public Output<Pulumi.AwsNative.MediaConnect.FlowEntitlementEntitlementStatus?> EntitlementStatus { get; private set; } = null!;

        /// <summary>
        /// The ARN of the flow.
        /// </summary>
        [Output("flowArn")]
        public Output<string> FlowArn { get; private set; } = null!;

        /// <summary>
        /// The name of the entitlement.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
        /// </summary>
        [Output("subscribers")]
        public Output<ImmutableArray<string>> Subscribers { get; private set; } = null!;


        /// <summary>
        /// Create a FlowEntitlement resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public FlowEntitlement(string name, FlowEntitlementArgs args, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:FlowEntitlement", name, args ?? new FlowEntitlementArgs(), MakeResourceOptions(options, ""))
        {
        }

        private FlowEntitlement(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:mediaconnect:FlowEntitlement", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing FlowEntitlement resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static FlowEntitlement Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new FlowEntitlement(name, id, options);
        }
    }

    public sealed class FlowEntitlementArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Percentage from 0-100 of the data transfer cost to be billed to the subscriber.
        /// </summary>
        [Input("dataTransferSubscriberFeePercent")]
        public Input<int>? DataTransferSubscriberFeePercent { get; set; }

        /// <summary>
        /// A description of the entitlement.
        /// </summary>
        [Input("description", required: true)]
        public Input<string> Description { get; set; } = null!;

        /// <summary>
        /// The type of encryption that will be used on the output that is associated with this entitlement.
        /// </summary>
        [Input("encryption")]
        public Input<Inputs.FlowEntitlementEncryptionArgs>? Encryption { get; set; }

        /// <summary>
        ///  An indication of whether the entitlement is enabled.
        /// </summary>
        [Input("entitlementStatus")]
        public Input<Pulumi.AwsNative.MediaConnect.FlowEntitlementEntitlementStatus>? EntitlementStatus { get; set; }

        /// <summary>
        /// The ARN of the flow.
        /// </summary>
        [Input("flowArn", required: true)]
        public Input<string> FlowArn { get; set; } = null!;

        /// <summary>
        /// The name of the entitlement.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("subscribers", required: true)]
        private InputList<string>? _subscribers;

        /// <summary>
        /// The AWS account IDs that you want to share your content with. The receiving accounts (subscribers) will be allowed to create their own flow using your content as the source.
        /// </summary>
        public InputList<string> Subscribers
        {
            get => _subscribers ?? (_subscribers = new InputList<string>());
            set => _subscribers = value;
        }

        public FlowEntitlementArgs()
        {
        }
    }
}
