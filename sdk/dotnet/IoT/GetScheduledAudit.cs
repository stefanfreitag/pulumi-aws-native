// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoT
{
    public static class GetScheduledAudit
    {
        /// <summary>
        /// Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.
        /// </summary>
        public static Task<GetScheduledAuditResult> InvokeAsync(GetScheduledAuditArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetScheduledAuditResult>("aws-native:iot:getScheduledAudit", args ?? new GetScheduledAuditArgs(), options.WithDefaults());

        /// <summary>
        /// Scheduled audits can be used to specify the checks you want to perform during an audit and how often the audit should be run.
        /// </summary>
        public static Output<GetScheduledAuditResult> Invoke(GetScheduledAuditInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetScheduledAuditResult>("aws-native:iot:getScheduledAudit", args ?? new GetScheduledAuditInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetScheduledAuditArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name you want to give to the scheduled audit.
        /// </summary>
        [Input("scheduledAuditName", required: true)]
        public string ScheduledAuditName { get; set; } = null!;

        public GetScheduledAuditArgs()
        {
        }
        public static new GetScheduledAuditArgs Empty => new GetScheduledAuditArgs();
    }

    public sealed class GetScheduledAuditInvokeArgs : global::Pulumi.InvokeArgs
    {
        /// <summary>
        /// The name you want to give to the scheduled audit.
        /// </summary>
        [Input("scheduledAuditName", required: true)]
        public Input<string> ScheduledAuditName { get; set; } = null!;

        public GetScheduledAuditInvokeArgs()
        {
        }
        public static new GetScheduledAuditInvokeArgs Empty => new GetScheduledAuditInvokeArgs();
    }


    [OutputType]
    public sealed class GetScheduledAuditResult
    {
        /// <summary>
        /// The day of the month on which the scheduled audit takes place. Can be 1 through 31 or LAST. This field is required if the frequency parameter is set to MONTHLY.
        /// </summary>
        public readonly string? DayOfMonth;
        /// <summary>
        /// The day of the week on which the scheduled audit takes place. Can be one of SUN, MON, TUE,WED, THU, FRI, or SAT. This field is required if the frequency parameter is set to WEEKLY or BIWEEKLY.
        /// </summary>
        public readonly Pulumi.AwsNative.IoT.ScheduledAuditDayOfWeek? DayOfWeek;
        /// <summary>
        /// How often the scheduled audit takes place. Can be one of DAILY, WEEKLY, BIWEEKLY, or MONTHLY.
        /// </summary>
        public readonly Pulumi.AwsNative.IoT.ScheduledAuditFrequency? Frequency;
        /// <summary>
        /// The ARN (Amazon resource name) of the scheduled audit.
        /// </summary>
        public readonly string? ScheduledAuditArn;
        /// <summary>
        /// An array of key-value pairs to apply to this resource.
        /// </summary>
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> Tags;
        /// <summary>
        /// Which checks are performed during the scheduled audit. Checks must be enabled for your account.
        /// </summary>
        public readonly ImmutableArray<string> TargetCheckNames;

        [OutputConstructor]
        private GetScheduledAuditResult(
            string? dayOfMonth,

            Pulumi.AwsNative.IoT.ScheduledAuditDayOfWeek? dayOfWeek,

            Pulumi.AwsNative.IoT.ScheduledAuditFrequency? frequency,

            string? scheduledAuditArn,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> tags,

            ImmutableArray<string> targetCheckNames)
        {
            DayOfMonth = dayOfMonth;
            DayOfWeek = dayOfWeek;
            Frequency = frequency;
            ScheduledAuditArn = scheduledAuditArn;
            Tags = tags;
            TargetCheckNames = targetCheckNames;
        }
    }
}
