// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTTwinMaker
{
    public static class GetScene
    {
        /// <summary>
        /// Resource schema for AWS::IoTTwinMaker::Scene
        /// </summary>
        public static Task<GetSceneResult> InvokeAsync(GetSceneArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetSceneResult>("aws-native:iottwinmaker:getScene", args ?? new GetSceneArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for AWS::IoTTwinMaker::Scene
        /// </summary>
        public static Output<GetSceneResult> Invoke(GetSceneInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetSceneResult>("aws-native:iottwinmaker:getScene", args ?? new GetSceneInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetSceneArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the scene.
        /// </summary>
        [Input("sceneId", required: true)]
        public string SceneId { get; set; } = null!;

        /// <summary>
        /// The ID of the scene.
        /// </summary>
        [Input("workspaceId", required: true)]
        public string WorkspaceId { get; set; } = null!;

        public GetSceneArgs()
        {
        }
        public static new GetSceneArgs Empty => new GetSceneArgs();
    }

    public sealed class GetSceneInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the scene.
        /// </summary>
        [Input("sceneId", required: true)]
        public Input<string> SceneId { get; set; } = null!;

        /// <summary>
        /// The ID of the scene.
        /// </summary>
        [Input("workspaceId", required: true)]
        public Input<string> WorkspaceId { get; set; } = null!;

        public GetSceneInvokeArgs()
        {
        }
        public static new GetSceneInvokeArgs Empty => new GetSceneInvokeArgs();
    }


    [OutputType]
    public sealed class GetSceneResult
    {
        /// <summary>
        /// The ARN of the scene.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// A list of capabilities that the scene uses to render.
        /// </summary>
        public readonly ImmutableArray<string> Capabilities;
        /// <summary>
        /// The relative path that specifies the location of the content definition file.
        /// </summary>
        public readonly string? ContentLocation;
        /// <summary>
        /// The date and time when the scene was created.
        /// </summary>
        public readonly string? CreationDateTime;
        /// <summary>
        /// The description of the scene.
        /// </summary>
        public readonly string? Description;
        /// <summary>
        /// A key-value pair to associate with a resource.
        /// </summary>
        public readonly object? Tags;
        /// <summary>
        /// The date and time of the current update.
        /// </summary>
        public readonly string? UpdateDateTime;

        [OutputConstructor]
        private GetSceneResult(
            string? arn,

            ImmutableArray<string> capabilities,

            string? contentLocation,

            string? creationDateTime,

            string? description,

            object? tags,

            string? updateDateTime)
        {
            Arn = arn;
            Capabilities = capabilities;
            ContentLocation = contentLocation;
            CreationDateTime = creationDateTime;
            Description = description;
            Tags = tags;
            UpdateDateTime = updateDateTime;
        }
    }
}
