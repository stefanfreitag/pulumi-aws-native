// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.GreengrassV2.Outputs
{

    [OutputType]
    public sealed class ComponentVersionLambdaLinuxProcessParams
    {
        public readonly Outputs.ComponentVersionLambdaContainerParams? ContainerParams;
        public readonly Pulumi.AwsNative.GreengrassV2.ComponentVersionLambdaLinuxProcessParamsIsolationMode? IsolationMode;

        [OutputConstructor]
        private ComponentVersionLambdaLinuxProcessParams(
            Outputs.ComponentVersionLambdaContainerParams? containerParams,

            Pulumi.AwsNative.GreengrassV2.ComponentVersionLambdaLinuxProcessParamsIsolationMode? isolationMode)
        {
            ContainerParams = containerParams;
            IsolationMode = isolationMode;
        }
    }
}
