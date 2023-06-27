// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppRunner
{
    public static class GetAutoScalingConfiguration
    {
        /// <summary>
        /// Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.
        /// </summary>
        public static Task<GetAutoScalingConfigurationResult> InvokeAsync(GetAutoScalingConfigurationArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAutoScalingConfigurationResult>("aws-native:apprunner:getAutoScalingConfiguration", args ?? new GetAutoScalingConfigurationArgs(), options.WithDefaults());

        /// <summary>
        /// Describes an AWS App Runner automatic configuration resource that enables automatic scaling of instances used to process web requests. You can share an auto scaling configuration across multiple services.
        /// </summary>
        public static Output<GetAutoScalingConfigurationResult> Invoke(GetAutoScalingConfigurationInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAutoScalingConfigurationResult>("aws-native:apprunner:getAutoScalingConfiguration", args ?? new GetAutoScalingConfigurationInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAutoScalingConfigurationArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this auto scaling configuration.
        /// </summary>
        [Input("autoScalingConfigurationArn", required: true)]
        public string AutoScalingConfigurationArn { get; set; } = null!;

        public GetAutoScalingConfigurationArgs()
        {
        }
        public static new GetAutoScalingConfigurationArgs Empty => new GetAutoScalingConfigurationArgs();
    }

    public sealed class GetAutoScalingConfigurationInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this auto scaling configuration.
        /// </summary>
        [Input("autoScalingConfigurationArn", required: true)]
        public Input<string> AutoScalingConfigurationArn { get; set; } = null!;

        public GetAutoScalingConfigurationInvokeArgs()
        {
        }
        public static new GetAutoScalingConfigurationInvokeArgs Empty => new GetAutoScalingConfigurationInvokeArgs();
    }


    [OutputType]
    public sealed class GetAutoScalingConfigurationResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of this auto scaling configuration.
        /// </summary>
        public readonly string? AutoScalingConfigurationArn;
        /// <summary>
        /// The revision of this auto scaling configuration. It's unique among all the active configurations ("Status": "ACTIVE") that share the same AutoScalingConfigurationName.
        /// </summary>
        public readonly int? AutoScalingConfigurationRevision;
        /// <summary>
        /// It's set to true for the configuration with the highest Revision among all configurations that share the same AutoScalingConfigurationName. It's set to false otherwise. App Runner temporarily doubles the number of provisioned instances during deployments, to maintain the same capacity for both old and new code.
        /// </summary>
        public readonly bool? Latest;

        [OutputConstructor]
        private GetAutoScalingConfigurationResult(
            string? autoScalingConfigurationArn,

            int? autoScalingConfigurationRevision,

            bool? latest)
        {
            AutoScalingConfigurationArn = autoScalingConfigurationArn;
            AutoScalingConfigurationRevision = autoScalingConfigurationRevision;
            Latest = latest;
        }
    }
}
