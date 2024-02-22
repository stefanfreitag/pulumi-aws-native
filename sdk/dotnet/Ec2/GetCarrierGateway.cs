// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetCarrierGateway
    {
        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Task<GetCarrierGatewayResult> InvokeAsync(GetCarrierGatewayArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCarrierGatewayResult>("aws-native:ec2:getCarrierGateway", args ?? new GetCarrierGatewayArgs(), options.WithDefaults());

        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Output<GetCarrierGatewayResult> Invoke(GetCarrierGatewayInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCarrierGatewayResult>("aws-native:ec2:getCarrierGateway", args ?? new GetCarrierGatewayInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCarrierGatewayArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the carrier gateway.
        /// </summary>
        [Input("carrierGatewayId", required: true)]
        public string CarrierGatewayId { get; set; } = null!;

        public GetCarrierGatewayArgs()
        {
        }
        public static new GetCarrierGatewayArgs Empty => new GetCarrierGatewayArgs();
    }

    public sealed class GetCarrierGatewayInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the carrier gateway.
        /// </summary>
        [Input("carrierGatewayId", required: true)]
        public Input<string> CarrierGatewayId { get; set; } = null!;

        public GetCarrierGatewayInvokeArgs()
        {
        }
        public static new GetCarrierGatewayInvokeArgs Empty => new GetCarrierGatewayInvokeArgs();
    }


    [OutputType]
    public sealed class GetCarrierGatewayResult
    {
        /// <summary>
        /// The ID of the carrier gateway.
        /// </summary>
        public readonly string? CarrierGatewayId;
        /// <summary>
        /// The ID of the owner.
        /// </summary>
        public readonly string? OwnerId;
        /// <summary>
        /// The state of the carrier gateway.
        /// </summary>
        public readonly string? State;
        /// <summary>
        /// The tags for the carrier gateway.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetCarrierGatewayResult(
            string? carrierGatewayId,

            string? ownerId,

            string? state,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            CarrierGatewayId = carrierGatewayId;
            OwnerId = ownerId;
            State = state;
            Tags = tags;
        }
    }
}
