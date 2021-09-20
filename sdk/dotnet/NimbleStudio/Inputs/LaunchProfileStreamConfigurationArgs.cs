// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.NimbleStudio.Inputs
{

    public sealed class LaunchProfileStreamConfigurationArgs : Pulumi.ResourceArgs
    {
        [Input("clipboardMode", required: true)]
        public Input<string> ClipboardMode { get; set; } = null!;

        [Input("ec2InstanceTypes", required: true)]
        private InputList<string>? _ec2InstanceTypes;
        public InputList<string> Ec2InstanceTypes
        {
            get => _ec2InstanceTypes ?? (_ec2InstanceTypes = new InputList<string>());
            set => _ec2InstanceTypes = value;
        }

        [Input("maxSessionLengthInMinutes")]
        public Input<double>? MaxSessionLengthInMinutes { get; set; }

        [Input("streamingImageIds", required: true)]
        private InputList<string>? _streamingImageIds;
        public InputList<string> StreamingImageIds
        {
            get => _streamingImageIds ?? (_streamingImageIds = new InputList<string>());
            set => _streamingImageIds = value;
        }

        public LaunchProfileStreamConfigurationArgs()
        {
        }
    }
}
