// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.KinesisFirehose.Inputs
{

    public sealed class DeliveryStreamProcessingConfigurationArgs : global::Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("processors")]
        private InputList<Inputs.DeliveryStreamProcessorArgs>? _processors;
        public InputList<Inputs.DeliveryStreamProcessorArgs> Processors
        {
            get => _processors ?? (_processors = new InputList<Inputs.DeliveryStreamProcessorArgs>());
            set => _processors = value;
        }

        public DeliveryStreamProcessingConfigurationArgs()
        {
        }
        public static new DeliveryStreamProcessingConfigurationArgs Empty => new DeliveryStreamProcessingConfigurationArgs();
    }
}
