// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AutoScaling
{
    /// <summary>
    /// Resource Type definition for AWS::AutoScaling::AutoScalingGroup
    /// </summary>
    [AwsNativeResourceType("aws-native:autoscaling:AutoScalingGroup")]
    public partial class AutoScalingGroup : global::Pulumi.CustomResource
    {
        [Output("autoScalingGroupName")]
        public Output<string?> AutoScalingGroupName { get; private set; } = null!;

        [Output("availabilityZones")]
        public Output<ImmutableArray<string>> AvailabilityZones { get; private set; } = null!;

        [Output("capacityRebalance")]
        public Output<bool?> CapacityRebalance { get; private set; } = null!;

        [Output("context")]
        public Output<string?> Context { get; private set; } = null!;

        [Output("cooldown")]
        public Output<string?> Cooldown { get; private set; } = null!;

        [Output("defaultInstanceWarmup")]
        public Output<int?> DefaultInstanceWarmup { get; private set; } = null!;

        [Output("desiredCapacity")]
        public Output<string?> DesiredCapacity { get; private set; } = null!;

        [Output("desiredCapacityType")]
        public Output<string?> DesiredCapacityType { get; private set; } = null!;

        [Output("healthCheckGracePeriod")]
        public Output<int?> HealthCheckGracePeriod { get; private set; } = null!;

        [Output("healthCheckType")]
        public Output<string?> HealthCheckType { get; private set; } = null!;

        [Output("instanceId")]
        public Output<string?> InstanceId { get; private set; } = null!;

        [Output("launchConfigurationName")]
        public Output<string?> LaunchConfigurationName { get; private set; } = null!;

        [Output("launchTemplate")]
        public Output<Outputs.AutoScalingGroupLaunchTemplateSpecification?> LaunchTemplate { get; private set; } = null!;

        [Output("lifecycleHookSpecificationList")]
        public Output<ImmutableArray<Outputs.AutoScalingGroupLifecycleHookSpecification>> LifecycleHookSpecificationList { get; private set; } = null!;

        [Output("loadBalancerNames")]
        public Output<ImmutableArray<string>> LoadBalancerNames { get; private set; } = null!;

        [Output("maxInstanceLifetime")]
        public Output<int?> MaxInstanceLifetime { get; private set; } = null!;

        [Output("maxSize")]
        public Output<string> MaxSize { get; private set; } = null!;

        [Output("metricsCollection")]
        public Output<ImmutableArray<Outputs.AutoScalingGroupMetricsCollection>> MetricsCollection { get; private set; } = null!;

        [Output("minSize")]
        public Output<string> MinSize { get; private set; } = null!;

        [Output("mixedInstancesPolicy")]
        public Output<Outputs.AutoScalingGroupMixedInstancesPolicy?> MixedInstancesPolicy { get; private set; } = null!;

        [Output("newInstancesProtectedFromScaleIn")]
        public Output<bool?> NewInstancesProtectedFromScaleIn { get; private set; } = null!;

        [Output("notificationConfiguration")]
        public Output<Outputs.AutoScalingGroupNotificationConfiguration?> NotificationConfiguration { get; private set; } = null!;

        [Output("notificationConfigurations")]
        public Output<ImmutableArray<Outputs.AutoScalingGroupNotificationConfiguration>> NotificationConfigurations { get; private set; } = null!;

        [Output("placementGroup")]
        public Output<string?> PlacementGroup { get; private set; } = null!;

        [Output("serviceLinkedRoleArn")]
        public Output<string?> ServiceLinkedRoleArn { get; private set; } = null!;

        [Output("tags")]
        public Output<ImmutableArray<Outputs.AutoScalingGroupTagProperty>> Tags { get; private set; } = null!;

        [Output("targetGroupArns")]
        public Output<ImmutableArray<string>> TargetGroupArns { get; private set; } = null!;

        [Output("terminationPolicies")]
        public Output<ImmutableArray<string>> TerminationPolicies { get; private set; } = null!;

        [Output("vpcZoneIdentifier")]
        public Output<ImmutableArray<string>> VpcZoneIdentifier { get; private set; } = null!;


        /// <summary>
        /// Create a AutoScalingGroup resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AutoScalingGroup(string name, AutoScalingGroupArgs args, CustomResourceOptions? options = null)
            : base("aws-native:autoscaling:AutoScalingGroup", name, args ?? new AutoScalingGroupArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AutoScalingGroup(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:autoscaling:AutoScalingGroup", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
                ReplaceOnChanges =
                {
                    "autoScalingGroupName",
                    "instanceId",
                },
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AutoScalingGroup resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AutoScalingGroup Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new AutoScalingGroup(name, id, options);
        }
    }

    public sealed class AutoScalingGroupArgs : global::Pulumi.ResourceArgs
    {
        [Input("autoScalingGroupName")]
        public Input<string>? AutoScalingGroupName { get; set; }

        [Input("availabilityZones")]
        private InputList<string>? _availabilityZones;
        public InputList<string> AvailabilityZones
        {
            get => _availabilityZones ?? (_availabilityZones = new InputList<string>());
            set => _availabilityZones = value;
        }

        [Input("capacityRebalance")]
        public Input<bool>? CapacityRebalance { get; set; }

        [Input("context")]
        public Input<string>? Context { get; set; }

        [Input("cooldown")]
        public Input<string>? Cooldown { get; set; }

        [Input("defaultInstanceWarmup")]
        public Input<int>? DefaultInstanceWarmup { get; set; }

        [Input("desiredCapacity")]
        public Input<string>? DesiredCapacity { get; set; }

        [Input("desiredCapacityType")]
        public Input<string>? DesiredCapacityType { get; set; }

        [Input("healthCheckGracePeriod")]
        public Input<int>? HealthCheckGracePeriod { get; set; }

        [Input("healthCheckType")]
        public Input<string>? HealthCheckType { get; set; }

        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        [Input("launchConfigurationName")]
        public Input<string>? LaunchConfigurationName { get; set; }

        [Input("launchTemplate")]
        public Input<Inputs.AutoScalingGroupLaunchTemplateSpecificationArgs>? LaunchTemplate { get; set; }

        [Input("lifecycleHookSpecificationList")]
        private InputList<Inputs.AutoScalingGroupLifecycleHookSpecificationArgs>? _lifecycleHookSpecificationList;
        public InputList<Inputs.AutoScalingGroupLifecycleHookSpecificationArgs> LifecycleHookSpecificationList
        {
            get => _lifecycleHookSpecificationList ?? (_lifecycleHookSpecificationList = new InputList<Inputs.AutoScalingGroupLifecycleHookSpecificationArgs>());
            set => _lifecycleHookSpecificationList = value;
        }

        [Input("loadBalancerNames")]
        private InputList<string>? _loadBalancerNames;
        public InputList<string> LoadBalancerNames
        {
            get => _loadBalancerNames ?? (_loadBalancerNames = new InputList<string>());
            set => _loadBalancerNames = value;
        }

        [Input("maxInstanceLifetime")]
        public Input<int>? MaxInstanceLifetime { get; set; }

        [Input("maxSize", required: true)]
        public Input<string> MaxSize { get; set; } = null!;

        [Input("metricsCollection")]
        private InputList<Inputs.AutoScalingGroupMetricsCollectionArgs>? _metricsCollection;
        public InputList<Inputs.AutoScalingGroupMetricsCollectionArgs> MetricsCollection
        {
            get => _metricsCollection ?? (_metricsCollection = new InputList<Inputs.AutoScalingGroupMetricsCollectionArgs>());
            set => _metricsCollection = value;
        }

        [Input("minSize", required: true)]
        public Input<string> MinSize { get; set; } = null!;

        [Input("mixedInstancesPolicy")]
        public Input<Inputs.AutoScalingGroupMixedInstancesPolicyArgs>? MixedInstancesPolicy { get; set; }

        [Input("newInstancesProtectedFromScaleIn")]
        public Input<bool>? NewInstancesProtectedFromScaleIn { get; set; }

        [Input("notificationConfiguration")]
        public Input<Inputs.AutoScalingGroupNotificationConfigurationArgs>? NotificationConfiguration { get; set; }

        [Input("notificationConfigurations")]
        private InputList<Inputs.AutoScalingGroupNotificationConfigurationArgs>? _notificationConfigurations;
        public InputList<Inputs.AutoScalingGroupNotificationConfigurationArgs> NotificationConfigurations
        {
            get => _notificationConfigurations ?? (_notificationConfigurations = new InputList<Inputs.AutoScalingGroupNotificationConfigurationArgs>());
            set => _notificationConfigurations = value;
        }

        [Input("placementGroup")]
        public Input<string>? PlacementGroup { get; set; }

        [Input("serviceLinkedRoleArn")]
        public Input<string>? ServiceLinkedRoleArn { get; set; }

        [Input("tags")]
        private InputList<Inputs.AutoScalingGroupTagPropertyArgs>? _tags;
        public InputList<Inputs.AutoScalingGroupTagPropertyArgs> Tags
        {
            get => _tags ?? (_tags = new InputList<Inputs.AutoScalingGroupTagPropertyArgs>());
            set => _tags = value;
        }

        [Input("targetGroupArns")]
        private InputList<string>? _targetGroupArns;
        public InputList<string> TargetGroupArns
        {
            get => _targetGroupArns ?? (_targetGroupArns = new InputList<string>());
            set => _targetGroupArns = value;
        }

        [Input("terminationPolicies")]
        private InputList<string>? _terminationPolicies;
        public InputList<string> TerminationPolicies
        {
            get => _terminationPolicies ?? (_terminationPolicies = new InputList<string>());
            set => _terminationPolicies = value;
        }

        [Input("vpcZoneIdentifier")]
        private InputList<string>? _vpcZoneIdentifier;
        public InputList<string> VpcZoneIdentifier
        {
            get => _vpcZoneIdentifier ?? (_vpcZoneIdentifier = new InputList<string>());
            set => _vpcZoneIdentifier = value;
        }

        public AutoScalingGroupArgs()
        {
        }
        public static new AutoScalingGroupArgs Empty => new AutoScalingGroupArgs();
    }
}
