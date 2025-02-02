// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Efs.Inputs
{

    public sealed class FileSystemReplicationDestinationArgs : global::Pulumi.ResourceArgs
    {
        [Input("availabilityZoneName")]
        public Input<string>? AvailabilityZoneName { get; set; }

        [Input("fileSystemId")]
        public Input<string>? FileSystemId { get; set; }

        [Input("kmsKeyId")]
        public Input<string>? KmsKeyId { get; set; }

        [Input("region")]
        public Input<string>? Region { get; set; }

        public FileSystemReplicationDestinationArgs()
        {
        }
        public static new FileSystemReplicationDestinationArgs Empty => new FileSystemReplicationDestinationArgs();
    }
}
