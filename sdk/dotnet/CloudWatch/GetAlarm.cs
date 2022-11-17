// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudWatch
{
    public static class GetAlarm
    {
        /// <summary>
        /// Resource Type definition for AWS::CloudWatch::Alarm
        /// </summary>
        public static Task<GetAlarmResult> InvokeAsync(GetAlarmArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetAlarmResult>("aws-native:cloudwatch:getAlarm", args ?? new GetAlarmArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CloudWatch::Alarm
        /// </summary>
        public static Output<GetAlarmResult> Invoke(GetAlarmInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetAlarmResult>("aws-native:cloudwatch:getAlarm", args ?? new GetAlarmInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAlarmArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the alarm.
        /// </summary>
        [Input("alarmName", required: true)]
        public string AlarmName { get; set; } = null!;

        public GetAlarmArgs()
        {
        }
        public static new GetAlarmArgs Empty => new GetAlarmArgs();
    }

    public sealed class GetAlarmInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name of the alarm.
        /// </summary>
        [Input("alarmName", required: true)]
        public Input<string> AlarmName { get; set; } = null!;

        public GetAlarmInvokeArgs()
        {
        }
        public static new GetAlarmInvokeArgs Empty => new GetAlarmInvokeArgs();
    }


    [OutputType]
    public sealed class GetAlarmResult
    {
        /// <summary>
        /// Indicates whether actions should be executed during any changes to the alarm state. The default is TRUE.
        /// </summary>
        public readonly bool? ActionsEnabled;
        /// <summary>
        /// The list of actions to execute when this alarm transitions into an ALARM state from any other state.
        /// </summary>
        public readonly ImmutableArray<string> AlarmActions;
        /// <summary>
        /// The description of the alarm.
        /// </summary>
        public readonly string? AlarmDescription;
        /// <summary>
        /// Amazon Resource Name is a unique name for each resource.
        /// </summary>
        public readonly string? Arn;
        /// <summary>
        /// The arithmetic operation to use when comparing the specified statistic and threshold.
        /// </summary>
        public readonly string? ComparisonOperator;
        /// <summary>
        /// The number of datapoints that must be breaching to trigger the alarm.
        /// </summary>
        public readonly int? DatapointsToAlarm;
        /// <summary>
        /// The dimensions for the metric associated with the alarm. For an alarm based on a math expression, you can't specify Dimensions. Instead, you use Metrics.
        /// </summary>
        public readonly ImmutableArray<Outputs.AlarmDimension> Dimensions;
        /// <summary>
        /// Used only for alarms based on percentiles.
        /// </summary>
        public readonly string? EvaluateLowSampleCountPercentile;
        /// <summary>
        /// The number of periods over which data is compared to the specified threshold.
        /// </summary>
        public readonly int? EvaluationPeriods;
        /// <summary>
        /// The percentile statistic for the metric associated with the alarm. Specify a value between p0.0 and p100.
        /// </summary>
        public readonly string? ExtendedStatistic;
        /// <summary>
        /// The actions to execute when this alarm transitions to the INSUFFICIENT_DATA state from any other state.
        /// </summary>
        public readonly ImmutableArray<string> InsufficientDataActions;
        /// <summary>
        /// The name of the metric associated with the alarm.
        /// </summary>
        public readonly string? MetricName;
        /// <summary>
        /// An array that enables you to create an alarm based on the result of a metric math expression.
        /// </summary>
        public readonly ImmutableArray<Outputs.AlarmMetricDataQuery> Metrics;
        /// <summary>
        /// The namespace of the metric associated with the alarm.
        /// </summary>
        public readonly string? Namespace;
        /// <summary>
        /// The actions to execute when this alarm transitions to the OK state from any other state.
        /// </summary>
        public readonly ImmutableArray<string> OKActions;
        /// <summary>
        /// The period in seconds, over which the statistic is applied.
        /// </summary>
        public readonly int? Period;
        /// <summary>
        /// The statistic for the metric associated with the alarm, other than percentile.
        /// </summary>
        public readonly string? Statistic;
        /// <summary>
        /// In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        /// </summary>
        public readonly double? Threshold;
        /// <summary>
        /// In an alarm based on an anomaly detection model, this is the ID of the ANOMALY_DETECTION_BAND function used as the threshold for the alarm.
        /// </summary>
        public readonly string? ThresholdMetricId;
        /// <summary>
        /// Sets how this alarm is to handle missing data points. Valid values are breaching, notBreaching, ignore, and missing.
        /// </summary>
        public readonly string? TreatMissingData;
        /// <summary>
        /// The unit of the metric associated with the alarm.
        /// </summary>
        public readonly string? Unit;

        [OutputConstructor]
        private GetAlarmResult(
            bool? actionsEnabled,

            ImmutableArray<string> alarmActions,

            string? alarmDescription,

            string? arn,

            string? comparisonOperator,

            int? datapointsToAlarm,

            ImmutableArray<Outputs.AlarmDimension> dimensions,

            string? evaluateLowSampleCountPercentile,

            int? evaluationPeriods,

            string? extendedStatistic,

            ImmutableArray<string> insufficientDataActions,

            string? metricName,

            ImmutableArray<Outputs.AlarmMetricDataQuery> metrics,

            string? @namespace,

            ImmutableArray<string> oKActions,

            int? period,

            string? statistic,

            double? threshold,

            string? thresholdMetricId,

            string? treatMissingData,

            string? unit)
        {
            ActionsEnabled = actionsEnabled;
            AlarmActions = alarmActions;
            AlarmDescription = alarmDescription;
            Arn = arn;
            ComparisonOperator = comparisonOperator;
            DatapointsToAlarm = datapointsToAlarm;
            Dimensions = dimensions;
            EvaluateLowSampleCountPercentile = evaluateLowSampleCountPercentile;
            EvaluationPeriods = evaluationPeriods;
            ExtendedStatistic = extendedStatistic;
            InsufficientDataActions = insufficientDataActions;
            MetricName = metricName;
            Metrics = metrics;
            Namespace = @namespace;
            OKActions = oKActions;
            Period = period;
            Statistic = statistic;
            Threshold = threshold;
            ThresholdMetricId = thresholdMetricId;
            TreatMissingData = treatMissingData;
            Unit = unit;
        }
    }
}
