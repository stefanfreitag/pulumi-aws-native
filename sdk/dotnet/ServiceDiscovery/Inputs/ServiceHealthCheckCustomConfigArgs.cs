// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.ServiceDiscovery.Inputs
{

    public sealed class ServiceHealthCheckCustomConfigArgs : global::Pulumi.ResourceArgs
    {
        [Input("failureThreshold")]
        public Input<double>? FailureThreshold { get; set; }

        public ServiceHealthCheckCustomConfigArgs()
        {
        }
        public static new ServiceHealthCheckCustomConfigArgs Empty => new ServiceHealthCheckCustomConfigArgs();
    }
}
