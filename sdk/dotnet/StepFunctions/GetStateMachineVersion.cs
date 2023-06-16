// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.StepFunctions
{
    public static class GetStateMachineVersion
    {
        /// <summary>
        /// Resource schema for StateMachineVersion
        /// </summary>
        public static Task<GetStateMachineVersionResult> InvokeAsync(GetStateMachineVersionArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetStateMachineVersionResult>("aws-native:stepfunctions:getStateMachineVersion", args ?? new GetStateMachineVersionArgs(), options.WithDefaults());

        /// <summary>
        /// Resource schema for StateMachineVersion
        /// </summary>
        public static Output<GetStateMachineVersionResult> Invoke(GetStateMachineVersionInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetStateMachineVersionResult>("aws-native:stepfunctions:getStateMachineVersion", args ?? new GetStateMachineVersionInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStateMachineVersionArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public string Arn { get; set; } = null!;

        public GetStateMachineVersionArgs()
        {
        }
        public static new GetStateMachineVersionArgs Empty => new GetStateMachineVersionArgs();
    }

    public sealed class GetStateMachineVersionInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("arn", required: true)]
        public Input<string> Arn { get; set; } = null!;

        public GetStateMachineVersionInvokeArgs()
        {
        }
        public static new GetStateMachineVersionInvokeArgs Empty => new GetStateMachineVersionInvokeArgs();
    }


    [OutputType]
    public sealed class GetStateMachineVersionResult
    {
        public readonly string? Arn;
        public readonly string? Description;

        [OutputConstructor]
        private GetStateMachineVersionResult(
            string? arn,

            string? description)
        {
            Arn = arn;
            Description = description;
        }
    }
}
