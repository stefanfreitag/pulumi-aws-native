// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lightsail
{
    /// <summary>
    /// Resource Type definition for AWS::Lightsail::Alarm
    /// </summary>
    [AwsNativeResourceType("aws-native:lightsail:Alarm")]
    public partial class Alarm : global::Pulumi.CustomResource
    {
        [Output("alarmArn")]
        public Output<string> AlarmArn { get; private set; } = null!;

        /// <summary>
        /// The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.
        /// </summary>
        [Output("alarmName")]
        public Output<string> AlarmName { get; private set; } = null!;

        /// <summary>
        /// The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.
        /// </summary>
        [Output("comparisonOperator")]
        public Output<string> ComparisonOperator { get; private set; } = null!;

        /// <summary>
        /// The contact protocols to use for the alarm, such as Email, SMS (text messaging), or both.
        /// </summary>
        [Output("contactProtocols")]
        public Output<ImmutableArray<string>> ContactProtocols { get; private set; } = null!;

        /// <summary>
        /// The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (datapointsToAlarm) is the M.
        /// </summary>
        [Output("datapointsToAlarm")]
        public Output<int?> DatapointsToAlarm { get; private set; } = null!;

        /// <summary>
        /// The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (evaluationPeriods) is the N.
        /// </summary>
        [Output("evaluationPeriods")]
        public Output<int> EvaluationPeriods { get; private set; } = null!;

        /// <summary>
        /// The name of the metric to associate with the alarm.
        /// </summary>
        [Output("metricName")]
        public Output<string> MetricName { get; private set; } = null!;

        /// <summary>
        /// The validation status of the SSL/TLS certificate.
        /// </summary>
        [Output("monitoredResourceName")]
        public Output<string> MonitoredResourceName { get; private set; } = null!;

        /// <summary>
        /// Indicates whether the alarm is enabled. Notifications are enabled by default if you don't specify this parameter.
        /// </summary>
        [Output("notificationEnabled")]
        public Output<bool?> NotificationEnabled { get; private set; } = null!;

        /// <summary>
        /// The alarm states that trigger a notification.
        /// </summary>
        [Output("notificationTriggers")]
        public Output<ImmutableArray<string>> NotificationTriggers { get; private set; } = null!;

        /// <summary>
        /// The current state of the alarm.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The value against which the specified statistic is compared.
        /// </summary>
        [Output("threshold")]
        public Output<double> Threshold { get; private set; } = null!;

        /// <summary>
        /// Sets how this alarm will handle missing data points.
        /// </summary>
        [Output("treatMissingData")]
        public Output<string?> TreatMissingData { get; private set; } = null!;


        /// <summary>
        /// Create a Alarm resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Alarm(string name, AlarmArgs args, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Alarm", name, args ?? new AlarmArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Alarm(string name, Input<string> id, CustomResourceOptions? options = null)
            : base("aws-native:lightsail:Alarm", name, null, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Alarm resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Alarm Get(string name, Input<string> id, CustomResourceOptions? options = null)
        {
            return new Alarm(name, id, options);
        }
    }

    public sealed class AlarmArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name for the alarm. Specify the name of an existing alarm to update, and overwrite the previous configuration of the alarm.
        /// </summary>
        [Input("alarmName")]
        public Input<string>? AlarmName { get; set; }

        /// <summary>
        /// The arithmetic operation to use when comparing the specified statistic to the threshold. The specified statistic value is used as the first operand.
        /// </summary>
        [Input("comparisonOperator", required: true)]
        public Input<string> ComparisonOperator { get; set; } = null!;

        [Input("contactProtocols")]
        private InputList<string>? _contactProtocols;

        /// <summary>
        /// The contact protocols to use for the alarm, such as Email, SMS (text messaging), or both.
        /// </summary>
        public InputList<string> ContactProtocols
        {
            get => _contactProtocols ?? (_contactProtocols = new InputList<string>());
            set => _contactProtocols = value;
        }

        /// <summary>
        /// The number of data points that must be not within the specified threshold to trigger the alarm. If you are setting an "M out of N" alarm, this value (datapointsToAlarm) is the M.
        /// </summary>
        [Input("datapointsToAlarm")]
        public Input<int>? DatapointsToAlarm { get; set; }

        /// <summary>
        /// The number of most recent periods over which data is compared to the specified threshold. If you are setting an "M out of N" alarm, this value (evaluationPeriods) is the N.
        /// </summary>
        [Input("evaluationPeriods", required: true)]
        public Input<int> EvaluationPeriods { get; set; } = null!;

        /// <summary>
        /// The name of the metric to associate with the alarm.
        /// </summary>
        [Input("metricName", required: true)]
        public Input<string> MetricName { get; set; } = null!;

        /// <summary>
        /// The validation status of the SSL/TLS certificate.
        /// </summary>
        [Input("monitoredResourceName", required: true)]
        public Input<string> MonitoredResourceName { get; set; } = null!;

        /// <summary>
        /// Indicates whether the alarm is enabled. Notifications are enabled by default if you don't specify this parameter.
        /// </summary>
        [Input("notificationEnabled")]
        public Input<bool>? NotificationEnabled { get; set; }

        [Input("notificationTriggers")]
        private InputList<string>? _notificationTriggers;

        /// <summary>
        /// The alarm states that trigger a notification.
        /// </summary>
        public InputList<string> NotificationTriggers
        {
            get => _notificationTriggers ?? (_notificationTriggers = new InputList<string>());
            set => _notificationTriggers = value;
        }

        /// <summary>
        /// The value against which the specified statistic is compared.
        /// </summary>
        [Input("threshold", required: true)]
        public Input<double> Threshold { get; set; } = null!;

        /// <summary>
        /// Sets how this alarm will handle missing data points.
        /// </summary>
        [Input("treatMissingData")]
        public Input<string>? TreatMissingData { get; set; }

        public AlarmArgs()
        {
        }
        public static new AlarmArgs Empty => new AlarmArgs();
    }
}
