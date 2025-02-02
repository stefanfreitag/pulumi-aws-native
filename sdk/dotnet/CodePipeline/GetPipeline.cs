// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline
{
    public static class GetPipeline
    {
        /// <summary>
        /// Resource Type definition for AWS::CodePipeline::Pipeline
        /// </summary>
        public static Task<GetPipelineResult> InvokeAsync(GetPipelineArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetPipelineResult>("aws-native:codepipeline:getPipeline", args ?? new GetPipelineArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CodePipeline::Pipeline
        /// </summary>
        public static Output<GetPipelineResult> Invoke(GetPipelineInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetPipelineResult>("aws-native:codepipeline:getPipeline", args ?? new GetPipelineInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetPipelineArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetPipelineArgs()
        {
        }
        public static new GetPipelineArgs Empty => new GetPipelineArgs();
    }

    public sealed class GetPipelineInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetPipelineInvokeArgs()
        {
        }
        public static new GetPipelineInvokeArgs Empty => new GetPipelineInvokeArgs();
    }


    [OutputType]
    public sealed class GetPipelineResult
    {
        public readonly Outputs.PipelineArtifactStore? ArtifactStore;
        public readonly ImmutableArray<Outputs.PipelineArtifactStoreMap> ArtifactStores;
        public readonly ImmutableArray<Outputs.PipelineStageTransition> DisableInboundStageTransitions;
        public readonly string? ExecutionMode;
        public readonly string? Id;
        public readonly string? PipelineType;
        public readonly bool? RestartExecutionOnUpdate;
        public readonly string? RoleArn;
        public readonly ImmutableArray<Outputs.PipelineStageDeclaration> Stages;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        public readonly ImmutableArray<Outputs.PipelineTriggerDeclaration> Triggers;
        public readonly ImmutableArray<Outputs.PipelineVariableDeclaration> Variables;
        public readonly string? Version;

        [OutputConstructor]
        private GetPipelineResult(
            Outputs.PipelineArtifactStore? artifactStore,

            ImmutableArray<Outputs.PipelineArtifactStoreMap> artifactStores,

            ImmutableArray<Outputs.PipelineStageTransition> disableInboundStageTransitions,

            string? executionMode,

            string? id,

            string? pipelineType,

            bool? restartExecutionOnUpdate,

            string? roleArn,

            ImmutableArray<Outputs.PipelineStageDeclaration> stages,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            ImmutableArray<Outputs.PipelineTriggerDeclaration> triggers,

            ImmutableArray<Outputs.PipelineVariableDeclaration> variables,

            string? version)
        {
            ArtifactStore = artifactStore;
            ArtifactStores = artifactStores;
            DisableInboundStageTransitions = disableInboundStageTransitions;
            ExecutionMode = executionMode;
            Id = id;
            PipelineType = pipelineType;
            RestartExecutionOnUpdate = restartExecutionOnUpdate;
            RoleArn = roleArn;
            Stages = stages;
            Tags = tags;
            Triggers = triggers;
            Variables = variables;
            Version = version;
        }
    }
}
