// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class DatasetActionArgs : global::Pulumi.ResourceArgs
    {
        [Input("actionName", required: true)]
        public Input<string> ActionName { get; set; } = null!;

        [Input("containerAction")]
        public Input<Inputs.DatasetContainerActionArgs>? ContainerAction { get; set; }

        [Input("queryAction")]
        public Input<Inputs.DatasetQueryActionArgs>? QueryAction { get; set; }

        public DatasetActionArgs()
        {
        }
        public static new DatasetActionArgs Empty => new DatasetActionArgs();
    }
}
