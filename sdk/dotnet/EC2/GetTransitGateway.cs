// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EC2
{
    public static class GetTransitGateway
    {
        /// <summary>
        /// Resource Type definition for AWS::EC2::TransitGateway
        /// </summary>
        public static Task<GetTransitGatewayResult> InvokeAsync(GetTransitGatewayArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTransitGatewayResult>("aws-native:ec2:getTransitGateway", args ?? new GetTransitGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EC2::TransitGateway
        /// </summary>
        public static Output<GetTransitGatewayResult> Invoke(GetTransitGatewayInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetTransitGatewayResult>("aws-native:ec2:getTransitGateway", args ?? new GetTransitGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTransitGatewayArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetTransitGatewayArgs()
        {
        }
        public static new GetTransitGatewayArgs Empty => new GetTransitGatewayArgs();
    }

    public sealed class GetTransitGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetTransitGatewayInvokeArgs()
        {
        }
        public static new GetTransitGatewayInvokeArgs Empty => new GetTransitGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetTransitGatewayResult
    {
        public readonly string? AssociationDefaultRouteTableId;
        public readonly string? AutoAcceptSharedAttachments;
        public readonly string? DefaultRouteTableAssociation;
        public readonly string? DefaultRouteTablePropagation;
        public readonly string? Description;
        public readonly string? DnsSupport;
        public readonly string? Id;
        public readonly string? PropagationDefaultRouteTableId;
        public readonly ImmutableArray<Outputs.TransitGatewayTag> Tags;
        public readonly ImmutableArray<string> TransitGatewayCidrBlocks;
        public readonly string? VpnEcmpSupport;

        [OutputConstructor]
        private GetTransitGatewayResult(
            string? associationDefaultRouteTableId,

            string? autoAcceptSharedAttachments,

            string? defaultRouteTableAssociation,

            string? defaultRouteTablePropagation,

            string? description,

            string? dnsSupport,

            string? id,

            string? propagationDefaultRouteTableId,

            ImmutableArray<Outputs.TransitGatewayTag> tags,

            ImmutableArray<string> transitGatewayCidrBlocks,

            string? vpnEcmpSupport)
        {
            AssociationDefaultRouteTableId = associationDefaultRouteTableId;
            AutoAcceptSharedAttachments = autoAcceptSharedAttachments;
            DefaultRouteTableAssociation = defaultRouteTableAssociation;
            DefaultRouteTablePropagation = defaultRouteTablePropagation;
            Description = description;
            DnsSupport = dnsSupport;
            Id = id;
            PropagationDefaultRouteTableId = propagationDefaultRouteTableId;
            Tags = tags;
            TransitGatewayCidrBlocks = transitGatewayCidrBlocks;
            VpnEcmpSupport = vpnEcmpSupport;
        }
    }
}
