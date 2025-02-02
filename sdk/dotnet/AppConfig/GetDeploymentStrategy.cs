// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppConfig
{
    public static class GetDeploymentStrategy
    {
        /// <summary>
        /// Resource Type definition for AWS::AppConfig::DeploymentStrategy
        /// </summary>
        public static Task<GetDeploymentStrategyResult> InvokeAsync(GetDeploymentStrategyArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetDeploymentStrategyResult>("aws-native:appconfig:getDeploymentStrategy", args ?? new GetDeploymentStrategyArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::AppConfig::DeploymentStrategy
        /// </summary>
        public static Output<GetDeploymentStrategyResult> Invoke(GetDeploymentStrategyInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetDeploymentStrategyResult>("aws-native:appconfig:getDeploymentStrategy", args ?? new GetDeploymentStrategyInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetDeploymentStrategyArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetDeploymentStrategyArgs()
        {
        }
        public static new GetDeploymentStrategyArgs Empty => new GetDeploymentStrategyArgs();
    }

    public sealed class GetDeploymentStrategyInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetDeploymentStrategyInvokeArgs()
        {
        }
        public static new GetDeploymentStrategyInvokeArgs Empty => new GetDeploymentStrategyInvokeArgs();
    }


    [OutputType]
    public sealed class GetDeploymentStrategyResult
    {
        public readonly double? DeploymentDurationInMinutes;
        public readonly string? Description;
        public readonly double? FinalBakeTimeInMinutes;
        public readonly double? GrowthFactor;
        public readonly string? GrowthType;
        public readonly string? Id;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;

        [OutputConstructor]
        private GetDeploymentStrategyResult(
            double? deploymentDurationInMinutes,

            string? description,

            double? finalBakeTimeInMinutes,

            double? growthFactor,

            string? growthType,

            string? id,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags)
        {
            DeploymentDurationInMinutes = deploymentDurationInMinutes;
            Description = description;
            FinalBakeTimeInMinutes = finalBakeTimeInMinutes;
            GrowthFactor = growthFactor;
            GrowthType = growthType;
            Id = id;
            Tags = tags;
        }
    }
}
