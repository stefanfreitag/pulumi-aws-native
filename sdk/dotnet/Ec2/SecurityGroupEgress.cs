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
    /// Resource Type definition for AWS::EC2::SecurityGroupEgress
    /// </summary>
    [AwsNativeResourceType("aws-native:ec2:SecurityGroupEgress")]
    public partial class SecurityGroupEgress : global::Pulumi.CustomResource
    {
        /// <summary>
        /// The IPv4 ranges
        /// </summary>
        [Output("cidrIp")]
        public Output<string?> CidrIp { get; private set; } = null!;

        /// <summary>
        /// [VPC only] The IPv6 ranges
        /// </summary>
        [Output("cidrIpv6")]
        public Output<string?> CidrIpv6 { get; private set; } = null!;

        /// <summary>
        /// Resource Type definition for an egress (outbound) security group rule.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// [EC2-VPC only] The ID of a prefix list.
        /// </summary>
        [Output("destinationPrefixListId")]
        public Output<string?> DestinationPrefixListId { get; private set; } = null!;

        /// <summary>
        /// You must specify a destination security group (DestinationPrefixListId or DestinationSecurityGroupId) or a CIDR range (CidrIp or CidrIpv6).
        /// </summary>
        [Output("destinationSecurityGroupId")]
        public Output<string?> DestinationSecurityGroupId { get; private set; } = null!;

        /// <summary>
        /// The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        /// </summary>
        [Output("fromPort")]
        public Output<int?> FromPort { get; private set; } = null!;

        /// <summary>
        /// The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        /// </summary>
        [Output("groupId")]
        public Output<string> GroupId { get; private set; } = null!;

        /// <summary>
        /// [VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or icmpv6 allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For icmpv6, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        /// </summary>
        [Output("ipProtocol")]
        public Output<string> IpProtocol { get; private set; } = null!;

        /// <summary>
        /// The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        /// </summary>
        [Output("toPort")]
        public Output<int?> ToPort { get; private set; } = null!;


        /// <summary>
        /// Create a SecurityGroupEgress resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public SecurityGroupEgress(string name, SecurityGroupEgressArgs args, CustomResourceOptions? options = null)
            : base("aws-native:ec2:SecurityGroupEgress", name, args ?? new SecurityGroupEgressArgs(), MakeResourceOptions(options, ""))
        {
        }

        private SecurityGroupEgress(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:ec2:SecurityGroupEgress", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "cidrIp",
                    "cidrIpv6",
                    "destinationPrefixListId",
                    "destinationSecurityGroupId",
                    "fromPort",
                    "groupId",
                    "ipProtocol",
                    "toPort",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing SecurityGroupEgress resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static SecurityGroupEgress Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new SecurityGroupEgress(name, id, options);
        }
    }

    public sealed class SecurityGroupEgressArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The IPv4 ranges
        /// </summary>
        [Input("cidrIp")]
        public Input<string>? CidrIp { get; set; }

        /// <summary>
        /// [VPC only] The IPv6 ranges
        /// </summary>
        [Input("cidrIpv6")]
        public Input<string>? CidrIpv6 { get; set; }

        /// <summary>
        /// Resource Type definition for an egress (outbound) security group rule.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// [EC2-VPC only] The ID of a prefix list.
        /// </summary>
        [Input("destinationPrefixListId")]
        public Input<string>? DestinationPrefixListId { get; set; }

        /// <summary>
        /// You must specify a destination security group (DestinationPrefixListId or DestinationSecurityGroupId) or a CIDR range (CidrIp or CidrIpv6).
        /// </summary>
        [Input("destinationSecurityGroupId")]
        public Input<string>? DestinationSecurityGroupId { get; set; }

        /// <summary>
        /// The start of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 type number. A value of -1 indicates all ICMP/ICMPv6 types. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        /// </summary>
        [Input("fromPort")]
        public Input<int>? FromPort { get; set; }

        /// <summary>
        /// The ID of the security group. You must specify either the security group ID or the security group name in the request. For security groups in a nondefault VPC, you must specify the security group ID.
        /// </summary>
        [Input("groupId", required: true)]
        public Input<string> GroupId { get; set; } = null!;

        /// <summary>
        /// [VPC only] Use -1 to specify all protocols. When authorizing security group rules, specifying -1 or a protocol number other than tcp, udp, icmp, or icmpv6 allows traffic on all ports, regardless of any port range you specify. For tcp, udp, and icmp, you must specify a port range. For icmpv6, the port range is optional; if you omit the port range, traffic for all types and codes is allowed.
        /// </summary>
        [Input("ipProtocol", required: true)]
        public Input<string> IpProtocol { get; set; } = null!;

        /// <summary>
        /// The end of port range for the TCP and UDP protocols, or an ICMP/ICMPv6 code. A value of -1 indicates all ICMP/ICMPv6 codes. If you specify all ICMP/ICMPv6 types, you must specify all codes.
        /// </summary>
        [Input("toPort")]
        public Input<int>? ToPort { get; set; }

        public SecurityGroupEgressArgs()
        {
        }
        public static new SecurityGroupEgressArgs Empty => new SecurityGroupEgressArgs();
    }
}
