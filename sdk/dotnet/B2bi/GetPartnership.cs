// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.B2bi
{
    public static class GetPartnership
    {
        /// <summary>
        /// Definition of AWS::B2BI::Partnership Resource Type
        /// </summary>
        public static Task<GetPartnershipResult> InvokeAsync(GetPartnershipArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPartnershipResult>("aws-native:b2bi:getPartnership", args ?? new GetPartnershipArgs(), options.WithDefaults());

        /// <summary>
        /// Definition of AWS::B2BI::Partnership Resource Type
        /// </summary>
        public static Output<GetPartnershipResult> Invoke(GetPartnershipInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPartnershipResult>("aws-native:b2bi:getPartnership", args ?? new GetPartnershipInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPartnershipArgs : global::Pulumi.InvokeArgs
    {
        [Input("partnershipId", required: true)]
        public string PartnershipId { get; set; } = null!;

        public GetPartnershipArgs()
        {
        }
        public static new GetPartnershipArgs Empty => new GetPartnershipArgs();
    }

    public sealed class GetPartnershipInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("partnershipId", required: true)]
        public Input<string> PartnershipId { get; set; } = null!;

        public GetPartnershipInvokeArgs()
        {
        }
        public static new GetPartnershipInvokeArgs Empty => new GetPartnershipInvokeArgs();
    }


    [OutputType]
    public sealed class GetPartnershipResult
    {
        public readonly ImmutableArray<string> Capabilities;
        public readonly string? CreatedAt;
        public readonly string? ModifiedAt;
        public readonly string? Name;
        public readonly string? PartnershipArn;
        public readonly string? PartnershipId;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        public readonly string? TradingPartnerId;

        [OutputConstructor]
        private GetPartnershipResult(
            ImmutableArray<string> capabilities,

            string? createdAt,

            string? modifiedAt,

            string? name,

            string? partnershipArn,

            string? partnershipId,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            string? tradingPartnerId)
        {
            Capabilities = capabilities;
            CreatedAt = createdAt;
            ModifiedAt = modifiedAt;
            Name = name;
            PartnershipArn = partnershipArn;
            PartnershipId = partnershipId;
            Tags = tags;
            TradingPartnerId = tradingPartnerId;
        }
    }
}
