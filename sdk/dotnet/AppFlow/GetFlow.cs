// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow
{
    public static class GetFlow
    {
        /// <summary>
        /// Resource schema for AWS::AppFlow::Flow.
        /// </summary>
        public static Task<GetFlowResult> InvokeAsync(GetFlowArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFlowResult>("aws-native:appflow:getFlow", args ?? new GetFlowArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::AppFlow::Flow.
        /// </summary>
        public static Output<GetFlowResult> Invoke(GetFlowInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFlowResult>("aws-native:appflow:getFlow", args ?? new GetFlowInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFlowArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the flow.
        /// </summary>
        [Input("flowName", required: true)]
        public string FlowName { get; set; } = null!;

        public GetFlowArgs()
        {
        }
        public static new GetFlowArgs Empty => new GetFlowArgs();
    }

    public sealed class GetFlowInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// Name of the flow.
        /// </summary>
        [Input("flowName", required: true)]
        public Input<string> FlowName { get; set; } = null!;

        public GetFlowInvokeArgs()
        {
        }
        public static new GetFlowInvokeArgs Empty => new GetFlowInvokeArgs();
    }


    [OutputType]
    public sealed class GetFlowResult
    {
        /// <summary>
        /// Description of the flow.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// List of Destination connectors of the flow.
        /// </summary>
        public readonly ImmutableArray<Outputs.FlowDestinationFlowConfig> DestinationFlowConfigList;
        /// <summary>
        /// ARN identifier of the flow.
        /// </summary>
        public readonly string? FlowArn;
        /// <summary>
        /// Flow activation status for Scheduled- and Event-triggered flows
        /// </summary>
        public readonly Pulumi.AwsNative.AppFlow.FlowStatus? FlowStatus;
        /// <summary>
        /// Configurations of metadata catalog of the flow.
        /// </summary>
        public readonly Outputs.FlowMetadataCatalogConfig? MetadataCatalogConfig;
        /// <summary>
        /// Configurations of Source connector of the flow.
        /// </summary>
        public readonly Outputs.FlowSourceFlowConfig? SourceFlowConfig;
        /// <summary>
        /// List of Tags.
        /// </summary>
        public readonly ImmutableArray<Outputs.FlowTag> Tags;
        /// <summary>
        /// List of tasks for the flow.
        /// </summary>
        public readonly ImmutableArray<Outputs.FlowTask> Tasks;
        /// <summary>
        /// Trigger settings of the flow.
        /// </summary>
        public readonly Outputs.FlowTriggerConfig? TriggerConfig;

        [OutputConstructor]
        private GetFlowResult(
            string? description,

            ImmutableArray<Outputs.FlowDestinationFlowConfig> destinationFlowConfigList,

            string? flowArn,

            Pulumi.AwsNative.AppFlow.FlowStatus? flowStatus,

            Outputs.FlowMetadataCatalogConfig? metadataCatalogConfig,

            Outputs.FlowSourceFlowConfig? sourceFlowConfig,

            ImmutableArray<Outputs.FlowTag> tags,

            ImmutableArray<Outputs.FlowTask> tasks,

            Outputs.FlowTriggerConfig? triggerConfig)
        {
            Description = description;
            DestinationFlowConfigList = destinationFlowConfigList;
            FlowArn = flowArn;
            FlowStatus = flowStatus;
            MetadataCatalogConfig = metadataCatalogConfig;
            SourceFlowConfig = sourceFlowConfig;
            Tags = tags;
            Tasks = tasks;
            TriggerConfig = triggerConfig;
        }
    }
}
