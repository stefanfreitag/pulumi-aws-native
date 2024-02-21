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
    /// Specifies a virtual private cloud (VPC).
    ///  You can optionally request an IPv6 CIDR block for the VPC. You can request an Amazon-provided IPv6 CIDR block from Amazon's pool of IPv6 addresses, or an IPv6 CIDR block from an IPv6 address pool that you provisioned through bring your own IP addresses (BYOIP).
    ///  For more information, see [Virtual private clouds (VPC)](https://docs.aws.amazon.com/vpc/latest/userguide/configure-your-vpc.html) in the *Amazon VPC User Guide*.
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:Vpc")]
    public partial class Vpc : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
        ///  You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        /// </summary>
        [Output("cidrBlock")]
        public Output<string?> CidrBlock { get; private set; } = null!;

        [Output("cidrBlockAssociations")]
        public Output<ImmutableArray<string>> CidrBlockAssociations { get; private set; } = null!;

        [Output("defaultNetworkAcl")]
        public Output<string> DefaultNetworkAcl { get; private set; } = null!;

        [Output("defaultSecurityGroup")]
        public Output<string> DefaultSecurityGroup { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        ///  You can only enable DNS hostnames if you've enabled DNS support.
        /// </summary>
        [Output("enableDnsHostnames")]
        public Output<bool?> EnableDnsHostnames { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        /// </summary>
        [Output("enableDnsSupport")]
        public Output<bool?> EnableDnsSupport { get; private set; } = null!;

        /// <summary>
        /// The allowed tenancy of instances launched into the VPC.
        ///   +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
        ///   +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
        ///   
        ///  Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        /// </summary>
        [Output("instanceTenancy")]
        public Output<string?> InstanceTenancy { get; private set; } = null!;

        /// <summary>
        /// The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        ///  You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        /// </summary>
        [Output("ipv4IpamPoolId")]
        public Output<string?> Ipv4IpamPoolId { get; private set; } = null!;

        /// <summary>
        /// The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        /// </summary>
        [Output("ipv4NetmaskLength")]
        public Output<int?> Ipv4NetmaskLength { get; private set; } = null!;

        [Output("ipv6CidrBlocks")]
        public Output<ImmutableArray<string>> Ipv6CidrBlocks { get; private set; } = null!;

        /// <summary>
        /// The tags for the VPC.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<Outputs.VpcTag>> Tags { get; private set; } = null!;

        [Output("vpcId")]
        public Output<string> VpcId { get; private set; } = null!;


        /// <summary>
        /// Create a Vpc resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Vpc(string name, VpcArgs? args = null, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Vpc", name, args ?? new VpcArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Vpc(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:Vpc", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "cidrBlock",
                    "ipv4IpamPoolId",
                    "ipv4NetmaskLength",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Vpc resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Vpc Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Vpc(name, id, options);
        }
    }

    public sealed class VpcArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IPv4 network range for the VPC, in CIDR notation. For example, ``10.0.0.0/16``. We modify the specified CIDR block to its canonical form; for example, if you specify ``100.68.0.18/18``, we modify it to ``100.68.0.0/18``.
        ///  You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        /// </summary>
        [Input("cidrBlock")]
        public Input<string>? CidrBlock { get; set; }

        /// <summary>
        /// Indicates whether the instances launched in the VPC get DNS hostnames. If enabled, instances in the VPC get DNS hostnames; otherwise, they do not. Disabled by default for nondefault VPCs. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        ///  You can only enable DNS hostnames if you've enabled DNS support.
        /// </summary>
        [Input("enableDnsHostnames")]
        public Input<bool>? EnableDnsHostnames { get; set; }

        /// <summary>
        /// Indicates whether the DNS resolution is supported for the VPC. If enabled, queries to the Amazon provided DNS server at the 169.254.169.253 IP address, or the reserved IP address at the base of the VPC network range "plus two" succeed. If disabled, the Amazon provided DNS service in the VPC that resolves public DNS hostnames to IP addresses is not enabled. Enabled by default. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).
        /// </summary>
        [Input("enableDnsSupport")]
        public Input<bool>? EnableDnsSupport { get; set; }

        /// <summary>
        /// The allowed tenancy of instances launched into the VPC.
        ///   +  ``default``: An instance launched into the VPC runs on shared hardware by default, unless you explicitly specify a different tenancy during instance launch.
        ///   +  ``dedicated``: An instance launched into the VPC runs on dedicated hardware by default, unless you explicitly specify a tenancy of ``host`` during instance launch. You cannot specify a tenancy of ``default`` during instance launch.
        ///   
        ///  Updating ``InstanceTenancy`` requires no replacement only if you are updating its value from ``dedicated`` to ``default``. Updating ``InstanceTenancy`` from ``default`` to ``dedicated`` requires replacement.
        /// </summary>
        [Input("instanceTenancy")]
        public Input<string>? InstanceTenancy { get; set; }

        /// <summary>
        /// The ID of an IPv4 IPAM pool you want to use for allocating this VPC's CIDR. For more information, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        ///  You must specify either``CidrBlock`` or ``Ipv4IpamPoolId``.
        /// </summary>
        [Input("ipv4IpamPoolId")]
        public Input<string>? Ipv4IpamPoolId { get; set; }

        /// <summary>
        /// The netmask length of the IPv4 CIDR you want to allocate to this VPC from an Amazon VPC IP Address Manager (IPAM) pool. For more information about IPAM, see [What is IPAM?](https://docs.aws.amazon.com//vpc/latest/ipam/what-is-it-ipam.html) in the *Amazon VPC IPAM User Guide*.
        /// </summary>
        [Input("ipv4NetmaskLength")]
        public Input<int>? Ipv4NetmaskLength { get; set; }

        [Input("tags")]
        private InputList<Inputs.VpcTagArgs>? _tags;

        /// <summary>
        /// The tags for the VPC.
        /// </summary>
        public InputList<Inputs.VpcTagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.VpcTagArgs>());
            set => _tags = value;
        }

        public VpcArgs()
        {
        }
        public static new VpcArgs Empty => new VpcArgs();
    }
}
