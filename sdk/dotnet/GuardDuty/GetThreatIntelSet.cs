// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GuardDuty
{
    public static class GetThreatIntelSet
    {
        /// <summary>
        /// Resource Type definition for AWS::GuardDuty::ThreatIntelSet
        /// </summary>
        public static Task<GetThreatIntelSetResult> InvokeAsync(GetThreatIntelSetArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetThreatIntelSetResult>("aws-native:guardduty:getThreatIntelSet", args ?? new GetThreatIntelSetArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::GuardDuty::ThreatIntelSet
        /// </summary>
        public static Output<GetThreatIntelSetResult> Invoke(GetThreatIntelSetInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetThreatIntelSetResult>("aws-native:guardduty:getThreatIntelSet", args ?? new GetThreatIntelSetInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetThreatIntelSetArgs : global::Pulumi.InvokeArgs
    {
        [Input("detectorId", required: true)]
        public string DetectorId { get; set; } = null!;

        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetThreatIntelSetArgs()
        {
        }
        public static new GetThreatIntelSetArgs Empty => new GetThreatIntelSetArgs();
    }

    public sealed class GetThreatIntelSetInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("detectorId", required: true)]
        public Input<string> DetectorId { get; set; } = null!;

        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetThreatIntelSetInvokeArgs()
        {
        }
        public static new GetThreatIntelSetInvokeArgs Empty => new GetThreatIntelSetInvokeArgs();
    }


    [OutputType]
    public sealed class GetThreatIntelSetResult
    {
        public readonly string? Id;
        public readonly string? Location;
        public readonly string? Name;
        public readonly ImmutableArray<Outputs.ThreatIntelSetTagItem> Tags;

        [OutputConstructor]
        private GetThreatIntelSetResult(
            string? id,

            string? location,

            string? name,

            ImmutableArray<Outputs.ThreatIntelSetTagItem> tags)
        {
            Id = id;
            Location = location;
            Name = name;
            Tags = tags;
        }
    }
}
