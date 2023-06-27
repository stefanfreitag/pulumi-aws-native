// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NetworkManager
{
    public static class GetTransitGatewayPeering
    {
        /// <summary>
        /// AWS::NetworkManager::TransitGatewayPeering Resoruce Type.
        /// </summary>
        public static Task<GetTransitGatewayPeeringResult> InvokeAsync(GetTransitGatewayPeeringArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTransitGatewayPeeringResult>("aws-native:networkmanager:getTransitGatewayPeering", args ?? new GetTransitGatewayPeeringArgs(), options.WithDefaults());

        /// <summary>
        /// AWS::NetworkManager::TransitGatewayPeering Resoruce Type.
        /// </summary>
        public static Output<GetTransitGatewayPeeringResult> Invoke(GetTransitGatewayPeeringInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTransitGatewayPeeringResult>("aws-native:networkmanager:getTransitGatewayPeering", args ?? new GetTransitGatewayPeeringInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTransitGatewayPeeringArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Id of the transit gateway peering
        /// </summary>
        [Input("peeringId", required: true)]
        public string PeeringId { get; set; } = null!;

        public GetTransitGatewayPeeringArgs()
        {
        }
        public static new GetTransitGatewayPeeringArgs Empty => new GetTransitGatewayPeeringArgs();
    }

    public sealed class GetTransitGatewayPeeringInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Id of the transit gateway peering
        /// </summary>
        [Input("peeringId", required: true)]
        public Input<string> PeeringId { get; set; } = null!;

        public GetTransitGatewayPeeringInvokeArgs()
        {
        }
        public static new GetTransitGatewayPeeringInvokeArgs Empty => new GetTransitGatewayPeeringInvokeArgs();
    }


    [OutputType]
    public sealed class GetTransitGatewayPeeringResult
    {
        /// <summary>
        /// The ARN (Amazon Resource Name) of the core network that you want to peer a transit gateway to.
        /// </summary>
        public readonly string? CoreNetworkArn;
        /// <summary>
        /// The creation time of the transit gateway peering
        /// </summary>
        public readonly string? CreatedAt;
        /// <summary>
        /// The location of the transit gateway peering
        /// </summary>
        public readonly string? EdgeLocation;
        /// <summary>
        /// Peering owner account Id
        /// </summary>
        public readonly string? OwnerAccountId;
        /// <summary>
        /// The Id of the transit gateway peering
        /// </summary>
        public readonly string? PeeringId;
        /// <summary>
        /// Peering type (TransitGatewayPeering)
        /// </summary>
        public readonly string? PeeringType;
        /// <summary>
        /// The ARN (Amazon Resource Name) of the resource that you will peer to a core network
        /// </summary>
        public readonly string? ResourceArn;
        /// <summary>
        /// The state of the transit gateway peering
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Outputs.TransitGatewayPeeringTag> Tags;
        /// <summary>
        /// The ID of the TransitGatewayPeeringAttachment
        /// </summary>
        public readonly string? TransitGatewayPeeringAttachmentId;

        [OutputConstructor]
        private GetTransitGatewayPeeringResult(
            string? coreNetworkArn,

            string? createdAt,

            string? edgeLocation,

            string? ownerAccountId,

            string? peeringId,

            string? peeringType,

            string? resourceArn,

            string? state,

            ImmutableArray<Outputs.TransitGatewayPeeringTag> tags,

            string? transitGatewayPeeringAttachmentId)
        {
            CoreNetworkArn = coreNetworkArn;
            CreatedAt = createdAt;
            EdgeLocation = edgeLocation;
            OwnerAccountId = ownerAccountId;
            PeeringId = peeringId;
            PeeringType = peeringType;
            ResourceArn = resourceArn;
            State = state;
            Tags = tags;
            TransitGatewayPeeringAttachmentId = transitGatewayPeeringAttachmentId;
        }
    }
}
