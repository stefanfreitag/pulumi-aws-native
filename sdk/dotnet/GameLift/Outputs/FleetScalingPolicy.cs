// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GameLift.Outputs
{

    /// <summary>
    /// Rule that controls how a fleet is scaled. Scaling policies are uniquely identified by the combination of name and fleet ID.
    /// </summary>
    [OutputType]
    public sealed class FleetScalingPolicy
    {
        /// <summary>
        /// Comparison operator to use when measuring a metric against the threshold value.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyComparisonOperator? ComparisonOperator;
        /// <summary>
        /// Length of time (in minutes) the metric must be at or beyond the threshold before a scaling event is triggered.
        /// </summary>
        public readonly int? EvaluationPeriods;
        public readonly string? Location;
        /// <summary>
        /// Name of the Amazon GameLift-defined metric that is used to trigger a scaling adjustment.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyMetricName MetricName;
        /// <summary>
        /// A descriptive label that is associated with a fleet's scaling policy. Policy names do not need to be unique.
        /// </summary>
        public readonly string Name;
        /// <summary>
        /// The type of scaling policy to create. For a target-based policy, set the parameter MetricName to 'PercentAvailableGameSessions' and specify a TargetConfiguration. For a rule-based policy set the following parameters: MetricName, ComparisonOperator, Threshold, EvaluationPeriods, ScalingAdjustmentType, and ScalingAdjustment.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyPolicyType? PolicyType;
        /// <summary>
        /// Amount of adjustment to make, based on the scaling adjustment type.
        /// </summary>
        public readonly int? ScalingAdjustment;
        /// <summary>
        /// The type of adjustment to make to a fleet's instance count.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyScalingAdjustmentType? ScalingAdjustmentType;
        /// <summary>
        /// Current status of the scaling policy. The scaling policy can be in force only when in an ACTIVE status. Scaling policies can be suspended for individual fleets. If the policy is suspended for a fleet, the policy status does not change.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyStatus? Status;
        /// <summary>
        /// An object that contains settings for a target-based scaling policy.
        /// </summary>
        public readonly Outputs.FleetTargetConfiguration? TargetConfiguration;
        /// <summary>
        /// Metric value used to trigger a scaling event.
        /// </summary>
        public readonly double? Threshold;
        /// <summary>
        /// The current status of the fleet's scaling policies in a requested fleet location. The status PENDING_UPDATE indicates that an update was requested for the fleet but has not yet been completed for the location.
        /// </summary>
        public readonly Pulumi.AwsNative.GameLift.FleetScalingPolicyUpdateStatus? UpdateStatus;

        [OutputConstructor]
        private FleetScalingPolicy(
            Pulumi.AwsNative.GameLift.FleetScalingPolicyComparisonOperator? comparisonOperator,

            int? evaluationPeriods,

            string? location,

            Pulumi.AwsNative.GameLift.FleetScalingPolicyMetricName metricName,

            string name,

            Pulumi.AwsNative.GameLift.FleetScalingPolicyPolicyType? policyType,

            int? scalingAdjustment,

            Pulumi.AwsNative.GameLift.FleetScalingPolicyScalingAdjustmentType? scalingAdjustmentType,

            Pulumi.AwsNative.GameLift.FleetScalingPolicyStatus? status,

            Outputs.FleetTargetConfiguration? targetConfiguration,

            double? threshold,

            Pulumi.AwsNative.GameLift.FleetScalingPolicyUpdateStatus? updateStatus)
        {
            ComparisonOperator = comparisonOperator;
            EvaluationPeriods = evaluationPeriods;
            Location = location;
            MetricName = metricName;
            Name = name;
            PolicyType = policyType;
            ScalingAdjustment = scalingAdjustment;
            ScalingAdjustmentType = scalingAdjustmentType;
            Status = status;
            TargetConfiguration = targetConfiguration;
            Threshold = threshold;
            UpdateStatus = updateStatus;
        }
    }
}
