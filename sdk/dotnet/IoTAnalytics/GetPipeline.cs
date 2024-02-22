// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics
{
    public static class GetPipeline
    {
        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Pipeline
        /// </summary>
        public static Task<GetPipelineResult> InvokeAsync(GetPipelineArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPipelineResult>("aws-native:iotanalytics:getPipeline", args ?? new GetPipelineArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::IoTAnalytics::Pipeline
        /// </summary>
        public static Output<GetPipelineResult> Invoke(GetPipelineInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPipelineResult>("aws-native:iotanalytics:getPipeline", args ?? new GetPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPipelineArgs : global::Pulumi.InvokeArgs
    {
        [Input("pipelineName", required: true)]
        public string PipelineName { get; set; } = null!;

        public GetPipelineArgs()
        {
        }
        public static new GetPipelineArgs Empty => new GetPipelineArgs();
    }

    public sealed class GetPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("pipelineName", required: true)]
        public Input<string> PipelineName { get; set; } = null!;

        public GetPipelineInvokeArgs()
        {
        }
        public static new GetPipelineInvokeArgs Empty => new GetPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPipelineResult
    {
        public readonly string? Id;
        public readonly ImmutableArray<Outputs.PipelineActivity> PipelineActivities;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetPipelineResult(
            string? id,

            ImmutableArray<Outputs.PipelineActivity> pipelineActivities,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Id = id;
            PipelineActivities = pipelineActivities;
            Tags = tags;
        }
    }
}
