// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    /// <summary>
    /// Parameters for a block device for an EBS volume in an Amazon EC2 launch template.
    /// </summary>
    public sealed class LaunchTemplateEbsArgs : global::Pulumi.ResourceArgs
    {
        /// <summary>
        /// Indicates whether the EBS volume is deleted on instance termination.
        /// </summary>
        [Input("deleteOnTermination")]
        public Input<bool>? DeleteOnTermination { get; set; }

        /// <summary>
        /// Indicates whether the EBS volume is encrypted. Encrypted volumes can only be attached to instances that support Amazon EBS encryption. If you are creating a volume from a snapshot, you can't specify an encryption value.
        /// </summary>
        [Input("encrypted")]
        public Input<bool>? Encrypted { get; set; }

        /// <summary>
        /// The number of I/O operations per second (IOPS).
        /// </summary>
        [Input("iops")]
        public Input<int>? Iops { get; set; }

        /// <summary>
        /// The ARN of the symmetric AWS Key Management Service (AWS KMS) CMK used for encryption.
        /// </summary>
        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        /// <summary>
        /// The ID of the snapshot.
        /// </summary>
        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        /// <summary>
        /// The throughput to provision for a gp3 volume, with a maximum of 1,000 MiB/s.
        /// </summary>
        [Input("throughput")]
        public Input<int>? Throughput { get; set; }

        /// <summary>
        /// The size of the volume, in GiBs. You must specify either a snapshot ID or a volume size.
        /// </summary>
        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        /// <summary>
        /// The volume type.
        /// </summary>
        [Input("volumeType")]
        public Input<string>? VolumeType { get; set; }

        public LaunchTemplateEbsArgs()
        {
        }
        public static new LaunchTemplateEbsArgs Empty => new LaunchTemplateEbsArgs();
    }
}
