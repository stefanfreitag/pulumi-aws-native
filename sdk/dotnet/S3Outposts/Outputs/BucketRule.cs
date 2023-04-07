// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3Outposts.Outputs
{

    /// <summary>
    /// Specifies lifecycle rules for an Amazon S3Outposts bucket. You must specify at least one of the following: AbortIncompleteMultipartUpload, ExpirationDate, ExpirationInDays.
    /// </summary>
    [OutputType]
    public sealed class BucketRule
    {
        /// <summary>
        /// Specifies a lifecycle rule that stops incomplete multipart uploads to an Amazon S3Outposts bucket.
        /// </summary>
        public readonly Outputs.BucketAbortIncompleteMultipartUpload? AbortIncompleteMultipartUpload;
        /// <summary>
        /// Indicates when objects are deleted from Amazon S3Outposts. The date value must be in ISO 8601 format. The time is always midnight UTC.
        /// </summary>
        public readonly string? ExpirationDate;
        /// <summary>
        /// Indicates the number of days after creation when objects are deleted from Amazon S3Outposts.
        /// </summary>
        public readonly int? ExpirationInDays;
        /// <summary>
        /// The container for the filter of the lifecycle rule.
        /// </summary>
        public readonly Outputs.BucketRuleFilterProperties? Filter;
        /// <summary>
        /// Unique identifier for the lifecycle rule. The value can't be longer than 255 characters.
        /// </summary>
        public readonly string? Id;
        public readonly Pulumi.AwsNative.S3Outposts.BucketRuleStatus? Status;

        [OutputConstructor]
        private BucketRule(
            Outputs.BucketAbortIncompleteMultipartUpload? abortIncompleteMultipartUpload,

            string? expirationDate,

            int? expirationInDays,

            Outputs.BucketRuleFilterProperties? filter,

            string? id,

            Pulumi.AwsNative.S3Outposts.BucketRuleStatus? status)
        {
            AbortIncompleteMultipartUpload = abortIncompleteMultipartUpload;
            ExpirationDate = expirationDate;
            ExpirationInDays = expirationInDays;
            Filter = filter;
            Id = id;
            Status = status;
        }
    }
}
