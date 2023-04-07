// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTAnalytics.Inputs
{

    public sealed class PipelineRemoveAttributesArgs : global::Pulumi.ResourceArgs
    {
        [Input("attributes", required: true)]
        private InputList<string>? _attributes;
        public InputList<string> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<string>());
            set => _attributes = value;
        }

        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        [Input("next")]
        public Input<string>? Next { get; set; }

        public PipelineRemoveAttributesArgs()
        {
        }
        public static new PipelineRemoveAttributesArgs Empty => new PipelineRemoveAttributesArgs();
    }
}
