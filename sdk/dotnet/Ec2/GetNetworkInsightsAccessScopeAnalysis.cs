// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2
{
    public static class GetNetworkInsightsAccessScopeAnalysis
    {
        /// <summary>
        /// Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
        /// </summary>
        public static Task<GetNetworkInsightsAccessScopeAnalysisResult> InvokeAsync(GetNetworkInsightsAccessScopeAnalysisArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetNetworkInsightsAccessScopeAnalysisResult>("aws-native:ec2:getNetworkInsightsAccessScopeAnalysis", args ?? new GetNetworkInsightsAccessScopeAnalysisArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::EC2::NetworkInsightsAccessScopeAnalysis
        /// </summary>
        public static Output<GetNetworkInsightsAccessScopeAnalysisResult> Invoke(GetNetworkInsightsAccessScopeAnalysisInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetNetworkInsightsAccessScopeAnalysisResult>("aws-native:ec2:getNetworkInsightsAccessScopeAnalysis", args ?? new GetNetworkInsightsAccessScopeAnalysisInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetNetworkInsightsAccessScopeAnalysisArgs : global::Pulumi.InvokeArgs
    {
        [Input("networkInsightsAccessScopeAnalysisId", required: true)]
        public string NetworkInsightsAccessScopeAnalysisId { get; set; } = null!;

        public GetNetworkInsightsAccessScopeAnalysisArgs()
        {
        }
        public static new GetNetworkInsightsAccessScopeAnalysisArgs Empty => new GetNetworkInsightsAccessScopeAnalysisArgs();
    }

    public sealed class GetNetworkInsightsAccessScopeAnalysisInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("networkInsightsAccessScopeAnalysisId", required: true)]
        public Input<string> NetworkInsightsAccessScopeAnalysisId { get; set; } = null!;

        public GetNetworkInsightsAccessScopeAnalysisInvokeArgs()
        {
        }
        public static new GetNetworkInsightsAccessScopeAnalysisInvokeArgs Empty => new GetNetworkInsightsAccessScopeAnalysisInvokeArgs();
    }


    [OutputType]
    public sealed class GetNetworkInsightsAccessScopeAnalysisResult
    {
        public readonly int? AnalyzedEniCount;
        public readonly string? EndDate;
        public readonly Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisFindingsFound? FindingsFound;
        public readonly string? NetworkInsightsAccessScopeAnalysisArn;
        public readonly string? NetworkInsightsAccessScopeAnalysisId;
        public readonly string? StartDate;
        public readonly Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisStatus? Status;
        public readonly string? StatusMessage;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetNetworkInsightsAccessScopeAnalysisResult(
            int? analyzedEniCount,

            string? endDate,

            Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisFindingsFound? findingsFound,

            string? networkInsightsAccessScopeAnalysisArn,

            string? networkInsightsAccessScopeAnalysisId,

            string? startDate,

            Pulumi.AwsNative.Ec2.NetworkInsightsAccessScopeAnalysisStatus? status,

            string? statusMessage,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            AnalyzedEniCount = analyzedEniCount;
            EndDate = endDate;
            FindingsFound = findingsFound;
            NetworkInsightsAccessScopeAnalysisArn = networkInsightsAccessScopeAnalysisArn;
            NetworkInsightsAccessScopeAnalysisId = networkInsightsAccessScopeAnalysisId;
            StartDate = startDate;
            Status = status;
            StatusMessage = statusMessage;
            Tags = tags;
        }
    }
}
