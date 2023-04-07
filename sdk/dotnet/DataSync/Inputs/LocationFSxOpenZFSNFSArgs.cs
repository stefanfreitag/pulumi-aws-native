// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.DataSync.Inputs
{

    /// <summary>
    /// FSx OpenZFS file system NFS protocol information
    /// </summary>
    public sealed class LocationFSxOpenZFSNFSArgs : global::Pulumi.ResourceArgs
    {
        [Input("mountOptions", required: true)]
        public Input<Inputs.LocationFSxOpenZFSMountOptionsArgs> MountOptions { get; set; } = null!;

        public LocationFSxOpenZFSNFSArgs()
        {
        }
        public static new LocationFSxOpenZFSNFSArgs Empty => new LocationFSxOpenZFSNFSArgs();
    }
}
