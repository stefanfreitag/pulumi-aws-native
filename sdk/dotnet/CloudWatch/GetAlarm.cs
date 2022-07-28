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
            => Pulumi.Deployment.Instance.InvokeAsync<GetAlarmResult>("aws-native:cloudwatch:getAlarm", args ?? new GetAlarmArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::CloudWatch::Alarm
        /// </summary>
        public static Output<GetAlarmResult> Invoke(GetAlarmInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetAlarmResult>("aws-native:cloudwatch:getAlarm", args ?? new GetAlarmInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetAlarmArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public string Id { get; set; } = null!;

        public GetAlarmArgs()
        {
        }
        public static new GetAlarmArgs Empty => new GetAlarmArgs();
    }

    public sealed class GetAlarmInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("id", required: true)]
        public Input<string> Id { get; set; } = null!;

        public GetAlarmInvokeArgs()
        {
        }
        public static new GetAlarmInvokeArgs Empty => new GetAlarmInvokeArgs();
    }


    [OutputType]
    public sealed class GetAlarmResult
    {
        public readonly bool? ActionsEnabled;
        public readonly ImmutableArray<string> AlarmActions;
        public readonly string? AlarmDescription;
        public readonly string? Arn;
        public readonly string? ComparisonOperator;
        public readonly int? DatapointsToAlarm;
        public readonly ImmutableArray<Outputs.AlarmDimension> Dimensions;
        public readonly string? EvaluateLowSampleCountPercentile;
        public readonly int? EvaluationPeriods;
        public readonly string? ExtendedStatistic;
        public readonly string? Id;
        public readonly ImmutableArray<string> InsufficientDataActions;
        public readonly string? MetricName;
        public readonly ImmutableArray<Outputs.AlarmMetricDataQuery> Metrics;
        public readonly string? Namespace;
        public readonly ImmutableArray<string> OKActions;
        public readonly int? Period;
        public readonly string? Statistic;
        public readonly double? Threshold;
        public readonly string? ThresholdMetricId;
        public readonly string? TreatMissingData;
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

            string? id,

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
            Id = id;
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
