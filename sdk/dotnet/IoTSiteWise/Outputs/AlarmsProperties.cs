// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTSiteWise.Outputs
{

    /// <summary>
    /// Contains the configuration information of an alarm created in an AWS IoT SiteWise Monitor portal. You can use the alarm to monitor an asset property and get notified when the asset property value is outside a specified range.
    /// </summary>
    [OutputType]
    public sealed class AlarmsProperties
    {
        /// <summary>
        /// The ARN of the IAM role that allows the alarm to perform actions and access AWS resources and services, such as AWS IoT Events.
        /// </summary>
        public readonly string? AlarmRoleArn;
        /// <summary>
        /// The ARN of the AWS Lambda function that manages alarm notifications. For more information, see Managing alarm notifications in the AWS IoT Events Developer Guide.
        /// </summary>
        public readonly string? NotificationLambdaArn;

        [OutputConstructor]
        private AlarmsProperties(
            string? alarmRoleArn,

            string? notificationLambdaArn)
        {
            AlarmRoleArn = alarmRoleArn;
            NotificationLambdaArn = notificationLambdaArn;
        }
    }
}
