// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    /// <summary>
    /// Resource Type definition for AWS::EC2::CustomerGateway
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:CustomerGateway")]
    public partial class CustomerGateway : global::Pulumi.CustomResource
    {
        /// <summary>
        /// For devices that support BGP, the customer gateway's BGP ASN.
        /// </summary>
        [Output("bgpAsn")]
        public Output<int> BgpAsn { get; private set; } = null!;

        /// <summary>
        /// CustomerGateway ID generated after customer gateway is created. Each customer gateway has a unique ID.
        /// </summary>
        [Output("customerGatewayId")]
        public Output<string> CustomerGatewayId { get; private set; } = null!;

        /// <summary>
        /// A name for the customer gateway device.
        /// </summary>
        [Output("deviceName")]
        public Output<string?> DeviceName { get; private set; } = null!;

        /// <summary>
        /// The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        /// </summary>
        [Output("ipAddress")]
        public Output<string> IpAddress { get; private set; } = null!;

        /// <summary>
        /// One or more tags for the customer gateway.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.CustomerGatewayTag>> Tags { get; private set; } = null!;

        /// <summary>
        /// The type of VPN connection that this customer gateway supports.
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;


        /// <summary>
        /// Create a CustomerGateway resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public CustomerGateway(string name, CustomerGatewayArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:CustomerGateway", name, args ?? new CustomerGatewayArgs(), MakeResourceOptions(options, ""))
        {
        }

        private CustomerGateway(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:CustomerGateway", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing CustomerGateway resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static CustomerGateway Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new CustomerGateway(name, id, options);
        }
    }

    public sealed class CustomerGatewayArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// For devices that support BGP, the customer gateway's BGP ASN.
        /// </summary>
        [Input("bgpAsn", required: true)]
        public Input<int> BgpAsn { get; set; } = null!;

        /// <summary>
        /// A name for the customer gateway device.
        /// </summary>
        [Input("deviceName")]
        public Input<string>? DeviceName { get; set; }

        /// <summary>
        /// The internet-routable IP address for the customer gateway's outside interface. The address must be static.
        /// </summary>
        [Input("ipAddress", required: true)]
        public Input<string> IpAddress { get; set; } = null!;

        [Input("tags")]
        private InputList<Inputs.CustomerGatewayTagArgs>? _tags;

        /// <summary>
        /// One or more tags for the customer gateway.
        /// </summary>
        public InputList<Inputs.CustomerGatewayTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.CustomerGatewayTagArgs>());
            set => _tags = value;
        }

        /// <summary>
        /// The type of VPN connection that this customer gateway supports.
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public CustomerGatewayArgs()
        {
        }
        public static new CustomerGatewayArgs Empty => new CustomerGatewayArgs();
    }
}
