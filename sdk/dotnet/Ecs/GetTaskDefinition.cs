// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs
{
    public static class GetTaskDefinition
    {
        /// <summary>
        /// Resource Schema describing various properties for ECS TaskDefinition
        /// </summary>
        public static Task<GetTaskDefinitionResult> InvokeAsync(GetTaskDefinitionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetTaskDefinitionResult>("aws-native:ecs:getTaskDefinition", args ?? new GetTaskDefinitionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Schema describing various properties for ECS TaskDefinition
        /// </summary>
        public static Output<GetTaskDefinitionResult> Invoke(GetTaskDefinitionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetTaskDefinitionResult>("aws-native:ecs:getTaskDefinition", args ?? new GetTaskDefinitionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTaskDefinitionArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon ECS task definition
        /// </summary>
        [Input("taskDefinitionArn", required: true)]
        public string TaskDefinitionArn { get; set; } = null!;

        public GetTaskDefinitionArgs()
        {
        }
        public static new GetTaskDefinitionArgs Empty => new GetTaskDefinitionArgs();
    }

    public sealed class GetTaskDefinitionInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon ECS task definition
        /// </summary>
        [Input("taskDefinitionArn", required: true)]
        public Input<string> TaskDefinitionArn { get; set; } = null!;

        public GetTaskDefinitionInvokeArgs()
        {
        }
        public static new GetTaskDefinitionInvokeArgs Empty => new GetTaskDefinitionInvokeArgs();
    }


    [OutputType]
    public sealed class GetTaskDefinitionResult
    {
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        /// <summary>
        /// The Amazon Resource Name (ARN) of the Amazon ECS task definition
        /// </summary>
        public readonly string? TaskDefinitionArn;

        [OutputConstructor]
        private GetTaskDefinitionResult(
            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            string? taskDefinitionArn)
        {
            Tags = tags;
            TaskDefinitionArn = taskDefinitionArn;
        }
    }
}
