// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GreengrassV2.Inputs
{

    public sealed class ComponentVersionLambdaContainerParamsArgs : Pulumi.ResourceArgs
    {
        [Input("devices")]
        private InputList<Inputs.ComponentVersionLambdaDeviceMountArgs>? _devices;
        public InputList<Inputs.ComponentVersionLambdaDeviceMountArgs> Devices
        {
            get => _devices ?? (_devices = new InputList<Inputs.ComponentVersionLambdaDeviceMountArgs>());
            set => _devices = value;
        }

        [Input("memorySizeInKB")]
        public Input<int>? MemorySizeInKB { get; set; }

        [Input("mountROSysfs")]
        public Input<bool>? MountROSysfs { get; set; }

        [Input("volumes")]
        private InputList<Inputs.ComponentVersionLambdaVolumeMountArgs>? _volumes;
        public InputList<Inputs.ComponentVersionLambdaVolumeMountArgs> Volumes
        {
            get => _volumes ?? (_volumes = new InputList<Inputs.ComponentVersionLambdaVolumeMountArgs>());
            set => _volumes = value;
        }

        public ComponentVersionLambdaContainerParamsArgs()
        {
        }
    }
}
