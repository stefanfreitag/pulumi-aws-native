// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2.Outputs
{

    [OutputType]
    public sealed class SecurityGroupIngress
    {
        public readonly string? CidrIp;
        public readonly string? CidrIpv6;
        public readonly string? Description;
        public readonly int? FromPort;
        public readonly string IpProtocol;
        public readonly string? SourcePrefixListId;
        public readonly string? SourceSecurityGroupId;
        public readonly string? SourceSecurityGroupName;
        public readonly string? SourceSecurityGroupOwnerId;
        public readonly int? ToPort;

        [OutputConstructor]
        private SecurityGroupIngress(
            string? cidrIp,

            string? cidrIpv6,

            string? description,

            int? fromPort,

            string ipProtocol,

            string? sourcePrefixListId,

            string? sourceSecurityGroupId,

            string? sourceSecurityGroupName,

            string? sourceSecurityGroupOwnerId,

            int? toPort)
        {
            CidrIp = cidrIp;
            CidrIpv6 = cidrIpv6;
            Description = description;
            FromPort = fromPort;
            IpProtocol = ipProtocol;
            SourcePrefixListId = sourcePrefixListId;
            SourceSecurityGroupId = sourceSecurityGroupId;
            SourceSecurityGroupName = sourceSecurityGroupName;
            SourceSecurityGroupOwnerId = sourceSecurityGroupOwnerId;
            ToPort = toPort;
        }
    }
}
