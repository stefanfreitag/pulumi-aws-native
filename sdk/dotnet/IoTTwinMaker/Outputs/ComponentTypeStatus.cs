// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.IoTTwinMaker.Outputs
{

    [OutputType]
    public sealed class ComponentTypeStatus
    {
        public readonly Union<object, Outputs.ComponentTypeStatusErrorProperties>? Error;
        public readonly Pulumi.AwsNative.IoTTwinMaker.ComponentTypeStatusState? State;

        [OutputConstructor]
        private ComponentTypeStatus(
            Union<object, Outputs.ComponentTypeStatusErrorProperties>? error,

            Pulumi.AwsNative.IoTTwinMaker.ComponentTypeStatusState? state)
        {
            Error = error;
            State = state;
        }
    }
}
