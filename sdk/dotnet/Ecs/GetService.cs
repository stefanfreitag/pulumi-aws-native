// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ecs
{
    public static class GetService
    {
        /// <summary>
        /// Resource Type definition for AWS::ECS::Service
        /// </summary>
        public static Task<GetServiceResult> InvokeAsync(GetServiceArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetServiceResult>("aws-native:ecs:getService", args ?? new GetServiceArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::ECS::Service
        /// </summary>
        public static Output<GetServiceResult> Invoke(GetServiceInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetServiceResult>("aws-native:ecs:getService", args ?? new GetServiceInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetServiceArgs : global::Pulumi.InvokeArgs
    {
        [Input("cluster", required: true)]
        public string Cluster { get; set; } = null!;

        [Input("serviceArn", required: true)]
        public string ServiceArn { get; set; } = null!;

        public GetServiceArgs()
        {
        }
        public static new GetServiceArgs Empty => new GetServiceArgs();
    }

    public sealed class GetServiceInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("cluster", required: true)]
        public Input<string> Cluster { get; set; } = null!;

        [Input("serviceArn", required: true)]
        public Input<string> ServiceArn { get; set; } = null!;

        public GetServiceInvokeArgs()
        {
        }
        public static new GetServiceInvokeArgs Empty => new GetServiceInvokeArgs();
    }


    [OutputType]
    public sealed class GetServiceResult
    {
        public readonly ImmutableArray<Outputs.ServiceCapacityProviderStrategyItem> CapacityProviderStrategy;
        public readonly Outputs.ServiceDeploymentConfiguration? DeploymentConfiguration;
        public readonly int? DesiredCount;
        public readonly bool? EnableEcsManagedTags;
        public readonly bool? EnableExecuteCommand;
        public readonly int? HealthCheckGracePeriodSeconds;
        public readonly ImmutableArray<Outputs.ServiceLoadBalancer> LoadBalancers;
        public readonly string? Name;
        public readonly Outputs.ServiceNetworkConfiguration? NetworkConfiguration;
        public readonly ImmutableArray<Outputs.ServicePlacementConstraint> PlacementConstraints;
        public readonly ImmutableArray<Outputs.ServicePlacementStrategy> PlacementStrategies;
        public readonly string? PlatformVersion;
        public readonly Pulumi.AwsNative.Ecs.ServicePropagateTags? PropagateTags;
        public readonly string? ServiceArn;
        public readonly ImmutableArray<Outputs.ServiceRegistry> ServiceRegistries;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        public readonly string? TaskDefinition;

        [OutputConstructor]
        private GetServiceResult(
            ImmutableArray<Outputs.ServiceCapacityProviderStrategyItem> capacityProviderStrategy,

            Outputs.ServiceDeploymentConfiguration? deploymentConfiguration,

            int? desiredCount,

            bool? enableEcsManagedTags,

            bool? enableExecuteCommand,

            int? healthCheckGracePeriodSeconds,

            ImmutableArray<Outputs.ServiceLoadBalancer> loadBalancers,

            string? name,

            Outputs.ServiceNetworkConfiguration? networkConfiguration,

            ImmutableArray<Outputs.ServicePlacementConstraint> placementConstraints,

            ImmutableArray<Outputs.ServicePlacementStrategy> placementStrategies,

            string? platformVersion,

            Pulumi.AwsNative.Ecs.ServicePropagateTags? propagateTags,

            string? serviceArn,

            ImmutableArray<Outputs.ServiceRegistry> serviceRegistries,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            string? taskDefinition)
        {
            CapacityProviderStrategy = capacityProviderStrategy;
            DeploymentConfiguration = deploymentConfiguration;
            DesiredCount = desiredCount;
            EnableEcsManagedTags = enableEcsManagedTags;
            EnableExecuteCommand = enableExecuteCommand;
            HealthCheckGracePeriodSeconds = healthCheckGracePeriodSeconds;
            LoadBalancers = loadBalancers;
            Name = name;
            NetworkConfiguration = networkConfiguration;
            PlacementConstraints = placementConstraints;
            PlacementStrategies = placementStrategies;
            PlatformVersion = platformVersion;
            PropagateTags = propagateTags;
            ServiceArn = serviceArn;
            ServiceRegistries = serviceRegistries;
            Tags = tags;
            TaskDefinition = taskDefinition;
        }
    }
}
