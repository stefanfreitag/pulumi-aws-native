// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.CloudTrail
{
    public static class GetTrail
    {
        /// <summary>
        /// Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.
        /// </summary>
        public static Task<GetTrailResult> InvokeAsync(GetTrailArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetTrailResult>("aws-native:cloudtrail:getTrail", args ?? new GetTrailArgs(), options.WithDefaults());

        /// <summary>
        /// Creates a trail that specifies the settings for delivery of log data to an Amazon S3 bucket. A maximum of five trails can exist in a region, irrespective of the region in which they were created.
        /// </summary>
        public static Output<GetTrailResult> Invoke(GetTrailInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetTrailResult>("aws-native:cloudtrail:getTrail", args ?? new GetTrailInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetTrailArgs : global::Pulumi.InvokeArgs
    {
        [Input("trailName", required: true)]
        public string TrailName { get; set; } = null!;

        public GetTrailArgs()
        {
        }
        public static new GetTrailArgs Empty => new GetTrailArgs();
    }

    public sealed class GetTrailInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("trailName", required: true)]
        public Input<string> TrailName { get; set; } = null!;

        public GetTrailInvokeArgs()
        {
        }
        public static new GetTrailInvokeArgs Empty => new GetTrailInvokeArgs();
    }


    [OutputType]
    public sealed class GetTrailResult
    {
        public readonly string? Arn;
        /// <summary>
        /// Specifies a log group name using an Amazon Resource Name (ARN), a unique identifier that represents the log group to which CloudTrail logs will be delivered. Not required unless you specify CloudWatchLogsRoleArn.
        /// </summary>
        public readonly string? CloudWatchLogsLogGroupArn;
        /// <summary>
        /// Specifies the role for the CloudWatch Logs endpoint to assume to write to a user's log group.
        /// </summary>
        public readonly string? CloudWatchLogsRoleArn;
        /// <summary>
        /// Specifies whether log file validation is enabled. The default is false.
        /// </summary>
        public readonly bool? EnableLogFileValidation;
        /// <summary>
        /// Use event selectors to further specify the management and data event settings for your trail. By default, trails created without specific event selectors will be configured to log all read and write management events, and no data events. When an event occurs in your account, CloudTrail evaluates the event selector for all trails. For each trail, if the event matches any event selector, the trail processes and logs the event. If the event doesn't match any event selector, the trail doesn't log the event. You can configure up to five event selectors for a trail.
        /// </summary>
        public readonly ImmutableArray<Outputs.TrailEventSelector> EventSelectors;
        /// <summary>
        /// Specifies whether the trail is publishing events from global services such as IAM to the log files.
        /// </summary>
        public readonly bool? IncludeGlobalServiceEvents;
        /// <summary>
        /// Lets you enable Insights event logging by specifying the Insights selectors that you want to enable on an existing trail.
        /// </summary>
        public readonly ImmutableArray<Outputs.TrailInsightSelector> InsightSelectors;
        /// <summary>
        /// Whether the CloudTrail is currently logging AWS API calls.
        /// </summary>
        public readonly bool? IsLogging;
        /// <summary>
        /// Specifies whether the trail applies only to the current region or to all regions. The default is false. If the trail exists only in the current region and this value is set to true, shadow trails (replications of the trail) will be created in the other regions. If the trail exists in all regions and this value is set to false, the trail will remain in the region where it was created, and its shadow trails in other regions will be deleted. As a best practice, consider using trails that log events in all regions.
        /// </summary>
        public readonly bool? IsMultiRegionTrail;
        /// <summary>
        /// Specifies whether the trail is created for all accounts in an organization in AWS Organizations, or only for the current AWS account. The default is false, and cannot be true unless the call is made on behalf of an AWS account that is the master account for an organization in AWS Organizations.
        /// </summary>
        public readonly bool? IsOrganizationTrail;
        /// <summary>
        /// Specifies the KMS key ID to use to encrypt the logs delivered by CloudTrail. The value can be an alias name prefixed by 'alias/', a fully specified ARN to an alias, a fully specified ARN to a key, or a globally unique identifier.
        /// </summary>
        public readonly string? KMSKeyId;
        /// <summary>
        /// Specifies the name of the Amazon S3 bucket designated for publishing log files. See Amazon S3 Bucket Naming Requirements.
        /// </summary>
        public readonly string? S3BucketName;
        /// <summary>
        /// Specifies the Amazon S3 key prefix that comes after the name of the bucket you have designated for log file delivery. For more information, see Finding Your CloudTrail Log Files. The maximum length is 200 characters.
        /// </summary>
        public readonly string? S3KeyPrefix;
        public readonly string? SnsTopicArn;
        /// <summary>
        /// Specifies the name of the Amazon SNS topic defined for notification of log file delivery. The maximum length is 256 characters.
        /// </summary>
        public readonly string? SnsTopicName;
        public readonly ImmutableArray<Outputs.TrailTag> Tags;

        [OutputConstructor]
        private GetTrailResult(
            string? arn,

            string? cloudWatchLogsLogGroupArn,

            string? cloudWatchLogsRoleArn,

            bool? enableLogFileValidation,

            ImmutableArray<Outputs.TrailEventSelector> eventSelectors,

            bool? includeGlobalServiceEvents,

            ImmutableArray<Outputs.TrailInsightSelector> insightSelectors,

            bool? isLogging,

            bool? isMultiRegionTrail,

            bool? isOrganizationTrail,

            string? kMSKeyId,

            string? s3BucketName,

            string? s3KeyPrefix,

            string? snsTopicArn,

            string? snsTopicName,

            ImmutableArray<Outputs.TrailTag> tags)
        {
            Arn = arn;
            CloudWatchLogsLogGroupArn = cloudWatchLogsLogGroupArn;
            CloudWatchLogsRoleArn = cloudWatchLogsRoleArn;
            EnableLogFileValidation = enableLogFileValidation;
            EventSelectors = eventSelectors;
            IncludeGlobalServiceEvents = includeGlobalServiceEvents;
            InsightSelectors = insightSelectors;
            IsLogging = isLogging;
            IsMultiRegionTrail = isMultiRegionTrail;
            IsOrganizationTrail = isOrganizationTrail;
            KMSKeyId = kMSKeyId;
            S3BucketName = s3BucketName;
            S3KeyPrefix = s3KeyPrefix;
            SnsTopicArn = snsTopicArn;
            SnsTopicName = snsTopicName;
            Tags = tags;
        }
    }
}
