// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.S3.Outputs
{

    [OutputType]
    public sealed class BucketReplicationDestination
    {
        public readonly Outputs.BucketAccessControlTranslation? AccessControlTranslation;
        public readonly string? Account;
        public readonly string Bucket;
        public readonly Outputs.BucketEncryptionConfiguration? EncryptionConfiguration;
        public readonly Outputs.BucketMetrics? Metrics;
        public readonly Outputs.BucketReplicationTime? ReplicationTime;
        public readonly string? StorageClass;

        [OutputConstructor]
        private BucketReplicationDestination(
            Outputs.BucketAccessControlTranslation? accessControlTranslation,

            string? account,

            string bucket,

            Outputs.BucketEncryptionConfiguration? encryptionConfiguration,

            Outputs.BucketMetrics? metrics,

            Outputs.BucketReplicationTime? replicationTime,

            string? storageClass)
        {
            AccessControlTranslation = accessControlTranslation;
            Account = account;
            Bucket = bucket;
            EncryptionConfiguration = encryptionConfiguration;
            Metrics = metrics;
            ReplicationTime = replicationTime;
            StorageClass = storageClass;
        }
    }
}
