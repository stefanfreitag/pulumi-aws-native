// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.AwsNative.MSK.Outputs
{

    [OutputType]
    public sealed class ClusterVpcConnectivityClientAuthentication
    {
        public readonly Outputs.ClusterVpcConnectivitySasl? Sasl;
        public readonly Outputs.ClusterVpcConnectivityTls? Tls;

        [OutputConstructor]
        private ClusterVpcConnectivityClientAuthentication(
            Outputs.ClusterVpcConnectivitySasl? sasl,

            Outputs.ClusterVpcConnectivityTls? tls)
        {
            Sasl = sasl;
            Tls = tls;
        }
    }
}
