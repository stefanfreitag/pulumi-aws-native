// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline
{
    /// <summary>
    /// Resource Type definition for AWS::CodePipeline::Pipeline
    /// </summary>
    [Obsolete(@"Pipeline is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")]
    [AwsNativeResourceType("aws-native:codepipeline:Pipeline")]
    public partial class Pipeline : global::Pulumi.CustomResource
    {
        [Output("artifactStore")]
        public Output<Outputs.PipelineArtifactStore?> ArtifactStore { get; private set; } = null!;

        [Output("artifactStores")]
        public Output<ImmutableArray<Outputs.PipelineArtifactStoreMap>> ArtifactStores { get; private set; } = null!;

        [Output("disableInboundStageTransitions")]
        public Output<ImmutableArray<Outputs.PipelineStageTransition>> DisableInboundStageTransitions { get; private set; } = null!;

        [Output("executionMode")]
        public Output<string?> ExecutionMode { get; private set; } = null!;

        [Output("name")]
        public Output<string?> Name { get; private set; } = null!;

        [Output("pipelineType")]
        public Output<string?> PipelineType { get; private set; } = null!;

        [Output("restartExecutionOnUpdate")]
        public Output<bool?> RestartExecutionOnUpdate { get; private set; } = null!;

        [Output("roleArn")]
        public Output<string> RoleArn { get; private set; } = null!;

        [Output("stages")]
        public Output<ImmutableArray<Outputs.PipelineStageDeclaration>> Stages { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Pulumi.AwsNative.Outputs.Tag>> Tags { get; private set; } = null!;

        [Output("triggers")]
        public Output<ImmutableArray<Outputs.PipelineTriggerDeclaration>> Triggers { get; private set; } = null!;

        [Output("variables")]
        public Output<ImmutableArray<Outputs.PipelineVariableDeclaration>> Variables { get; private set; } = null!;

        [Output("version")]
        public Output<string> Version { get; private set; } = null!;


        /// <summary>
        /// Create a Pipeline resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Pipeline(string name, PipelineArgs args, CustomResourceOptions? options = null)
            : base("aws-native:codepipeline:Pipeline", name, args ?? new PipelineArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Pipeline(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:codepipeline:Pipeline", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "name",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Pipeline resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Pipeline Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Pipeline(name, id, options);
        }
    }

    public sealed class PipelineArgs : global::Pulumi.ResourceArgs
    {
        [Input("artifactStore")]
        public Input<Inputs.PipelineArtifactStoreArgs>? ArtifactStore { get; set; }

        [Input("artifactStores")]
        private InputList<Inputs.PipelineArtifactStoreMapArgs>? _artifactStores;
        public InputList<Inputs.PipelineArtifactStoreMapArgs> ArtifactStores
        {
            get => _artifactStores ?? (_artifactStores = new InputList<Inputs.PipelineArtifactStoreMapArgs>());
            set => _artifactStores = value;
        }

        [Input("disableInboundStageTransitions")]
        private InputList<Inputs.PipelineStageTransitionArgs>? _disableInboundStageTransitions;
        public InputList<Inputs.PipelineStageTransitionArgs> DisableInboundStageTransitions
        {
            get => _disableInboundStageTransitions ?? (_disableInboundStageTransitions = new InputList<Inputs.PipelineStageTransitionArgs>());
            set => _disableInboundStageTransitions = value;
        }

        [Input("executionMode")]
        public Input<string>? ExecutionMode { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("pipelineType")]
        public Input<string>? PipelineType { get; set; }

        [Input("restartExecutionOnUpdate")]
        public Input<bool>? RestartExecutionOnUpdate { get; set; }

        [Input("roleArn", required: true)]
        public Input<string> RoleArn { get; set; } = null!;

        [Input("stages", required: true)]
        private InputList<Inputs.PipelineStageDeclarationArgs>? _stages;
        public InputList<Inputs.PipelineStageDeclarationArgs> Stages
        {
            get => _stages ?? (_stages = new InputList<Inputs.PipelineStageDeclarationArgs>());
            set => _stages = value;
        }

        [Input("tags")]
        private InputList<Pulumi.AwsNative.Inputs.TagArgs>? _tags;
        public InputList<Pulumi.AwsNative.Inputs.TagArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Pulumi.AwsNative.Inputs.TagArgs>());
            set => _tags = value;
        }

        [Input("triggers")]
        private InputList<Inputs.PipelineTriggerDeclarationArgs>? _triggers;
        public InputList<Inputs.PipelineTriggerDeclarationArgs> Triggers
        {
            get => _triggers ?? (_triggers = new InputList<Inputs.PipelineTriggerDeclarationArgs>());
            set => _triggers = value;
        }

        [Input("variables")]
        private InputList<Inputs.PipelineVariableDeclarationArgs>? _variables;
        public InputList<Inputs.PipelineVariableDeclarationArgs> Variables
        {
            get => _variables ?? (_variables = new InputList<Inputs.PipelineVariableDeclarationArgs>());
            set => _variables = value;
        }

        public PipelineArgs()
        {
        }
        public static new PipelineArgs Empty => new PipelineArgs();
    }
}
