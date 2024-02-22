// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CodePipeline
{
    public static class GetCustomActionType
    {
        /// <summary>
        /// The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.
        /// </summary>
        public static Task<GetCustomActionTypeResult> InvokeAsync(GetCustomActionTypeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetCustomActionTypeResult>("aws-native:codepipeline:getCustomActionType", args ?? new GetCustomActionTypeArgs(), options.WithDefaults());

        /// <summary>
        /// The AWS::CodePipeline::CustomActionType resource creates a custom action for activities that aren't included in the CodePipeline default actions, such as running an internally developed build process or a test suite. You can use these custom actions in the stage of a pipeline.
        /// </summary>
        public static Output<GetCustomActionTypeResult> Invoke(GetCustomActionTypeInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetCustomActionTypeResult>("aws-native:codepipeline:getCustomActionType", args ?? new GetCustomActionTypeInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetCustomActionTypeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The category of the custom action, such as a build action or a test action.
        /// </summary>
        [Input("category", required: true)]
        public string Category { get; set; } = null!;

        /// <summary>
        /// The provider of the service used in the custom action, such as AWS CodeDeploy.
        /// </summary>
        [Input("provider", required: true)]
        public string Provider { get; set; } = null!;

        /// <summary>
        /// The version identifier of the custom action.
        /// </summary>
        [Input("version", required: true)]
        public string Version { get; set; } = null!;

        public GetCustomActionTypeArgs()
        {
        }
        public static new GetCustomActionTypeArgs Empty => new GetCustomActionTypeArgs();
    }

    public sealed class GetCustomActionTypeInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The category of the custom action, such as a build action or a test action.
        /// </summary>
        [Input("category", required: true)]
        public Input<string> Category { get; set; } = null!;

        /// <summary>
        /// The provider of the service used in the custom action, such as AWS CodeDeploy.
        /// </summary>
        [Input("provider", required: true)]
        public Input<string> Provider { get; set; } = null!;

        /// <summary>
        /// The version identifier of the custom action.
        /// </summary>
        [Input("version", required: true)]
        public Input<string> Version { get; set; } = null!;

        public GetCustomActionTypeInvokeArgs()
        {
        }
        public static new GetCustomActionTypeInvokeArgs Empty => new GetCustomActionTypeInvokeArgs();
    }


    [OutputType]
    public sealed class GetCustomActionTypeResult
    {
        public readonly string? Id;
        /// <summary>
        /// Any tags assigned to the custom action.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetCustomActionTypeResult(
            string? id,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            Id = id;
            Tags = tags;
        }
    }
}
