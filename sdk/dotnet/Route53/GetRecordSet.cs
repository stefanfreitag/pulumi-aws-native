// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Route53
{
    public static class GetRecordSet
    {
        /// <summary>
        /// Resource Type definition for AWS::Route53::RecordSet
        /// </summary>
        public static Task<GetRecordSetResult> InvokeAsync(GetRecordSetArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetRecordSetResult>("aws-native:route53:getRecordSet", args ?? new GetRecordSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::Route53::RecordSet
        /// </summary>
        public static Output<GetRecordSetResult> Invoke(GetRecordSetInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetRecordSetResult>("aws-native:route53:getRecordSet", args ?? new GetRecordSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetRecordSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetRecordSetArgs()
        {
        }
        public static new GetRecordSetArgs Empty => new GetRecordSetArgs();
    }

    public sealed class GetRecordSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetRecordSetInvokeArgs()
        {
        }
        public static new GetRecordSetInvokeArgs Empty => new GetRecordSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetRecordSetResult
    {
        public readonly Outputs.RecordSetAliasTarget? AliasTarget;
        public readonly string? Comment;
        public readonly string? Failover;
        public readonly Outputs.RecordSetGeoLocation? GeoLocation;
        public readonly string? HealthCheckId;
        public readonly string? Id;
        public readonly bool? MultiValueAnswer;
        public readonly string? Region;
        public readonly ImmutableArray<string> ResourceRecords;
        public readonly string? SetIdentifier;
        public readonly string? TTL;
        public readonly string? Type;
        public readonly int? Weight;

        [OutputConstructor]
        private GetRecordSetResult(
            Outputs.RecordSetAliasTarget? aliasTarget,

            string? comment,

            string? failover,

            Outputs.RecordSetGeoLocation? geoLocation,

            string? healthCheckId,

            string? id,

            bool? multiValueAnswer,

            string? region,

            ImmutableArray<string> resourceRecords,

            string? setIdentifier,

            string? tTL,

            string? type,

            int? weight)
        {
            AliasTarget = aliasTarget;
            Comment = comment;
            Failover = failover;
            GeoLocation = geoLocation;
            HealthCheckId = healthCheckId;
            Id = id;
            MultiValueAnswer = multiValueAnswer;
            Region = region;
            ResourceRecords = resourceRecords;
            SetIdentifier = setIdentifier;
            TTL = tTL;
            Type = type;
            Weight = weight;
        }
    }
}
