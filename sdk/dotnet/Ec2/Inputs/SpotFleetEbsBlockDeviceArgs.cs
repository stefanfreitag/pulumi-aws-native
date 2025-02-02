// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Ec2.Inputs
{

    public sealed class SpotFleetEbsBlockDeviceArgs : global::Pulumi.ResourceArgs
    {
        [Input("deleteOnTermination")]
        public Input<bool>? DeleteOnTermination { get; set; }

        [Input("encrypted")]
        public Input<bool>? Encrypted { get; set; }

        [Input("iops")]
        public Input<int>? Iops { get; set; }

        [Input("snapshotId")]
        public Input<string>? SnapshotId { get; set; }

        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        [Input("volumeType")]
        public Input<Pulumi.AwsNative.Ec2.SpotFleetEbsBlockDeviceVolumeType>? VolumeType { get; set; }

        public SpotFleetEbsBlockDeviceArgs()
        {
        }
        public static new SpotFleetEbsBlockDeviceArgs Empty => new SpotFleetEbsBlockDeviceArgs();
    }
}
