// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.AppFlow.Inputs
{

    public sealed class FlowAmplitudeSourcePropertiesArgs : global::Pulumi.ResourceArgs
    {
        [Input("object", required: true)]
        public Input<string> Object { get; set; } = null!;

        public FlowAmplitudeSourcePropertiesArgs()
        {
        }
        public static new FlowAmplitudeSourcePropertiesArgs Empty => new FlowAmplitudeSourcePropertiesArgs();
    }
}
