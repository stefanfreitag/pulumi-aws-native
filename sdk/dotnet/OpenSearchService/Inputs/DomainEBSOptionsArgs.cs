// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.OpenSearchService.Inputs
{

    public sealed class DomainEBSOptionsArgs : global::Pulumi.ResourceArgs
    {
        [Input("eBSEnabled")]
        public Input<bool>? EBSEnabled { get; set; }

        [Input("iops")]
        public Input<int>? Iops { get; set; }

        [Input("volumeSize")]
        public Input<int>? VolumeSize { get; set; }

        [Input("volumeType")]
        public Input<string>? VolumeType { get; set; }

        public DomainEBSOptionsArgs()
        {
        }
        public static new DomainEBSOptionsArgs Empty => new DomainEBSOptionsArgs();
    }
}
