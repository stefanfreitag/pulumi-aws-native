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
    /// Resource Type definition for AWS::EC2::Route
    /// </summary>
    [Obsolete(@"Route is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:ec2:Route")]
    public partial class Route : global::Pulumi.CustomResource
    {
        [Output("carrierGatewayId")]
        public Output<string?> CarrierGatewayId { get; private set; } = null!;

        [Output("destinationCidrBlock")]
        public Output<string?> DestinationCidrBlock { get; private set; } = null!;

        [Output("destinationIpv6CidrBlock")]
        public Output<string?> DestinationIpv6CidrBlock { get; private set; } = null!;

        [Output("egressOnlyInternetGatewayId")]
        public Output<string?> EgressOnlyInternetGatewayId { get; private set; } = null!;

        [Output("gatewayId")]
        public Output<string?> GatewayId { get; private set; } = null!;

        [Output("instanceId")]
        public Output<string?> InstanceId { get; private set; } = null!;

        [Output("localGatewayId")]
        public Output<string?> LocalGatewayId { get; private set; } = null!;

        [Output("natGatewayId")]
        public Output<string?> NatGatewayId { get; private set; } = null!;

        [Output("networkInterfaceId")]
        public Output<string?> NetworkInterfaceId { get; private set; } = null!;

        [Output("routeTableId")]
        public Output<string> RouteTableId { get; private set; } = null!;

        [Output("transitGatewayId")]
        public Output<string?> TransitGatewayId { get; private set; } = null!;

        [Output("vpcEndpointId")]
        public Output<string?> VpcEndpointId { get; private set; } = null!;

        [Output("vpcPeeringConnectionId")]
        public Output<string?> VpcPeeringConnectionId { get; private set; } = null!;


        /// <summary>
        /// Create a Route resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Route(string name, RouteArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Route", name, args ?? new RouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Route(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Route", name, null, MakeResourceOptions(options, id))
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
        /// Get an existing Route resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Route Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Route(name, id, options);
        }
    }

    public sealed class RouteArgs : global::Pulumi.ResourceArgs
    {
        [Input("carrierGatewayId")]
        public Input<string>? CarrierGatewayId { get; set; }

        [Input("destinationCidrBlock")]
        public Input<string>? DestinationCidrBlock { get; set; }

        [Input("destinationIpv6CidrBlock")]
        public Input<string>? DestinationIpv6CidrBlock { get; set; }

        [Input("egressOnlyInternetGatewayId")]
        public Input<string>? EgressOnlyInternetGatewayId { get; set; }

        [Input("gatewayId")]
        public Input<string>? GatewayId { get; set; }

        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("localGatewayId")]
        public Input<string>? LocalGatewayId { get; set; }

        [Input("natGatewayId")]
        public Input<string>? NatGatewayId { get; set; }

        [Input("networkInterfaceId")]
        public Input<string>? NetworkInterfaceId { get; set; }

        [Input("routeTableId", required: true)]
        public Input<string> RouteTableId { get; set; } = null!;

        [Input("transitGatewayId")]
        public Input<string>? TransitGatewayId { get; set; }

        [Input("vpcEndpointId")]
        public Input<string>? VpcEndpointId { get; set; }

        [Input("vpcPeeringConnectionId")]
        public Input<string>? VpcPeeringConnectionId { get; set; }

        public RouteArgs()
        {
        }
        public static new RouteArgs Empty => new RouteArgs();
    }
}
