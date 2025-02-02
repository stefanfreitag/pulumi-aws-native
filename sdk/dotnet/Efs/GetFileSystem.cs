// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Efs
{
    public static class GetFileSystem
    {
        /// <summary>
        /// Resource Type definition for AWS::EFS::FileSystem
        /// </summary>
        public static Task<GetFileSystemResult> InvokeAsync(GetFileSystemArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.InvokeAsync<GetFileSystemResult>("aws-native:efs:getFileSystem", args ?? new GetFileSystemArgs(), options.WithDefaults());

        /// <summary>
        /// Resource Type definition for AWS::EFS::FileSystem
        /// </summary>
        public static Output<GetFileSystemResult> Invoke(GetFileSystemInvokeArgs args, InvokeOptions? options = null)
            => global::Pulumi.Deployment.Instance.Invoke<GetFileSystemResult>("aws-native:efs:getFileSystem", args ?? new GetFileSystemInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetFileSystemArgs : global::Pulumi.InvokeArgs
    {
        [Input("fileSystemId", required: true)]
        public string FileSystemId { get; set; } = null!;

        public GetFileSystemArgs()
        {
        }
        public static new GetFileSystemArgs Empty => new GetFileSystemArgs();
    }

    public sealed class GetFileSystemInvokeArgs : global::Pulumi.InvokeArgs
    {
        [Input("fileSystemId", required: true)]
        public Input<string> FileSystemId { get; set; } = null!;

        public GetFileSystemInvokeArgs()
        {
        }
        public static new GetFileSystemInvokeArgs Empty => new GetFileSystemInvokeArgs();
    }


    [OutputType]
    public sealed class GetFileSystemResult
    {
        public readonly string? Arn;
        public readonly Outputs.FileSystemBackupPolicy? BackupPolicy;
        public readonly string? FileSystemId;
        /// <summary>
        /// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::EFS::FileSystem` for more information about the expected schema for this property.
        /// </summary>
        public readonly object? FileSystemPolicy;
        public readonly Outputs.FileSystemProtection? FileSystemProtection;
        public readonly ImmutableArray<Pulumi.AwsNative.Outputs.Tag> FileSystemTags;
        public readonly ImmutableArray<Outputs.FileSystemLifecyclePolicy> LifecyclePolicies;
        public readonly double? ProvisionedThroughputInMibps;
        public readonly Outputs.FileSystemReplicationConfiguration? ReplicationConfiguration;
        public readonly string? ThroughputMode;

        [OutputConstructor]
        private GetFileSystemResult(
            string? arn,

            Outputs.FileSystemBackupPolicy? backupPolicy,

            string? fileSystemId,

            object? fileSystemPolicy,

            Outputs.FileSystemProtection? fileSystemProtection,

            ImmutableArray<Pulumi.AwsNative.Outputs.Tag> fileSystemTags,

            ImmutableArray<Outputs.FileSystemLifecyclePolicy> lifecyclePolicies,

            double? provisionedThroughputInMibps,

            Outputs.FileSystemReplicationConfiguration? replicationConfiguration,

            string? throughputMode)
        {
            Arn = arn;
            BackupPolicy = backupPolicy;
            FileSystemId = fileSystemId;
            FileSystemPolicy = fileSystemPolicy;
            FileSystemProtection = fileSystemProtection;
            FileSystemTags = fileSystemTags;
            LifecyclePolicies = lifecyclePolicies;
            ProvisionedThroughputInMibps = provisionedThroughputInMibps;
            ReplicationConfiguration = replicationConfiguration;
            ThroughputMode = throughputMode;
        }
    }
}
