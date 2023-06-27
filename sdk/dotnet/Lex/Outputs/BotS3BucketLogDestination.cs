// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Lex.Outputs
{

    /// <summary>
    /// Specifies an Amazon S3 bucket for logging audio conversations
    /// </summary>
    [OutputType]
    public sealed class BotS3BucketLogDestination
    {
        /// <summary>
        /// The Amazon Resource Name (ARN) of an AWS Key Management Service (KMS) key for encrypting audio log files stored in an S3 bucket.
        /// </summary>
        public readonly string? KmsKeyArn;
        /// <summary>
        /// The Amazon S3 key of the deployment package.
        /// </summary>
        public readonly string LogPrefix;
        /// <summary>
        /// The Amazon Resource Name (ARN) of an Amazon S3 bucket where audio log files are stored.
        /// </summary>
        public readonly string S3BucketArn;

        [OutputConstructor]
        private BotS3BucketLogDestination(
            string? kmsKeyArn,

            string logPrefix,

            string s3BucketArn)
        {
            KmsKeyArn = kmsKeyArn;
            LogPrefix = logPrefix;
            S3BucketArn = s3BucketArn;
        }
    }
}
