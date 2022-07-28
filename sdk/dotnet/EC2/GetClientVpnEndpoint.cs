// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetClientVpnEndpoint
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::ClientVpnEndpoint
        /// </summary>
        public static Task<GetClientVpnEndpointResult> InvokeAsync(GetClientVpnEndpointArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetClientVpnEndpointResult>("aws-native:ec2:getClientVpnEndpoint", args ?? new GetClientVpnEndpointArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::ClientVpnEndpoint
        /// </summary>
        public static Output<GetClientVpnEndpointResult> Invoke(GetClientVpnEndpointInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetClientVpnEndpointResult>("aws-native:ec2:getClientVpnEndpoint", args ?? new GetClientVpnEndpointInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetClientVpnEndpointArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetClientVpnEndpointArgs()
        {
        }
        public static new GetClientVpnEndpointArgs Empty => new GetClientVpnEndpointArgs();
    }

    public sealed class GetClientVpnEndpointInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetClientVpnEndpointInvokeArgs()
        {
        }
        public static new GetClientVpnEndpointInvokeArgs Empty => new GetClientVpnEndpointInvokeArgs();
    }


    [OutputType]
    public sealed class GetClientVpnEndpointResult
    {
        public readonly Outputs.ClientVpnEndpointClientConnectOptions? ClientConnectOptions;
        public readonly Outputs.ClientVpnEndpointClientLoginBannerOptions? ClientLoginBannerOptions;
        public readonly Outputs.ClientVpnEndpointConnectionLogOptions? ConnectionLogOptions;
        public readonly string? Description;
        public readonly ImmutableArray<string> DnsServers;
        public readonly string? Id;
        public readonly ImmutableArray<string> SecurityGroupIds;
        public readonly string? SelfServicePortal;
        public readonly string? ServerCertificateArn;
        public readonly int? SessionTimeoutHours;
        public readonly bool? SplitTunnel;
        public readonly string? VpcId;
        public readonly int? VpnPort;

        [OutputConstructor]
        private GetClientVpnEndpointResult(
            Outputs.ClientVpnEndpointClientConnectOptions? clientConnectOptions,

            Outputs.ClientVpnEndpointClientLoginBannerOptions? clientLoginBannerOptions,

            Outputs.ClientVpnEndpointConnectionLogOptions? connectionLogOptions,

            string? description,

            ImmutableArray<string> dnsServers,

            string? id,

            ImmutableArray<string> securityGroupIds,

            string? selfServicePortal,

            string? serverCertificateArn,

            int? sessionTimeoutHours,

            bool? splitTunnel,

            string? vpcId,

            int? vpnPort)
        {
            ClientConnectOptions = clientConnectOptions;
            ClientLoginBannerOptions = clientLoginBannerOptions;
            ConnectionLogOptions = connectionLogOptions;
            Description = description;
            DnsServers = dnsServers;
            Id = id;
            SecurityGroupIds = securityGroupIds;
            SelfServicePortal = selfServicePortal;
            ServerCertificateArn = serverCertificateArn;
            SessionTimeoutHours = sessionTimeoutHours;
            SplitTunnel = splitTunnel;
            VpcId = vpcId;
            VpnPort = vpnPort;
        }
    }
}
