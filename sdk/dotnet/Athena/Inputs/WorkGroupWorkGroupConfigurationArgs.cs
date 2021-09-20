// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.Athena.Inputs
{

    public sealed class WorkGroupWorkGroupConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("bytesScannedCutoffPerQuery")]
        public Input<int>? BytesScannedCutoffPerQuery { get; set; }

        [Input("enforceWorkGroupConfiguration")]
        public Input<bool>? EnforceWorkGroupConfiguration { get; set; }

        [Input("engineVersion")]
        public Input<Inputs.WorkGroupEngineVersionArgs>? EngineVersion { get; set; }

        [Input("publishCloudWatchMetricsEnabled")]
        public Input<bool>? PublishCloudWatchMetricsEnabled { get; set; }

        [Input("requesterPaysEnabled")]
        public Input<bool>? RequesterPaysEnabled { get; set; }

        [Input("resultConfiguration")]
        public Input<Inputs.WorkGroupResultConfigurationArgs>? ResultConfiguration { get; set; }

        public WorkGroupWorkGroupConfigurationArgs()
        {
        }
    }
}
