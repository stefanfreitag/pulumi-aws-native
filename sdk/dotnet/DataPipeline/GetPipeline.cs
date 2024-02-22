// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataPipeline
{
    public static class GetPipeline
    {
        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Task<GetPipelineResult> InvokeAsync(GetPipelineArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPipelineResult>("aws-native:datapipeline:getPipeline", args ?? new GetPipelineArgs(), options.WithDefaults());

        /// <summary>
        /// An example resource schema demonstrating some basic constructs and validation rules.
        /// </summary>
        public static Output<GetPipelineResult> Invoke(GetPipelineInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPipelineResult>("aws-native:datapipeline:getPipeline", args ?? new GetPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPipelineArgs : global::Pulumi.InvokeArgs
    {
        [Input("pipelineId", required: true)]
        public string PipelineId { get; set; } = null!;

        public GetPipelineArgs()
        {
        }
        public static new GetPipelineArgs Empty => new GetPipelineArgs();
    }

    public sealed class GetPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("pipelineId", required: true)]
        public Input<string> PipelineId { get; set; } = null!;

        public GetPipelineInvokeArgs()
        {
        }
        public static new GetPipelineInvokeArgs Empty => new GetPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPipelineResult
    {
        /// <summary>
        /// Indicates whether to validate and start the pipeline or stop an active pipeline. By default, the value is set to true.
        /// </summary>
        public readonly bool? Activate;
        /// <summary>
        /// The parameter objects used with the pipeline.
        /// </summary>
        public readonly ImmutableArray<Outputs.PipelineParameterObject> ParameterObjects;
        /// <summary>
        /// The parameter values used with the pipeline.
        /// </summary>
        public readonly ImmutableArray<Outputs.PipelineParameterValue> ParameterValues;
        public readonly string? PipelineId;
        /// <summary>
        /// The objects that define the pipeline. These objects overwrite the existing pipeline definition. Not all objects, fields, and values can be updated. For information about restrictions, see Editing Your Pipeline in the AWS Data Pipeline Developer Guide.
        /// </summary>
        public readonly ImmutableArray<Outputs.PipelineObject> PipelineObjects;
        /// <summary>
        /// A list of arbitrary tags (key-value pairs) to associate with the pipeline, which you can use to control permissions. For more information, see Controlling Access to Pipelines and Resources in the AWS Data Pipeline Developer Guide.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> PipelineTags;

        [OutputConstructor]
        private GetPipelineResult(
            bool? activate,

            ImmutableArray<Outputs.PipelineParameterObject> parameterObjects,

            ImmutableArray<Outputs.PipelineParameterValue> parameterValues,

            string? pipelineId,

            ImmutableArray<Outputs.PipelineObject> pipelineObjects,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> pipelineTags)
        {
            Activate = activate;
            ParameterObjects = parameterObjects;
            ParameterValues = parameterValues;
            PipelineId = pipelineId;
            PipelineObjects = pipelineObjects;
            PipelineTags = pipelineTags;
        }
    }
}
