// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.PinpointEmail.Inputs
{

    public sealed class ConfigurationSetEventDestinationDimensionConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("defaultDimensionValue", required: true)]
        public Input<string> DefaultDimensionValue { get; set; } = null!;

        [Input("dimensionName", required: true)]
        public Input<string> DimensionName { get; set; } = null!;

        [Input("dimensionValueSource", required: true)]
        public Input<string> DimensionValueSource { get; set; } = null!;

        public ConfigurationSetEventDestinationDimensionConfigurationArgs()
        {
        }
        public static new ConfigurationSetEventDestinationDimensionConfigurationArgs Empty => new ConfigurationSetEventDestinationDimensionConfigurationArgs();
    }
}
