// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.SageMaker
{
    public static class GetAppImageConfig
    {
        /// <summary>
        /// Resource Type definition for AWS::SageMaker::AppImageConfig
        /// </summary>
        public static Task<GetAppImageConfigResult> InvokeAsync(GetAppImageConfigArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetAppImageConfigResult>("aws-native:sagemaker:getAppImageConfig", args ?? new GetAppImageConfigArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::SageMaker::AppImageConfig
        /// </summary>
        public static Output<GetAppImageConfigResult> Invoke(GetAppImageConfigInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetAppImageConfigResult>("aws-native:sagemaker:getAppImageConfig", args ?? new GetAppImageConfigInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAppImageConfigArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Name of the AppImageConfig.
        /// </summary>
        [Input("appImageConfigName", required: true)]
        public string AppImageConfigName { get; set; } = null!;

        public GetAppImageConfigArgs()
        {
        }
        public static new GetAppImageConfigArgs Empty => new GetAppImageConfigArgs();
    }

    public sealed class GetAppImageConfigInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The Name of the AppImageConfig.
        /// </summary>
        [Input("appImageConfigName", required: true)]
        public Input<string> AppImageConfigName { get; set; } = null!;

        public GetAppImageConfigInvokeArgs()
        {
        }
        public static new GetAppImageConfigInvokeArgs Empty => new GetAppImageConfigInvokeArgs();
    }


    [OutputType]
    public sealed class GetAppImageConfigResult
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of the AppImageConfig.
        /// </summary>
        public readonly string? AppImageConfigArn;
        /// <summary>
        /// The KernelGatewayImageConfig.
        /// </summary>
        public readonly Outputs.AppImageConfigKernelGatewayImageConfig? KernelGatewayImageConfig;

        [OutputConstructor]
        private GetAppImageConfigResult(
            string? appImageConfigArn,

            Outputs.AppImageConfigKernelGatewayImageConfig? kernelGatewayImageConfig)
        {
            AppImageConfigArn = appImageConfigArn;
            KernelGatewayImageConfig = kernelGatewayImageConfig;
        }
    }
}
