// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.EMR
{
    public static class GetStep
    {
        /// <summary>
        /// Resource Type definition for AWS::EMR::Step
        /// </summary>
        public static Task<GetStepResult> InvokeAsync(GetStepArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetStepResult>("aws-native:emr:getStep", args ?? new GetStepArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EMR::Step
        /// </summary>
        public static Output<GetStepResult> Invoke(GetStepInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetStepResult>("aws-native:emr:getStep", args ?? new GetStepInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetStepArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetStepArgs()
        {
        }
        public static new GetStepArgs Empty => new GetStepArgs();
    }

    public sealed class GetStepInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetStepInvokeArgs()
        {
        }
        public static new GetStepInvokeArgs Empty => new GetStepInvokeArgs();
    }


    [OutputType]
    public sealed class GetStepResult
    {
        public readonly string? Id;

        [OutputConstructor]
        private GetStepResult(string? id)
        {
            Id = id;
        }
    }
}
