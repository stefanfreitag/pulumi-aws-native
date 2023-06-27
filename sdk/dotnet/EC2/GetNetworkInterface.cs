// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetNetworkInterface
    {
        /// <summary>
        /// The AWS::EC2::NetworkInterface resource creates network interface
        /// </summary>
        public static Task<GetNetworkInterfaceResult> InvokeAsync(GetNetworkInterfaceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkInterfaceResult>("aws-native:ec2:getNetworkInterface", args ?? new GetNetworkInterfaceArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::EC2::NetworkInterface resource creates network interface
        /// </summary>
        public static Output<GetNetworkInterfaceResult> Invoke(GetNetworkInterfaceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkInterfaceResult>("aws-native:ec2:getNetworkInterface", args ?? new GetNetworkInterfaceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkInterfaceArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Network interface id.
        /// </summary>
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetNetworkInterfaceArgs()
        {
        }
        public static new GetNetworkInterfaceArgs Empty => new GetNetworkInterfaceArgs();
    }

    public sealed class GetNetworkInterfaceInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Network interface id.
        /// </summary>
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetNetworkInterfaceInvokeArgs()
        {
        }
        public static new GetNetworkInterfaceInvokeArgs Empty => new GetNetworkInterfaceInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkInterfaceResult
    {
        /// <summary>
        /// A description for the network interface.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// If you have instances or ENIs that rely on the IPv6 address not changing, to avoid disrupting traffic to instances or ENIs, you can enable a primary IPv6 address. Enable this option to automatically assign an IPv6 associated with the ENI attached to your instance to be the primary IPv6 address. When you enable an IPv6 address to be a primary IPv6, you cannot disable it. Traffic will be routed to the primary IPv6 address until the instance is terminated or the ENI is detached. If you have multiple IPv6 addresses associated with an ENI and you enable a primary IPv6 address, the first IPv6 address associated with the ENI becomes the primary IPv6 address.
        /// </summary>
        public readonly bool? EnablePrimaryIpv6;
        /// <summary>
        /// A list of security group IDs associated with this network interface.
        /// </summary>
        public readonly ImmutableArray<string> GroupSet;
        /// <summary>
        /// Network interface id.
        /// </summary>
        public readonly string? Id;
        /// <summary>
        /// The number of IPv6 addresses to assign to a network interface. Amazon EC2 automatically selects the IPv6 addresses from the subnet range. To specify specific IPv6 addresses, use the Ipv6Addresses property and don't specify this property.
        /// </summary>
        public readonly int? Ipv6AddressCount;
        /// <summary>
        /// One or more specific IPv6 addresses from the IPv6 CIDR block range of your subnet to associate with the network interface. If you're specifying a number of IPv6 addresses, use the Ipv6AddressCount property and don't specify this property.
        /// </summary>
        public readonly ImmutableArray<Outputs.NetworkInterfaceInstanceIpv6Address> Ipv6Addresses;
        /// <summary>
        /// Returns the primary private IP address of the network interface.
        /// </summary>
        public readonly string? PrimaryPrivateIpAddress;
        /// <summary>
        /// Assigns a list of private IP addresses to the network interface. You can specify a primary private IP address by setting the value of the Primary property to true in the PrivateIpAddressSpecification property. If you want EC2 to automatically assign private IP addresses, use the SecondaryPrivateIpAddressCount property and do not specify this property.
        /// </summary>
        public readonly ImmutableArray<Outputs.NetworkInterfacePrivateIpAddressSpecification> PrivateIpAddresses;
        /// <summary>
        /// The number of secondary private IPv4 addresses to assign to a network interface. When you specify a number of secondary IPv4 addresses, Amazon EC2 selects these IP addresses within the subnet's IPv4 CIDR range. You can't specify this option and specify more than one private IP address using privateIpAddresses
        /// </summary>
        public readonly int? SecondaryPrivateIpAddressCount;
        /// <summary>
        /// Returns the secondary private IP addresses of the network interface.
        /// </summary>
        public readonly ImmutableArray<string> SecondaryPrivateIpAddresses;
        /// <summary>
        /// Indicates whether traffic to or from the instance is validated.
        /// </summary>
        public readonly bool? SourceDestCheck;
        /// <summary>
        /// An arbitrary set of tags (key-value pairs) for this network interface.
        /// </summary>
        public readonly ImmutableArray<Outputs.NetworkInterfaceTag> Tags;

        [OutputConstructor]
        private GetNetworkInterfaceResult(
            string? description,

            bool? enablePrimaryIpv6,

            ImmutableArray<string> groupSet,

            string? id,

            int? ipv6AddressCount,

            ImmutableArray<Outputs.NetworkInterfaceInstanceIpv6Address> ipv6Addresses,

            string? primaryPrivateIpAddress,

            ImmutableArray<Outputs.NetworkInterfacePrivateIpAddressSpecification> privateIpAddresses,

            int? secondaryPrivateIpAddressCount,

            ImmutableArray<string> secondaryPrivateIpAddresses,

            bool? sourceDestCheck,

            ImmutableArray<Outputs.NetworkInterfaceTag> tags)
        {
            Description = description;
            EnablePrimaryIpv6 = enablePrimaryIpv6;
            GroupSet = groupSet;
            Id = id;
            Ipv6AddressCount = ipv6AddressCount;
            Ipv6Addresses = ipv6Addresses;
            PrimaryPrivateIpAddress = primaryPrivateIpAddress;
            PrivateIpAddresses = privateIpAddresses;
            SecondaryPrivateIpAddressCount = secondaryPrivateIpAddressCount;
            SecondaryPrivateIpAddresses = secondaryPrivateIpAddresses;
            SourceDestCheck = sourceDestCheck;
            Tags = tags;
        }
    }
}
