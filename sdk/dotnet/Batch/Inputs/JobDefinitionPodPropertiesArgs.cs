// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Batch.Inputs
{

    public sealed class JobDefinitionPodPropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("containers")]
        private InputList<Inputs.JobDefinitionEksContainerArgs>? _containers;
        public InputList<Inputs.JobDefinitionEksContainerArgs> Containers
        {
            get => _containers ?? (_containers = new InputList<Inputs.JobDefinitionEksContainerArgs>());
            set => _containers = value;
        }

        [Input("dnsPolicy")]
        public Input<string>? DnsPolicy { get; set; }

        [Input("hostNetwork")]
        public Input<bool>? HostNetwork { get; set; }

        [Input("metadata")]
        public Input<Inputs.JobDefinitionMetadataArgs>? Metadata { get; set; }

        [Input("serviceAccountName")]
        public Input<string>? ServiceAccountName { get; set; }

        [Input("volumes")]
        private InputList<Inputs.JobDefinitionEksVolumeArgs>? _volumes;
        public InputList<Inputs.JobDefinitionEksVolumeArgs> Volumes
        {
            get => _volumes ?? (_volumes = new InputList<Inputs.JobDefinitionEksVolumeArgs>());
            set => _volumes = value;
        }

        public JobDefinitionPodPropertiesArgs()
        {
        }
        public static new JobDefinitionPodPropertiesArgs Empty => new JobDefinitionPodPropertiesArgs();
    }
}
