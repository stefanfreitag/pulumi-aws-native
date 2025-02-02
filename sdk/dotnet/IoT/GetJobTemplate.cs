// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetJobTemplate
    {
        /// <summary>
        /// Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.
        /// </summary>
        public static Task<GetJobTemplateResult> InvokeAsync(GetJobTemplateArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetJobTemplateResult>("aws-native:iot:getJobTemplate", args ?? new GetJobTemplateArgs(), options.WithDefaults());

        /// <summary>
        /// Job templates enable you to preconfigure jobs so that you can deploy them to multiple sets of target devices.
        /// </summary>
        public static Output<GetJobTemplateResult> Invoke(GetJobTemplateInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetJobTemplateResult>("aws-native:iot:getJobTemplate", args ?? new GetJobTemplateInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetJobTemplateArgs : global::Pulumi.InvokeArgs
    {
        [Input("jobTemplateId", required: true)]
        public string JobTemplateId { get; set; } = null!;

        public GetJobTemplateArgs()
        {
        }
        public static new GetJobTemplateArgs Empty => new GetJobTemplateArgs();
    }

    public sealed class GetJobTemplateInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("jobTemplateId", required: true)]
        public Input<string> JobTemplateId { get; set; } = null!;

        public GetJobTemplateInvokeArgs()
        {
        }
        public static new GetJobTemplateInvokeArgs Empty => new GetJobTemplateInvokeArgs();
    }


    [OutputType]
    public sealed class GetJobTemplateResult
    {
        public readonly string? Arn;

        [OutputConstructor]
        private GetJobTemplateResult(string? arn)
        {
            Arn = arn;
        }
    }
}
